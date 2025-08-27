#!/usr/bin/env python3
"""
Tests for doc_utils module.
"""

import os
import pytest
import tempfile
import shutil
from doc_utils import (
    YAMLLoader, NavTraverser, PathResolver, LinkExtractor,
    HTMLLinkExtractor, LinkValidator, SummaryReporter
)


class TestYAMLLoader:
    """Test YAML loading functionality."""
    
    def test_load_valid_yaml(self):
        """Test loading a valid YAML file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("""
site_name: Test Site
nav:
  - Home: index.md
  - About: about.md
""")
            f.flush()
            
            loader = YAMLLoader()
            config = loader.load_file(f.name)
            
            assert config is not None
            assert config['site_name'] == 'Test Site'
            assert 'nav' in config
            assert len(config['nav']) == 2
            
            os.unlink(f.name)
    
    def test_load_invalid_file(self):
        """Test loading a non-existent file."""
        loader = YAMLLoader()
        config = loader.load_file('/non/existent/file.yml')
        assert config is None
    
    def test_load_with_includes(self):
        """Test loading YAML with !include directives."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as f:
            f.write("""
nav:
  - Getting Started: "!include ./subsite/mkdocs.yml"
  - Reference: reference.md
""")
            f.flush()
            
            loader = YAMLLoader()
            config = loader.load_file(f.name)
            
            assert config is not None
            assert 'nav' in config
            assert config['nav'][0]['Getting Started'] == '!include ./subsite/mkdocs.yml'
            
            os.unlink(f.name)


class TestNavTraverser:
    """Test navigation traversal functionality."""
    
    def test_extract_markdown_files(self):
        """Test extracting markdown files from nav structure."""
        nav = [
            {'Home': 'index.md'},
            {'Guide': [
                {'Installation': 'guide/install.md'},
                {'Configuration': 'guide/config.md'}
            ]},
            'about.md'
        ]
        
        files = NavTraverser.extract_markdown_files(nav)
        
        assert len(files) == 4
        assert 'index.md' in files
        assert 'guide/install.md' in files
        assert 'guide/config.md' in files
        assert 'about.md' in files
    
    def test_find_includes(self):
        """Test finding !include directives."""
        nav = [
            {'Home': 'index.md'},
            {'Subsite': '!include ./subsite/mkdocs.yml'},
            {'Another': '!include ./another/mkdocs.yml'},
            'regular.md'
        ]
        
        includes = NavTraverser.find_includes(nav)
        
        assert len(includes) == 2
        assert './subsite/mkdocs.yml' in includes
        assert './another/mkdocs.yml' in includes
    
    def test_iterate_nav_items(self):
        """Test nav iteration with callback."""
        nav = [
            {'Home': 'index.md'},
            {'Nested': [
                {'Deep': [
                    {'Very Deep': 'deep.md'}
                ]}
            ]}
        ]
        
        items = []
        def collect_item(item, context):
            items.append(item)
        
        NavTraverser.iterate_nav_items(nav, collect_item)
        
        # Should collect all items including dicts and lists
        assert 'index.md' in items
        assert 'deep.md' in items


class TestPathResolver:
    """Test path resolution functionality."""
    
    def test_resolve_include(self):
        """Test resolving !include paths."""
        with tempfile.TemporaryDirectory() as tmpdir:
            resolver = PathResolver(tmpdir)
            
            # Test with ./ prefix
            resolved = resolver.resolve_include('./subsite/mkdocs.yml')
            expected = os.path.join(tmpdir, 'subsite', 'mkdocs.yml')
            assert os.path.normpath(resolved) == os.path.normpath(expected)
            
            # Test without ./ prefix
            resolved = resolver.resolve_include('subsite/mkdocs.yml')
            assert os.path.normpath(resolved) == os.path.normpath(expected)
            
            # Test with custom base path
            base = os.path.join(tmpdir, 'docs')
            resolved = resolver.resolve_include('config.yml', base)
            expected = os.path.join(base, 'config.yml')
            assert os.path.normpath(resolved) == os.path.normpath(expected)
    
    def test_markdown_file_path(self):
        """Test markdown file path resolution."""
        resolver = PathResolver('/root')
        
        # Test relative path
        path = resolver.markdown_file_path('/site', 'guide/install.md')
        assert path == os.path.join('/site', 'docs', 'guide', 'install.md')
        
        # Test absolute path (starts with /)
        path = resolver.markdown_file_path('/site', '/guide/install.md')
        assert path == os.path.join('/site', 'guide', 'install.md')
    
    def test_count_levels_up(self):
        """Test counting directory levels."""
        assert PathResolver.count_levels_up('file.md') == 0
        assert PathResolver.count_levels_up('../file.md') == 1
        assert PathResolver.count_levels_up('../../file.md') == 2
        assert PathResolver.count_levels_up('../../../dir/file.md') == 3
        assert PathResolver.count_levels_up('dir/file.md') == 0


