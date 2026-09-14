#!/usr/bin/env python3
"""
Audit object-reference/ against the captured GUI object model.

Compares every cross-reference list in the Object Reference Guide against
objectmodel.json -- the member lists the interpreter itself reports, captured by
MAKEALL on Windows (see README.md). Catches drift that no amount of proofreading
will: an object page listing a property the interpreter no longer has, an A-Z
index that stopped being regenerated, a link whose text no longer matches what it
points at.

Self-contained: standard library only, no dependency on tools/utils/doc_utils.
Link resolution is implemented here rather than reused, because the rules are
easy to get wrong and quietly produce hundreds of false positives (see
resolve_link).

    python objref_audit.py                      # text report
    python objref_audit.py --markdown -o a.md   # regenerate objref-audit.md

Exits 1 if anything is found, 0 if clean, so it can gate CI.
"""

import argparse
import json
import os
import posixpath
import re
import sys
from collections import defaultdict

# The report contains APL glyphs (⎕SE). Windows consoles default to a legacy
# code page, so printing them raises UnicodeEncodeError unless stdout is UTF-8.
# Harmless where UTF-8 is already the default, as on macOS and Linux.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):  # pragma: no cover - exotic streams
            pass

# --------------------------------------------------------------------------
# Known-good exceptions. Each is a deliberate decision, not an oversight;
# without them the report is noise. The reasons are data, not comments, so the
# generated report can declare exactly what it chose not to look at.
# --------------------------------------------------------------------------

# Windows CE / PocketAPL-era vestiges. Present in the interpreter's member
# lists, and so in objectmodel.json, but deliberately excluded from the guide.
# Do not document. EvaluationDays (Root) is the PocketAPL evaluation-copy
# counter; the others are Windows CE artefacts.
EXCLUDED_MEMBERS = {"ShowSIP", "SIPMode", "SIPResize", "OKButton",
                    "EvaluationDays"}

# Members whose page is not named after them. 'Index' would collide with the
# directory index, so the page is index-property.md.
PAGE_ALIASES = {"Index": "index-property"}

# Pages under methodorevents/ that document Session (⎕SE) members. Session is
# excluded from Objects, so these are legitimately outside the model.
SESSION_PAGES = {
    "afterfix", "fix", "format", "sessionprint", "sessiontrace", "workspaceloaded",
}

# Documented, and present in #.ObjectMembers, but missing from Objects, so it
# gets no cross-reference tables. Pre-existing; see README.md.
KNOWN_EXTRA_OBJECT_PAGES = {"netcontrol"}

# The deployed site has a top-level files/ directory of downloadable assets
# (PDFs and similar), populated at deploy time and absent from this
# repository. Links into it cannot be verified here.
DEPLOY_TIME_DIRS = {"files"}


def exclusions():
    """The deliberate exceptions, as (reason, items) for reporting."""
    return [
        ("Members excluded from the guide; present in the interpreter and in "
         "objectmodel.json, undocumented on purpose (Windows CE / "
         "PocketAPL-era vestiges)",
         sorted(EXCLUDED_MEMBERS)),
        ("Members whose page is not named after them",
         [f"{k} -> {v}.md" for k, v in sorted(PAGE_ALIASES.items())]),
        ("Pages under methodorevents/ documenting Session (⎕SE) members, which "
         "fall outside the model because Session is excluded from Objects",
         sorted(SESSION_PAGES)),
        ("Object pages outside the model; documented and present in "
         "#.ObjectMembers but missing from Objects, so they get no "
         "cross-reference tables",
         sorted(KNOWN_EXTRA_OBJECT_PAGES)),
        ("Site directories populated at deploy time and absent from the "
         "repository; links into them are not checked",
         sorted(DEPLOY_TIME_DIRS)),
    ]

