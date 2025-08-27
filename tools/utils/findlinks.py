#!/usr/bin/env python3
"""
Find links in markdown files containing a specified substring.
This version uses the doc_utils module to iterate only through files in nav.
"""

import argparse
import os
import sys
from typing import List, Tuple

# Add the utils directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doc_utils import MkDocsRepo, LinkExtractor


def find_links_in_file(filepath: str, target_substring: str) -> List[Tuple[str, str]]:
    """
    Search a markdown file for links whose URL contains a specified substring.

    Args:
        filepath: Path to the markdown file to search
        target_substring: Substring to search for in the URLs

    Returns:
        List of (link_text, url) tuples where URL contains the target substring
    """
    results = []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return results

    # Use LinkExtractor to get links (excludes code blocks)
    links = LinkExtractor.extract_markdown_links(content)

    for link_text, url in links:
        if target_substring in url:
            results.append((link_text, url))

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find links in markdown files containing a specified substring."
    )
    parser.add_argument(
        "--target",
        default="json",
        help='Substring to search for in URLs (default: "json")',
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Root directory containing mkdocs.yml (default: current directory)",
    )

    args = parser.parse_args()
    target_substring = args.target
    root_dir = os.path.abspath(args.root)

    # Check if mkdocs.yml exists
    mkdocs_path = os.path.join(root_dir, "mkdocs.yml")
    if not os.path.exists(mkdocs_path):
        sys.exit(f"Error: mkdocs.yml not found at {mkdocs_path}")

    # Create MkDocsRepo instance
    repo = MkDocsRepo(root_dir)

    # Track files we've already processed (to avoid duplicates from print_mkdocs.yml)
    processed_files = set()
    total_links_found = 0

    print(
        f"Searching for links containing '{target_substring}' in navigation files...\n"
    )

    # Process main nav files
    for base_path, file_ref in repo.iter_nav_files():
        # Resolve to actual file path
        if file_ref.startswith("/"):
            file_path = os.path.join(base_path, file_ref[1:])
        else:
            file_path = os.path.join(base_path, "docs", file_ref)

        # Normalise path and skip if already processed
        file_path = os.path.normpath(file_path)
        if file_path in processed_files:
            continue
        processed_files.add(file_path)

        if not os.path.exists(file_path):
            continue

        # Find links in the file
        links = find_links_in_file(file_path, target_substring)

        if links:
            # Display relative path for cleaner output
            rel_path = os.path.relpath(file_path, root_dir)
            for link_text, url in links:
                print(f"{rel_path} : [{link_text}]({url})")
                total_links_found += 1

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Total files checked: {len(processed_files)}")
    print(f"Links found containing '{target_substring}': {total_links_found}")


if __name__ == "__main__":
    main()