class TestLinkExtractor:
    """Test link extraction functionality."""
    
    def test_extract_markdown_links(self):
        """Test extracting markdown links."""
        content = """
        This is a [test link](test.md) and another [external](https://example.com).
        Here's an [anchor link](#section) too.
        """
        
        links = LinkExtractor.extract_markdown_links(content)
        
        assert len(links) == 3
        assert ('test link', 'test.md') in links
        assert ('external', 'https://example.com') in links
        assert ('anchor link', '#section') in links
    
    def test_extract_image_refs(self):
        """Test extracting image references."""
        content = """
        ![Alt text](image.png)
        ![](another.jpg)
        Regular [link](test.md) should not be included.
        """
        
        images = LinkExtractor.extract_image_refs(content)
        
        assert len(images) == 2
        assert 'image.png' in images
        assert 'another.jpg' in images
    
    def test_categorise_link(self):
        """Test link categorisation."""
        assert LinkExtractor.categorise_link('http://example.com') == 'external'
        assert LinkExtractor.categorise_link('https://example.com') == 'external'
        assert LinkExtractor.categorise_link('#section') == 'anchor'
        assert LinkExtractor.categorise_link('mailto:test@example.com') == 'email'
        assert LinkExtractor.categorise_link('guide/install.md') == 'internal'
        assert LinkExtractor.categorise_link('../about.md') == 'internal'
    
    def test_extract_links_excludes_code_blocks(self):
        """Test that links in code blocks are excluded."""
        content = """
        Regular [link](test.md) here.
        
        ```
        # This is code
        [link in code](code.md) should be ignored
        ```
        
        Another [valid link](valid.md).
        
        ```apl
        ⍝ APL code block
        result←[.5](1 2)  ⍝ This looks like a link but isn't
        ```
        
        And [final link](final.md).
        """
        
        links = LinkExtractor.extract_markdown_links(content)
        
        # Should only find the regular links, not ones in code blocks
        assert len(links) == 3
        link_urls = [url for _, url in links]
        assert 'test.md' in link_urls
        assert 'valid.md' in link_urls
        assert 'final.md' in link_urls
        assert 'code.md' not in link_urls
        assert '.5' not in link_urls


class TestHTMLLinkExtractor:
    """Test HTML link extraction functionality."""
    
    def test_extract_links(self):
        """Test extracting links from HTML."""
        html = """
        <html>
        <body>
            <a href="page1.html">Page 1</a>
            <a href="https://example.com">External</a>
            <a>No href</a>
            <a href="#section">Anchor</a>
        </body>
        </html>
        """
        
        links = HTMLLinkExtractor.extract_links(html)
        
        assert len(links) == 3
        assert 'page1.html' in links
        assert 'https://example.com' in links
        assert '#section' in links


