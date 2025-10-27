#!/usr/bin/env python3
"""
Spider a deployed documentation site using a multi-process worker pool
and report any internal links that fail (HTTP status >= 400).
"""

import argparse
import multiprocessing as mp
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from typing import Dict, Iterable, List, Sequence, Tuple
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from ruamel.yaml import YAML


# Globals initialised in worker processes
SESSION = None
BASE_URL = None
REQUEST_TIMEOUT = None


LINK_RE = re.compile(
    r'<a\b[^>]*href\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))',
    re.IGNORECASE | re.DOTALL,
)
ARTICLE_SECTION_RE = re.compile(
    r'<article\b[^>]*>(.*?)</article>',
    re.IGNORECASE | re.DOTALL,
)
MAIN_SECTION_RE = re.compile(
    r'<main\b[^>]*>(.*?)</main>',
    re.IGNORECASE | re.DOTALL,
)
CONTENT_SECTION_RE = re.compile(
    r'<div\b[^>]*class[^>]*md-content[^>]*>(.*?)</div>',
    re.IGNORECASE | re.DOTALL,
)


def extract_primary_content(html: str) -> str:
    """Return the most relevant content section from the HTML, falling back to the whole page."""
    for pattern in (ARTICLE_SECTION_RE, MAIN_SECTION_RE, CONTENT_SECTION_RE):
        match = pattern.search(html)
        if match:
            return match.group(1)
    return html


def collect_internal_links(html: str, page_base: str, base_url: str) -> set:
    """Extract internal links from the provided HTML snippet using regular expressions."""
    links = set()
    for match in LINK_RE.finditer(html):
        href = (match.group(1) or match.group(2) or match.group(3) or "").strip()
        if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        absolute_url = urljoin(page_base, href)
        if absolute_url.lower().endswith((".pdf", ".docx")):
            continue
        normalized = normalize_url(absolute_url)
        if is_internal_link(normalized, base_url):
            links.add(normalized)
    return links


def init_worker(base_url: str, request_timeout: float) -> None:
    """Initialise a requests.Session in each worker process."""
    global SESSION, BASE_URL, REQUEST_TIMEOUT

    BASE_URL = base_url
    REQUEST_TIMEOUT = request_timeout

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=32,
        pool_maxsize=32,
        max_retries=0,
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    SESSION = session


def normalize_url(url: str) -> str:
    """Normalise a URL by removing fragments but keeping query parameters."""
    parsed = urlparse(url)
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, "")
    )


def is_internal_link(url: str, base_url: str) -> bool:
    """Determine whether the URL points to the same site we are checking."""
    return url.startswith(base_url)


def extract_navigation_pages(html: str, base_url: str) -> Sequence[str]:
    """Extract all pages from the MkDocs navigation and main content areas."""
    pages = collect_internal_links(html, base_url + "/", base_url)
    content_html = extract_primary_content(html)
    pages.update(collect_internal_links(content_html, base_url + "/", base_url))

    return tuple(sorted(pages))


def get_requests_session() -> requests.Session:
    """Return the session initialised for the current worker."""
    if SESSION is None:
        raise RuntimeError("Worker session not initialised")
    return SESSION


def process_page(page_url: str) -> Dict[str, object]:
    """
    Fetch a single page, extract all internal links inside the main content, and
    return a summary dictionary describing the outcome.
    """
    session = get_requests_session()
    result: Dict[str, object] = {
        "page_url": page_url,
        "links": [],
        "status": None,
        "error": None,
    }

    try:
        response = session.get(page_url, timeout=REQUEST_TIMEOUT)
        result["status"] = response.status_code
        if response.status_code >= 400:
            result["error"] = f"Status {response.status_code}"
            return result
        html = response.text
    except Exception as exc:  # pylint: disable=broad-except
        result["error"] = f"Error: {exc}"
        return result

    content_html = extract_primary_content(html)
    links = collect_internal_links(content_html, page_url, BASE_URL)

    result["links"] = tuple(sorted(links))
    return result


def check_link(url: str) -> Dict[str, object]:
    """Check a single link and report status information."""
    session = get_requests_session()
    try:
        response = session.head(url, allow_redirects=True, timeout=REQUEST_TIMEOUT)
        status = response.status_code
        if status in (405, 403) or status >= 400:
            # Fall back to GET for servers that dislike HEAD or to confirm failures
            response = session.get(url, allow_redirects=True, timeout=REQUEST_TIMEOUT)
            status = response.status_code
        return {
            "url": url,
            "ok": status < 400,
            "status": status,
        }
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "url": url,
            "ok": False,
            "status": f"Error: {exc}",
        }


