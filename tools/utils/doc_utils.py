#!/usr/bin/env python3
"""
Common utilities for processing mkdocs documentation.
Provides shared functionality for scripts that analyse and validate documentation.
"""

import os
import re
import sys
from typing import Dict, List, Set, Tuple, Optional, Iterator
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
from ruamel.yaml import YAML


class YAMLLoader:
    """Unified YAML loader with mkdocs custom tag support."""
    
    def __init__(self):
        self.yaml = YAML()
        self.yaml.preserve_quotes = True
    
    def load_file(self, filepath: str) -> Optional[Dict]:
        """Load a YAML file, handling mkdocs custom tags."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return self.yaml.load(f)
        except Exception as e:
            print(f"Error loading {filepath}: {e}", file=sys.stderr)
            return None


class NavTraverser:
    """Traverse mkdocs navigation structures."""
    
    @staticmethod
    def iterate_nav_items(nav_item, callback, context=None):
        """
        Recursively traverse nav structure, calling callback for each item.
        
        Args:
            nav_item: The nav item (dict, list, or string)
            callback: Function to call for each item (item, context) -> None
            context: Optional context passed to callback
        """
        if isinstance(nav_item, dict):
            for _, value in nav_item.items():
                callback(value, context)
                NavTraverser.iterate_nav_items(value, callback, context)
        elif isinstance(nav_item, list):
            for item in nav_item:
                callback(item, context)
                NavTraverser.iterate_nav_items(item, callback, context)
        elif isinstance(nav_item, str):
            callback(nav_item, context)
    
    @staticmethod
    def extract_markdown_files(nav_item) -> Set[str]:
        """Extract all markdown file references from nav structure."""
        files = set()
        
        def collect_file(item, files_set):
            if isinstance(item, str) and item.endswith('.md'):
                files_set.add(item)
        
        NavTraverser.iterate_nav_items(nav_item, collect_file, files)
        return files
    
    @staticmethod
    def find_includes(nav_item) -> Set[str]:
        """Find all !include directives in nav structure."""
        includes = set()
        
        def collect_include(item, includes_set):
            if isinstance(item, str) and item.startswith('!include '):
                include_path = item.replace('!include ', '').strip()
                includes_set.add(include_path)
        
        NavTraverser.iterate_nav_items(nav_item, collect_include, includes)
        return includes


class PathResolver:
    """Handle path resolution for mkdocs structures."""
    
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
    
    def resolve_include(self, include_path: str, base_path: Optional[str] = None) -> str:
        """Resolve an !include directive to full path."""
        if base_path is None:
            base_path = self.root_dir
        
        # Remove ./ prefix if present
        if include_path.startswith('./'):
            include_path = include_path[2:]
        
        return os.path.abspath(os.path.join(base_path, include_path))
    
    def markdown_file_path(self, subsite_dir: str, md_ref: str) -> str:
        """Get the full path for a markdown file reference."""
        # Handle absolute paths
        if md_ref.startswith('/'):
            return os.path.join(subsite_dir, md_ref[1:])
        else:
            return os.path.join(subsite_dir, 'docs', md_ref)
    
    def url_to_source_path(self, url: str, site_mappings: Dict[str, str]) -> Optional[str]:
        """Convert a documentation URL to source file path."""
        # Parse URL to get path components
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p]
        
        if not path_parts:
            return None
        
        # Check if first part matches a known site
        for site_url, site_dir in site_mappings.items():
            if path_parts[0] == site_url:
                # Remove site part and reconstruct path
                remaining = '/'.join(path_parts[1:])
                if not remaining.endswith('.md'):
                    remaining += '.md'
                return self.markdown_file_path(site_dir, remaining)
        
        return None
    
    @staticmethod
    def count_levels_up(path: str) -> int:
        """Count how many directory levels a relative path goes up."""
        levels = 0
        parts = path.split('/')
        for part in parts:
            if part == '..':
                levels += 1
            else:
                break
        return levels


class LinkExtractor:
    """Extract links from markdown content."""
    
    @staticmethod
    def extract_markdown_links(content: str) -> List[Tuple[str, str]]:
        """
        Extract markdown links from content, excluding code blocks.
        Returns list of (text, url) tuples.
        """
        # First, identify code blocks and create a mask to exclude them
        code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
        code_blocks = [(m.start(), m.end()) for m in code_block_pattern.finditer(content)]
        
        # Create a function to check if a position is inside a code block
        def is_in_code_block(pos):
            return any(start <= pos <= end for start, end in code_blocks)
        
        # Pattern to match markdown links [text](url) - excluding image links
        md_link_pattern = re.compile(r'(?<!!)\[(?P<text>[^\]]+)\]\((?P<url>[^)]+)\)')
        
        # Find all markdown style links, excluding those in code blocks
        md_links = []
        for match in md_link_pattern.finditer(content):
            if not is_in_code_block(match.start()):
                md_links.append((match.group('text'), match.group('url')))
        
        return md_links
    
    @staticmethod
    def extract_image_refs(content: str) -> List[str]:
        """Extract image references from markdown content."""
        # Match ![alt](url) pattern
        pattern = r'!\[[^\]]*\]\(([^)]+)\)'
        return re.findall(pattern, content)
    
    @staticmethod
    def categorise_link(url: str) -> str:
        """Categorise a link as internal, external, anchor, etc."""
        if url.startswith('http://') or url.startswith('https://'):
            return 'external'
        elif url.startswith('#'):
            return 'anchor'
        elif url.startswith('mailto:'):
            return 'email'
        else:
            return 'internal'


class HTMLLinkExtractor:
    """Extract links from HTML content using BeautifulSoup."""
    
    @staticmethod
    def extract_links(html_content: str) -> List[str]:
        """Extract all links from HTML content."""
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            links.append(a_tag['href'])
        return links


class MkDocsRepo:
    """Represent a mkdocs monorepo structure."""
    
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
        self.loader = YAMLLoader()
        self.resolver = PathResolver(root_dir)
        self._main_config = None
        self._site_mappings = None
    
    @property
    def main_config(self) -> Dict:
        """Load and cache the main mkdocs.yml configuration."""
        if self._main_config is None:
            config_path = os.path.join(self.root_dir, 'mkdocs.yml')
            self._main_config = self.loader.load_file(config_path)
            if self._main_config is None:
                self._main_config = {}
        return self._main_config
    
    @property
    def site_mappings(self) -> Dict[str, str]:
        """Get mapping of URL paths to source directories."""
        if self._site_mappings is None:
            self._site_mappings = {}
            self._build_site_mappings()
        return self._site_mappings
    
    def _build_site_mappings(self):
        """Build subsite name to directory mappings from included subsites."""
        if 'nav' not in self.main_config:
            return
        
        includes = NavTraverser.find_includes(self.main_config['nav'])
        for include in includes:
            include_path = self.resolver.resolve_include(include)
            if os.path.exists(include_path):
                site_dir = os.path.dirname(include_path)
                # Use directory name as key, matching the original script
                subsite_name = os.path.basename(site_dir)
                site_rel_path = os.path.relpath(site_dir, self.root_dir)
                self._site_mappings[subsite_name] = site_rel_path
    
    @staticmethod
    def _site_name_to_url(site_name: str) -> str:
        """Convert a site name to URL path format."""
        # Simple conversion - in reality mkdocs might have more complex rules
        return site_name.lower().replace(' ', '-').replace('.', '')
    
    def iter_subsites(self) -> Iterator[Tuple[str, str, Dict]]:
        """
        Iterate over all subsites.
        Yields (name, path, config) tuples.
        """
        if 'nav' not in self.main_config:
            return
        
        includes = NavTraverser.find_includes(self.main_config['nav'])
        for include in includes:
            include_path = self.resolver.resolve_include(include)
            if os.path.exists(include_path):
                config = self.loader.load_file(include_path)
                if config:
                    name = os.path.basename(os.path.dirname(include_path))
                    yield name, os.path.dirname(include_path), config
    
    def iter_all_markdown_files(self) -> Iterator[str]:
        """Iterate over all markdown files in all subsites."""
        # Main docs directory
        main_docs = os.path.join(self.root_dir, 'docs')
        if os.path.exists(main_docs):
            for root, _, files in os.walk(main_docs):
                for file in files:
                    if file.endswith('.md'):
                        yield os.path.join(root, file)
        
        # Subsite docs directories
        for _, path, _ in self.iter_subsites():
            docs_dir = os.path.join(path, 'docs')
            if os.path.exists(docs_dir):
                for root, _, files in os.walk(docs_dir):
                    for file in files:
                        if file.endswith('.md'):
                            yield os.path.join(root, file)
    
    def iter_nav_files(self, subsite: Optional[str] = None) -> Iterator[Tuple[str, str]]:
        """
        Iterate over markdown files referenced in navigation.
        
        When a subsite is specified, this still returns ALL files from the entire
        documentation (including main nav), but the caller can filter by path.
        This matches the behaviour of the original dangling_links.py script.
        
        Args:
            subsite: Optional specific subsite to process (used for filtering in caller)
            
        Yields:
            (base_path, file_ref) tuples
        """
        # Always process main nav first
        if 'nav' in self.main_config:
            # First collect files from main nav (excluding includes)
            for item in self._process_nav_item(self.main_config['nav']):
                if isinstance(item, str) and item.endswith('.md'):
                    yield self.root_dir, item
            
            # Then process all subsites
            for name, path, config in self.iter_subsites():
                if 'nav' in config:
                    nav_files = NavTraverser.extract_markdown_files(config['nav'])
                    for file_ref in nav_files:
                        yield path, file_ref
    
    def _process_nav_item(self, nav_item):
        """Process nav item to extract direct markdown references (not includes)."""
        if isinstance(nav_item, dict):
            for _, value in nav_item.items():
                yield from self._process_nav_item(value)
        elif isinstance(nav_item, list):
            for item in nav_item:
                yield from self._process_nav_item(item)
        elif isinstance(nav_item, str):
            if not nav_item.startswith('!include'):
                yield nav_item
    
    def find_print_configs(self) -> Iterator[Tuple[str, str]]:
        """Find all print_mkdocs.yml files in included subsites."""
        for name, path, _ in self.iter_subsites():
            print_config = os.path.join(path, 'print_mkdocs.yml')
            if os.path.exists(print_config):
                yield name, print_config
    
    def determine_file_subsite(self, file_path: str) -> str:
        """
        Determine which subsite a file belongs to.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Subsite name or 'root' if not in a subsite
        """
        rel_path = os.path.relpath(file_path, self.root_dir)
        
        # Check against site directory mappings
        for url_name, site_dir in self.site_mappings.items():
            site_rel_path = os.path.relpath(site_dir, self.root_dir)
            if rel_path.startswith(site_rel_path + os.sep):
                # Return the directory name as the subsite identifier
                return os.path.basename(site_dir)
        
        return 'root'


class LinkValidator:
    """Validate various types of links."""
    
    @staticmethod
    def is_valid_relative_path(source_file: str, relative_link: str, 
                              root_dir: Optional[str] = None,
                              site_mappings: Optional[Dict[str, str]] = None) -> bool:
        """
        Check if a relative link from source_file is valid.
        
        This is an exact port of the validate_links logic from the original dangling_links.py.
        """
        base_dir = os.path.dirname(source_file)
        subsites = site_mappings or {}
        
        # Skip external links, anchor links, and mailto links
        if relative_link.startswith(('http://', 'https://', '#', 'mailto:')):
            return True
        
        # Handle URLs with anchors or query parameters
        url_parts = relative_link.split('#')[0].split('?')[0]
        
        # Parse URL and get the path
        parsed_url = urlparse(url_parts)
        path = unquote(parsed_url.path)
        
        if not path:  # Just an anchor
            return True
        
        # Determine which subsite the current file belongs to
        current_subsite = None
        if root_dir and subsites:
            rel_file_path = os.path.relpath(source_file, root_dir)
            for subsite_name, subsite_path in subsites.items():
                if rel_file_path.startswith(subsite_path + os.sep):
                    current_subsite = subsite_name
                    break
        
        # Initialize variables to track if we found a valid target
        target_found = False
        checked_paths = []
        
        # Determine the target file path
        if os.path.isabs(path):
            # For absolute paths, resolve from the root directory
            target_path = os.path.normpath(os.path.join(root_dir, path.lstrip('/')))
        else:
            # For relative paths, resolve from the current file's directory
            target_path = os.path.normpath(os.path.join(base_dir, path))
        
        # List of possible target paths to check
        paths_to_check = []
        
        # 1. Check the exact path
        paths_to_check.append(target_path)
        
        # 2. If it doesn't end with .md, try adding it
        if not path.endswith('.md'):
            paths_to_check.append(target_path + '.md')
        
        # 3. Check if it's a directory with index.md
        paths_to_check.append(os.path.join(target_path, 'index.md'))
        
        # 3.5 For within-subsite links that might be missing the /docs/ subdirectory
        # This handles cases like ../../the-i-beam-operator/i-beam from within a subsite
        if current_subsite and not path.startswith('/'):
            # Check if the target_path is within the current subsite but missing /docs/
            rel_target = os.path.relpath(target_path, root_dir)
            if rel_target.startswith(current_subsite + '/') and '/docs/' not in rel_target:
                # Extract the part after the subsite name
                path_within_subsite = rel_target[len(current_subsite) + 1:]
                docs_path = os.path.join(root_dir, current_subsite, 'docs', path_within_subsite)
                paths_to_check.append(docs_path)
                if not path.endswith('.md'):
                    paths_to_check.append(docs_path + '.md')
                paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # 4. For paths that look like they might be cross-subsite references,
        # try with 'docs' subdirectory
        if '/' in path and not path.startswith('/'):
            path_parts = target_path.split('/')
            if path_parts and path_parts[0] in subsites:
                subsite_root = os.path.join(root_dir, subsites[path_parts[0]])
                rest_of_path = '/'.join(path_parts[1:])
                docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                paths_to_check.append(docs_path)
                if not rest_of_path.endswith('.md'):
                    # Strip trailing slash before appending .md
                    docs_path_clean = docs_path.rstrip('/')
                    paths_to_check.append(docs_path_clean + '.md')
                paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # 4. For MkDocs-style links without extensions
        # MkDocs resolves these differently than filesystem paths
        if not path.endswith('.md') and not path.endswith('/'):
            # For links that go up levels (../)
            if path.startswith('../'):
                # Try resolving as if we're already at the docs root
                # This handles cases where MkDocs flattens the URL structure
                path_parts = path.split('/')
                non_dot_parts = [p for p in path_parts if p != '..']
                if non_dot_parts:
                    # Try from the same directory as current file
                    same_level_path = os.path.join(base_dir, '/'.join(non_dot_parts))
                    paths_to_check.append(same_level_path)
                    paths_to_check.append(same_level_path + '.md')
                    paths_to_check.append(os.path.join(same_level_path, 'index.md'))
                    
                    # Also try from docs root for deeply nested references
                    from_root = os.path.join(root_dir, '/'.join(non_dot_parts))
                    paths_to_check.append(from_root)
                    paths_to_check.append(from_root + '.md')
                    paths_to_check.append(os.path.join(from_root, 'index.md'))
        
        # 5. For cross-subsite references, try different resolution strategies
        if path.startswith('../') and subsites:
            # Count how many levels up we go
            path_parts = path.split('/')
            up_levels = sum(1 for part in path_parts if part == '..')
            remaining_path = '/'.join(part for part in path_parts if part != '..')
            
            # Try resolving from the root of the current subsite
            if current_subsite:
                current_subsite_root = os.path.join(root_dir, subsites[current_subsite])
                subsite_relative_target = os.path.normpath(os.path.join(current_subsite_root, remaining_path))
                paths_to_check.append(subsite_relative_target)
                if not remaining_path.endswith('.md'):
                    paths_to_check.append(subsite_relative_target + '.md')
                paths_to_check.append(os.path.join(subsite_relative_target, 'index.md'))
            
            # Check if it's a cross-subsite reference
            # e.g., ../windows-ui-guide/session-window -> windows-ui-guide/docs/session-window.md
            if remaining_path and '/' in remaining_path:
                potential_subsite = remaining_path.split('/')[0]
                if potential_subsite in subsites:
                    subsite_root = os.path.join(root_dir, subsites[potential_subsite])
                    # Try with 'docs' subdirectory (common pattern)
                    rest_of_path = '/'.join(remaining_path.split('/')[1:])
                    docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                    paths_to_check.append(docs_path)
                    if not rest_of_path.endswith('.md'):
                        # Strip trailing slash before appending .md
                        docs_path_clean = docs_path.rstrip('/')
                        paths_to_check.append(docs_path_clean + '.md')
                    paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # 5. Handle absolute paths that might be subsite references
        elif path.startswith('/') and subsites:
            path_parts = path.strip('/').split('/')
            if path_parts and path_parts[0] in subsites:
                potential_subsite = path_parts[0]
                subsite_root = os.path.join(root_dir, subsites[potential_subsite])
                # Try with 'docs' subdirectory
                if len(path_parts) > 1:
                    rest_of_path = '/'.join(path_parts[1:])
                    docs_path = os.path.join(subsite_root, 'docs', rest_of_path)
                    paths_to_check.append(docs_path)
                    if not rest_of_path.endswith('.md'):
                        # Strip trailing slash before appending .md
                        docs_path_clean = docs_path.rstrip('/')
                        paths_to_check.append(docs_path_clean + '.md')
                    paths_to_check.append(os.path.join(docs_path, 'index.md'))
        
        # Check all possible paths
        for check_path in paths_to_check:
            checked_paths.append(check_path)
            if os.path.exists(check_path):
                target_found = True
                break
        
        # If still not found, report as invalid
        return target_found
    
    @staticmethod
    def extract_anchor(url: str) -> Optional[str]:
        """Extract anchor from URL if present."""
        if '#' in url:
            return url.split('#', 1)[1]
        return None


class SummaryReporter:
    """Generate consistent summary reports."""
    
    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.errors = []
        self.warnings_list = []
    
    def add_result(self, success: bool, error_msg: Optional[str] = None, warning: bool = False):
        """Add a test result."""
        self.total += 1
        if warning:
            self.warnings += 1
            if error_msg:
                self.warnings_list.append(error_msg)
        elif success:
            self.passed += 1
        else:
            self.failed += 1
            if error_msg:
                self.errors.append(error_msg)
    
    def print_summary(self) -> bool:
        """Print a formatted summary and return True if all passed."""
        print("=" * 60)
        print("SUMMARY:")
        print(f"  Total checked: {self.total}")
        print(f"  Passed: {self.passed}")
        print(f"  Failed: {self.failed}")
        if self.warnings > 0:
            print(f"  Warnings: {self.warnings}")
        
        if self.errors:
            print(f"\nErrors ({len(self.errors)}):")
            for error in self.errors[:10]:  # Show first 10
                print(f"  - {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more")
        
        if self.warnings_list:
            print(f"\nWarnings ({len(self.warnings_list)}):")
            for warning in self.warnings_list[:5]:  # Show first 5
                print(f"  - {warning}")
            if len(self.warnings_list) > 5:
                print(f"  ... and {len(self.warnings_list) - 5} more")
        
        return self.failed == 0