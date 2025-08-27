#!/usr/bin/env python3
"""
Add APL symbol synonyms to markdown files.

This script processes all .md files in a directory (non-recursively) and:
1. Finds the first <h1> tag
2. Checks if it has a <span class="command"> child
3. Extracts any non-alphanumeric symbol from that span
4. Adds a hidden div with the symbol at the beginning of the file
"""

import os
import sys
import argparse
import re
from typing import Optional, Tuple, Set
from bs4 import BeautifulSoup


def extract_apl_symbol(html_content: str) -> Optional[str]:
    """
    Extract APL symbol from the first h1 tag with a command span.
    
    Returns the symbol if found, None otherwise.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first h1 tag
    h1 = soup.find('h1')
    if not h1:
        return None
    
    # Check if h1 has a span with class "command"
    command_span = h1.find('span', class_='command')
    if not command_span:
        return None
    
    # Get the text content
    command_text = command_span.get_text()
    
    # Characters to ignore
    ignore_chars: Set[str] = set('{}()[]\'"\' ')
    
    # Extract non-alphanumeric symbols (excluding the ignore list)
    symbols = []
    for char in command_text:
        if not char.isalnum() and char not in ignore_chars:
            symbols.append(char)
    
    # Return the last symbol found (if any)
    if symbols:
        return symbols[-1]
    
    return None


def check_existing_hidden_div(content: str) -> Tuple[bool, Optional[str]]:
    """
    Check if content already has a hidden div with APL symbol.
    
    Returns:
        (has_div, symbol_in_div) - True if has div, and the symbol if found
    """
    # Pattern to match hidden div at the beginning with APL symbol
    # Allow for variations in formatting (quotes, semicolon, whitespace)
    pattern = r'^<div\s+style\s*=\s*["\']display:\s*none;?["\']>\s*\n\s*(.+?)\s*\n\s*</div>'
    match = re.match(pattern, content, re.IGNORECASE | re.MULTILINE)
    
    if match:
        symbol_content = match.group(1).strip()
        # Check if it's a single non-alphanumeric character (APL symbol)
        if len(symbol_content) == 1 and not symbol_content.isalnum():
            return True, symbol_content
        return True, None
    
    return False, None


def parse_front_matter(content: str) -> Tuple[Optional[str], str, int]:
    """
    Parse front matter from the beginning of content.
    
    Returns:
        (front_matter, remaining_content, end_position) - front matter if found, remaining content, and end position
    """
    # Pattern to match front matter at the very beginning
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        return match.group(0), content[match.end():], match.end()
    
    return None, content, 0


def is_search_excluded(front_matter_content: str) -> bool:
    """
    Check if front matter contains search exclusion.
    
    Returns:
        True if search is excluded, False otherwise
    """
    return bool(re.search(r'search:\s*\n\s*exclude:\s*true', front_matter_content))


def process_file(filepath: str, dry_run: bool = False) -> bool:
    """
    Process a single markdown file.
    
    Returns True if the file was modified (or would be modified in dry-run), False otherwise.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    
    # Parse front matter
    front_matter, remaining_content, _ = parse_front_matter(content)
    
    # Check if file is excluded from search
    if front_matter and is_search_excluded(front_matter):
        print(f"  Skipped: {filename} - excluded from search (synonyms not allowed)")
        return False
    
    # Check if the file already has a hidden div
    has_div, existing_symbol = check_existing_hidden_div(content)
    
    if has_div:
        if existing_symbol:
            print(f"  Skipped: {filename} - already has hidden div with symbol '{existing_symbol}'")
        else:
            print(f"  Skipped: {filename} - already has hidden div")
        return False
    
    # Extract the APL symbol from h1
    symbol = extract_apl_symbol(content)
    
    if symbol:
        if dry_run:
            print(f"  Would add: {filename} - symbol '{symbol}'")
            if front_matter:
                print(f"           (after front matter)")
        else:
            # Create the hidden div
            hidden_div = f'<div style="display: none;">\n  {symbol}\n</div>\n\n'
            
            # Add the div after front matter if present, otherwise at beginning
            if front_matter:
                new_content = front_matter + hidden_div + remaining_content
            else:
                new_content = hidden_div + content
            
            # Write the modified content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  Modified: {filename} - added symbol '{symbol}'")
            if front_matter:
                print(f"           (added after front matter)")
        return True
    else:
        print(f"  Skipped: {filename} - no APL symbol found in <h1><span class='command'>")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Add APL symbol synonyms to markdown files'
    )
    parser.add_argument(
        'directory',
        help='Directory containing markdown files to process'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Only list files that would be modified without making changes'
    )
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a valid directory")
        sys.exit(1)
    
    # Get all .md files in the directory (non-recursive)
    md_files = [
        os.path.join(args.directory, f)
        for f in os.listdir(args.directory)
        if f.endswith('.md') and os.path.isfile(os.path.join(args.directory, f))
    ]
    
    if not md_files:
        print(f"No .md files found in {args.directory}")
        return
    
    # Sort files for consistent output
    md_files.sort()
    
    if args.dry_run:
        print(f"DRY RUN: Checking {len(md_files)} markdown files in {args.directory}...")
    else:
        print(f"Processing {len(md_files)} markdown files in {args.directory}...")
    
    print()  # Empty line for better readability
    
    modified_count = 0
    skipped_count = 0
    
    for filepath in md_files:
        if process_file(filepath, dry_run=args.dry_run):
            modified_count += 1
        else:
            skipped_count += 1
    
    # Summary
    print(f"\n{'=' * 60}")
    if args.dry_run:
        print(f"DRY RUN Summary:")
        print(f"  Would modify: {modified_count} files")
        print(f"  Would skip: {skipped_count} files")
    else:
        print(f"Summary:")
        print(f"  Modified: {modified_count} files")
        print(f"  Skipped: {skipped_count} files")
    print(f"  Total processed: {len(md_files)} files")


if __name__ == '__main__':
    main()