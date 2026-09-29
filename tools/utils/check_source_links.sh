#!/usr/bin/env bash
#
# Validate internal documentation links with ghost (https://github.com/xpqz/ghost).
#
# ghost resolves links exactly as MkDocs renders the monorepo (cross-subsite
# includes, the docs/ URL stripping, directory-style links, anchors), so it
# catches the ../ depth and #fragment mistakes that plain greps miss.
#
# Usage:
#   tools/utils/check_source_links.sh                 # gate: fail on broken links/anchors in files changed vs origin/main
#   tools/utils/check_source_links.sh --changed REF   # ... changed vs REF (a branch or commit)
#   tools/utils/check_source_links.sh --all           # report every broken link/anchor in the whole monorepo
#
# The gate mode only fails on items whose SOURCE file is part of the change set,
# so it flags regressions without tripping over the pre-existing backlog.
#
# ghost is found on PATH, or via $GHOST, or built from source with cargo if absent.
#
# This checks the links in the markdown source. check_links.py, in this directory,
# spiders a deployed site over HTTP instead, so it needs a deployment to test.
set -euo pipefail

GHOST_VERSION="v0.2.0"

cd "$(git rev-parse --show-toplevel)"

mode="changed"
base="origin/main"
while [ $# -gt 0 ]; do
  case "$1" in
    --all)     mode="all" ;;
    --changed) mode="changed"; base="${2:-origin/main}"; shift ;;
    -h|--help) awk 'NR>1 && /^#/ {print; next} NR>1 {exit}' "$0"; exit 0 ;;
    *) echo "check_source_links: unknown argument '$1'" >&2; exit 2 ;;
  esac
  shift
done

# Locate ghost: $GHOST override, then PATH, then build from source.
ghost_bin="${GHOST:-}"
if [ -z "$ghost_bin" ]; then
  if command -v ghost >/dev/null 2>&1; then
    ghost_bin="ghost"
  else
    echo "check_source_links: ghost not found; building ${GHOST_VERSION} with cargo..." >&2
    cargo install --git https://github.com/xpqz/ghost --tag "$GHOST_VERSION" ghost-cli >&2
    ghost_bin="$HOME/.cargo/bin/ghost"
  fi
fi

# ghost requires --help-urls, but link checking does not use it; an empty header is fine.
help_urls="$(mktemp)"
trap 'rm -f "$help_urls"' EXIT

# Collect "source -> target" item lines from the broken-links and broken-anchors reports.
# Item lines look like "  path/to/page.md -> target" with an optional "[H] " tag.
# ghost exits non-zero when it finds issues; that is expected, so do not let it
# abort the script (set -e / pipefail). Capture the report regardless.
items="$(
  { "$ghost_bin" --mkdocs-yaml mkdocs.yml --help-urls "$help_urls" --broken-links --broken-anchors 2>/dev/null || true; } \
    | sed -nE 's/^[[:space:]]+(\[[A-Z]\] )?([^[:space:]]+) -> (.*)$/\2 -> \3/p'
)"

if [ "$mode" = "all" ]; then
  if [ -n "$items" ]; then
    echo "Broken links/anchors in the monorepo ($(printf '%s\n' "$items" | grep -c .)):"
    printf '%s\n' "$items" | sed 's/^/  /'
    exit 1
  fi
  echo "No broken links or anchors."
  exit 0
fi

# Gate mode: only fail on items whose source file changed vs $base.
changed="$(git diff --name-only --diff-filter=d "$base"...HEAD -- '*.md' '*/mkdocs.yml' mkdocs.yml 2>/dev/null || true)"
if [ -z "$changed" ]; then
  echo "check_source_links: no changed markdown files vs $base; nothing to check."
  exit 0
fi

hits=""
while IFS= read -r line; do
  [ -n "$line" ] || continue
  src="${line%% -> *}"
  src="${src#./}"   # ghost prefixes ./ with a relative mkdocs.yml; git diff does not
  if printf '%s\n' "$changed" | grep -qxF "$src"; then
    hits="${hits}  ${line}"$'\n'
  fi
done <<< "$items"

if [ -n "$hits" ]; then
  echo "Broken links/anchors introduced in changed files (vs $base):"
  printf '%s' "$hits"
  cat >&2 <<'EOF'

How to fix (see https://github.com/xpqz/ghost):
  - Within a guide (sub-site): use the file form with the .md extension, e.g.
      [Notes](../primitive-functions/notes.md)          # always safe
  - Across guides: use the extension-less directory form with the right depth:
      regular page  -> (dir-depth + 2) ../
      index.md page -> (dir-depth + 1) ../   # index pages render one level shallower
  - Anchors: the #fragment must match a heading's generated slug on the target page.
EOF
  exit 1
fi

echo "check_source_links: no broken links or anchors in changed files (vs $base)."
