#!/usr/bin/env python3
"""
Locate markdown sources that contain footnotes.

The script scans every markdown file reachable from a mkdocs-style repository
and reports those that use footnote references (``[^label]``) or definitions
(``[^label]:``). Each file is listed once, regardless of how many footnotes it
contains.
"""

import argparse
import os
import sys
from collections import defaultdict
from typing import Dict, List

# Ensure doc_utils can be imported when the script is executed from any location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from doc_utils import MkDocsRepo, FootnoteExtractor, FootnoteReference  # noqa: E402


class FootnoteFinder:
    """Scan markdown files for footnote usage."""

    def __init__(self, root_dir: str, include_references: bool = True, include_definitions: bool = True):
        self.root_dir = os.path.abspath(root_dir)
        self.repo = MkDocsRepo(self.root_dir)
        self.include_references = include_references
        self.include_definitions = include_definitions
        self.files_with_footnotes: Dict[str, List[FootnoteReference]] = defaultdict(list)

    def scan(self) -> None:
        """Scan every markdown file and record those containing footnotes."""
        for md_file in self.repo.iter_all_markdown_files():
            footnotes = FootnoteExtractor.extract_footnotes(
                md_file,
                include_references=self.include_references,
                include_definitions=self.include_definitions,
            )
            if footnotes:
                rel_path = os.path.relpath(md_file, self.root_dir)
                self.files_with_footnotes[rel_path] = footnotes

    def render_report(self, show_counts: bool = False) -> None:
        """Print a summary of files that contain footnotes."""
        total_files = len(self.files_with_footnotes)
        total_occurrences = sum(len(v) for v in self.files_with_footnotes.values())

        if total_files == 0:
            print("No footnotes found in markdown sources.")
            return

        scope_parts = []
        if not self.include_references:
            scope_parts.append("definitions only")
        if not self.include_definitions:
            scope_parts.append("references only")
        scope_desc = f" ({', '.join(scope_parts)})" if scope_parts else ""

        print(f"Found {total_files} markdown file(s) containing footnotes{scope_desc}.")
        if show_counts:
            print(f"Total footnote occurrences recorded: {total_occurrences}")

        print("\nFiles:")
        for path in sorted(self.files_with_footnotes.keys()):
            if show_counts:
                refs = self.files_with_footnotes[path]
                def_count = sum(1 for item in refs if item.is_definition)
                ref_count = len(refs) - def_count
                print(f"  - {path} (definitions: {def_count}, references: {ref_count}, total: {len(refs)})")
            else:
                print(f"  - {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List markdown sources that contain footnotes.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--root-dir",
        default=".",
        help="Root directory of the documentation (must contain mkdocs.yml).",
    )
    parser.add_argument(
        "--definitions-only",
        action="store_true",
        help="Only consider footnote definition blocks (ignore inline references).",
    )
    parser.add_argument(
        "--references-only",
        action="store_true",
        help="Only consider inline footnote references (ignore definitions).",
    )
    parser.add_argument(
        "--show-counts",
        action="store_true",
        help="Show reference/definition counts for each file.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    root_dir = os.path.abspath(args.root_dir)
    mkdocs_config = os.path.join(root_dir, "mkdocs.yml")
    if not os.path.exists(mkdocs_config):
        print(f"Error: {root_dir} does not appear to contain mkdocs.yml", file=sys.stderr)
        sys.exit(1)

    include_definitions = not args.references_only
    include_references = not args.definitions_only

    if not include_definitions and not include_references:
        print("Error: At least one of definitions or references must be included.", file=sys.stderr)
        sys.exit(1)

    finder = FootnoteFinder(
        root_dir=root_dir,
        include_references=include_references,
        include_definitions=include_definitions,
    )
    finder.scan()
    finder.render_report(show_counts=args.show_counts)


if __name__ == "__main__":
    main()
