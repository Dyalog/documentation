#!/usr/bin/env python3
"""
Find "ghost pages" - Markdown files that exist in docs directories but are NOT
referenced in any nav section. This version uses the doc_utils module.
"""

import argparse
import os
import sys
from pathlib import Path

# Add the utils directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from doc_utils import MkDocsRepo, YAMLLoader, NavTraverser


def find_ghost_pages(root_yaml: Path) -> tuple[set[Path], set[Path], set[Path], int]:
    """
    Find all ghost pages in the documentation.
    
    Returns:
        (referenced_files, all_md_files, ghost_pages, docs_roots_count)
    """
    # Create MkDocsRepo instance
    root_dir = root_yaml.parent
    repo = MkDocsRepo(str(root_dir))
    loader = YAMLLoader()
    
    referenced_files = set()
    docs_roots = set()
    
    # Process main mkdocs.yml
    main_config = loader.load_file(str(root_yaml))
    if not main_config:
        sys.exit(f"[ERROR] Cannot parse {root_yaml}")
    
    # Get docs_dir for main site
    docs_dir = main_config.get("docs_dir", "docs").lstrip("./\\")
    main_docs_root = (root_dir / docs_dir).resolve()
    if main_docs_root.is_dir():
        docs_roots.add(main_docs_root)
    
    # Collect files from main nav
    if 'nav' in main_config:
        main_files = NavTraverser.extract_markdown_files(main_config['nav'])
        for file_ref in main_files:
            # Resolve to actual path
            if file_ref.startswith('/'):
                file_path = (root_dir / file_ref[1:]).resolve()
            else:
                file_path = (main_docs_root / file_ref).resolve()
            if not file_path.exists():
                # Fallback to base_dir
                file_path = (root_dir / file_ref).resolve()
            referenced_files.add(file_path)
    
    # Process subsites
    for name, subsite_dir, config in repo.iter_subsites():
        subsite_path = Path(subsite_dir)
        
        # Get docs_dir for subsite
        docs_dir = config.get("docs_dir", "docs").lstrip("./\\")
        docs_root = (subsite_path / docs_dir).resolve()
        if docs_root.is_dir():
            docs_roots.add(docs_root)
        
        # Collect files from subsite nav
        if 'nav' in config:
            subsite_files = NavTraverser.extract_markdown_files(config['nav'])
            for file_ref in subsite_files:
                # Resolve to actual path
                if file_ref.startswith('/'):
                    file_path = (subsite_path / file_ref[1:]).resolve()
                else:
                    file_path = (docs_root / file_ref).resolve()
                if not file_path.exists():
                    # Fallback to subsite base_dir
                    file_path = (subsite_path / file_ref).resolve()
                referenced_files.add(file_path)
        
    
    # Discover all *.md files under the collected docs roots
    all_md_files = set()
    for docs_root in docs_roots:
        all_md_files.update(p.resolve() for p in docs_root.rglob("*.md"))
    
    # Find ghost pages
    ghost_pages = all_md_files - referenced_files
    
    return referenced_files, all_md_files, ghost_pages, len(docs_roots)


def main():
    parser = argparse.ArgumentParser(
        description="List Markdown files inside docs trees that are not "
                    "referenced from any MkDocs nav entry.")
    parser.add_argument("--root", required=True, type=Path,
                        help="Path to the top-level mkdocs.yml")
    args = parser.parse_args()
    
    root_yaml = args.root.resolve()
    if not root_yaml.is_file():
        sys.exit(f"[ERROR] {root_yaml} does not exist or is unreadable")
    
    referenced, all_md, ghosts, docs_roots_count = find_ghost_pages(root_yaml)
    
    # Sort ghost pages for consistent output
    sorted_ghosts = sorted(ghosts)
    
    # Print summary
    print(f"Docs roots         : {docs_roots_count:>5}")
    print(f"Referenced pages   : {len(referenced):>5}")
    print(f"Markdown discovered: {len(all_md):>5}")
    print(f"Ghost pages        : {len(sorted_ghosts):>5}\n")
    
    if sorted_ghosts:
        for p in sorted_ghosts:
            print(p)  # absolute path
    else:
        print("None")


if __name__ == "__main__":
    main()