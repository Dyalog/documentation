#!/usr/bin/env python3
"""
Validate image references in markdown files.

This script checks that all image references in markdown files point to existing files.
Files get moved around, and it's easy to forget to update a relative link.

Usage:
    python validate_images.py [--output report.yaml] [--root-dir /path/to/docs]

Output:
    YAML report mapping page paths to broken image references.
"""

import argparse
import os
import re
import sys
from typing import Dict, List, Set, Tuple
from pathlib import Path

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))

from doc_utils import MkDocsRepo, LinkExtractor
from ruamel.yaml import YAML


class ImageReference:
    """Represents an image reference found in markdown."""

    def __init__(self, alt_text: str, image_path: str, line_number: int, raw_text: str = ''):
        self.alt_text = alt_text
        self.image_path = image_path
        self.line_number = line_number
        self.raw_text = raw_text  # The actual markdown text as it appears in the file

    def __repr__(self):
        return f"ImageReference(line={self.line_number}, raw='{self.raw_text}')"


class ImageValidator:
    """Validate image references in markdown files."""

    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
        self.repo = MkDocsRepo(root_dir)
        self.broken_refs: Dict[str, List[str]] = {}
        self.total_images = 0
        self.broken_images = 0

    def extract_image_references(self, md_file: str) -> List[ImageReference]:
        """
        Extract all image references from a markdown file with line numbers.

        Returns:
            List of ImageReference objects
        """
        refs = []

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Pattern for markdown images: ![alt text](path)
            # Also handles HTML img tags: <img src="path" ...>
            md_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
            html_pattern = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

            for line_num, line in enumerate(lines, start=1):
                # Find markdown-style images
                for match in md_pattern.finditer(line):
                    alt_text = match.group(1)
                    image_path = match.group(2)
                    raw_text = match.group(0)  # Full match: ![alt](path)
                    refs.append(ImageReference(alt_text, image_path, line_num, raw_text))

                # Find HTML-style images
                for match in html_pattern.finditer(line):
                    image_path = match.group(1)
                    raw_text = match.group(0)  # Full match: <img src="..." />
                    refs.append(ImageReference('', image_path, line_num, raw_text))

        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}", file=sys.stderr)

        return refs

    def resolve_image_path(self, md_file: str, image_ref: str) -> str:
        """
        Resolve an image reference to an absolute path.

        Args:
            md_file: Path to the markdown file containing the reference
            image_ref: The image reference from the markdown

        Returns:
            Absolute path to where the image should be
        """
        # Skip external URLs
        if image_ref.startswith(('http://', 'https://', 'data:')):
            return None

        # Get the directory of the markdown file
        md_dir = os.path.dirname(md_file)

        # Handle absolute paths (from repo root)
        if image_ref.startswith('/'):
            return os.path.abspath(os.path.join(self.root_dir, image_ref.lstrip('/')))

        # Handle relative paths
        return os.path.abspath(os.path.join(md_dir, image_ref))

    def validate_file(self, md_file: str) -> List[str]:
        """
        Validate all image references in a single markdown file.

        Returns:
            List of strings in format "line_no: ![...](path)"
        """
        broken = []
        refs = self.extract_image_references(md_file)

        for ref in refs:
            self.total_images += 1

            # Resolve the image path
            resolved_path = self.resolve_image_path(md_file, ref.image_path)

            # Skip external URLs
            if resolved_path is None:
                continue

            # Check if the file exists
            if not os.path.exists(resolved_path):
                self.broken_images += 1

                # Store as "line_no: ![...](path)"
                broken.append(f"{ref.line_number}: {ref.raw_text}")

        return broken

    def validate_all(self) -> Dict[str, List[str]]:
        """
        Validate all markdown files in the repository.

        Returns:
            Dictionary mapping file paths to lists of broken references
        """
        print("Scanning markdown files for image references...")

        for md_file in self.repo.iter_all_markdown_files():
            broken = self.validate_file(md_file)
            if broken:
                # Store relative path from root
                rel_path = os.path.relpath(md_file, self.root_dir)
                self.broken_refs[rel_path] = broken

        return self.broken_refs

    def print_summary(self):
        """Print a summary of validation results."""
        print("\n" + "=" * 70)
        print("IMAGE VALIDATION SUMMARY")
        print("=" * 70)
        print(f"Total images checked: {self.total_images}")
        print(f"Broken references: {self.broken_images}")
        print(f"Files with broken references: {len(self.broken_refs)}")

        if self.broken_refs:
            print(f"\nBroken references found in {len(self.broken_refs)} file(s)")
            print("\nSample issues (first 5 files):")
            for i, (file_path, issues) in enumerate(list(self.broken_refs.items())[:5]):
                print(f"\n  {i+1}. {file_path}")
                for issue in issues[:2]:  # Show first 2 issues per file
                    print(f"     {issue}")
                if len(issues) > 2:
                    print(f"     ... and {len(issues) - 2} more issue(s)")

            if len(self.broken_refs) > 5:
                print(f"\n  ... and {len(self.broken_refs) - 5} more file(s)")
        else:
            print("\n✓ All image references are valid!")

    def write_report(self, output_file: str):
        """Write validation results to a YAML file."""
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.width = 120
        yaml.preserve_quotes = True

        # Create a more readable structure
        report = {
            'summary': {
                'total_images': self.total_images,
                'broken_images': self.broken_images,
                'files_with_issues': len(self.broken_refs)
            },
            'broken_references': self.broken_refs
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(report, f)

        print(f"\nDetailed report written to: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Validate image references in markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate from documentation root
  python validate_images.py

  # Validate and save report
  python validate_images.py --output broken_images.yaml

  # Validate specific directory
  python validate_images.py --root-dir /path/to/docs
        """
    )

    parser.add_argument(
        '--root-dir',
        type=str,
        default='..',
        help='Root directory of the documentation (default: parent of tools/)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='broken_images.yaml',
        help='Output YAML file for the report (default: broken_images.yaml)'
    )

    args = parser.parse_args()

    # Resolve root directory
    root_dir = os.path.abspath(args.root_dir)

    if not os.path.exists(os.path.join(root_dir, 'mkdocs.yml')):
        print(f"Error: {root_dir} does not appear to be a mkdocs documentation root", file=sys.stderr)
        print("       (mkdocs.yml not found)", file=sys.stderr)
        sys.exit(1)

    # Run validation
    validator = ImageValidator(root_dir)
    validator.validate_all()

    # Print summary
    validator.print_summary()

    # Write report
    validator.write_report(args.output)

    # Exit with error code if broken references found
    sys.exit(1 if validator.broken_images > 0 else 0)


if __name__ == '__main__':
    main()
