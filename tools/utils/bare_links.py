#!/usr/bin/env python3
"""Report internal links written without a .md suffix, and rewrite them.

MkDocs only resolves links whose target ends in .md. Any other target, whether
bare (`../../language-reference-guide/pcre-specifications`) or directory-style
(`../../language-reference-guide/pcre-specifications/`), is passed through to
the rendered HTML verbatim, so the build never checks that the page exists. The
bare form also costs every reader a redirect, because the server wants the
trailing slash. Rewriting the target as a source-tree relative .md path lets
MkDocs validate it at build time and emit the canonical URL.

Targets are resolved the way the rendered site resolves them (page-as-directory
semantics) against the merged docs tree that mkdocs-monorepo-plugin assembles,
where each guide lives under the slug of its site_name. The rewritten link is
then expressed relative to the page's position in that same tree.

Raw HTML anchors (<a href="...">) are reported but never rewritten and do not
affect the exit status: MkDocs does not touch raw HTML, so a .md target there
would render as a broken link.

Exit status is 0 when no bare markdown links remain, 1 otherwise. Without
--apply the tool only reports, so it can run as a lint.
"""

import argparse
import os
import posixpath
import re
import sys

INLINE = re.compile(
    r'(?<!\\)(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^()\s]+(?:\([^()\s]*\))?)(\s+"[^"]*")?\)'
)
REFDEF = re.compile(r"^\s{0,3}\[([^\]^][^\]]*)\]:\s*(\S+)", re.M)
HREF = re.compile(r"""(<a\b[^>]*?\bhref=)(["'])([^"']+)\2""", re.I)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
CODE_SPAN = re.compile(r"`+[^`]*`+")
EXTENSION = re.compile(r"\.[A-Za-z][A-Za-z0-9]{0,4}$")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
INCLUDE = re.compile(r"!include \./([^/]+)/mkdocs\.yml")
SITE_NAME = re.compile(r"^site_name:\s*(.+)$", re.M)


