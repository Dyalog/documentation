#!/usr/bin/env bash
#
# Validate MkDocs admonitions against the Dyalog documentation guidelines.
#
# Every admonition must be written as `!!! <type> "<exact title>"`, using one of
# the fixed types (Hint, Info, Warning, Legacy, linux, unix, macos, windows),
# whose name is matched case-insensitively, each with its required exact title;
# "note" is not a valid type. The check itself is performed by
# scripts/check-admonitions.py; this wrapper selects which files to check.
#
# Usage:
#   scripts/check-admonitions.sh                 # gate: fail on non-compliant admonitions in files changed vs origin/main
#   scripts/check-admonitions.sh --changed REF   # ... changed vs REF (a branch or commit)
#   scripts/check-admonitions.sh --all           # report every non-compliant admonition in the whole monorepo
#
# The gate mode only checks changed markdown files, so it flags regressions
# without tripping over the pre-existing backlog.
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

mode="changed"
base="origin/main"
while [ $# -gt 0 ]; do
  case "$1" in
    --all)     mode="all" ;;
    --changed) mode="changed"; base="${2:-origin/main}"; shift ;;
    -h|--help) sed -n '2,17p' "$0"; exit 0 ;;
    *) echo "check-admonitions: unknown argument '$1'" >&2; exit 2 ;;
  esac
  shift
done

checker="$(cd "$(dirname "$0")" && pwd)/check-admonitions.py"

if [ "$mode" = "all" ]; then
  exec python3 "$checker" .
fi

# Gate mode: only check markdown files changed vs $base.
mapfile -t changed < <(git diff --name-only --diff-filter=d "$base"...HEAD -- '*.md' 2>/dev/null || true)
if [ "${#changed[@]}" -eq 0 ]; then
  echo "check-admonitions: no changed markdown files vs $base; nothing to check."
  exit 0
fi
exec python3 "$checker" "${changed[@]}"
