#!/usr/bin/env python3
"""
find_orphans.py - Find truly orphaned markdown files

Finds markdown pages that are invisible in ALL output formats:
- MkDocs (standard and print configurations)
- PDF builds
- CHM builds
- Not referenced by any markdown or HTML links
- Not referenced in C header help_urls files

Files named index.md are excluded (intentional landing pages).

A file is NOT an orphan if it's referenced by:
1. Any mkdocs.yml nav section (standard or print_mkdocs.yml)
2. Any markdown link from another file
3. Any HTML link in converted HTML
4. CHM welcome.md (special case)
5. PDF configuration files
6. C header HELP_URL() macros (if --help_urls specified)

This correctly handles files like those in object-reference that are only
accessible via links, not nav entries.

Usage:
    # Local:
    python find_orphans.py --root /path/to/mkdocs.yml

    # Docker:
    docker compose run --rm utils python /utils/find_orphans.py --root /docs/mkdocs.yml

    # With help_urls file:
    python find_orphans.py --root mkdocs.yml --help_urls tools/help_urls.h

Options:
    --root PATH       Path to top-level mkdocs.yml (required)
    --output FILE     Write YAML report to file (optional)
    --help_urls FILE  Parse C header file for HELP_URL references (optional)
    --exclude LIST    Comma-separated subsites to exclude (optional)
    --verbose, -v     Show detailed progress
"""

import argparse
import os
import sys
import re
from pathlib import Path
from typing import Set, Dict, List, Tuple
from collections import defaultdict

# Add the utils directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doc_utils import MkDocsRepo, YAMLLoader, NavTraverser, LinkExtractor, HelpUrlsParser


