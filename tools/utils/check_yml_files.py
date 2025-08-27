#!/usr/bin/env python3
"""
Check that all markdown files referenced in mkdocs.yml nav sections exist.
This version uses the doc_utils module for shared functionality.
"""

import os
import sys

# Add the utils directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doc_utils import YAMLLoader, NavTraverser, PathResolver


def check_file_exists(base_path, file_ref):
    """Check if a markdown file exists using PathResolver."""
    resolver = PathResolver(base_path)
    file_path = resolver.markdown_file_path(base_path, file_ref)
    return os.path.exists(file_path), file_path


def process_config(config_path, base_path, files_found):
    """Process a mkdocs.yml file to extract nav files."""
    loader = YAMLLoader()
    config = loader.load_file(config_path)
    
    if not config or 'nav' not in config:
        return
    
    # Extract markdown files from nav
    nav_files = NavTraverser.extract_markdown_files(config['nav'])
    for file_ref in nav_files:
        files_found.add((base_path, file_ref))
    
    # Process includes
    includes = NavTraverser.find_includes(config['nav'])
    for include in includes:
        include_path = include.replace('!include ', '').strip()
        if include_path.startswith('./'):
            include_path = include_path[2:]
        
        full_include_path = os.path.join(base_path, include_path)
        if os.path.exists(full_include_path):
            include_dir = os.path.dirname(full_include_path)
            process_config(full_include_path, include_dir, files_found)
            
            # Also check for print_mkdocs.yml
            print_mkdocs = os.path.join(include_dir, 'print_mkdocs.yml')
            if os.path.exists(print_mkdocs):
                print(f"Found print_mkdocs.yml in {os.path.basename(include_dir)}")
                process_config(print_mkdocs, include_dir, files_found)


def main():
    # Get the root directory (where the main mkdocs.yml is)
    # Check if we're running in Docker (mounted at /docs) or locally
    if os.path.exists('/docs/mkdocs.yml'):
        root_dir = '/docs'
    else:
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    # Load the main mkdocs.yml
    main_mkdocs_path = os.path.join(root_dir, 'mkdocs.yml')
    if not os.path.exists(main_mkdocs_path):
        print(f"Error: Main mkdocs.yml not found at {main_mkdocs_path}")
        sys.exit(1)
    
    print(f"Checking mkdocs.yml files starting from: {root_dir}\n")
    
    # Extract all file references
    files_found = set()
    process_config(main_mkdocs_path, root_dir, files_found)
    
    # Check each file
    missing_files = []
    checked_count = 0
    
    print(f"\nChecking {len(files_found)} markdown file references...\n")
    
    for base_path, file_ref in sorted(files_found):
        checked_count += 1
        exists, full_path = check_file_exists(base_path, file_ref)
        
        if not exists:
            missing_files.append((base_path, file_ref, full_path))
            print(f"✗ Missing: {file_ref}")
            print(f"  Expected at: {full_path}")
            print(f"  Referenced from: {base_path}")
            print()
    
    # Summary
    print("=" * 60)
    print(f"SUMMARY:")
    print(f"  Total files checked: {checked_count}")
    print(f"  Missing files: {len(missing_files)}")
    print(f"  Valid files: {checked_count - len(missing_files)}")
    
    if missing_files:
        print(f"\nMissing files by directory:")
        
        # Group by base path
        by_dir = {}
        for base_path, file_ref, full_path in missing_files:
            if base_path not in by_dir:
                by_dir[base_path] = []
            by_dir[base_path].append(file_ref)
        
        for dir_path, files in by_dir.items():
            print(f"\n  {os.path.relpath(dir_path, root_dir)}:")
            for f in files:
                print(f"    - {f}")
        
        sys.exit(1)
    else:
        print("\n✓ All referenced markdown files exist!")
        sys.exit(0)


if __name__ == '__main__':
    main()