#!/usr/bin/env python3
"""
Regenerate the Properties cross-reference lines on the object pages.

GUI object properties have a positional ("default") order, reported by the
interpreter's PropList and captured in objectmodel.json. Knowing that order is
essential when reading and writing GUI code, so each object page carries the
list twice, in the Application section:

    Properties (default order): ...
    Properties (alphabetical order): ...

This script does not modify the guide. It reads objectmodel.json and the
guide as it stands, and writes a complete copy of object-reference/ to
--output, identical except that on object pages carrying a Properties list it
emits the two lines above, generated from the model. Review the new state,
then swap it in for object-reference/ to apply. Re-running on an
already-converted guide regenerates the same two lines, so the script is the
single source of these lists from now on.

NetControl is documented but absent from the model (see README.md), so its
default order comes from ObjectMembers/NetControl/PropList.apla instead.

    python3 regen_properties.py -o /path/to/new/object-reference

--output must not already exist. Exits 1 if any page disagrees with the model
about having a Properties list at all; such a page is left as copied and
needs a human decision.
"""

import argparse
import json
import os
import re
import shutil
import sys

from objref_audit import EXCLUDED_MEMBERS, LINK_RE, slugify

# Every form the Properties entry has taken. The first is the pre-conversion
# single alphabetical list; the other two are what this script emits.
PROP_LABELS = (
    "Properties: ",
    "Properties (default order): ",
    "Properties (alphabetical order): ",
)


def read(path):
    return open(path, encoding="utf-8").read()


def apla_names(path):
    """Member names from a Link .apla array: one quoted name per line."""
    return re.findall(r"'([^']+)'", read(path))


def property_lines(names):
    """The two Properties lines for one object, from its default-order list."""
    links = {n: f"[{n}](../properties/{slugify(n)}.md)" for n in names}
    default = PROP_LABELS[1] + ", ".join(links[n] for n in names)
    alpha = PROP_LABELS[2] + ", ".join(
        links[n] for n in sorted(names, key=str.lower))
    return default, alpha


def transform(lines, pair):
    """Replace the Properties entry, whatever form it is in, with pair.

    The first Properties line becomes the new pair; any further Properties
    line (the alphabetical half of an already-converted page) is dropped,
    along with the blank separator it followed.
    """
    out, replaced = [], False
    for line in lines:
        if line.startswith(PROP_LABELS):
            if not replaced:
                out.extend([pair[0], "", pair[1]])
                replaced = True
            elif out and out[-1] == "":
                out.pop()
        else:
            out.append(line)
    return out


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_root = os.path.abspath(os.path.join(here, "..", ".."))
    ap = argparse.ArgumentParser(description=(__doc__ or "").split("\n\n")[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=default_root,
                    help="repository root (defaults to two levels above this script)")
    ap.add_argument("--model", help="path to objectmodel.json "
                                    "(defaults to alongside this script)")
    ap.add_argument("-o", "--output", required=True,
                    help="destination for the new object-reference tree; "
                         "must not already exist")
    args = ap.parse_args()

    guide = os.path.join(args.dir, "object-reference")
    if not os.path.isdir(os.path.join(guide, "docs", "objects")):
        sys.stderr.write(f"error: no object pages under {guide}\n")
        return 2
    if os.path.exists(args.output):
        sys.stderr.write(f"error: {args.output} already exists\n")
        return 2

    model_path = args.model or os.path.join(here, "objectmodel.json")
    model = json.load(open(model_path, encoding="utf-8"))
    order = {}
    for name, props in zip(model["Objects"], model["Properties"]):
        order[slugify(name)] = [p for p in props if p not in EXCLUDED_MEMBERS]
    netcontrol = apla_names(
        os.path.join(here, "ObjectMembers", "NetControl", "PropList.apla"))
    order["netcontrol"] = [p for p in netcontrol if p not in EXCLUDED_MEMBERS]

    shutil.copytree(guide, args.output)
    objdir = os.path.join(args.output, "docs", "objects")
    propdir = os.path.join(args.output, "docs", "properties")

    errors, changes, pageless = [], [], set()
    rewritten = 0
    for fn in sorted(os.listdir(objdir)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(objdir, fn)
        names = order.get(fn[:-3])
        lines = read(path).split("\n")
        prop_lines = [l for l in lines if l.startswith(PROP_LABELS)]

        if not names or not prop_lines:
            if names:
                errors.append(f"{fn}: model lists {len(names)} properties "
                              f"but the page has no Properties line")
            elif prop_lines:
                errors.append(f"{fn}: page has a Properties line but "
                              + ("the object is not in the model"
                                 if names is None else
                                 "the model lists no properties for it"))
            continue

        new = "\n".join(transform(lines, property_lines(names)))
        open(path, "w", encoding="utf-8", newline="\n").write(new)
        rewritten += 1

        old = list(dict.fromkeys(
            label for l in prop_lines for label, _ in LINK_RE.findall(l)))
        added = [n for n in names if n not in old]
        removed = [n for n in old if n not in names]
        if added:
            changes.append(f"{fn}: added {', '.join(added)}")
        if removed:
            changes.append(f"{fn}: removed {', '.join(removed)}")
        pageless.update(n for n in names if not os.path.exists(
            os.path.join(propdir, f"{slugify(n)}.md")))

    nfiles = sum(len(fs) for _, _, fs in os.walk(args.output))
    w = sys.stdout.write
    w(f"{nfiles} files written to {args.output}; "
      f"{rewritten} object pages rewritten, the rest copied verbatim\n")
    if changes:
        w("\nMembership changes (page now mirrors the model):\n")
        for c in changes:
            w(f"  {c}\n")
    if pageless:
        w("\nLinked properties with no page under properties/ "
          "(links are broken until the pages exist):\n")
        for n in sorted(pageless, key=str.lower):
            w(f"  {n}\n")
    if errors:
        w("\nErrors (pages copied verbatim, human decision needed):\n")
        for e in errors:
            w(f"  {e}\n")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