# Page label -> Model.members key for the cross-reference blocks on each
# object page. Properties appears twice: once in the interpreter's positional
# ("default") order, once alphabetically. A bare "Properties: " line is the
# retired single-list format, reported as its own finding.
SECTIONS = (
    ("Parents", "Parents"),
    ("Children", "Children"),
    ("Properties (default order)", "PropertiesDefault"),
    ("Properties (alphabetical order)", "Properties"),
    ("Methods", "Methods"),
    ("Events", "Events"),
)
LEGACY_PROPERTIES = "Properties: "
SINGULAR = {"Objects": "object", "Properties": "property",
            "Methods": "method", "Events": "event"}
AZ_INDEXES = {
    "objects-a-z": ("../objects/", "Objects"),
    "properties-a-z": ("../properties/", "Properties"),
    "methods-a-z": ("../methodorevents/", "Methods"),
    "events-a-z": ("../methodorevents/", "Events"),
}

LINK_RE = re.compile(r"\[\s*([^\]]*?)\s*\]\(\s*([^)\s]+)")
HEADING_RE = re.compile(r"^#\s+(.*)$", re.M)
TAG_RE = re.compile(r"<[^>]*>")


def slugify(name):
    return PAGE_ALIASES.get(name, name.lower())


class Model:
    """The captured object model, with the deliberate exclusions applied."""

    def __init__(self, path):
        raw = json.load(open(path, encoding="utf-8"))
        self.objects = raw["Objects"]
        self.index = {o: i for i, o in enumerate(self.objects)}
        pmap = raw["ParentMap"]

        def keep_order(names):
            return [n for n in names if n not in EXCLUDED_MEMBERS]

        def keep(names):
            return sorted(keep_order(names), key=str.lower)

        self.members = {}
        for o in self.objects:
            i = self.index[o]
            self.members[o] = {
                "Parents": keep(p for p in self.objects if pmap[self.index[p]][i]),
                "Children": keep(c for c in self.objects if pmap[i][self.index[c]]),
                "Properties": keep(raw["Properties"][i]),
                "PropertiesDefault": keep_order(raw["Properties"][i]),
                "Methods": keep(raw["Methods"][i]),
                "Events": keep(raw["Events"][i]),
            }
        self.all = {
            kind: sorted({m for o in self.objects for m in self.members[o][kind]},
                         key=str.lower)
            for kind in ("Properties", "Methods", "Events")
        }
        self.all["Objects"] = sorted(self.objects, key=str.lower)
        # Which kind each member name belongs to, for the classification check.
        self.kind_of = {}
        for kind in ("Properties", "Methods", "Events"):
            for name in self.all[kind]:
                self.kind_of.setdefault(name, set()).add(kind)


def guides_in(root):
    return {
        d for d in os.listdir(root)
        if os.path.isfile(os.path.join(root, d, "mkdocs.yml"))
        and os.path.isdir(os.path.join(root, d, "docs"))
    }


def page_url(guide, relpath):
    """Deployed URL of a source file, mkdocs directory-urls style."""
    p = relpath.replace(os.sep, "/")[:-3]
    if p == "index" or p.endswith("/index"):
        p = p[: -len("index")]
    return "/" + posixpath.join(guide, p).strip("/") + "/"


def resolve_link(root, guides, srcdir, pageurl, target):
    """True if a relative link resolves.

    Two rules, and both are needed:

    1. File-relative. Covers intra-guide '.md' links and every asset, because
       mkdocs rewrites relative paths from the *source* file's location.
    2. Deployed-site-relative. Extensionless cross-guide links such as
       '../../../language-reference-guide/system-functions/dq' resolve against
       the site root -- each guide is its own mkdocs site with 'docs/' stripped.

    Checking only rule 2 marks every image broken; only rule 1 marks every
    cross-guide link broken. object-reference alone yields ~224 false positives
    if either is missing.
    """
    if os.path.exists(os.path.normpath(os.path.join(srcdir, target))):
        return True
    parts = [p for p in posixpath.normpath(posixpath.join(pageurl, target)).split("/") if p]
    if not parts or parts[0] not in guides:
        return False
    base = os.path.join(root, parts[0], "docs")
    rest = parts[1:]
    candidates = ([os.path.join(base, "index.md")] if not rest else
                  [os.path.join(base, *rest) + ".md",
                   os.path.join(base, *rest, "index.md"),
                   os.path.join(base, *rest)])
    return any(os.path.exists(c) for c in candidates)


