#!/usr/bin/env python3
"""
Spider the deployed Dyalog documentation and verify that all internal links work.
"""

import argparse
import asyncio
import aiohttp
from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime
import sys
from ruamel.yaml import YAML


class LinkChecker:
    def __init__(self, base_url, max_concurrent=5, output_file="broken_links.yaml"):
        self.base_url = base_url.rstrip("/")
        self.max_concurrent = max_concurrent
        self.pages = set()  # All pages found in navigation
        self.checked_links = {}  # Map of link -> (is_valid, status)
        self.broken_links = defaultdict(
            set
        )  # Map of broken link -> pages that reference it
        self.page_broken_links = defaultdict(
            list
        )  # Map of page -> list of broken links
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.pages_processed = 0
        self.pages_failed = 0
        self.output_file = output_file
        self.problematic_pages = set()  # Pages with broken links

    def normalize_url(self, url):
        """Normalise a URL by removing fragments and ensuring consistent format."""
        parsed = urlparse(url)
        # Remove fragment
        normalized = urlunparse(
            (parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, "")
        )
        # For MkDocs, directories often redirect to add trailing slash
        # Don't remove trailing slashes as they may be significant
        # IMPORTANT: Keep .md extensions to track exactly what links are broken
        return normalized

    def is_internal_link(self, url):
        """Check if a URL is internal to the documentation site."""
        return url.startswith(self.base_url)

    def extract_navigation_pages(self, html):
        """Extract all pages from the MkDocs navigation structure."""
        soup = BeautifulSoup(html, "html.parser")
        pages = set()

        # Find all navigation links
        nav_areas = soup.find_all(["nav", "div"], class_=["md-nav", "md-sidebar"])

        for nav in nav_areas:
            # Find all links within navigation
            for link in nav.find_all("a", href=True):
                href = link["href"]
                if not href.startswith(("#", "javascript:", "mailto:", "tel:")):
                    absolute_url = urljoin(self.base_url + "/", href)
                    if self.is_internal_link(absolute_url):
                        normalized = self.normalize_url(absolute_url)
                        pages.add(normalized)

        # Also get links from the main content area to catch any we missed
        content = soup.find("main") or soup.find("div", class_="md-content")
        if content and hasattr(content, "find_all"):
            for link in content.find_all("a", href=True):
                href = link["href"]
                if not href.startswith(("#", "javascript:", "mailto:", "tel:")):
                    absolute_url = urljoin(self.base_url + "/", href)
                    if self.is_internal_link(absolute_url):
                        normalized = self.normalize_url(absolute_url)
                        pages.add(normalized)

        return pages

    def extract_all_links(self, url, html):
        """Extract all links from an HTML page."""
        soup = BeautifulSoup(html, "html.parser")
        links = set()

        # Find the main content area (skip navigation)
        content = (
            soup.find("article")
            or soup.find("main")
            or soup.find("div", class_="md-content")
        )

        if not content:
            # Fallback to the whole page
            content = soup

        # Find all anchor tags in the content area only
        if hasattr(content, "find_all"):
            for tag in content.find_all("a", href=True):
                href = tag["href"]

                # Skip fragments-only links
                if href.startswith("#"):
                    continue

                # Skip special protocols
                if href.startswith(("javascript:", "mailto:", "tel:")):
                    continue

                # Convert relative URLs to absolute
                absolute_url = urljoin(url, href)

                # Only process internal links
                if self.is_internal_link(absolute_url):
                    normalized = self.normalize_url(absolute_url)
                    links.add(normalized)

        return links

    async def check_url(self, session, url):
        """Check if a URL is accessible."""
        # Return cached result if we already checked this URL
        if url in self.checked_links:
            return url, self.checked_links[url][0], self.checked_links[url][1]

        async with self.semaphore:
            try:
                # First try GET (more reliable than HEAD for some servers)
                async with session.get(
                    url, allow_redirects=True, timeout=aiohttp.ClientTimeout(total=5)
                ) as response:
                    # Consider any 2xx or 3xx status as valid (including redirects)
                    is_valid = response.status < 400
                    self.checked_links[url] = (is_valid, response.status)
                    return url, is_valid, response.status
            except asyncio.TimeoutError:
                self.checked_links[url] = (False, "Timeout")
                return url, False, "Timeout"
            except Exception as e:
                error_msg = str(e)[:50]  # Truncate long error messages
                self.checked_links[url] = (False, error_msg)
                return url, False, error_msg

    async def process_page(self, session, page_url):
        """Fetch a page and check all its links."""
        try:
            async with session.get(
                page_url, timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status < 400:
                    html = await response.text()

                    # Extract links from this page
                    links = self.extract_all_links(page_url, html)

                    # Check each link
                    link_tasks = []
                    for link in links:
                        # Only check internal links we haven't checked before
                        if link not in self.checked_links:
                            link_tasks.append(self.check_url(session, link))

                    # Check all links for this page
                    if link_tasks:
                        results = await asyncio.gather(
                            *link_tasks, return_exceptions=True
                        )
                        for result in results:
                            if isinstance(result, Exception):
                                continue
                            if isinstance(result, tuple) and len(result) == 3:
                                url, is_valid, status = result
                                if not is_valid and url in links:
                                    self.broken_links[url].add(page_url)

                    # Also record any previously checked broken links
                    for link in links:
                        if (
                            link in self.checked_links
                            and not self.checked_links[link][0]
                        ):
                            self.broken_links[link].add(page_url)

                    self.pages_processed += 1
                    # Collect broken links for this page with their status
                    page_broken = []
                    for link in links:
                        if link in self.broken_links:
                            status = self.checked_links[link][1]
                            page_broken.append({'url': link, 'status': status})
                    if page_broken:
                        self.problematic_pages.add(page_url)
                        self.page_broken_links[page_url] = page_broken
                    return True
                else:
                    self.pages_failed += 1
                    self.problematic_pages.add(page_url)
                    # Record that this page from navigation couldn't be fetched
                    # This indicates the navigation contains a broken link
                    self.page_broken_links[page_url] = [{
                        'url': page_url,
                        'status': response.status,
                        'found_on': 'NAVIGATION (page in nav but returns error)'
                    }]
                    return False
        except Exception as e:
            self.pages_failed += 1
            self.problematic_pages.add(page_url)
            # Record the error fetching the page from navigation
            error_msg = str(e)[:100]
            self.page_broken_links[page_url] = [{
                'url': page_url,
                'status': f'Error: {error_msg}',
                'found_on': 'NAVIGATION (page in nav but failed to fetch)'
            }]
            return False

    async def spider(self):
        """Spider the documentation starting from the base URL."""
        try:
            # Create a session with custom headers
            connector = aiohttp.TCPConnector(limit=100)
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; Dyalog Documentation Link Checker)"
            }

            async with aiohttp.ClientSession(
                connector=connector, headers=headers
            ) as session:
                # First, get the home page and extract all navigation pages
                start_url = self.base_url
                if not start_url.endswith("/"):
                    start_url += "/"

                # Fetch navigation structure
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Fetching navigation structure...",
                    file=sys.stderr,
                )
                try:
                    async with session.get(
                        start_url, timeout=aiohttp.ClientTimeout(total=30)
                    ) as response:
                        if response.status >= 400:
                            print(
                                f"ERROR: Could not fetch home page: {response.status}",
                                file=sys.stderr,
                            )
                            return
                        html = await response.text()
                except Exception as e:
                    print(f"ERROR: Could not fetch home page: {e}", file=sys.stderr)
                    return

                # Extract all pages from navigation
                self.pages = self.extract_navigation_pages(html)
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Found {len(self.pages)} pages in navigation",
                    file=sys.stderr,
                )

                # Process all pages concurrently
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] Processing pages and checking links...",
                    file=sys.stderr,
                )
                tasks = [
                    self.process_page(session, page_url) for page_url in self.pages
                ]

                # Process in batches with progress
                batch_size = 20
                for i in range(0, len(tasks), batch_size):
                    batch = tasks[i : i + batch_size]
                    await asyncio.gather(*batch, return_exceptions=True)

                    # Progress update
                    print(
                        f"[{datetime.now().strftime('%H:%M:%S')}] Progress: {min(i+batch_size, len(tasks))}/{len(tasks)} pages | "
                        f"{len(self.checked_links)} links checked | "
                        f"{len(self.problematic_pages)} pages with issues | "
                        f"{len(self.broken_links)} broken links",
                        file=sys.stderr,
                    )
        finally:
            # Write YAML output at the end
            self.write_yaml_output()

    def write_yaml_output(self):
        """Write the results to a YAML file."""
        # Separate navigation errors from page content errors
        output_data = {}
        bad_nav_links = []

        for page_url, broken_links in self.page_broken_links.items():
            # Make page URL relative to base URL for cleaner output
            relative_page = page_url.replace(self.base_url, "")
            if not relative_page:
                relative_page = "/"

            # Check if this is a navigation error
            is_nav_error = False
            for link_info in broken_links:
                if isinstance(link_info, dict):
                    found_on = link_info.get('found_on', '')
                    if found_on and 'NAVIGATION' in found_on:
                        is_nav_error = True
                        break

            if is_nav_error:
                # Add to bad navigation links list
                status = broken_links[0]['status'] if broken_links else 'Unknown'
                bad_nav_links.append(f"{relative_page} (Status: {status})")
            else:
                # Regular page with broken links
                formatted_links = []
                for link_info in broken_links:
                    if isinstance(link_info, dict):
                        url = link_info['url']
                        status = link_info['status']

                        # Make internal URLs relative
                        if url.startswith(self.base_url):
                            url = url.replace(self.base_url, "")

                        formatted_links.append(f"{url} (Status: {status})")
                    else:
                        # Fallback for any legacy format
                        formatted_links.append(str(link_info))

                output_data[relative_page] = formatted_links

        # Add bad nav links as a special entry if any exist
        if bad_nav_links:
            # Sort and group bad nav links for better readability
            bad_nav_links.sort()
            output_data = {'Bad nav links:': bad_nav_links, **output_data}

        # Write to YAML file with header comment
        yaml = YAML()
        yaml.preserve_quotes = True
        yaml.default_flow_style = False
        yaml.width = 4096  # Prevent line wrapping
        yaml.indent(mapping=2, sequence=4, offset=2)  # Proper indentation like other scripts

        with open(self.output_file, "w") as f:
            f.write("# Broken Links Report\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Base URL: {self.base_url}\n")
            f.write(f"# Pages with issues: {len(output_data)}\n")
            f.write("#\n")
            f.write("# Format:\n")
            f.write("#   - 'Bad nav links:' = Pages listed in navigation that don't exist\n")
            f.write("#   - Other keys = Pages that exist but contain broken links\n")
            f.write("#   - Values = The broken links found (with HTTP status)\n")
            f.write("#   - Links with .md extensions indicate incorrect markdown links\n")
            f.write("#\n\n")

            if output_data:
                yaml.dump(output_data, f)
            else:
                f.write("# No broken links found\n{}\n")

    def report(self):
        """Show summary of the link check."""
        # Summary to stderr
        print(
            f"\n[{datetime.now().strftime('%H:%M:%S')}] Link check complete!",
            file=sys.stderr,
        )
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Summary:", file=sys.stderr)
        print(f"  - Pages processed: {self.pages_processed}", file=sys.stderr)
        print(f"  - Failed pages: {self.pages_failed}", file=sys.stderr)
        print(f"  - Total links checked: {len(self.checked_links)}", file=sys.stderr)
        print(f"  - Broken links found: {len(self.broken_links)}", file=sys.stderr)
        print(f"  - Pages with issues: {len(self.problematic_pages)}", file=sys.stderr)
        print(
            f"\n[{datetime.now().strftime('%H:%M:%S')}] Broken links report written to: {self.output_file}",
            file=sys.stderr,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Check for broken links in deployed Dyalog documentation"
    )
    parser.add_argument(
        "--base-url",
        default="https://dyalog.github.io/documentation/20.0",
        help="Base URL to check (default: https://dyalog.github.io/documentation/20.0)",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=5,
        help="Maximum concurrent requests (default: 5)",
    )
    parser.add_argument(
        "--output",
        default="broken_links.yaml",
        help="Output file for broken links report in YAML format (default: broken_links.yaml)",
    )

    args = parser.parse_args()

    # Start message
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Starting link check for: {args.base_url}",
        file=sys.stderr,
    )
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Max concurrent requests: {args.max_concurrent}",
        file=sys.stderr,
    )
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Output file: {args.output}",
        file=sys.stderr,
    )

    checker = LinkChecker(args.base_url, args.max_concurrent, args.output)

    # Run the async spider
    asyncio.run(checker.spider())

    checker.report()


if __name__ == "__main__":
    main()
