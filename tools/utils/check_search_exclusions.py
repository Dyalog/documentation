#!/usr/bin/env python3
"""
Check for markdown files with conflicting search exclusions and synonym divs.

This script traverses all .md files under the root dirs defined by the top-level
mkdocs.yml's '!include' statements and flags any files that have both search
exclude YAML front matter and hidden divs for synonyms.
"""

import os
import re
import yaml
from pathlib import Path
from typing import List, Tuple, Optional, Dict
import argparse


def parse_mkdocs_includes(mkdocs_path: str) -> List[str]:
    """
    Parse mkdocs.yml to find all !include directives and extract the directories.
    
    Returns:
        List of directories referenced in !include statements
    """
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all !include statements in the nav section
    include_pattern = r'"!include\s+\./([^/]+)/mkdocs\.yml"'
    matches = re.findall(include_pattern, content)
    
    return matches


def has_search_exclude_front_matter(content: str) -> Tuple[bool, Optional[int]]:
    """
    Check if the content has search exclude in front matter.
    
    Returns:
        (has_exclude, line_number) - True if excluded from search, and the line number
    """
    lines = content.split('\n')
    
    # Find the start of front matter (may not be at beginning)
    start_line = None
    for i, line in enumerate(lines):
        if line.strip() == '---':
            start_line = i
            break
    
    if start_line is None or start_line + 2 >= len(lines):
        return False, None
    
    # Find the closing ---
    end_line = None
    for i in range(start_line + 1, len(lines)):
        if lines[i].strip() == '---':
            end_line = i
            break
    
    if end_line is None:
        return False, None
    
    # Check for search exclude in front matter
    front_matter_content = '\n'.join(lines[start_line + 1:end_line])
    if re.search(r'search:\s*\n\s*exclude:\s*true', front_matter_content):
        # Find the actual line number of the exclude directive
        for i in range(start_line + 1, end_line):
            if 'search:' in lines[i]:
                return True, i + 1  # Convert to 1-based line number
        return True, None
    
    return False, None


def has_hidden_synonym_div(content: str) -> Tuple[bool, Optional[str], Optional[int]]:
    """
    Check if the content has a hidden div with APL symbol.
    
    Returns:
        (has_div, symbol, line_number) - True if has div, the symbol if found, and line number
    """
    lines = content.split('\n')
    
    # Pattern to match hidden div with APL symbol
    div_pattern = r'<div\s+style\s*=\s*["\']display:\s*none;?["\']>'
    
    for i, line in enumerate(lines):
        if re.search(div_pattern, line, re.IGNORECASE):
            # Check if the next line contains a single non-alphanumeric character
            if i + 1 < len(lines):
                symbol_line = lines[i + 1].strip()
                if len(symbol_line) == 1 and not symbol_line.isalnum():
                    return True, symbol_line, i + 1  # Convert to 1-based line number
            return True, None, i + 1
    
    return False, None, None


def check_file(filepath: str) -> Optional[Dict[str, any]]:
    """
    Check a single markdown file for conflicts.
    
    Returns:
        Dictionary with conflict info if found, None otherwise
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_exclude, exclude_line = has_search_exclude_front_matter(content)
    has_div, symbol, div_line = has_hidden_synonym_div(content)
    
    if has_exclude and has_div:
        # Check order (div should not come before front matter)
        wrong_order = False
        if div_line and exclude_line and div_line < exclude_line:
            wrong_order = True
        
        return {
            'path': filepath,
            'has_search_exclude': True,
            'exclude_line': exclude_line,
            'has_synonym_div': True,
            'symbol': symbol,
            'div_line': div_line,
            'wrong_order': wrong_order
        }
    
    return None


def find_markdown_files(directory: str) -> List[str]:
    """
    Recursively find all .md files in a directory.
    """
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def main():
    parser = argparse.ArgumentParser(
        description='Check for conflicting search exclusions and synonym divs in markdown files'
    )
    parser.add_argument(
        '--mkdocs',
        default='mkdocs.yml',
        help='Path to the main mkdocs.yml file (default: mkdocs.yml)'
    )
    parser.add_argument(
        '--format',
        choices=['detailed', 'summary', 'paths'],
        default='detailed',
        help='Output format (default: detailed)'
    )
    
    args = parser.parse_args()
    
    # Get the base directory
    base_dir = os.path.dirname(os.path.abspath(args.mkdocs))
    
    print(f"Checking documentation structure from: {args.mkdocs}")
    print(f"Base directory: {base_dir}\n")
    
    # Parse mkdocs.yml to find included directories
    try:
        include_dirs = parse_mkdocs_includes(args.mkdocs)
        print(f"Found {len(include_dirs)} included directories:")
        for dir_name in include_dirs:
            print(f"  - {dir_name}")
        print()
    except Exception as e:
        print(f"Error parsing mkdocs.yml: {e}")
        return 1
    
    # Find all markdown files in included directories
    all_conflicts = []
    total_files = 0
    
    for dir_name in include_dirs:
        dir_path = os.path.join(base_dir, dir_name)
        if os.path.exists(dir_path):
            print(f"Scanning {dir_name}/...")
            md_files = find_markdown_files(dir_path)
            total_files += len(md_files)
            
            for filepath in md_files:
                conflict = check_file(filepath)
                if conflict:
                    all_conflicts.append(conflict)
    
    # Report results
    print(f"\n{'=' * 70}")
    print(f"SUMMARY: Checked {total_files} markdown files")
    print(f"Found {len(all_conflicts)} files with conflicts")
    
    if all_conflicts:
        print(f"\n{'=' * 70}")
        print("CONFLICTS FOUND:")
        print(f"{'=' * 70}\n")
        
        if args.format == 'paths':
            # Just print paths
            for conflict in all_conflicts:
                print(conflict['path'])
        
        elif args.format == 'summary':
            # Print summary table
            print(f"{'File':<60} {'Symbol':<10} {'Wrong Order'}")
            print(f"{'-'*60} {'-'*10} {'-'*11}")
            for conflict in all_conflicts:
                rel_path = os.path.relpath(conflict['path'], base_dir)
                symbol = conflict['symbol'] or 'N/A'
                wrong = 'Yes' if conflict['wrong_order'] else 'No'
                print(f"{rel_path:<60} {symbol:<10} {wrong}")
        
        else:  # detailed
            for i, conflict in enumerate(all_conflicts, 1):
                rel_path = os.path.relpath(conflict['path'], base_dir)
                print(f"{i}. {rel_path}")
                print(f"   - Search exclude at line: {conflict['exclude_line']}")
                print(f"   - Hidden div at line: {conflict['div_line']}")
                if conflict['symbol']:
                    print(f"   - Symbol: '{conflict['symbol']}'")
                if conflict['wrong_order']:
                    print(f"   - WARNING: Hidden div appears BEFORE front matter!")
                print()
        
        # Statistics
        wrong_order_count = sum(1 for c in all_conflicts if c['wrong_order'])
        if wrong_order_count > 0:
            print(f"\n⚠️  {wrong_order_count} files have hidden div before front matter")
            
        print(f"\n💡 To fix these conflicts:")
        print(f"   1. Remove the hidden synonym divs from these files")
        print(f"   2. Or remove the search exclusion if synonyms are needed")
    else:
        print("\n✅ No conflicts found!")
    
    return 0 if not all_conflicts else 1


if __name__ == '__main__':
    exit(main())