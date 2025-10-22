#!/usr/bin/env python3
"""
render.py - Live Markdown Renderer with Auto-Reload

A live markdown renderer that converts markdown files to HTML with automatic
browser refresh. Perfect for testing markdown files before building the full site.

FEATURES
--------
- Live preview with auto-reload on file changes
- Uses exact same CSS as the live MkDocs site (from documentation-assets)
- Uses same markdown extensions as MkDocs (pymdownx, tables, admonitions, etc.)
- Proper rendering of tables with column alignment
- Built-in HTTP server for proper JavaScript execution

USAGE
-----

Docker Usage (Recommended):
    From the tools/ directory, with DOCS_DIR and ASSETS_DIR in .env:

    $ docker compose run --rm utils python /utils/render.py /docs/tools/file.md --no-browser

    Note: Use --no-browser in Docker as browser can't be opened from container.
    The HTML file will be created in the same directory as the source file.

Local Usage:
    $ cd tools
    $ source ../docs-venv/bin/activate
    $ python utils/render.py primitive-functions-by-category.md

    This will:
    1. Render the markdown to HTML
    2. Start a local web server on port 8000
    3. Open your default browser to view the rendered HTML
    4. Watch for changes to the markdown file
    5. Auto-reload the browser when changes are detected

OPTIONS
-------
    --output, -o FILE    Custom output HTML file (default: same name as input with .html)
    --port, -p PORT      Port for HTTP server (default: 8000)
    --no-browser         Don't open browser automatically (useful for Docker)
    --help, -h           Show help message

EXAMPLES
--------
    # Basic local usage with auto-browser-open
    $ python utils/render.py document.md

    # Docker usage
    $ docker compose run --rm utils python /utils/render.py /docs/tools/document.md --no-browser

    # Custom output file
    $ python utils/render.py input.md --output /tmp/preview.html

    # Custom port
    $ python utils/render.py input.md --port 8080

CSS SOURCES
-----------
The script automatically loads CSS with the following priority:

1. External CSS (Preferred):
   Loads main.css and extra.css from documentation-assets:
   - In Docker: Mounted at /docs/docs/documentation-assets
   - Locally: Auto-detected relative to the script location
   - Gives exact same styling as the live MkDocs site
   - Includes all custom Dyalog documentation styles
   - Table alignment rules that respect markdown column syntax
   - Success message: "✓ Loaded CSS from /path/to/documentation-assets"

2. Embedded CSS (Fallback):
   Falls back to built-in CSS if documentation-assets not found:
   - Warning: "⚠ Warning: documentation-assets not found, using embedded CSS"
   - Still provides good styling but may not match live site exactly
   - Useful for standalone usage without the git submodule

To use external CSS:
   - Make sure documentation-assets submodule is initialized
   - Set ASSETS_DIR in your .env file (for Docker)

MARKDOWN EXTENSIONS
-------------------
Renders markdown using the same extensions as MkDocs:
- admonition - Admonition blocks (notes, warnings, tips, etc.)
- pymdownx.details - Collapsible details/summary blocks
- pymdownx.keys - Keyboard key rendering (++ctrl+alt+del++)
- pymdownx.superfences - Enhanced code fences
- pymdownx.highlight - Syntax highlighting with Pygments
- pymdownx.arithmatex - Math notation support (MathJax/KaTeX)
- attr_list - Attribute lists for styling
- abbr - Abbreviations
- footnotes - Footnote support
- md_in_html - Markdown inside HTML blocks
- markdown_tables_extended - Extended table syntax (colspan, rowspan, captions)
- toc - Table of contents with heading anchors

STYLING
-------
The rendered HTML includes comprehensive CSS for:
- Clean, readable typography
- Syntax highlighting via Pygments
- Extended table support - column/row spans, captions, alignment (:--:, ---:, :---)
- Admonition blocks - styled notes, warnings, tips, info boxes
- Collapsible sections - details/summary elements
- Keyboard keys - <kbd> styling for key combinations
- Support for .heading and .name classes (used in Dyalog docs)
- Responsive layout optimized for documentation

TIPS
----
- Keep the terminal window open to see render status messages
- Edit your markdown file in any editor - changes will be detected automatically
- Press Ctrl+C in the terminal to stop the server
- The generated HTML file is saved next to the markdown file

TROUBLESHOOTING
---------------
Port already in use:
    $ python utils/render.py input.md --port 8080

Browser doesn't open:
    - Manually navigate to http://localhost:8000/filename.html
    - Or use --no-browser flag and open manually

Changes not detected:
    - Make sure you're saving the file
    - Check the terminal for error messages
    - Try editing from a different editor (some use atomic saves that confuse watchers)
"""

import argparse
import os
import sys
import time
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import markdown
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def find_assets_dir():
    """
    Find the documentation-assets directory.

    Checks multiple locations:
    1. /docs/docs/documentation-assets (Docker mount)
    2. ../documentation-assets (local relative)
    3. ../../documentation-assets (from tools/utils)
    """
    candidates = [
        Path('/docs/docs/documentation-assets'),  # Docker
        Path(__file__).parent.parent.parent / 'documentation-assets',  # Local from tools/utils/
        Path(__file__).parent.parent / 'documentation-assets',  # Local from tools/
    ]

    for path in candidates:
        if path.exists() and (path / 'css').exists():
            return path

    return None


