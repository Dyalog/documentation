#!/usr/bin/env python3
"""
Update the language-reference-guide/mkdocs.yml nav section for "System Functions (A-Z)"
by extracting command names from the H1 tags in the referenced markdown files
and reordering alphabetically. Also updates all other references to the same files
throughout the mkdocs.yml to maintain consistency.
"""

import re
import argparse
import sys
from pathlib import Path
from ruamel.yaml import YAML


def extract_command_from_h1(file_path):
    """Extract the command name from the H1 tag in a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the specific H1 pattern
        h1_pattern = r'<h1\s+class="heading">.*?<span\s+class="command">(.*?)</span>.*?</h1>'
        match = re.search(h1_pattern, content, re.DOTALL)
        
        if match:
            command = match.group(1).strip()
            # Remove parentheses if present
            command = command.strip('()')
            # Find ⎕ and capture uppercase letters immediately after it
            # Only capture the main command name (uppercase letters only)
            quad_pattern = r'⎕([A-Z]+)'
            quad_match = re.search(quad_pattern, command)
            if quad_match:
                return quad_match.group(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return None


def find_system_functions_section(nav_data):
    """Recursively find the System Functions (A-Z) section in the navigation."""
    for item in nav_data:
        if isinstance(item, dict):
            for key, value in item.items():
                if key == 'System Functions (A-Z)':
                    return value
                elif isinstance(value, list):
                    result = find_system_functions_section(value)
                    if result is not None:
                        return result
    return None


def process_system_functions(sys_funcs_list, base_path):
    """Process the system functions list and return updated entries and file mapping."""
    preserved_entries = []
    items_to_sort = []
    file_path_mapping = {}  # Maps file paths to new titles
    
    # Special entries that shouldn't be processed
    skip_titles = [
        "Introduction",
        "Character Input Output",
        "Evaluated Input Output", 
        "Underscored Alphabetic Characters"
    ]
    
    for item in sys_funcs_list:
        if isinstance(item, dict):
            for title, path in item.items():
                if title in skip_titles:
                    preserved_entries.append(item)
                elif isinstance(path, str) and path.startswith("system-functions/") and path.endswith(".md"):
                    file_path = base_path / "docs" / path
                    command = extract_command_from_h1(file_path)
                    
                    if command:
                        # Create new title with command prefix in code tags with quad symbol
                        new_title = f"<code>⎕{command}</code>: {title}"
                        new_item = {new_title: path}
                        items_to_sort.append((command, new_item))
                        # Store the mapping for this file
                        file_path_mapping[path] = new_title
                    else:
                        # If we couldn't extract a command, preserve as-is
                        items_to_sort.append((title, item))
                else:
                    # Non-system function entries
                    preserved_entries.append(item)
    
    # Sort the items by command name
    items_to_sort.sort(key=lambda x: x[0])
    
    # Build the new list
    new_list = preserved_entries + [item[1] for item in items_to_sort]
    
    return new_list, file_path_mapping


def update_nav_recursively(nav_data, file_path_mapping):
    """Recursively update all navigation entries based on the file path mapping."""
    if isinstance(nav_data, list):
        for i, item in enumerate(nav_data):
            if isinstance(item, dict):
                for key, value in list(item.items()):
                    if isinstance(value, str) and value in file_path_mapping:
                        # Update this entry with the new title
                        del item[key]
                        item[file_path_mapping[value]] = value
                    elif isinstance(value, list):
                        update_nav_recursively(value, file_path_mapping)
    elif isinstance(nav_data, dict):
        for key, value in nav_data.items():
            if isinstance(value, list):
                update_nav_recursively(value, file_path_mapping)


def process_yaml_file(yaml_path, base_path, file_path_mapping, yaml, dry_run=False):
    """Process a single YAML file with the given mappings."""
    if not yaml_path.exists():
        return False
    
    # Load the YAML file
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
    
    # Find the System Functions (A-Z) section
    sys_funcs_section = find_system_functions_section(data['nav'])
    
    if sys_funcs_section is None:
        print(f"Could not find 'System Functions (A-Z)' section in {yaml_path.name}")
        return False
    
    # If we're processing a secondary file, use existing mappings
    if file_path_mapping:
        # Update the section with existing mappings
        for i, item in enumerate(sys_funcs_section):
            if isinstance(item, dict):
                for title, path in list(item.items()):
                    if path in file_path_mapping:
                        del item[title]
                        item[file_path_mapping[path]] = path
    else:
        # This is the primary file, create new mappings
        new_section, file_path_mapping = process_system_functions(sys_funcs_section, base_path)
        sys_funcs_section[:] = new_section
    
    # Update all references throughout the entire navigation
    update_nav_recursively(data['nav'], file_path_mapping)
    
    if not dry_run:
        # Write back the file
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
        print(f"Successfully updated {yaml_path}")
        print(f"Applied {len(file_path_mapping)} file path mappings throughout the navigation")
    
    return file_path_mapping


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Update System Functions (A-Z) section in mkdocs.yml")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without modifying the file")
    args = parser.parse_args()
    
    # Path to the mkdocs.yml file
    base_path = Path(__file__).parent.parent.parent / "language-reference-guide"
    mkdocs_path = base_path / "mkdocs.yml"
    
    # Set up YAML parser to preserve formatting
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)
    
    if args.dry_run:
        # For dry run, just show what would be done
        with open(mkdocs_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
        
        sys_funcs_section = find_system_functions_section(data['nav'])
        if sys_funcs_section is None:
            print("Could not find 'System Functions (A-Z)' section in mkdocs.yml")
            return
        
        new_section, file_path_mapping = process_system_functions(sys_funcs_section, base_path)
        
        print("File path mappings that will be applied:")
        print("-" * 50)
        for path, new_title in sorted(file_path_mapping.items()):
            print(f"{path} -> {new_title}")
        print("-" * 50)
        print(f"Total mappings: {len(file_path_mapping)}")
        print("\nUpdated 'System Functions (A-Z)' section:")
        print("-" * 50)
        yaml_temp = YAML()
        yaml_temp.default_flow_style = False
        yaml_temp.dump({'System Functions (A-Z)': new_section}, sys.stdout)
        print("-" * 50)
        print("(Dry run - no changes made)")
    else:
        # Process mkdocs.yml
        file_path_mapping = process_yaml_file(mkdocs_path, base_path, None, yaml, args.dry_run)


if __name__ == "__main__":
    main()