def read(path):
    return open(path, encoding="utf-8", errors="replace").read()


def audit(root, guide="object-reference", model_path=None):
    docs = os.path.join(root, guide, "docs")
    model = Model(model_path or os.path.join(root, "tools", "buildgui", "objectmodel.json"))
    guides = guides_in(root)
    f = defaultdict(list)  # finding bucket -> list of strings

    def pages_in(sub):
        d = os.path.join(docs, sub)
        return {p[:-3] for p in os.listdir(d) if p.endswith(".md")} if os.path.isdir(d) else set()

    object_pages = pages_in("objects")
    prop_pages = pages_in("properties")
    me_pages = pages_in("methodorevents")

    # -- 1. object page coverage -------------------------------------------
    for o in model.objects:
        if slugify(o) not in object_pages:
            f["missing-object-pages"].append(o)
    for p in sorted(object_pages - {slugify(o) for o in model.objects} - KNOWN_EXTRA_OBJECT_PAGES):
        f["extra-object-pages"].append(p)

    # -- 2. cross-reference blocks on each object page ----------------------
    def sections_of(slug):
        out, legacy = {}, False
        for line in read(os.path.join(docs, "objects", slug + ".md")).splitlines():
            if line.startswith(LEGACY_PROPERTIES):
                legacy = True
            for label, _ in SECTIONS:
                if line.startswith(label + ": "):
                    out[label] = LINK_RE.findall(line[len(label) + 2:])
        return out, legacy

    for o in model.objects:
        slug = slugify(o)
        if slug not in object_pages:
            continue
        found, legacy = sections_of(slug)
        if legacy:
            f["block-legacy"].append(
                f"{slug}.md  single alphabetical Properties list; expected "
                f"the default order / alphabetical order pair")
        for label, key in SECTIONS:
            # A legacy page has neither Properties list; the legacy finding
            # already says so, so per-member noise helps nobody.
            if legacy and label.startswith("Properties"):
                continue
            expect = model.members[o][key]
            got = [l for l, _ in found.get(label, [])]
            if not expect and not got:
                continue
            missing = [x for x in expect if x not in got]
            extra = [x for x in got if x not in expect]
            if missing:
                f["block-missing"].append(f"{slug}.md  {label}: absent from page: {', '.join(missing)}")
            if extra:
                f["block-extra"].append(f"{slug}.md  {label}: on page, not in model: {', '.join(extra)}")
            if not missing and not extra and got != expect:
                f["block-order"].append(f"{slug}.md  {label}: correct members, wrong order")

        # Parents/Children duplication: a whole list copied from its sibling.
        par = [l for l, _ in found.get("Parents", [])]
        chi = [l for l, _ in found.get("Children", [])]
        if par and chi and par == chi:
            f["duplicated-lists"].append(
                f"{slug}.md  Parents and Children are identical "
                f"({len(par)} {'entry' if len(par) == 1 else 'entries'})")

    # -- 3. member page coverage --------------------------------------------
    for kind, pages in (("Properties", prop_pages), ("Methods", me_pages), ("Events", me_pages)):
        for name in model.all[kind]:
            if slugify(name) not in pages:
                f["missing-member-pages"].append(f"{SINGULAR[kind]} {name}")
    documented = {slugify(n) for k in ("Properties",) for n in model.all[k]}
    for p in sorted(prop_pages - documented):
        f["orphan-member-pages"].append(f"properties/{p}.md")
    me_documented = {slugify(n) for k in ("Methods", "Events") for n in model.all[k]}
    for p in sorted(me_pages - me_documented - SESSION_PAGES):
        f["orphan-member-pages"].append(f"methodorevents/{p}.md")

    # -- 4. A-Z indexes ------------------------------------------------------
    for page, (prefix, kind) in AZ_INDEXES.items():
        path = os.path.join(docs, "gui-overview", page + ".md")
        if not os.path.exists(path):
            f["missing-az"].append(page + ".md")
            continue
        listed = []
        for label, target in LINK_RE.findall(read(path)):
            if target.startswith(prefix) and label not in listed:
                listed.append(label)
        expect = model.all[kind]
        known_extra = KNOWN_EXTRA_OBJECT_PAGES if kind == "Objects" else set()
        missing = [x for x in expect if x not in listed]
        extra = [x for x in listed if x not in expect and slugify(x) not in known_extra]
        if missing:
            f["az-missing"].append(f"{page}.md: {len(missing)} not listed: {', '.join(missing)}")
        if extra:
            f["az-extra"].append(
                f"{page}.md: listed but not a model {SINGULAR[kind]}: {', '.join(extra)}")

    # -- 5. link label vs link target ---------------------------------------
    # A link whose text is not the name of the page it points at misnames the
    # member and, in an A-Z table, files it under the wrong letter.
    #
    # Prose labels are not errors -- "see the Grid object", "CoolBands are
    # positioned..." -- so only flag a label that reads as a bare identifier and
    # still disagrees with its target. Plurals are accepted.
    def normalise(s):
        return re.sub(r"[^A-Za-z0-9]", "", s).lower()

    seen_labels = set()
    for sub in ("objects", "properties", "methodorevents", "gui-overview"):
        d = os.path.join(docs, sub)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            for label, target in LINK_RE.findall(read(os.path.join(d, fn))):
                m = re.match(r"^\.\./(properties|methodorevents|objects)/([^/]+)\.md$", target)
                if not m or not label:
                    continue
                stem = m.group(2)
                norm = normalise(label)
                if stem in (norm, norm.rstrip("s"), slugify(label.strip())):
                    continue
                if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", label.strip()):
                    continue  # prose, not a name
                key = (sub, fn, label, stem)
                if key in seen_labels:
                    continue  # same mistake repeated down the page
                seen_labels.add(key)
                f["label-mismatch"].append(f"{sub}/{fn}: [{label}] -> {m.group(1)}/{stem}.md")

    # -- 6. method/event classification --------------------------------------
    # The page heading is 'Name Method NNN' or 'Name Event NNN'. Compare with
    # how the interpreter classifies it.
    for p in sorted(me_pages - SESSION_PAGES):
        text = read(os.path.join(docs, "methodorevents", p + ".md"))
        h = HEADING_RE.search(text)
        if not h:
            continue
        heading = TAG_RE.sub("", h.group(1))
        says = ("Methods" if re.search(r"\bMethod\b", heading) else
                "Events" if re.search(r"\bEvent\b", heading) else None)
        if not says:
            continue
        name = heading.split()[0]
        kinds = model.kind_of.get(name)
        if kinds and says not in kinds:
            f["classification"].append(
                f"methodorevents/{p}.md: heading says {says[:-1]}, model says "
                f"{'/'.join(sorted(k[:-1] for k in kinds))}")

    # -- 7. broken links ------------------------------------------------------
    for dirpath, _, files in os.walk(docs):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, docs)
            purl = page_url(guide, rel)
            for label, target in LINK_RE.findall(read(full)):
                if target.startswith(("http://", "https://", "#", "mailto:", "<")):
                    continue
                t = target.split("#")[0].split("?")[0]
                if not t:
                    continue
                site = [p for p in posixpath.normpath(posixpath.join(purl, t)).split("/") if p]
                if site and site[0] in DEPLOY_TIME_DIRS:
                    continue
                if not resolve_link(root, guides, dirpath, purl, t):
                    f["broken-links"].append(
                        f"{rel.replace(os.sep, '/')}: [{label or 'image'}] -> {target}")

    return model, f