class OrphanFinder:
    """Find orphaned markdown files across all output formats."""

    def __init__(self, root_yaml: Path, verbose: bool = False, exclude_subsites: Set[str] = None, help_urls_file: Path = None):
        self.root_yaml = root_yaml.resolve()
        self.root_dir = root_yaml.parent
        self.verbose = verbose
        self.exclude_subsites = exclude_subsites or set()
        self.help_urls_file = help_urls_file
        self.loader = YAMLLoader()
        self.repo = MkDocsRepo(str(self.root_dir))

        # Sets to track referenced files
        self.referenced_files: Set[Path] = set()
        self.all_md_files: Set[Path] = set()
        self.docs_roots: Set[Path] = set()

        # Track reference sources for reporting
        self.reference_sources: Dict[Path, List[str]] = defaultdict(list)

    def log(self, message: str):
        """Print message if verbose mode is enabled."""
        if self.verbose:
            print(f"[INFO] {message}")

    def is_excluded(self, file_path: Path) -> bool:
        """Check if a file is in an excluded subsite."""
        if not self.exclude_subsites:
            return False

        try:
            rel_path = file_path.relative_to(self.root_dir)
            # Check if first path component is in exclude list
            if rel_path.parts and rel_path.parts[0] in self.exclude_subsites:
                return True
        except ValueError:
            pass

        return False

    def find_all_markdown_files(self):
        """Discover all markdown files in docs directories."""
        self.log("Discovering all markdown files...")

        # Main config
        main_config = self.loader.load_file(str(self.root_yaml))
        if not main_config:
            sys.exit(f"[ERROR] Cannot parse {self.root_yaml}")

        # Get main docs_dir
        docs_dir = main_config.get("docs_dir", "docs").lstrip("./\\")
        main_docs_root = (self.root_dir / docs_dir).resolve()
        if main_docs_root.is_dir():
            self.docs_roots.add(main_docs_root)

        # Get subsite docs_dirs
        for name, subsite_dir, config in self.repo.iter_subsites():
            # Skip excluded subsites
            if name in self.exclude_subsites:
                self.log(f"Skipping excluded subsite: {name}")
                continue

            docs_dir = config.get("docs_dir", "docs").lstrip("./\\")
            docs_root = (Path(subsite_dir) / docs_dir).resolve()
            if docs_root.is_dir():
                self.docs_roots.add(docs_root)

        # Find all .md files, excluding those in excluded subsites
        excluded_count = 0
        for docs_root in self.docs_roots:
            for md_file in docs_root.rglob("*.md"):
                resolved_file = md_file.resolve()
                if not self.is_excluded(resolved_file):
                    self.all_md_files.add(resolved_file)
                else:
                    excluded_count += 1

        if excluded_count > 0:
            self.log(f"Excluded {excluded_count} files from {len(self.exclude_subsites)} subsites")
        self.log(f"Found {len(self.all_md_files)} markdown files in {len(self.docs_roots)} docs roots")

    def collect_nav_references(self):
        """Collect files referenced in all mkdocs.yml nav sections."""
        self.log("Collecting nav references from mkdocs.yml files...")

        # Main mkdocs.yml
        main_config = self.loader.load_file(str(self.root_yaml))
        if main_config and 'nav' in main_config:
            docs_dir = main_config.get("docs_dir", "docs").lstrip("./\\")
            docs_root = (self.root_dir / docs_dir).resolve()

            nav_files = NavTraverser.extract_markdown_files(main_config['nav'])
            for file_ref in nav_files:
                file_path = self._resolve_file_ref(file_ref, docs_root, self.root_dir)
                if file_path and file_path.exists():
                    self.referenced_files.add(file_path)
                    self.reference_sources[file_path].append("main:nav")

        # Subsite mkdocs.yml files
        for name, subsite_dir, config in self.repo.iter_subsites():
            if 'nav' in config:
                docs_dir = config.get("docs_dir", "docs").lstrip("./\\")
                docs_root = (Path(subsite_dir) / docs_dir).resolve()

                nav_files = NavTraverser.extract_markdown_files(config['nav'])
                for file_ref in nav_files:
                    file_path = self._resolve_file_ref(file_ref, docs_root, Path(subsite_dir))
                    if file_path and file_path.exists():
                        self.referenced_files.add(file_path)
                        self.reference_sources[file_path].append(f"{name}:nav")

        self.log(f"Found {len(self.referenced_files)} files in nav sections")

    def collect_print_config_references(self):
        """Collect files referenced in print_mkdocs.yml files."""
        self.log("Collecting references from print_mkdocs.yml files...")

        count = 0
        for name, subsite_dir, config in self.repo.iter_subsites():
            print_config_path = Path(subsite_dir) / 'print_mkdocs.yml'
            if print_config_path.exists():
                print_config = self.loader.load_file(str(print_config_path))
                if print_config and 'nav' in print_config:
                    docs_dir = print_config.get("docs_dir", "docs").lstrip("./\\")
                    docs_root = (Path(subsite_dir) / docs_dir).resolve()

                    nav_files = NavTraverser.extract_markdown_files(print_config['nav'])
                    for file_ref in nav_files:
                        file_path = self._resolve_file_ref(file_ref, docs_root, Path(subsite_dir))
                        if file_path and file_path.exists():
                            self.referenced_files.add(file_path)
                            self.reference_sources[file_path].append(f"{name}:print_nav")
                            count += 1

        self.log(f"Found {count} additional files in print configurations")

    def collect_chm_special_files(self):
        """Collect special files referenced by CHM build (e.g., welcome.md)."""
        self.log("Collecting CHM special files...")

        # CHM uses welcome.md (can be in chm/ or root)
        candidates = [
            self.root_dir / 'chm' / 'welcome.md',
            self.root_dir / 'welcome.md',
        ]

        for welcome_file in candidates:
            if welcome_file.exists():
                self.referenced_files.add(welcome_file.resolve())
                self.reference_sources[welcome_file.resolve()].append("chm:welcome")
                self.log(f"Found CHM welcome file: {welcome_file}")
                break

    def collect_markdown_link_references(self):
        """Collect files referenced by markdown links in other markdown files."""
        self.log("Collecting markdown link references...")

        link_count = 0
        for md_file in self.all_md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract markdown links
                links = LinkExtractor.extract_markdown_links(content)

                for link_text, url in links:
                    # Skip external links, anchors, etc.
                    if url.startswith(('http://', 'https://', '#', 'mailto:')):
                        continue

                    # Try to resolve the link to a markdown file
                    target = self._resolve_link(md_file, url)
                    if target and target.exists() and target.suffix == '.md':
                        self.referenced_files.add(target)
                        rel_source = md_file.relative_to(self.root_dir)
                        self.reference_sources[target].append(f"link:{rel_source}")
                        link_count += 1

            except Exception as e:
                if self.verbose:
                    print(f"[WARN] Error processing {md_file}: {e}", file=sys.stderr)

        self.log(f"Found {link_count} markdown link references")

    def collect_html_link_references(self):
        """Collect files that might be referenced via HTML links in markdown."""
        self.log("Collecting HTML link references...")

        html_link_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
        link_count = 0

        for md_file in self.all_md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                for match in html_link_pattern.finditer(content):
                    url = match.group(1)

                    # Skip external links, anchors, etc.
                    if url.startswith(('http://', 'https://', '#', 'mailto:', 'javascript:')):
                        continue

                    # Try to resolve the link
                    target = self._resolve_link(md_file, url)
                    if target and target.exists() and target.suffix == '.md':
                        self.referenced_files.add(target)
                        rel_source = md_file.relative_to(self.root_dir)
                        self.reference_sources[target].append(f"html_link:{rel_source}")
                        link_count += 1

            except Exception as e:
                if self.verbose:
                    print(f"[WARN] Error processing HTML links in {md_file}: {e}", file=sys.stderr)

        self.log(f"Found {link_count} HTML link references")

    def collect_help_urls_references(self):
        """Parse C header file containing HELP_URL macros."""
        if not self.help_urls_file:
            return

        self.log(f"Parsing help_urls file: {self.help_urls_file}")

        if not self.help_urls_file.exists():
            print(f"[WARN] Help URLs file not found: {self.help_urls_file}", file=sys.stderr)
            return

        # Parse the help URLs file
        url_entries = HelpUrlsParser.parse_help_urls(str(self.help_urls_file))

        # Count defines by checking for duplicates (simple heuristic)
        unique_prefixes = set()
        for _, url in url_entries:
            if '/' in url:
                unique_prefixes.add(url.split('/')[0])
        self.log(f"Found {len(unique_prefixes)} preprocessor defines")

        # Convert URLs to markdown paths
        url_count = 0
        for symbol, url in url_entries:
            md_path = HelpUrlsParser.url_to_markdown_path(url, str(self.root_dir))

            if md_path:
                md_file = Path(md_path)
                if md_file.exists():
                    self.referenced_files.add(md_file)
                    self.reference_sources[md_file].append("help_urls")
                    url_count += 1

        self.log(f"Found {url_count} help URL references")

    def _resolve_file_ref(self, file_ref: str, docs_root: Path, base_path: Path) -> Path:
        """Resolve a file reference from nav to an absolute path."""
        if file_ref.startswith('/'):
            return (base_path / file_ref[1:]).resolve()
        else:
            file_path = (docs_root / file_ref).resolve()
            if not file_path.exists():
                # Fallback to base_path
                file_path = (base_path / file_ref).resolve()
            return file_path

    def _resolve_link(self, source_file: Path, link: str) -> Path:
        """Resolve a markdown link to a target file."""
        # Remove anchors and query parameters
        link = link.split('#')[0].split('?')[0]

        if not link:
            return None

        # Get source directory
        source_dir = source_file.parent

        # Try to resolve the link
        if link.startswith('/'):
            # Absolute from root
            target = self.root_dir / link[1:]
        else:
            # Relative to source file
            target = (source_dir / link).resolve()

        # Try various extensions and index patterns
        candidates = [
            target,
            target.with_suffix('.md'),
            target / 'index.md',
        ]

        # Also try without .md if it's there
        if target.suffix == '.md':
            candidates.append(target.with_suffix(''))

        for candidate in candidates:
            if candidate.exists() and candidate.suffix == '.md':
                return candidate

        return None

    def find_orphans(self) -> Tuple[Set[Path], Dict[Path, List[str]]]:
        """
        Find all orphaned files.

        Returns:
            (orphaned_files, referenced_files_with_sources)
        """
        self.find_all_markdown_files()
        self.collect_nav_references()
        self.collect_print_config_references()
        self.collect_chm_special_files()
        self.collect_markdown_link_references()
        self.collect_html_link_references()
        self.collect_help_urls_references()

        # Calculate orphans, excluding index.md files (intentional landing pages)
        orphans = self.all_md_files - self.referenced_files
        orphans = {f for f in orphans if f.name != 'index.md'}

        return orphans, dict(self.reference_sources)

    def generate_report(self, orphans: Set[Path], reference_sources: Dict[Path, List[str]]) -> Dict:
        """Generate a simplified report dictionary."""
        # Sort orphans by path
        sorted_orphans = sorted(orphans)

        # Group orphans by subsite/location
        orphans_by_location = defaultdict(list)
        for orphan in sorted_orphans:
            try:
                rel_path = orphan.relative_to(self.root_dir)
                # Determine location (first directory component)
                parts = rel_path.parts
                if parts:
                    location = parts[0]
                else:
                    location = 'root'
                orphans_by_location[location].append(str(rel_path))
            except ValueError:
                orphans_by_location['external'].append(str(orphan))

        # Build simplified report
        report = {
            'summary': {
                'total_markdown_files': len(self.all_md_files),
                'referenced_files': len(self.referenced_files),
                'orphaned_files': len(orphans),
                'docs_roots': len(self.docs_roots),
            }
        }

        # Add orphans by location directly to report root
        for location, files in sorted(orphans_by_location.items()):
            report[location] = sorted(files)

        return report


