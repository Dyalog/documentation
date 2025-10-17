#!/usr/bin/env python3
"""
Find and report admonitions in markdown files.

This script:
1. Scans all markdown files in the documentation
2. Identifies admonition blocks (note, info, warning, hint, legacy, etc.)
3. Reports usage statistics and locations

Admonitions are special callout blocks in markdown that render with icons and colors.
They use the syntax:

    !!! type "Optional Title"
        Content here

or collapsible version:

    ??? type "Optional Title"
        Content here

Supported admonition types (from pdf/assets/styles/admonitions.css):
- note: General notes and observations
- info: Informational content
- warning: Important warnings
- hint: Tips and suggestions
- legacy: Deprecated or legacy features
- linux/unix/macos/windows: OS-specific notes

Usage:
    python find_admonitions.py [--output report.yaml] [--root-dir /path/to/docs]

Output:
    YAML report with:
    - summary: Total counts by type
    - by_file: Admonitions grouped by file
    - by_type: Admonitions grouped by type

Example:
    python find_admonitions.py --output admonitions.yaml --root-dir ..
"""

import argparse
import os
import sys
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))

from doc_utils import MkDocsRepo, AdmonitionReference, AdmonitionExtractor
from ruamel.yaml import YAML


class AdmonitionFinder:
    """Find admonitions in markdown files."""

    def __init__(self, root_dir: str, filter_contains: str = None, case_sensitive: bool = False,
                 filter_types: Set[str] = None):
        self.root_dir = os.path.abspath(root_dir)
        self.repo = MkDocsRepo(root_dir)
        self.filter_contains = filter_contains
        self.case_sensitive = case_sensitive
        self.filter_types = set(t.lower() for t in filter_types) if filter_types else None
        self.by_file: Dict[str, List[AdmonitionReference]] = defaultdict(list)
        self.by_type: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.total_admonitions = 0
        self.filtered_count = 0
        self.type_counts: Dict[str, int] = defaultdict(int)
        self.collapsible_count = 0
        self.unknown_types: Set[str] = set()

    def extract_admonitions(self, md_file: str) -> List[AdmonitionReference]:
        """
        Extract all admonition blocks from a markdown file, applying filters.

        Args:
            md_file: Path to the markdown file

        Returns:
            List of AdmonitionReference objects
        """
        # Use the shared extractor from doc_utils
        admonitions = AdmonitionExtractor.extract_admonitions(
            md_file,
            filter_types=self.filter_types,
            filter_contains=self.filter_contains,
            case_sensitive=self.case_sensitive
        )

        # Track unknown types
        unknown = AdmonitionExtractor.get_unknown_types(admonitions)
        self.unknown_types.update(unknown)

        return admonitions

    def scan_all(self):
        """Scan all markdown files in the repository."""
        filter_parts = []
        if self.filter_types:
            filter_parts.append(f"types: {', '.join(sorted(self.filter_types))}")
        if self.filter_contains:
            content_filter = f'contains: "{self.filter_contains}"'
            if self.case_sensitive:
                content_filter += ' (case-sensitive)'
            filter_parts.append(content_filter)

        if filter_parts:
            filter_msg = f" (filtering: {'; '.join(filter_parts)})"
            print(f"Scanning markdown files for admonitions{filter_msg}...")
        else:
            print("Scanning markdown files for admonitions...")

        total_before_filter = 0

        for md_file in self.repo.iter_all_markdown_files():
            admonitions = self.extract_admonitions(md_file)

            if admonitions:
                rel_path = os.path.relpath(md_file, self.root_dir)
                self.by_file[rel_path] = admonitions

                for adm in admonitions:
                    self.total_admonitions += 1
                    self.type_counts[adm.adm_type] += 1
                    self.by_type[adm.adm_type].append((rel_path, adm.line_number))

                    if adm.is_collapsible:
                        self.collapsible_count += 1

        if self.filter_contains or self.filter_types:
            print(f"Found {self.total_admonitions} matching admonitions in {len(self.by_file)} files")
        else:
            print(f"Found {self.total_admonitions} admonitions in {len(self.by_file)} files")

    def print_summary(self):
        """Print a summary of findings."""
        print("\n" + "=" * 70)
        print("ADMONITION USAGE SUMMARY")
        print("=" * 70)

        # Display active filters
        if self.filter_types or self.filter_contains:
            print("Active filters:")
            if self.filter_types:
                print(f"  Types: {', '.join(sorted(self.filter_types))}")
            if self.filter_contains:
                print(f"  Contains: '{self.filter_contains}'" +
                      (" (case-sensitive)" if self.case_sensitive else ""))
            print()

        print(f"Total admonitions: {self.total_admonitions}")
        print(f"Files with admonitions: {len(self.by_file)}")
        print(f"Collapsible (???) admonitions: {self.collapsible_count}")
        print(f"Static (!!!) admonitions: {self.total_admonitions - self.collapsible_count}")

        if self.type_counts:
            print("\nAdmonitions by type:")
            # Sort by count descending
            sorted_types = sorted(self.type_counts.items(), key=lambda x: x[1], reverse=True)
            for adm_type, count in sorted_types:
                status = "" if adm_type in AdmonitionExtractor.KNOWN_TYPES else " (unknown type)"
                print(f"  {adm_type:15} : {count:4}{status}")

        if self.unknown_types:
            print(f"\nUnknown admonition types found: {len(self.unknown_types)}")
            print("  These may not have styling defined in admonitions.css:")
            for unknown in sorted(self.unknown_types):
                print(f"    - {unknown}")

        if self.by_file:
            print(f"\nTop files by admonition count (first 10):")
            sorted_files = sorted(self.by_file.items(),
                                key=lambda x: len(x[1]), reverse=True)
            for i, (file_path, adms) in enumerate(sorted_files[:10], 1):
                type_summary = {}
                for adm in adms:
                    type_summary[adm.adm_type] = type_summary.get(adm.adm_type, 0) + 1
                types_str = ", ".join(f"{t}:{c}" for t, c in sorted(type_summary.items()))
                print(f"  {i:2}. {file_path}")
                print(f"      Count: {len(adms)} ({types_str})")

    def write_report(self, output_file: str):
        """Write findings to a YAML file."""
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.width = 120
        yaml.preserve_quotes = True

        # Convert by_file to serializable format
        by_file_dict = {}
        for file_path, adms in self.by_file.items():
            by_file_dict[file_path] = [
                {
                    'line': adm.line_number,
                    'type': adm.adm_type,
                    'title': adm.title,
                    'collapsible': adm.is_collapsible,
                    'text': adm.raw_text,
                    'body': adm.body
                }
                for adm in adms
            ]

        # Convert by_type to serializable format
        by_type_dict = {}
        for adm_type, locations in self.by_type.items():
            by_type_dict[adm_type] = [
                f"{file_path}:{line_num}"
                for file_path, line_num in sorted(locations)
            ]

        summary = {
            'total_admonitions': self.total_admonitions,
            'files_with_admonitions': len(self.by_file),
            'collapsible_count': self.collapsible_count,
            'static_count': self.total_admonitions - self.collapsible_count,
            'unique_types': len(self.type_counts),
            'unknown_types': sorted(list(self.unknown_types)) if self.unknown_types else []
        }

        # Add filter info if used
        if self.filter_types or self.filter_contains:
            summary['filter'] = {}
            if self.filter_types:
                summary['filter']['types'] = sorted(list(self.filter_types))
            if self.filter_contains:
                summary['filter']['contains'] = self.filter_contains
                summary['filter']['case_sensitive'] = self.case_sensitive

        report = {
            'summary': summary,
            'type_counts': dict(sorted(self.type_counts.items(),
                                      key=lambda x: x[1], reverse=True)),
            'by_file': by_file_dict,
            'by_type': by_type_dict
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(report, f)

        print(f"\nDetailed report written to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Find and report admonitions in markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan from documentation root
  python find_admonitions.py

  # When running from tools/ subdirectory
  python find_admonitions.py --root-dir ..

  # Scan and save report
  python find_admonitions.py --output admonitions.yaml

  # Filter by type
  python find_admonitions.py --type warning,note

  # Filter by multiple types
  python find_admonitions.py --type "warning,hint,info"

  # Find admonitions containing specific text
  python find_admonitions.py --contains "strong INTERRUPT"

  # Case-sensitive search
  python find_admonitions.py --contains "INTERRUPT" --case-sensitive

  # Combine type and content filters
  python find_admonitions.py --type warning --contains "deprecated"

  # Complex filter example
  python find_admonitions.py --root-dir /path/to/docs --type "warning,note" --contains "deprecated" --output /tmp/filtered.yaml

Admonition types supported (from admonitions.css):
  note, info, warning, hint, legacy, linux, unix, macos, windows

Output format:
  The YAML report includes:
  - summary: Overall statistics (with filter info if used)
  - type_counts: Count of each admonition type
  - by_file: Admonitions organized by file location (with body content)
  - by_type: Files using each admonition type
        """
    )

    parser.add_argument(
        '--root-dir',
        type=str,
        default='.',
        help='Root directory of the documentation (default: current directory)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='admonitions.yaml',
        help='Output YAML file for the report (default: admonitions.yaml)'
    )

    parser.add_argument(
        '--type',
        type=str,
        default=None,
        help='Filter by admonition type(s), comma-separated (e.g., "warning,note")'
    )

    parser.add_argument(
        '--contains',
        type=str,
        default=None,
        help='Filter admonitions to only those containing this text in their body'
    )

    parser.add_argument(
        '--case-sensitive',
        action='store_true',
        help='Make the --contains filter case-sensitive (default: case-insensitive)'
    )

    args = parser.parse_args()

    # Parse type filter
    filter_types = None
    if args.type:
        filter_types = set(t.strip() for t in args.type.split(',') if t.strip())

    # Resolve root directory
    root_dir = os.path.abspath(args.root_dir)

    if not os.path.exists(os.path.join(root_dir, 'mkdocs.yml')):
        print(f"Error: {root_dir} does not appear to be a mkdocs documentation root",
              file=sys.stderr)
        print("       (mkdocs.yml not found)", file=sys.stderr)
        sys.exit(1)

    # Run scan
    finder = AdmonitionFinder(root_dir,
                             filter_contains=args.contains,
                             case_sensitive=args.case_sensitive,
                             filter_types=filter_types)
    finder.scan_all()

    # Print summary
    finder.print_summary()

    # Write report
    finder.write_report(args.output)


if __name__ == '__main__':
    main()
