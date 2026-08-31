#!/usr/bin/env python3
"""Check MkDocs admonitions against the Dyalog documentation guidelines.

Every line that begins with `!!!` (optionally indented) must name one of the
fixed admonition types and carry its exact required quoted title, for example:

    !!! Info "Information"

The fixed type -> title set is defined in the guidelines (the documentation-
guidelines repository, docs/style.md, "Note types"). The type name is matched
case-insensitively, but the quoted title is mandatory and must match exactly;
"note" is not a valid type at all. Lines inside fenced code blocks
(``` ... ```) are ignored, since those are illustrative rather than real
admonitions.

Usage:
    scripts/check-admonitions.py [PATH ...]   # files or directories; default: .

Reports each offending line as "path:line: reason" and exits non-zero if any
admonition is non-compliant.
"""
import os
import re
import sys

# type -> set of allowed exact titles (guidelines: docs/style.md "Note types").
VALID = {
    "Hint": {"Hints and Recommendations"},
    "Info": {"Information"},
    "Warning": {"Warning"},
    "Legacy": {"Legacy"},
    "linux": {"Dyalog on Linux"},
    "unix": {"Dyalog on UNIX", "Dyalog on AIX"},
    "macos": {"Dyalog on macOS"},
    "windows": {"Dyalog on Microsoft Windows"},
}

BANG = re.compile(r'^\s*!!!\+?\s*(.*)$')             # an admonition marker line
FENCE = re.compile(r'^\s*(```+|~~~+)')               # fenced code block delimiter
PARSE = re.compile(r'^(\S+)(?:\s+"([^"]*)")?\s*$')   # <type> optionally "<title>"


def check_file(path):
    problems = []
    in_fence = False
    try:
        text = open(path, encoding='utf-8').read()
    except (UnicodeDecodeError, OSError):
        return problems
    for n, line in enumerate(text.split('\n'), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = BANG.match(line)
        if not m:
            continue
        rest = m.group(1).strip()
        if not rest:
            problems.append((n, "`!!!` with no type or title"))
            continue
        p = PARSE.match(rest)
        if not p:
            problems.append((n, f"malformed admonition header: {rest!r}"))
            continue
        atype, title = p.group(1), p.group(2)
        canon = next((t for t in VALID if t.lower() == atype.lower()), None)  # type is case-insensitive
        if canon is None:
            problems.append((n, f"unknown type {atype!r} (valid: {', '.join(sorted(VALID))})"))
            continue
        if title is None:
            problems.append((n, f"type {atype!r} is missing its quoted title (expected {sorted(VALID[canon])})"))
            continue
        if title not in VALID[canon]:
            want = ' or '.join(f'"{t}"' for t in sorted(VALID[canon]))
            problems.append((n, f'type {atype!r} has title "{title}"; guidelines require {want}'))
    return problems


def iter_md(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, files in os.walk(p):
                for f in files:
                    if f.endswith('.md'):
                        yield os.path.join(root, f)
        elif p.endswith('.md') and os.path.isfile(p):
            yield p


def main(argv):
    paths = argv[1:] or ['.']
    total = 0
    for path in sorted(iter_md(paths)):
        for n, msg in check_file(path):
            print(f"{path}:{n}: {msg}")
            total += 1
    if total:
        print(f"\n{total} admonition issue(s).", file=sys.stderr)
        return 1
    print("Admonitions OK.")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