def main():
    parser = argparse.ArgumentParser(
        description="Find truly orphaned markdown files across all output formats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
A file is considered an orphan only if it's not referenced by:
  - Any mkdocs.yml nav section
  - Any print_mkdocs.yml nav section
  - Any markdown link from another file
  - Any HTML link in markdown files
  - CHM special files (welcome.md)
  - C header HELP_URL() macros (if --help_urls specified)

Files named index.md are excluded (intentional landing pages).
Files in object-reference/ that are only linked (not in nav) are NOT orphans.

Examples:
  %(prog)s --root mkdocs.yml
  %(prog)s --root mkdocs.yml --output orphans.yaml --verbose
  %(prog)s --root mkdocs.yml --exclude object-reference,unix-installation-and-configuration-guide
  %(prog)s --root mkdocs.yml --help_urls tools/help_urls.h
        """
    )
    parser.add_argument("--root", required=True, type=Path,
                        help="Path to the top-level mkdocs.yml")
    parser.add_argument("--output", type=Path,
                        help="Write YAML report to file")
    parser.add_argument("--help_urls", type=Path,
                        help="Parse C header file for HELP_URL references")
    parser.add_argument("--exclude", type=str,
                        help="Comma-separated list of subsites to exclude (e.g., object-reference,unix-user-guide)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show detailed progress")
    args = parser.parse_args()

    root_yaml = args.root.resolve()
    if not root_yaml.is_file():
        sys.exit(f"[ERROR] {root_yaml} does not exist or is unreadable")

    # Parse exclude list
    exclude_subsites = set()
    if args.exclude:
        exclude_subsites = {s.strip() for s in args.exclude.split(',') if s.strip()}

    # Validate help_urls file if provided
    help_urls_file = None
    if args.help_urls:
        help_urls_file = args.help_urls.resolve()
        if not help_urls_file.is_file():
            sys.exit(f"[ERROR] Help URLs file not found: {help_urls_file}")

    # Find orphans
    finder = OrphanFinder(root_yaml, verbose=args.verbose, exclude_subsites=exclude_subsites, help_urls_file=help_urls_file)
    orphans, reference_sources = finder.find_orphans()

    # Generate report
    report = finder.generate_report(orphans, reference_sources)

    # Print summary to console
    print(f"Total markdown files  : {report['summary']['total_markdown_files']}")
    print(f"Referenced files      : {report['summary']['referenced_files']}")
    print(f"Orphaned files        : {report['summary']['orphaned_files']}")
    print(f"Docs roots scanned    : {report['summary']['docs_roots']}")

    # Show orphans by location
    orphan_count = report['summary']['orphaned_files']
    if orphan_count > 0:
        print()
        for location in sorted(report.keys()):
            if location != 'summary':
                files = report[location]
                print(f"{location}: {len(files)} files")
    else:
        print("\n✓ No orphaned files found!")

    # Write YAML output if requested
    if args.output:
        try:
            from ruamel.yaml import YAML
            yaml = YAML()
            yaml.default_flow_style = False
            yaml.indent(mapping=2, sequence=2, offset=2)
            yaml.preserve_quotes = True
            yaml.width = 4096  # Prevent line wrapping
            with open(args.output, 'w') as f:
                yaml.dump(report, f)
            print(f"\n✓ Report written to {args.output}")
        except Exception as e:
            print(f"\n✗ Error writing report: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
