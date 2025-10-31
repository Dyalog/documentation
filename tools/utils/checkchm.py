#!/usr/bin/env python3

from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


@dataclass
class HelpUrlEntry:
    key: str
    expression: str
    relative_path: str
    source_line: int


@dataclass
class ResolvedEntry:
    entry: HelpUrlEntry
    found_path: Path | None
    dropped_segments: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify CHM help URLs against generated project files.")
    parser.add_argument(
        "--help_urls",
        required=True,
        type=Path,
        help="Path to help_urls.h",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Root directory that contains chm/project (defaults to repository root).",
    )
    return parser.parse_args()


def strip_line_comment(line: str) -> str:
    """Remove // comments while respecting string literals."""
    result = []
    in_string = False
    escape = False
    idx = 0
    while idx < len(line):
        ch = line[idx]
        if not in_string and ch == "/" and idx + 1 < len(line) and line[idx + 1] == "/":
            break
        result.append(ch)
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
                escape = False
        idx += 1
    return "".join(result)


def split_args(arguments: str) -> Tuple[str, str]:
    """Split HELP_URL arguments into two parts."""
    parts: List[str] = []
    current: List[str] = []
    in_string = False
    escape = False
    for ch in arguments:
        if in_string:
            current.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
            current.append(ch)
            continue
        if ch == ",":
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    parts.append("".join(current).strip())
    if len(parts) != 2:
        raise ValueError(f"Unexpected HELP_URL signature: {arguments!r}")
    return parts[0], parts[1]


def parse_string_literal(literal: str) -> str:
    try:
        return ast.literal_eval(literal)
    except Exception as exc:  # pragma: no cover - defensive
        raise ValueError(f"Failed to parse string literal {literal!r}") from exc


def expand_expression(expr: str, macros: Dict[str, str]) -> str:
    result: List[str] = []
    idx = 0
    length = len(expr)
    while idx < length:
        ch = expr[idx]
        if ch.isspace():
            idx += 1
            continue
        if ch == '"':
            end = idx + 1
            escape = False
            while end < length:
                cur = expr[end]
                if escape:
                    escape = False
                elif cur == "\\":
                    escape = True
                elif cur == '"':
                    break
                end += 1
            else:  # pragma: no cover - malformed literal safeguard
                raise ValueError(f"Unterminated string literal in {expr!r}")
            literal = expr[idx : end + 1]
            result.append(parse_string_literal(literal))
            idx = end + 1
            continue
        start = idx
        while idx < length and (expr[idx].isalnum() or expr[idx] == "_"):
            idx += 1
        if start == idx:
            raise ValueError(f"Unexpected character {expr[idx]!r} in expression {expr!r}")
        macro_name = expr[start:idx]
        if macro_name not in macros:
            raise KeyError(f"Unknown macro {macro_name} in expression {expr!r}")
        result.append(macros[macro_name])
    return "".join(result)


def parse_help_urls(lines: Iterable[str]) -> Tuple[List[HelpUrlEntry], Dict[str, str]]:
    macros: Dict[str, str] = {}
    entries: List[HelpUrlEntry] = []
    active_stack: List[bool] = [True]
    for lineno, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if stripped.startswith("#if"):
            condition_text = stripped[3:].strip()
            parent_active = active_stack[-1]
            condition_value = 0
            if condition_text:
                try:
                    condition_value = int(condition_text, 0)
                except ValueError:
                    condition_value = 1  # treat non-numeric as true
            active_stack.append(parent_active and condition_value != 0)
            continue
        if stripped.startswith("#endif"):
            if len(active_stack) == 1:
                raise ValueError(f"Unmatched #endif on line {lineno}")
            active_stack.pop()
            continue
        if not active_stack[-1]:
            continue

        line_no_comment = strip_line_comment(raw_line).strip()
        if not line_no_comment:
            continue

        if line_no_comment.startswith("#define"):
            parts = line_no_comment.split(None, 2)
            if len(parts) < 3:
                raise ValueError(f"Unable to parse macro definition on line {lineno}: {raw_line.strip()}")
            macro_name = parts[1]
            macro_value = parse_string_literal(parts[2])
            macros[macro_name] = macro_value
            continue

        if "HELP_URL" not in line_no_comment:
            continue

        call_text = line_no_comment[line_no_comment.index("HELP_URL") :]
        args_start = call_text.find("(")
        args_end = call_text.rfind(")")
        if args_start == -1 or args_end == -1 or args_end <= args_start:
            raise ValueError(f"Malformed HELP_URL invocation on line {lineno}: {call_text}")
        args = call_text[args_start + 1 : args_end]
        raw_key, expression = split_args(args)
        key = parse_string_literal(raw_key)
        expanded = expand_expression(expression, macros).rstrip("/") + ".htm"
        entries.append(HelpUrlEntry(key=key, expression=expression, relative_path=expanded, source_line=lineno))

    if len(active_stack) != 1:
        raise ValueError("Unbalanced preprocessor directives in help_urls file")
    return entries, macros


def resolve_entry(entry: HelpUrlEntry, project_root: Path) -> ResolvedEntry:
    relative = Path(entry.relative_path)
    candidate = project_root / relative
    if candidate.exists():
        return ResolvedEntry(entry=entry, found_path=candidate, dropped_segments=0)
    parts = relative.parts
    for dropped in range(1, len(parts)):
        candidate = project_root.joinpath(*parts[dropped:])
        if candidate.exists():
            return ResolvedEntry(entry=entry, found_path=candidate, dropped_segments=dropped)
    return ResolvedEntry(entry=entry, found_path=None, dropped_segments=len(parts))


def main() -> int:
    args = parse_args()
    help_urls_path = args.help_urls.resolve()
    if not help_urls_path.is_file():
        print(f"error: {help_urls_path} does not exist or is not a file", file=sys.stderr)
        return 2

    repo_root = args.project_root.resolve() if args.project_root else help_urls_path.parents[1]
    project_root = repo_root / "chm" / "project"
    if not project_root.is_dir():
        print(f"error: {project_root} is not a directory", file=sys.stderr)
        return 2

    entries, _ = parse_help_urls(help_urls_path.read_text(encoding="utf-8").splitlines())
    resolved_entries = [resolve_entry(entry, project_root) for entry in entries]

    missing = [item for item in resolved_entries if item.found_path is None]
    trimmed = [item for item in resolved_entries if item.found_path is not None and item.dropped_segments > 0]

    if missing:
        print("Missing files:", file=sys.stderr)
        for item in missing:
            print(
                f"  {item.entry.relative_path} (from {item.entry.key!r} on line {item.entry.source_line})",
                file=sys.stderr,
            )
    if trimmed:
        print("Resolved after dropping leading segments:")
        for item in trimmed:
            found_rel = item.found_path.relative_to(project_root)
            print(
                f"  {item.entry.relative_path} -> {found_rel} (dropped {item.dropped_segments} segment(s))"
            )

    total = len(entries)
    print(f"Checked {total} HELP_URL entries; {len(missing)} missing; {len(trimmed)} trimmed.")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
