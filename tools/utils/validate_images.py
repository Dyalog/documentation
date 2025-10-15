#!/usr/bin/env python3
"""
Validate image references in markdown files.

This script:
1. Checks that all image references in markdown files point to existing files
2. Detects cross-document image references (bad practice that breaks isolated builds)
3. Identifies truly unreferenced images using ripgrep verification

The verification step searches for bare filenames across all markdown files to ensure
no false positives in the unreferenced images list.

Files get moved around, and it's easy to forget to update a relative link.
Only processes the directory hierarchy as defined by the top-level mkdocs.yml.

Important Notes:
- Duplicate images: The codebase may contain duplicate images across subsites (e.g.,
  the same image in both earlier-release-notes/docs/img/ and object-reference/docs/img/).
  Path-based checking marks one copy as "unreferenced" if references point to the other
  copy. Ripgrep verification prevents deletion of such duplicates by detecting that the
  filename appears in markdown files somewhere. This is the expected behavior.

- The difference between path-based unreferenced count (e.g., 571) and ripgrep-verified
  count (e.g., 215) is largely due to duplicate images where one copy is referenced and
  other copies are not directly referenced but share the same filename.

Usage:
    python validate_images.py [--output report.yaml] [--root-dir /path/to/docs]

Output:
    YAML report with:
    - broken_references: markdown files with broken image links
    - cross_document_references: images referenced across document boundaries
    - unreferenced_images: images safe to delete (verified with ripgrep)

Requires:
    - ripgrep (rg) for verification (required - script will exit if not found)
"""

import argparse
import asyncio
import os
import subprocess
import sys
from typing import Dict, List, Set, Tuple

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))

from doc_utils import MkDocsRepo, LinkExtractor
from ruamel.yaml import YAML


