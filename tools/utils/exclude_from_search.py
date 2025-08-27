import os
import re
import argparse
from typing import Optional, Tuple

def check_and_remove_hidden_div(content: str) -> Tuple[str, bool, Optional[str]]:
    """
    Check for and remove hidden div with APL symbol.
    
    Returns:
        (modified_content, had_div, symbol) - modified content, whether div was found, and the symbol if found
    """
    # Pattern to match hidden div at the beginning with APL symbol
    # Allow for variations in formatting (quotes, semicolon, whitespace)
    pattern = r'^<div\s+style\s*=\s*["\'']display:\s*none;?["\'']>\s*\n\s*(.+?)\s*\n\s*</div>\s*\n\n?'
    match = re.match(pattern, content, re.IGNORECASE | re.MULTILINE)
    
    if match:
        symbol_content = match.group(1).strip()
        # Check if it's a single non-alphanumeric character (APL symbol)
        if len(symbol_content) == 1 and not symbol_content.isalnum():
            # Remove the hidden div
            modified_content = content[match.end():]
            return modified_content, True, symbol_content
        # Non-APL hidden div found
        return content, True, None
    
    return content, False, None


def add_front_matter(file_path: str) -> None:
    """
    Adds MkDocs 'exclude from search' front matter to markdown file
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} does not exist. Skipping.")
        return
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check for and potentially remove hidden div
    content, had_div, symbol = check_and_remove_hidden_div(content)
    removed_synonym = False
    if had_div and symbol:
        print(f"Removed hidden synonym div with symbol '{symbol}' from {file_path}")
        removed_synonym = True
    
    # Check if the file already has front matter with search exclude
    front_matter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = front_matter_pattern.match(content)
    
    if match:
        # File has front matter, check if it has search exclude
        front_matter_content = match.group(1)
        if re.search(r'search:\s*\n\s*exclude:\s*true', front_matter_content):
            if removed_synonym:
                # We removed a synonym but the search exclude already exists, so rewrite the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Search exclude front matter already exists in {file_path}, but removed synonym div.")
            else:
                print(f"Search exclude front matter already exists in {file_path}. Skipping.")
            return
        else:
            print(f"File {file_path} has front matter but missing search exclude. Leaving unchanged as requested.")
            return
    
    # Front matter to add
    new_front_matter = """---
search:
  exclude: true
---

"""
    
    # Add front matter to the beginning
    new_content = new_front_matter + content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    if removed_synonym:
        print(f"Added front matter to {file_path} and removed synonym div")
    else:
        print(f"Added front matter to {file_path}")

def process_file_list(list_file: str) -> None:
    """
    Reads a text file containing paths and adds front matter to each markdown file
    """
    if not os.path.exists(list_file):
        print(f"Error: List file {list_file} does not exist.")
        return
    
    with open(list_file, 'r', encoding='utf-8') as file:
        for line in file:
            file_path = line.strip()
            if file_path:  # Skip empty lines
                add_front_matter(file_path)

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add 'exclude from search' front matter to markdown files listed in a file"
    )
    parser.add_argument(
        '--exclude-file',
        default='ghost.txt',
        help='Path to the file containing list of markdown files to exclude (default: ghost.txt)'
    )
    args = parser.parse_args()
    
    print(f"Processing files from: {args.exclude_file}")
    process_file_list(args.exclude_file)
    print("Processing complete.")

if __name__ == "__main__":
    main()