def write_yaml_output(
    base_url: str,
    output_file: str,
    nav_errors: Sequence[Tuple[str, str]],
    page_broken_links: Dict[str, Sequence[Dict[str, object]]],
    total_links_checked: int,
) -> None:
    """Write results to a YAML file mirroring the existing tool format."""
    def to_relative(url: str) -> str:
        relative = url.replace(base_url, "", 1)
        return relative or "/"

    output_data: Dict[str, Iterable[str]] = {}

    for page_url, broken in sorted(page_broken_links.items()):
        relative_page = to_relative(page_url)
        formatted = []
        for info in broken:
            link_url = info["url"]
            status = info["status"]
            if isinstance(link_url, str) and link_url.startswith(base_url):
                link_url = link_url.replace(base_url, "", 1)
            formatted.append(f"{link_url} (Status: {status})")
        output_data[relative_page] = sorted(formatted)

    if nav_errors:
        nav_entries = [
            f"{to_relative(page_url)} (Status: {status})"
            for page_url, status in sorted(nav_errors)
        ]
        output_data = {"Bad nav links:": nav_entries, **output_data}

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 4096
    yaml.indent(mapping=2, sequence=4, offset=2)

    with open(output_file, "w", encoding="utf-8") as handle:
        handle.write("# Broken Links Report\n")
        handle.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        handle.write(f"# Base URL: {base_url}\n")
        handle.write(f"# Links checked: {total_links_checked}\n")
        handle.write("#\n")
        if output_data:
            yaml.dump(output_data, handle)
        else:
            handle.write("# No broken links found\n{}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multiprocess link checker for deployed documentation sites."
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:8080",
        help="Base URL of the deployed documentation site.",
    )
    parser.add_argument(
        "--processes",
        type=int,
        default=max(mp.cpu_count() - 1, 1),
        help="Number of worker processes to use (default: CPU count - 1).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="Request timeout in seconds.",
    )
    parser.add_argument(
        "--output",
        default="broken_links.yaml",
        help="Path to the YAML output file.",
    )

    args = parser.parse_args()
    base_url = args.base_url.rstrip("/")

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Starting link check for: {base_url}",
        file=sys.stderr,
    )
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Worker processes: {args.processes}",
        file=sys.stderr,
    )
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Output file: {args.output}",
        file=sys.stderr,
    )

    start_time = time.time()

    # Fetch navigation in the main process
    session = requests.Session()
    try:
        home_url = base_url if base_url.endswith("/") else base_url + "/"
        response = session.get(home_url, timeout=args.timeout)
        response.raise_for_status()
        navigation_html = response.text
    except Exception as exc:  # pylint: disable=broad-except
        print(f"ERROR: Failed to load base page: {exc}", file=sys.stderr)
        sys.exit(1)

    pages = set(extract_navigation_pages(navigation_html, base_url))
    pages.add(base_url)  # Ensure the landing page is included
    pages = tuple(sorted(pages))

    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] Discovered {len(pages)} pages",
        file=sys.stderr,
    )

    page_broken_links: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    nav_errors: List[Tuple[str, str]] = []
    link_to_pages: Dict[str, List[str]] = defaultdict(list)

    with mp.Pool(
        processes=args.processes,
        initializer=init_worker,
        initargs=(base_url, args.timeout),
    ) as pool:
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Processing pages...",
            file=sys.stderr,
        )

        for idx, result in enumerate(pool.imap_unordered(process_page, pages), start=1):
            page_url = result["page_url"]
            error = result["error"]
            if error:
                nav_errors.append((page_url, error))
            else:
                links = result["links"]
                for link_url in links:
                    link_to_pages[link_url].append(page_url)

            if idx % 50 == 0 or idx == len(pages):
                elapsed = time.time() - start_time
                rate = idx / elapsed if elapsed else 0.0
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] "
                    f"Pages processed: {idx}/{len(pages)} ({rate:.1f}/s)",
                    file=sys.stderr,
                )

        unique_links = tuple(sorted(link_to_pages.keys()))
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Checking {len(unique_links)} unique links...",
            file=sys.stderr,
        )

        link_status: Dict[str, Tuple[bool, object]] = {}
        for idx, result in enumerate(pool.imap_unordered(check_link, unique_links), start=1):
            link_status[result["url"]] = (result["ok"], result["status"])
            if idx % 200 == 0 or idx == len(unique_links):
                elapsed = time.time() - start_time
                rate = idx / elapsed if elapsed else 0.0
                print(
                    f"[{datetime.now().strftime('%H:%M:%S')}] "
                    f"Links checked: {idx}/{len(unique_links)} ({rate:.1f}/s)",
                    file=sys.stderr,
                )

    # Accumulate broken links per page
    for link_url, pages_with_link in link_to_pages.items():
        ok, status = link_status.get(link_url, (False, "Unknown"))
        if ok:
            continue
        for page_url in pages_with_link:
            page_broken_links[page_url].append({"url": link_url, "status": status})

    total_broken = sum(len(entries) for entries in page_broken_links.values())

    elapsed = time.time() - start_time
    print(
        f"\n[{datetime.now().strftime('%H:%M:%S')}] Link check complete!",
        file=sys.stderr,
    )
    print(f"  - Pages processed: {len(pages)}", file=sys.stderr)
    print(f"  - Unique links checked: {len(unique_links)}", file=sys.stderr)
    print(f"  - Broken link references: {total_broken}", file=sys.stderr)
    print(f"  - Pages with issues: {len(page_broken_links)}", file=sys.stderr)
    print(f"  - Navigation errors: {len(nav_errors)}", file=sys.stderr)
    print(f"  - Elapsed time: {elapsed:.1f}s", file=sys.stderr)

    write_yaml_output(
        base_url=base_url,
        output_file=args.output,
        nav_errors=nav_errors,
        page_broken_links=page_broken_links,
        total_links_checked=len(unique_links),
    )

    print(
        f"\n[{datetime.now().strftime('%H:%M:%S')}] Results written to: {args.output}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    mp.freeze_support()
    main()