class ImageValidator:
    """Validate image references in markdown files."""

    def __init__(self, root_dir: str, report_all: bool = False):
        self.root_dir = os.path.abspath(root_dir)
        self.repo = MkDocsRepo(root_dir)
        self.broken_refs: Dict[str, List[str]] = {}
        self.all_refs: Dict[str, List[str]] = {}  # For --all mode
        self.unreferenced_images: List[str] = []
        self.cross_document_refs: Dict[str, List[str]] = {}  # Cross-document image references (bad practice)
        self.total_images = 0
        self.broken_images = 0
        self.referenced_images: Set[str] = set()  # Track which images are referenced
        self.report_all = report_all  # Whether to report all references or just broken ones

    def get_subsite(self, file_path: str) -> str:
        """
        Determine which subsite (or main docs) a file belongs to.

        Args:
            file_path: Absolute path to the file

        Returns:
            Subsite name or 'docs' for main documentation
        """
        rel_path = os.path.relpath(file_path, self.root_dir)
        parts = rel_path.split(os.sep)

        if parts[0] == 'docs':
            return 'docs'
        else:
            # First part is the subsite name
            return parts[0]

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

    def validate_file(self, md_file: str) -> Tuple[List[str], List[str]]:
        """
        Validate all image references in a single markdown file.
        Also detects cross-document references.

        Returns:
            Tuple of (broken_refs, all_refs) where each is a list of strings in format "line_no: ![...](path)"
        """
        broken = []
        all_images = []
        refs = self.repo.extract_image_references(md_file)

        # Determine which subsite this markdown file belongs to
        md_subsite = self.get_subsite(md_file)

        for ref in refs:
            self.total_images += 1

            # Resolve the image path
            resolved_path = self.resolve_image_path(md_file, ref.image_path)

            # Skip external URLs
            if resolved_path is None:
                continue

            # Track this image as referenced (if it exists)
            if resolved_path and os.path.exists(resolved_path):
                self.referenced_images.add(os.path.abspath(resolved_path))

            # Check for cross-document references (even if broken)
            if resolved_path:
                # Determine the subsite from the resolved path
                img_subsite = self.get_subsite(resolved_path)
                if img_subsite != md_subsite:
                    # Cross-document reference detected
                    rel_md_path = os.path.relpath(md_file, self.root_dir)
                    ref_text = f"{ref.line_number}: {ref.raw_text}"

                    if rel_md_path not in self.cross_document_refs:
                        self.cross_document_refs[rel_md_path] = []
                    self.cross_document_refs[rel_md_path].append(ref_text)

            # Format the reference
            ref_text = f"{ref.line_number}: {ref.raw_text}"

            # In --all mode, capture all references
            if self.report_all:
                all_images.append(ref_text)

            # Check if the file exists
            if not os.path.exists(resolved_path):
                self.broken_images += 1
                broken.append(ref_text)

        return broken, all_images

    def check_ripgrep_available(self) -> bool:
        """
        Check if ripgrep is available.

        Returns:
            True if ripgrep is available, False otherwise
        """
        try:
            result = subprocess.run(
                ['rg', '--version'],
                capture_output=True,
                check=False
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    async def verify_with_ripgrep_async(self, filename: str) -> List[str]:
        """
        Use ripgrep to search for bare filename references across all markdown files (async).
        This catches cases where images are referenced from a different directory structure.

        Args:
            filename: Bare filename to search for (e.g., "image.png")

        Returns:
            List of markdown files that reference this filename
        """
        try:
            # Use ripgrep to search for the filename in all markdown files
            process = await asyncio.create_subprocess_exec(
                'rg', '-l', '-F', filename, '--type', 'md', self.root_dir,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                # Found matches - return list of files
                output = stdout.decode('utf-8').strip()
                return [line.strip() for line in output.split('\n') if line.strip()]
            else:
                # No matches found
                return []
        except Exception as e:
            print(f"Error: ripgrep verification failed: {e}", file=sys.stderr)
            sys.exit(1)

    async def verify_batch_async(self, candidates: List[Tuple[str, str]]) -> List[str]:
        """
        Verify a batch of candidate images using ripgrep concurrently.

        Args:
            candidates: List of (rel_path, filename) tuples

        Returns:
            List of relative paths that are truly unreferenced
        """
        tasks = []
        for rel_path, filename in candidates:
            tasks.append(self.verify_with_ripgrep_async(filename))

        # Run all ripgrep searches concurrently
        results = await asyncio.gather(*tasks)

        # Filter to only truly unreferenced images
        unreferenced = []
        for (rel_path, filename), rg_matches in zip(candidates, results):
            if not rg_matches:
                # Truly unreferenced - not found by ripgrep either
                unreferenced.append(rel_path)

        return unreferenced

    def find_unreferenced_images(self) -> List[str]:
        """
        Find images that exist in img directories but are not referenced by any markdown file.
        Uses ripgrep to verify each unreferenced image by searching for bare filename.
        Uses async/await to parallelize ripgrep searches for speed.

        Returns:
            List of relative paths to truly unreferenced images
        """
        # Check if ripgrep is available
        if not self.check_ripgrep_available():
            print("\n" + "=" * 70, file=sys.stderr)
            print("ERROR: ripgrep (rg) is required but not found!", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            print("\nRipgrep is required to verify unreferenced images.", file=sys.stderr)
            print("Without it, the unreferenced images list will contain false positives.", file=sys.stderr)
            print("\nInstall ripgrep:", file=sys.stderr)
            print("  - macOS:   brew install ripgrep", file=sys.stderr)
            print("  - Ubuntu:  apt install ripgrep", file=sys.stderr)
            print("  - Docker:  Rebuild the image with 'docker compose build utils'", file=sys.stderr)
            print("\nFor more info: https://github.com/BurntSushi/ripgrep", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            sys.exit(1)

        all_images = self.repo.find_all_image_files()

        print("Verifying unreferenced images with ripgrep (parallel)...")

        # Collect candidates
        candidates = []
        for img_path in sorted(all_images):
            if img_path not in self.referenced_images:
                rel_path = os.path.relpath(img_path, self.root_dir)
                filename = os.path.basename(img_path)
                candidates.append((rel_path, filename))

        total_candidates = len(candidates)
        print(f"  Found {total_candidates} candidates to verify...")

        if total_candidates == 0:
            return []

        # Process in batches for better progress reporting
        batch_size = 100
        unreferenced = []

        for i in range(0, total_candidates, batch_size):
            batch = candidates[i:i+batch_size]
            batch_unreferenced = asyncio.run(self.verify_batch_async(batch))
            unreferenced.extend(batch_unreferenced)

            processed = min(i + batch_size, total_candidates)
            print(f"  Verified {processed}/{total_candidates} candidates...")

        verified_count = len(unreferenced)
        print(f"  Complete: {verified_count} truly unreferenced, {total_candidates - verified_count} referenced elsewhere")

        return unreferenced

    def validate_all(self) -> Dict[str, List[str]]:
        """
        Validate all markdown files in the repository.

        Returns:
            Dictionary mapping file paths to lists of references (broken or all, depending on mode)
        """
        if self.report_all:
            print("Scanning markdown files for all image references...")
        else:
            print("Scanning markdown files for image references...")

        for md_file in self.repo.iter_all_markdown_files():
            broken, all_images = self.validate_file(md_file)
            rel_path = os.path.relpath(md_file, self.root_dir)

            if self.report_all:
                # In --all mode, report all references
                if all_images:
                    self.all_refs[rel_path] = all_images
            else:
                # In normal mode, report only broken references
                if broken:
                    self.broken_refs[rel_path] = broken

        # Only scan for unreferenced images in normal mode
        if not self.report_all:
            print("Scanning for unreferenced images...")
            self.unreferenced_images = self.find_unreferenced_images()

        return self.all_refs if self.report_all else self.broken_refs

    def print_summary(self):
        """Print a summary of validation results."""
        print("\n" + "=" * 70)
        print("IMAGE VALIDATION SUMMARY")
        print("=" * 70)

        if self.report_all:
            # Summary for --all mode
            print(f"Total image references found: {self.total_images}")
            print(f"Files with image references: {len(self.all_refs)}")

            if self.all_refs:
                print(f"\nImage references found in {len(self.all_refs)} file(s)")
                print("\nSample files (first 5):")
                for i, (file_path, refs) in enumerate(list(self.all_refs.items())[:5]):
                    print(f"\n  {i+1}. {file_path}")
                    for ref in refs[:2]:  # Show first 2 refs per file
                        print(f"     {ref}")
                    if len(refs) > 2:
                        print(f"     ... and {len(refs) - 2} more reference(s)")

                if len(self.all_refs) > 5:
                    print(f"\n  ... and {len(self.all_refs) - 5} more file(s)")
            else:
                print("\nNo image references found!")
        else:
            # Summary for normal mode
            print(f"Total images checked: {self.total_images}")
            print(f"Broken references: {self.broken_images}")
            print(f"Files with broken references: {len(self.broken_refs)}")
            print(f"Cross-document references: {len(self.cross_document_refs)}")
            print(f"Unreferenced images: {len(self.unreferenced_images)}")

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

            if self.cross_document_refs:
                print(f"\nCross-document references (breaks isolated builds): {len(self.cross_document_refs)}")
                print("\nSample cross-document references (first 5):")
                for i, (file_path, refs) in enumerate(list(self.cross_document_refs.items())[:5]):
                    print(f"\n  {i+1}. {file_path}")
                    for ref in refs[:3]:
                        print(f"     {ref}")
                    if len(refs) > 3:
                        print(f"     ... and {len(refs) - 3} more")
                if len(self.cross_document_refs) > 5:
                    print(f"\n  ... and {len(self.cross_document_refs) - 5} more file(s)")

            if self.unreferenced_images:
                print(f"\nUnreferenced images (safe to delete): {len(self.unreferenced_images)}")
                print("\nSample unreferenced images (first 10):")
                for img in self.unreferenced_images[:10]:
                    print(f"  - {img}")
                if len(self.unreferenced_images) > 10:
                    print(f"  ... and {len(self.unreferenced_images) - 10} more")
            else:
                print("\n✓ No unreferenced images found!")

    def write_report(self, output_file: str):
        """Write validation results to a YAML file."""
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.width = 120
        yaml.preserve_quotes = True

        if self.report_all:
            # Report format for --all mode
            report = {
                'summary': {
                    'total_image_references': self.total_images,
                    'files_with_references': len(self.all_refs)
                },
                'all_references': self.all_refs
            }
        else:
            # Report format for normal mode
            report = {
                'summary': {
                    'total_images': self.total_images,
                    'broken_images': self.broken_images,
                    'files_with_issues': len(self.broken_refs),
                    'cross_document_refs': len(self.cross_document_refs),
                    'unreferenced_images': len(self.unreferenced_images)
                },
                'broken_references': self.broken_refs,
                'cross_document_references': self.cross_document_refs,
                'unreferenced_images': self.unreferenced_images
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

  # When running from tools/ subdirectory
  python validate_images.py --root-dir ..

  # Validate and save report
  python validate_images.py --output broken_images.yaml

  # Validate specific directory
  python validate_images.py --root-dir /path/to/docs
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
        default='broken_images.yaml',
        help='Output YAML file for the report (default: broken_images.yaml)'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        dest='report_all',
        help='Report all image references, not just broken ones (skips unreferenced image check)'
    )

    args = parser.parse_args()

    # Resolve root directory
    root_dir = os.path.abspath(args.root_dir)

    if not os.path.exists(os.path.join(root_dir, 'mkdocs.yml')):
        print(f"Error: {root_dir} does not appear to be a mkdocs documentation root", file=sys.stderr)
        print("       (mkdocs.yml not found)", file=sys.stderr)
        sys.exit(1)

    # Run validation
    validator = ImageValidator(root_dir, report_all=args.report_all)
    validator.validate_all()

    # Print summary
    validator.print_summary()

    # Write report
    validator.write_report(args.output)

    # Exit with error code if broken references found (only in normal mode)
    if not args.report_all:
        sys.exit(1 if validator.broken_images > 0 else 0)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
