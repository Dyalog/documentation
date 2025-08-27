#!/usr/bin/env python3
"""
Check for dangling local links in markdown files referenced in mkdocs.yml navigation.
"""

import os
import sys
import argparse
from doc_utils import MkDocsRepo, LinkExtractor, LinkValidator, SummaryReporter


def is_internal_non_anchor_link(url):
    """Check if a URL is internal and not just an anchor."""
    return (
        not url.startswith(("http://", "https://", "#", "mailto:"))
        and url != ""
        and not url.startswith("javascript:")
    )


def check_file_links(file_path, root_dir, site_mappings, verbose=False):
    """Check all links in a single markdown file."""
    dangling_links = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        if verbose:
            print(f"Error reading {file_path}: {e}")
        return dangling_links

    # Extract all links from the file
    links = LinkExtractor.extract_markdown_links(content)

    for link_text, link_url in links:
        # Skip external links, anchors, and special links
        if not is_internal_non_anchor_link(link_url):
            continue

        # Remove anchor from URL if present
        if "#" in link_url:
            link_url_no_anchor = link_url.split("#")[0]
        else:
            link_url_no_anchor = link_url

        # Remove query parameters
        if "?" in link_url_no_anchor:
            link_url_no_anchor = link_url_no_anchor.split("?")[0]

        # Check if the link is valid
        is_valid = LinkValidator.is_valid_relative_path(
            file_path, link_url_no_anchor, root_dir, site_mappings
        )
        if not is_valid:
            dangling_links.append((link_text, link_url))

    return dangling_links


def check_dangling_links(
    directory,
    mkdocs_file=None,
    target_subsite=None,
    stats_only=False,
    debug=False,
    verbose=False,
):
    # Initialise repo
    repo = MkDocsRepo(directory)

    # Get navigation files to check
    nav_files = []
    for base_path, file_ref in repo.iter_nav_files(target_subsite):
        file_path = repo.resolver.markdown_file_path(base_path, file_ref)

        # If target_subsite is specified, only include files from that subsite
        if target_subsite:
            file_subsite = repo.determine_file_subsite(file_path)
            if file_subsite != target_subsite:
                continue

        if os.path.exists(file_path):
            nav_files.append(file_path)
        elif debug:
            print(f"Warning: Navigation file does not exist: {file_path}")

    # Get site mappings for cross-reference resolution
    site_mappings = repo.site_mappings

    if debug:
        print(f"Site mappings available: {sorted(site_mappings.keys())}")

    # Statistics
    total_files = len(nav_files)
    total_links = 0
    dangling_links = []
    subsite_stats = {}

    # Check each file
    for i, file_path in enumerate(nav_files, 1):
        relative_path = os.path.relpath(file_path, directory)
        if not stats_only:
            print(f"Checking file [{i}/{total_files}]: {relative_path}", end="\r")

        # Check links in this file
        file_dangling = check_file_links(file_path, directory, site_mappings, verbose)

        # Count total links
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            all_links = LinkExtractor.extract_markdown_links(content)
            total_links += len(all_links)
        except:
            pass

        if file_dangling:
            # Determine subsite
            subsite = repo.determine_file_subsite(file_path)

            if stats_only:
                # Just count for stats
                if subsite not in subsite_stats:
                    subsite_stats[subsite] = 0
                subsite_stats[subsite] += len(file_dangling)
            else:
                # Full reporting
                for link_text, link_url in file_dangling:
                    dangling_links.append((file_path, link_text, link_url))

    # Report results
    if stats_only:
        print("\n\nSubsite Statistics:")
        print("-------------------")
        total_dangling = sum(subsite_stats.values())

        if target_subsite:
            # Only show stats for the target subsite
            count = subsite_stats.get(target_subsite, 0)
            print(f"{target_subsite}: {count}")
            print(f"\nTotal dangling links: {count}")
        else:
            # Show stats for all subsites
            for subsite in sorted(subsite_stats.keys()):
                if subsite_stats[subsite] > 0:
                    print(f"{subsite}: {subsite_stats[subsite]}")
            print(f"\nTotal dangling links: {total_dangling}")
    else:
        print("\n\nLink check complete!")
        print(f"Total files checked: {total_files}")
        print(f"Total links found: {total_links}")
        print(f"Dangling links found: {len(dangling_links)}")

        if dangling_links:
            print("\nDangling Links:")
            print("---------------")
            for source_file, link_text, link_url in dangling_links:
                rel_source = os.path.relpath(source_file, directory)
                link_display = (
                    f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                )
                print(f"File: {rel_source}")
                print(f"  Raw link: {link_display}")
                # Try to show what path was checked
                source_dir = os.path.dirname(source_file)
                if "#" in link_url:
                    clean_url = link_url.split("#")[0]
                else:
                    clean_url = link_url
                target_path = os.path.join(source_dir, clean_url)
                print(f"  Target not found: {os.path.relpath(target_path, directory)}")
                print()

    return dangling_links


def main():
    parser = argparse.ArgumentParser(
        description="Check for dangling local links in markdown files referenced in mkdocs.yml navigation."
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Directory containing mkdocs.yml (defaults to current directory)",
    )
    parser.add_argument(
        "--mkdocs", help="Path to mkdocs.yml file (defaults to DIR/mkdocs.yml)"
    )
    parser.add_argument(
        "--subsite",
        help="Check only a specific subsite (e.g., windows-installation-and-configuration-guide)",
    )
    parser.add_argument(
        "--stats", action="store_true", help="Show only statistics per subsite"
    )
    parser.add_argument(
        "--output", help="Write results to this file instead of console"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print more detailed information"
    )
    parser.add_argument(
        "--debug", action="store_true", help="Show debug information during processing"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"Error: '{args.dir}' is not a valid directory.")
        return

    # Determine the mkdocs file path
    mkdocs_path = args.mkdocs
    if not mkdocs_path:
        mkdocs_path = os.path.join(args.dir, "mkdocs.yml")
        if not os.path.isfile(mkdocs_path):
            print(f"Error: No mkdocs.yml found at '{mkdocs_path}'")
            return
    elif not os.path.isfile(mkdocs_path):
        print(f"Error: Specified mkdocs.yml not found at '{mkdocs_path}'")
        return

    # Redirect output to file if specified
    if args.output:
        original_stdout = sys.stdout
        with open(args.output, "w", encoding="utf-8") as f:
            sys.stdout = f
            dangling_links = check_dangling_links(
                args.dir,
                mkdocs_path,
                args.subsite,
                args.stats,
                args.debug,
                args.verbose,
            )
            sys.stdout = original_stdout
        print(f"Results written to {args.output}")
    else:
        dangling_links = check_dangling_links(
            args.dir, mkdocs_path, args.subsite, args.stats, args.debug, args.verbose
        )

    # Exit with error code if dangling links found
    if dangling_links:
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