def slugify(name):
    """Mirror python-slugify for the ASCII site names in this repo."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def guide_alias(name):
    """The directory mkdocs-monorepo-plugin gives a guide in the merged tree."""
    return name if re.fullmatch(r"[a-zA-Z0-9_.\-/]+", name) else slugify(name)


class MergedTree:
    """The docs tree as mkdocs-monorepo-plugin assembles it: <alias>/<path under docs/>."""

    def __init__(self, root):
        self.root = root
        self.pages = {}
        config = open(os.path.join(root, "mkdocs.yml"), encoding="utf-8").read()
        docs_dirs = {"": os.path.join(root, "docs")}
        for folder in INCLUDE.findall(config):
            guide_config = open(os.path.join(root, folder, "mkdocs.yml"), encoding="utf-8").read()
            name = SITE_NAME.search(guide_config).group(1).strip()
            docs_dirs[guide_alias(name)] = os.path.join(root, folder, "docs")
        for alias, docs in docs_dirs.items():
            for dirpath, _, filenames in os.walk(docs):
                for filename in filenames:
                    if filename.endswith(".md"):
                        disk = os.path.join(dirpath, filename)
                        rel = os.path.relpath(disk, docs).replace(os.sep, "/")
                        self.pages[posixpath.join(alias, rel)] = disk

    @staticmethod
    def page_url(page):
        directory, base = posixpath.split(page[:-3])
        return (directory if base == "index" else page[:-3]) + "/"

    def resolve(self, target, page):
        """Resolve a bare target from a page as the rendered site would. Returns (page, fragment) or None."""
        path, sep, fragment = target.partition("#")
        url = posixpath.normpath(posixpath.join(self.page_url(page), path)).strip("/")
        if url.startswith(".."):
            return None
        candidates = [url + ".md", url + "/index.md", url + "/README.md"] if url else ["index.md"]
        for candidate in candidates:
            if candidate in self.pages:
                return candidate, sep + fragment
        return None

    @staticmethod
    def md_link(target, page, fragment):
        return posixpath.relpath(target, posixpath.dirname(page)) + fragment


def is_bare(target):
    if SCHEME.match(target) or target.startswith(("#", "/", "<", "{", "$")):
        return False
    path = target.partition("#")[0].partition("?")[0].rstrip("/")
    if not path:
        return False
    last = path.rsplit("/", 1)[-1]
    return (
        last not in (".", "..")
        and not EXTENSION.search(last)
        and re.fullmatch(r"[A-Za-z0-9_./-]+", path) is not None
    )


def fenced_lines(lines):
    """1-based numbers of the lines inside fenced code blocks, fences included.

    A fence opener counts only if a closer follows: the same character, at least as
    long, alone on its line. The renderer treats an opener that never closes as
    ordinary text, so the rest of the page still carries links that must be checked.
    """
    fenced = set()
    i = 0
    while i < len(lines):
        opener = FENCE.match(lines[i])
        if opener is None:
            i += 1
            continue
        char, width = opener.group(1)[0], len(opener.group(1))
        closer = next(
            (
                j
                for j in range(i + 1, len(lines))
                if re.fullmatch(rf"\s*{re.escape(char)}{{{width},}}\s*", lines[j])
            ),
            None,
        )
        if closer is None:
            i += 1
            continue
        fenced.update(range(i + 1, closer + 2))
        i = closer + 1
    return fenced


def rewrite_page(tree, page, text, changes, unresolved, raw_html):
    """Return the page text with bare links rewritten; record what happened."""
    disk = tree.pages[page]
    out = []
    lines = text.split("\n")
    fenced = fenced_lines(lines)
    for lineno, line in enumerate(lines, 1):
        if lineno in fenced:
            out.append(line)
            continue

        spans = [(m.start(), m.end()) for m in CODE_SPAN.finditer(line)]

        def in_code(pos):
            return any(start <= pos < end for start, end in spans)

        def replacement(target):
            if not is_bare(target):
                return None
            resolved = tree.resolve(target, page)
            if resolved is None:
                unresolved.append((disk, lineno, target))
                return None
            new = tree.md_link(resolved[0], page, resolved[1])
            changes.append((disk, lineno, target, new))
            return new

        def sub_inline(m):
            bang, label, target, title = m.groups()
            if bang or in_code(m.start(3)):
                return m.group(0)
            new = replacement(target)
            return m.group(0) if new is None else f"[{label}]({new}{title or ''})"

        def sub_refdef(m):
            new = replacement(m.group(2))
            return m.group(0) if new is None else f"[{m.group(1)}]: {new}"

        def note_href(m):
            if not in_code(m.start(3)) and is_bare(m.group(3)):
                raw_html.append((disk, lineno, m.group(3)))
            return m.group(0)

        line = INLINE.sub(sub_inline, line)
        line = REFDEF.sub(sub_refdef, line)
        HREF.sub(note_href, line)
        out.append(line)
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    default_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    parser.add_argument("root", nargs="?", default=default_root, help="repository root holding mkdocs.yml")
    parser.add_argument("--apply", action="store_true", help="rewrite the files instead of only reporting")
    parser.add_argument("-q", "--quiet", action="store_true", help="print the summary only")
    args = parser.parse_args()

    tree = MergedTree(args.root)
    changes, unresolved, raw_html = [], [], []
    files_changed = 0
    for page in sorted(tree.pages):
        disk = tree.pages[page]
        text = open(disk, encoding="utf-8").read()
        new_text = rewrite_page(tree, page, text, changes, unresolved, raw_html)
        if new_text != text:
            files_changed += 1
            if args.apply:
                open(disk, "w", encoding="utf-8").write(new_text)

    def show(path):
        return os.path.relpath(path, args.root)

    if not args.quiet:
        for disk, lineno, old, new in changes:
            print(f"{show(disk)}:{lineno}  {old}  ->  {new}")
        for disk, lineno, target in unresolved:
            print(f"{show(disk)}:{lineno}  {target}  (unresolved, left unchanged)")
        for disk, lineno, target in raw_html:
            print(f"{show(disk)}:{lineno}  {target}  (raw HTML href, left unchanged)")

    verb = "rewritten" if args.apply else "found"
    print(
        f"bare links {verb}: {len(changes)} in {files_changed} files; "
        f"unresolved: {len(unresolved)}; raw HTML hrefs: {len(raw_html)}"
    )
    remaining = len(unresolved) + (0 if args.apply else len(changes))
    return 1 if remaining else 0


if __name__ == "__main__":
    sys.exit(main())