class TestLinkValidator:
    """Test link validation functionality."""
    
    def test_is_valid_relative_path(self):
        """Test relative path validation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test files
            source_file = os.path.join(tmpdir, 'docs', 'index.md')
            os.makedirs(os.path.dirname(source_file))
            
            # Create target file
            target_file = os.path.join(tmpdir, 'docs', 'about.md')
            with open(target_file, 'w') as f:
                f.write('# About')
            
            # Test valid relative link
            assert LinkValidator.is_valid_relative_path(source_file, 'about.md')
            
            # Test invalid relative link
            assert not LinkValidator.is_valid_relative_path(source_file, 'missing.md')
            
            # Test link with anchor
            assert LinkValidator.is_valid_relative_path(source_file, 'about.md#section')
    
    def test_extract_anchor(self):
        """Test anchor extraction."""
        assert LinkValidator.extract_anchor('page.md#section') == 'section'
        assert LinkValidator.extract_anchor('page.md#section#subsection') == 'section#subsection'
        assert LinkValidator.extract_anchor('page.md') is None
    
    def test_cross_subsite_links(self):
        """Test cross-subsite link resolution with proper MkDocs handling."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure mimicking the real documentation
            os.makedirs(os.path.join(tmpdir, 'release-notes', 'docs', 'announcements'))
            os.makedirs(os.path.join(tmpdir, 'programming-reference-guide', 'docs', 'introduction', 'arrays'))
            os.makedirs(os.path.join(tmpdir, 'language-reference-guide', 'docs', 'primitive-operators'))
            
            # Create target files
            with open(os.path.join(tmpdir, 'programming-reference-guide', 'docs', 'introduction', 'arrays', 'array-notation.md'), 'w') as f:
                f.write('# Array Notation')
            
            with open(os.path.join(tmpdir, 'language-reference-guide', 'docs', 'primitive-operators', 'behind.md'), 'w') as f:
                f.write('# Behind')
            
            # Source file
            source_file = os.path.join(tmpdir, 'release-notes', 'docs', 'announcements', 'index.md')
            with open(source_file, 'w') as f:
                f.write('# Announcements')
            
            # Site mappings
            site_mappings = {
                'release-notes': 'release-notes',
                'programming-reference-guide': 'programming-reference-guide',
                'language-reference-guide': 'language-reference-guide'
            }
            
            # Test 1: Cross-subsite link with trailing slash (should be VALID)
            # Trailing slashes have no special meaning in MkDocs
            link1 = '../../programming-reference-guide/introduction/arrays/array-notation/'
            result1 = LinkValidator.is_valid_relative_path(source_file, link1, tmpdir, site_mappings)
            assert result1, (
                f"Link '{link1}' should be VALID. MkDocs resolves this to the .md file, "
                f"and trailing slashes have no special meaning."
            )
            
            # Test 2: Another cross-subsite link with trailing slash (should be VALID)
            link2 = '../../language-reference-guide/primitive-operators/behind/'
            result2 = LinkValidator.is_valid_relative_path(source_file, link2, tmpdir, site_mappings)
            assert result2, (
                f"Link '{link2}' should be VALID. The implementation correctly handles "
                f"cross-subsite references with trailing slashes."
            )
            
            # Test 3: Cross-subsite link without .md extension (should be VALID)
            link3 = '../../programming-reference-guide/introduction/arrays/array-notation'
            result3 = LinkValidator.is_valid_relative_path(source_file, link3, tmpdir, site_mappings)
            assert result3, (
                f"Link '{link3}' should be VALID. MkDocs resolves links without .md extension."
            )
            
            # Test 4: Actually broken link (file doesn't exist)
            broken_link = '../../programming-reference-guide/introduction/arrays/missing-file/'
            result4 = LinkValidator.is_valid_relative_path(source_file, broken_link, tmpdir, site_mappings)
            assert not result4, (
                f"Link '{broken_link}' should be INVALID because the target file doesn't exist."
            )
    
    def test_trailing_slash_handling(self):
        """Test that trailing slashes have no special meaning in MkDocs."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test structure
            os.makedirs(os.path.join(tmpdir, 'docs', 'guide'))
            
            # Create a file
            with open(os.path.join(tmpdir, 'docs', 'guide', 'test.md'), 'w') as f:
                f.write('# Test')
            
            source_file = os.path.join(tmpdir, 'docs', 'index.md')
            with open(source_file, 'w') as f:
                f.write('# Index')
            
            # Test 1: Link without trailing slash and without .md (should resolve via MkDocs style)
            link_no_slash = 'guide/test'
            result1 = LinkValidator.is_valid_relative_path(source_file, link_no_slash)
            assert result1, "MkDocs-style link (no .md, no slash) should resolve to guide/test.md"
            
            # Test 2: Link WITH trailing slash (should also resolve)
            link_with_slash = 'guide/test/'
            result2 = LinkValidator.is_valid_relative_path(source_file, link_with_slash)
            assert result2, (
                "Link with trailing slash should ALSO resolve to guide/test.md because "
                "trailing slashes have no special meaning in MkDocs"
            )
            
            # Test 3: Link with .md extension (should resolve)
            link_with_md = 'guide/test.md'
            result3 = LinkValidator.is_valid_relative_path(source_file, link_with_md)
            assert result3, "Link with .md extension should resolve"
            
            # Test 4: Actually broken link
            broken_link = 'guide/missing/'
            result4 = LinkValidator.is_valid_relative_path(source_file, broken_link)
            assert not result4, "Link to non-existent file should not resolve"
    
    def test_within_subsite_links_without_md(self):
        """Test within-subsite links without .md extension are resolved correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create subsite structure
            os.makedirs(os.path.join(tmpdir, 'language-reference-guide', 'docs', 'primitive-operators'))
            os.makedirs(os.path.join(tmpdir, 'language-reference-guide', 'docs', 'the-i-beam-operator'))
            
            # Create target file
            with open(os.path.join(tmpdir, 'language-reference-guide', 'docs', 'the-i-beam-operator', 'i-beam.md'), 'w') as f:
                f.write('# I-Beam')
            
            # Source file
            source_file = os.path.join(tmpdir, 'language-reference-guide', 'docs', 'primitive-operators', 'i-beam-short.md')
            with open(source_file, 'w') as f:
                f.write('# I-Beam Short')
            
            # Site mappings
            site_mappings = {
                'language-reference-guide': 'language-reference-guide'
            }
            
            # Test: Link without .md extension within same subsite
            link = '../../the-i-beam-operator/i-beam'
            result = LinkValidator.is_valid_relative_path(source_file, link, tmpdir, site_mappings)
            assert result, (
                f"Link '{link}' should resolve to i-beam.md. "
                f"Within-subsite links without .md extension should be handled correctly."
            )


