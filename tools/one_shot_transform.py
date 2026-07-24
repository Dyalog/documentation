#!/usr/bin/env python3
"""Fold the cross-reference lists into each Object Reference page.

Run-once tool. Rewrites three page groups, moving their cross-reference lists
from the top of the page into an Application section at the end:

  objects/         Removes the nav line ("Parents, Children, ...") and appends
                   an Application section with the parents, children,
                   properties, methods and events embedded inline, read from
                   the parentlists/childlists/proplists/methodlists/eventlists
                   pages.
  properties/      Removes the "Applies To" line (inline "**Applies To:** ..."
  methodorevents/  or linked "[**Applies To**](../propertyapplies/x.md)") and
                   appends an Application section listing the objects the
                   property/method/event applies to. Linked lists are read from
                   the propertyapplies/methodoreventapplies pages; inline lists
                   are taken from the line itself.

All lists are sorted alphabetically; link targets are copied verbatim. Any YAML
frontmatter and the title are preserved.

Once the lists are embedded, the cross-reference directories they came from are
linked by nothing, so the script removes them from the destination (see
ORPHAN_DIRS).

Strictly read-only on the source: transformed pages are written under a
separate destination guide root for side-by-side comparison, and only the
destination is ever deleted from. Invoke from the repository root, passing
source and destination guide roots (each containing a docs/ directory):

    python tools/one_shot_transform.py object-reference object-reference-new

Delete this script after use; it is not part of the documentation build.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

# Object pages: category label -> list directory, rendered in this order.
CATEGORIES = [
    ("Parents", "parentlists"),
    ("Children", "childlists"),
    ("Properties", "proplists"),
    ("Methods", "methodlists"),
    ("Events", "eventlists"),
]

# The five object pages whose nav omits a populated category; flagged in the
# report so the surfaced content can be spot-checked.
EDGE_CASES = {
    "root": "Parents surfaced (nav omits it)",
    "activexcontainer": "Children surfaced (nav omits it)",
    "colorbutton": "Children surfaced (nav omits it)",
    "ocxclass": "Children surfaced (nav omits it)",
    "timer": "Children surfaced (nav omits it)",
}

# Property/method/event page groups that carry an "Applies To" list.
MEMBER_GROUPS = ["properties", "methodorevents"]

# Cross-reference directories that hold the lists being embedded. After the
# transform nothing links to them, so they are deleted from the destination.
ORPHAN_DIRS = [
    "parentlists", "childlists", "proplists", "methodlists", "eventlists",
    "propertyapplies", "methodoreventapplies",
]

# Object-list links (parentlists etc. and the *applies pages): ../dir/name.md.
LINK_RE = re.compile(r"\[\s*([^\]]+?)\s*\]\((\.\./[^)]+\.md)\)")
# Any markdown link, for the inline "Applies To" line whose targets may be
# cross-subsite and extensionless (e.g. ../../../windows-ui-guide/...).
LINK_ANY_RE = re.compile(r"\[\s*([^\]]+?)\s*\]\(([^)]+)\)")
NAV_RE = re.compile(r"(parentlists|childlists|proplists|methodlists|eventlists)/")
APPLIES_RE = re.compile(r"\*\*Applies\s*To")
LINKED_APPLIES_RE = re.compile(r"\[\*\*Applies To\*\*\]\(\.\./(\w+)/([^)]+\.md)\)")


def extract_links(path):
    """Return [(name, target)] for every object-list link in a file.

    Skips &nbsp; padding, stray pipes, empty cells, the heading and frontmatter,
    because those contain no matching link. Returns [] if the file is absent.
    """
    if not path.is_file():
        return []
    return LINK_RE.findall(path.read_text(encoding="utf-8"))


def render_list(links):
    """Sort links case-insensitively by display text and render them inline."""
    ordered = sorted(links, key=lambda pair: pair[0].strip().lower())
    return ", ".join(f"[{name.strip()}]({target})" for name, target in ordered)


def build_object_application(name, docs):
    """Assemble the Application section lines for object <name>."""
    lines = ["**Application**", ""]
    for label, directory in CATEGORIES:
        links = extract_links(docs / directory / f"{name}.md")
        if not links:
            continue
        lines.append(f"{label}: {render_list(links)}")
        lines.append("")
    return lines


def strip_nav(lines):
    """Drop the object nav block and reflow the head.

    Returns (new_lines, found). Keeps line 1 (the title) plus a single blank,
    then every line after the nav line with leading blanks removed. Everything
    before the nav line (the title's blank, plus netcontrol's pipe-table
    separator) is discarded; the Purpose/Description body is preserved verbatim.
    """
    nav_idx = next((i for i, ln in enumerate(lines) if NAV_RE.search(ln)), None)
    if nav_idx is None:
        return lines, False

    tail = lines[nav_idx + 1:]
    while tail and tail[0].strip() == "":
        tail.pop(0)

    return [lines[0], ""] + tail, True


def transform_object(name, docs):
    """Return (text, found_nav, categories_present) for object <name>."""
    lines = (docs / "objects" / f"{name}.md").read_text(encoding="utf-8").splitlines()
    body, found = strip_nav(lines)

    while body and body[-1].strip() == "":
        body.pop()

    app = build_object_application(name, docs)
    present = [line.split(":", 1)[0] for line in app if ":" in line]

    text = "\n".join(body + [""] + app).rstrip("\n") + "\n"
    return text, found, present


def transform_member(name, docs, group):
    """Return (text, found_applies) for a property/method/event page.

    Removes the "Applies To" line and appends an Application section listing the
    objects it applies to. Frontmatter and title are preserved.
    """
    original = (docs / group / f"{name}.md").read_text(encoding="utf-8")
    lines = original.splitlines()

    idx = next((i for i, ln in enumerate(lines) if APPLIES_RE.search(ln)), None)
    if idx is None:
        return original, False

    line = lines[idx]
    linked = LINKED_APPLIES_RE.search(line)
    if linked:
        objects = extract_links(docs / linked.group(1) / linked.group(2))
    else:
        objects = LINK_ANY_RE.findall(line)

    head = lines[:idx]
    while head and head[-1].strip() == "":
        head.pop()
    tail = lines[idx + 1:]
    while tail and tail[0].strip() == "":
        tail.pop(0)
    body = head + [""] + tail
    while body and body[-1].strip() == "":
        body.pop()

    if objects:
        body += ["", "**Application**", "", f"Objects: {render_list(objects)}"]

    return "\n".join(body).rstrip("\n") + "\n", True


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src", type=Path,
                        help="source guide root containing docs/, e.g. object-reference")
    parser.add_argument("dst", type=Path,
                        help="destination guide root, e.g. object-reference-new")
    parser.add_argument("--dry-run", action="store_true",
                        help="print the report without writing files")
    args = parser.parse_args()

    src = args.src / "docs"
    dst = args.dst / "docs"
    if not (src / "objects").is_dir():
        sys.exit(f"no objects/ directory found under {src}")
    if src.resolve() == dst.resolve():
        sys.exit("source and destination are the same; refusing to run")

    # Object pages.
    obj_names = sorted(p.stem for p in (src / "objects").glob("*.md"))
    if not args.dry_run:
        (dst / "objects").mkdir(parents=True, exist_ok=True)
    no_nav = []
    for name in obj_names:
        text, found, present = transform_object(name, src)
        if not found:
            no_nav.append(name)
        if not args.dry_run:
            (dst / "objects" / f"{name}.md").write_text(text, encoding="utf-8")
        flag = f"  <- {EDGE_CASES[name]}" if name in EDGE_CASES else ""
        print(f"objects/{name:24} {', '.join(present) or '(none)'}{flag}")
    print(f"\n{len(obj_names)} object pages"
          + ("" if not no_nav else f"  WARNING no nav line: {', '.join(no_nav)}"))

    # Property and method/event pages.
    for group in MEMBER_GROUPS:
        names = sorted(p.stem for p in (src / group).glob("*.md"))
        if not args.dry_run:
            (dst / group).mkdir(parents=True, exist_ok=True)
        no_applies = []
        for name in names:
            text, found = transform_member(name, src, group)
            if not found:
                no_applies.append(name)
            if not args.dry_run:
                (dst / group / f"{name}.md").write_text(text, encoding="utf-8")
        note = "" if not no_applies else f"  (no Applies To, left as-is: {', '.join(no_applies)})"
        print(f"{len(names)} {group} pages{note}")

    # Remove the now-orphaned cross-reference directories from the destination.
    for name in ORPHAN_DIRS:
        target = dst / name
        if not target.exists():
            continue
        count = sum(1 for _ in target.glob("*.md"))
        if not args.dry_run:
            shutil.rmtree(target)
        print(f"removed orphaned {name}/ ({count} pages)")

    if args.dry_run:
        print("\n(dry run, nothing written)")
    else:
        print(f"\n-> {dst}")


if __name__ == "__main__":
    main()