TITLES = {
    "missing-object-pages": "Objects in the model with no page",
    "extra-object-pages": "Object pages not in the model",
    "duplicated-lists": "Parents and Children lists identical (likely a copy)",
    "block-missing": "Cross-reference lists missing members",
    "block-extra": "Cross-reference lists with members not in the model",
    "block-legacy": "Properties entries in the retired single-list format",
    "block-order": "Cross-reference lists out of order",
    "missing-member-pages": "Members in the model with no page",
    "orphan-member-pages": "Member pages not in the model",
    "missing-az": "A-Z index pages not found",
    "az-missing": "A-Z indexes missing entries",
    "az-extra": "A-Z indexes with entries not in the model",
    "label-mismatch": "Link text does not match the page it points at",
    "classification": "Page heading disagrees with the model on method vs event",
    "broken-links": "Broken links",
}
ORDER = list(TITLES)


def report(model, f, markdown=False, out=sys.stdout):
    total = sum(len(v) for v in f.values())
    w = out.write
    if markdown:
        w("# Object Reference audit\n\n")
        w(f"Generated by `tools/buildgui/objref_audit.py` from `objectmodel.json`: "
          f"{len(model.objects)} objects, {len(model.all['Properties'])} properties, "
          f"{len(model.all['Methods'])} methods, {len(model.all['Events'])} events, "
          f"after the exclusions below.\n\n")
        w(f"Findings: {total}\n\n")
        for key in ORDER:
            if f.get(key):
                w(f"## {TITLES[key]} ({len(f[key])})\n\n")
                for line in f[key]:
                    w(f"- {line}\n")
                w("\n")
        if not total:
            w("No findings.\n\n")
        w("## Excluded by design\n\n")
        w("Not defects. Deliberate decisions, encoded in the script, listed here so a "
          "clean run means clean.\n\n")
        for reason, items in exclusions():
            w(f"{reason}:\n\n")
            for item in items:
                w(f"- `{item}`\n")
            w("\n")
    else:
        w(f"Model: {len(model.objects)} objects, {len(model.all['Properties'])} properties, "
          f"{len(model.all['Methods'])} methods, {len(model.all['Events'])} events "
          f"(excluding {', '.join(sorted(EXCLUDED_MEMBERS))})\n")
        w(f"Findings: {total}\n")
        for key in ORDER:
            if f.get(key):
                w(f"\n{TITLES[key]} ({len(f[key])})\n")
                w("-" * 70 + "\n")
                for line in f[key]:
                    w(f"  {line}\n")
        if not total:
            w("\nClean.\n")
        w("\nExcluded by design (not defects)\n")
        w("-" * 70 + "\n")
        for reason, items in exclusions():
            w(f"  {reason}:\n")
            for item in items:
                w(f"    {item}\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_root = os.path.abspath(os.path.join(here, "..", ".."))
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=default_root,
                    help="repository root (defaults to two levels above this script)")
    ap.add_argument("--model", help="path to objectmodel.json "
                                    "(defaults to alongside this script)")
    ap.add_argument("--guide", default="object-reference", help="guide to audit")
    ap.add_argument("--markdown", action="store_true", help="emit a markdown document")
    ap.add_argument("-o", "--output", help="write to this file instead of stdout")
    args = ap.parse_args()

    if not os.path.isdir(args.dir):
        sys.stderr.write(f"error: {args.dir} is not a directory\n")
        return 2
    model_path = args.model or os.path.join(here, "objectmodel.json")
    if not os.path.isfile(model_path):
        sys.stderr.write(f"error: no model at {model_path}\n"
                         f"       generate it with MAKEALL -- see README.md\n")
        return 2

    model, f = audit(args.dir, args.guide, model_path)
    if args.output:
        with open(args.output, "w", encoding="utf-8", newline="\n") as fh:
            report(model, f, args.markdown, fh)
        sys.stderr.write(f"written to {args.output}\n")
    else:
        report(model, f, args.markdown)
    return 1 if any(f.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