class TestSummaryReporter:
    """Test summary reporting functionality."""
    
    def test_add_results(self):
        """Test adding test results."""
        reporter = SummaryReporter()
        
        reporter.add_result(True)
        reporter.add_result(True)
        reporter.add_result(False, "Error 1")
        reporter.add_result(False, "Error 2")
        reporter.add_result(True, "Warning 1", warning=True)
        
        assert reporter.total == 5
        assert reporter.passed == 2
        assert reporter.failed == 2
        assert reporter.warnings == 1
        assert len(reporter.errors) == 2
        assert len(reporter.warnings_list) == 1
    
    def test_print_summary(self, capsys):
        """Test summary printing."""
        reporter = SummaryReporter()
        
        reporter.add_result(True)
        reporter.add_result(False, "Test error")
        reporter.add_result(True, "Test warning", warning=True)
        
        result = reporter.print_summary()
        
        assert not result  # Should return False because there's a failure
        
        captured = capsys.readouterr()
        assert "Total checked: 3" in captured.out
        assert "Passed: 1" in captured.out
        assert "Failed: 1" in captured.out
        assert "Warnings: 1" in captured.out
        assert "Test error" in captured.out
        assert "Test warning" in captured.out
    
    def test_print_summary_all_passed(self):
        """Test summary when all tests pass."""
        reporter = SummaryReporter()
        
        reporter.add_result(True)
        reporter.add_result(True)
        reporter.add_result(True)
        
        result = reporter.print_summary()
        
        assert result  # Should return True when all pass


if __name__ == '__main__':
    pytest.main([__file__, '-v'])