def load_external_css():
    """Load CSS from documentation-assets if available."""
    assets_dir = find_assets_dir()

    if not assets_dir:
        print("⚠ Warning: documentation-assets not found, using embedded CSS", file=sys.stderr)
        return None

    css_files = [
        assets_dir / 'css' / 'main.css',
        assets_dir / 'css' / 'extra.css',
    ]

    combined_css = []
    for css_file in css_files:
        if css_file.exists():
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    combined_css.append(f"/* From {css_file.name} */\n{f.read()}\n")
            except Exception as e:
                print(f"⚠ Warning: Could not read {css_file}: {e}", file=sys.stderr)

    if combined_css:
        print(f"✓ Loaded CSS from {assets_dir}")
        return '\n'.join(combined_css)

    return None

# HTML template with live-reload script
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css}
    </style>
    <script>
        let lastModified = {timestamp};

        function checkForUpdates() {{
            fetch('?check=' + Date.now())
                .then(response => response.text())
                .then(html => {{
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newTimestamp = parseInt(doc.querySelector('script').textContent.match(/lastModified = (\\d+)/)[1]);

                    if (newTimestamp > lastModified) {{
                        console.log('Content updated, reloading...');
                        showReloadIndicator();
                        setTimeout(() => location.reload(), 500);
                    }}
                }})
                .catch(err => console.error('Check failed:', err));
        }}

        function showReloadIndicator() {{
            const indicator = document.getElementById('reload-indicator');
            indicator.style.display = 'block';
            setTimeout(() => indicator.style.display = 'none', 1000);
        }}

        // Check for updates every second
        setInterval(checkForUpdates, 1000);
    </script>
</head>
<body>
    <div id="reload-indicator">Updated ✓</div>
    {content}
</body>
</html>
"""


class MarkdownRenderer:
    def __init__(self, input_file, output_file=None):
        self.input_file = Path(input_file).resolve()
        if not self.input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        if output_file:
            self.output_file = Path(output_file).resolve()
        else:
            self.output_file = self.input_file.with_suffix('.html')

        self.last_render_time = 0

    def _get_embedded_css(self):
        """Return embedded CSS as fallback when documentation-assets is not available."""
        return """        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
            color: #333;
        }
        code {
            font-family: "APL385 Unicode", Consolas, Monaco, monospace;
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
        }
        pre {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
        }
        pre code {
            background: none;
            padding: 0;
        }
        /* Tables - with extended syntax support */
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            display: table;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
        }
        /* Default left alignment, but allow align attribute to override */
        th:not([align]), td:not([align]) {
            text-align: left;
        }
        /* Respect align attributes from markdown */
        th[align="left"], td[align="left"] {
            text-align: left;
        }
        th[align="center"], td[align="center"] {
            text-align: center;
        }
        th[align="right"], td[align="right"] {
            text-align: right;
        }
        th {
            background-color: #f8f8f8;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        /* Support for column/row spans from markdown_tables_extended */
        td[colspan], th[colspan] {
            text-align: center;
        }
        /* Caption support */
        table caption {
            caption-side: top;
            padding: 10px;
            font-weight: bold;
            text-align: left;
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        h1 {
            font-size: 2em;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.3em;
        }
        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.3em;
        }
        h3 { font-size: 1.25em; }
        h4 { font-size: 1em; }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        blockquote {
            border-left: 4px solid #ddd;
            padding: 0 15px;
            color: #666;
            margin: 20px 0;
        }
        .heading {
            overflow: hidden;
            background-color: #d9d9d9;
            border: solid 1px #000;
            font-size: 14pt;
            padding: 10px;
            margin-bottom: 20px;
        }
        .name {
            color: black;
            font-weight: bold;
        }
        /* Admonitions */
        .admonition {
            margin: 20px 0;
            padding: 0;
            border-left: 4px solid #448aff;
            border-radius: 4px;
            background-color: #e7f2ff;
        }
        .admonition-title {
            margin: 0;
            padding: 10px 15px;
            font-weight: bold;
            background-color: rgba(68, 138, 255, 0.1);
        }
        .admonition > p {
            padding: 10px 15px;
            margin: 0;
        }
        .admonition.note {
            border-left-color: #448aff;
            background-color: #e7f2ff;
        }
        .admonition.warning {
            border-left-color: #ff9800;
            background-color: #fff3e0;
        }
        .admonition.danger {
            border-left-color: #f44336;
            background-color: #ffebee;
        }
        .admonition.tip {
            border-left-color: #00bcd4;
            background-color: #e0f7fa;
        }
        .admonition.info {
            border-left-color: #00b0ff;
            background-color: #e1f5fe;
        }
        /* Details/Summary (collapsible sections) */
        details {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #fafafa;
        }
        details summary {
            cursor: pointer;
            font-weight: bold;
            user-select: none;
            margin: -15px;
            padding: 15px;
            background-color: #f5f5f5;
            border-radius: 4px 4px 0 0;
        }
        details[open] summary {
            margin-bottom: 15px;
            border-bottom: 1px solid #ddd;
        }
        details summary:hover {
            background-color: #eee;
        }
        /* Keyboard keys */
        kbd, .keys kbd {
            display: inline-block;
            padding: 3px 7px;
            font-family: monospace;
            font-size: 0.9em;
            color: #333;
            background-color: #f7f7f7;
            border: 1px solid #ccc;
            border-radius: 3px;
            box-shadow: 0 1px 0 rgba(0,0,0,0.2);
        }
        /* Syntax highlighting via Pygments */
        .highlight {
            background: #f8f8f8;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
        }
        .highlight pre {
            margin: 0;
            padding: 0;
            border: none;
            background: none;
        }
        #reload-indicator {
            position: fixed;
            top: 10px;
            right: 10px;
            background: #4CAF50;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 14px;
            display: none;
            z-index: 1000;
            animation: fadeInOut 1s;
        }
        @keyframes fadeInOut {
            0%, 100% { opacity: 0; }
            50% { opacity: 1; }
        }"""

    def render(self):
        """Render the markdown file to HTML."""
        print(f"Rendering {self.input_file.name}...")

        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # Render markdown to HTML with same extensions as mkdocs
            html_content = markdown.markdown(
                md_content,
                extensions=[
                    'admonition',
                    'pymdownx.details',
                    'pymdownx.keys',
                    'pymdownx.superfences',
                    'pymdownx.highlight',
                    'pymdownx.arithmatex',
                    'attr_list',
                    'abbr',
                    'footnotes',
                    'md_in_html',
                    'markdown_tables_extended',
                    'toc',
                ],
                extension_configs={
                    'pymdownx.highlight': {
                        'pygments_lang_class': True,
                    },
                    'pymdownx.arithmatex': {
                        'generic': True,
                    },
                    'toc': {
                        'title': 'On this page',
                    }
                }
            )

            # Get title from filename
            title = self.input_file.stem.replace('-', ' ').title()

            # Load CSS (external if available, embedded as fallback)
            external_css = load_external_css()
            css_content = external_css if external_css else self._get_embedded_css()

            # Create full HTML with template
            timestamp = int(time.time() * 1000)
            full_html = HTML_TEMPLATE.format(
                title=title,
                css=css_content,
                content=html_content,
                timestamp=timestamp
            )

            # Write to output file
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(full_html)

            self.last_render_time = time.time()
            print(f"✓ Rendered to {self.output_file}")
            return True

        except Exception as e:
            print(f"✗ Error rendering: {e}", file=sys.stderr)
            return False


class MarkdownWatcher(FileSystemEventHandler):
    def __init__(self, renderer):
        self.renderer = renderer
        self.last_modified = 0

    def on_modified(self, event):
        if event.src_path == str(self.renderer.input_file):
            # Debounce: only render if more than 0.5 seconds have passed
            current_time = time.time()
            if current_time - self.last_modified > 0.5:
                self.last_modified = current_time
                self.renderer.render()


class QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
    """HTTP request handler that only logs errors."""

    def log_message(self, format, *args):
        # Only log errors, not every request
        if args[1] != '200':
            super().log_message(format, *args)


def serve_file(output_file, port=8000):
    """Start a simple HTTP server to serve the HTML file."""
    os.chdir(output_file.parent)

    handler = QuietHTTPRequestHandler
    httpd = HTTPServer(('localhost', port), handler)

    print(f"\n📡 Serving at http://localhost:{port}/{output_file.name}")
    print(f"👁  Watching {output_file.parent} for changes...")
    print("Press Ctrl+C to stop\n")

    httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(
        description='Live Markdown renderer with auto-reload',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.md
  %(prog)s document.md --output custom.html
  %(prog)s document.md --port 8080 --no-browser
        """
    )
    parser.add_argument('input_file', help='Markdown file to render')
    parser.add_argument('-o', '--output', help='Output HTML file (default: same name as input with .html extension)')
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port for HTTP server (default: 8000)')
    parser.add_argument('--no-browser', action='store_true', help='Do not open browser automatically')

    args = parser.parse_args()

    try:
        # Create renderer
        renderer = MarkdownRenderer(args.input_file, args.output)

        # Initial render
        if not renderer.render():
            sys.exit(1)

        # Set up file watcher
        event_handler = MarkdownWatcher(renderer)
        observer = Observer()
        observer.schedule(event_handler, str(renderer.input_file.parent), recursive=False)
        observer.start()

        # Start HTTP server in a thread
        server_thread = threading.Thread(
            target=serve_file,
            args=(renderer.output_file, args.port),
            daemon=True
        )
        server_thread.start()

        # Open browser
        if not args.no_browser:
            time.sleep(0.5)  # Give server time to start
            url = f"http://localhost:{args.port}/{renderer.output_file.name}"
            print(f"🌐 Opening {url} in browser...")
            webbrowser.open(url)

        # Keep running until Ctrl+C
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
            observer.stop()
            observer.join()

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
