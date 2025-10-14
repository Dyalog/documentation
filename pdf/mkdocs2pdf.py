#!/usr/bin/env python3

"""
Convert a mkdocs site to a PDF file.

By Stefan Kruger <stefan@dyalog.com>

python mkdocs2pdf.py           \
    --mkdocs-yml ../mkdocs.yml \
    --project-dir project      \
    --assets-dir assets        \
    --config config.json                

Optional switches:

    --document language-reference-guide  Use instead of --config for single doc
    --exclude list-of-files.json         Exclude files present in source mkdocs.yml
    --disable-toc                        Disable print-style table of contents listing
    --disable-link-rewriting             Disable print-style section numbering of links
    --disable-syntax-highlighting        Disable syntax highlighting
    --disable-section-numbers            Disable print-style section numbers
    --screen                             Make screen-oriented PDF (no ToC, no section numbers)
    --html-only                          Generate unified HTML-file, but not PDF-conversion
    --verbose                            Show verbose Weasyprint output 

The results will end up as

    <project-dir>/<document>.[htm|pdf]


NOTES:

The PDF table of contents is generated entirely in paged-media CSS. It ignores the mkdocs.yml navigation titles, relying entirely on the headings in the markdown files: CSS for obvious reasons doesn't see the mkdocs.yml file.

For anyone tempted to change how the ToC is generated, remember Chesterton's Fence. You break it, you own it -- and break it you will.
"""

import argparse
from datetime import datetime
import json
import os
import re
import shutil
from subprocess import Popen, run, CalledProcessError
import sys
from typing import Callable, Dict, Generator, Iterator, List, Tuple, Union

from bs4 import BeautifulSoup
import markdown
from markdown.extensions.toc import slugify_unicode
from ruamel.yaml import YAML

NavItem = Union[str, List["NavItem"]]
NavDict = Dict[str, NavItem]
NavType = Union[List[NavDict], NavDict]


def create_title_page(soup, title, subtitle=None, version_majmin=""):
    """Create a title page with the specified metadata."""
    title_page = soup.new_tag("div", **{"class": "title-page"})

    # Create header container
    header_div = soup.new_tag("div", **{"class": "header-group"})

    # Add main title
    h1 = soup.new_tag("h1")
    h1.string = title
    header_div.append(h1)

    # Add subtitle if provided
    if subtitle:
        h2 = soup.new_tag("h2")
        h2.string = subtitle
        header_div.append(h2)

    title_page.append(header_div)

    # Add background image and stripes
    bg_image = soup.new_tag("div", **{"class": "title-background"})
    top_stripe = soup.new_tag("div", **{"class": "title-stripe-top"})
    bottom_stripe = soup.new_tag("div", **{"class": "title-stripe-bottom"})

    title_page.append(bg_image)
    title_page.append(top_stripe)
    title_page.append(bottom_stripe)

    # Add version info
    version_div = soup.new_tag("div", **{"class": "version"})
    version_span = soup.new_tag("span", **{"class": "version-number"})
    version_span.string = str(version_majmin or "")

    # Add "Version " text node followed by the span with the number
    version_div.append("Dyalog version ")
    version_div.append(version_span)

    title_page.append(version_div)

    # Create container for bottom image and tagline
    bottom_container = soup.new_tag("div", **{"class": "bottom-content"})

    # Add bottom DocDyalog image
    # doc_image = soup.new_tag('img', src="../assets/img/DocDyalog.png", **{'class': 'doc-dyalog'})
    # bottom_container.append(doc_image)

    doc_image = soup.new_tag(
        "img",
        src="../assets/img/dyalog-logo-2025_orange.svg",
        **{"class": "doc-dyalog"},
    )
    bottom_container.append(doc_image)

    # Add tagline
    # tagline = soup.new_tag('div', **{'class': 'tagline'})
    # tagline.string = "The tool of thought for software solutions"
    # bottom_container.append(tagline)

    title_page.append(bottom_container)

    return title_page


def format_copyright(name, version, revision):
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_dir, "assets", "templates", "copyright.md")

    # Read the template file
    try:
        with open(template_path, "r", encoding="utf-8") as file:
            template = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Copyright template not found at {template_path}")

    # Replace the placeholders
    content = template.replace("{NAME}", str(name))
    content = content.replace("{VERSION}", str(version))
    content = content.replace("{REVISION}", str(revision))

    # Convert markdown to HTML
    # Use extra=True to enable line breaks with <br>
    # Use extensions=['extra'] to enable additional markdown features
    html = markdown.markdown(content, extensions=["extra"])

    return html


def get_git_info(repo_path=None):
    """Get git info from environment variable or git commands."""
    # First try environment variable
    git_info = os.environ.get("GIT_INFO")
    if git_info:
        return git_info

    # Fall back to git commands
    try:
        # Get branch name
        branch = run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_path,
        )

        # Get commit hash
        hash_result = run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=repo_path,
        )

        return f"{branch.stdout.strip()}:{hash_result.stdout.strip()}"
    except (CalledProcessError, FileNotFoundError):
        return "unknown"


def get_build_date():
    """Get build date from environment variable or current time."""
    # First try environment variable
    build_date = os.environ.get("BUILD_DATE")
    if build_date:
        return build_date

    # Fall back to current date
    return datetime.now().strftime("%Y-%m-%d")


def shift_headings(soup: BeautifulSoup, n: int, article_id: str) -> None:
    # Find all heading tags
    headings = soup.find_all(re.compile("^h[1-6]$"))

    delta = 0  # The first heading is considered to be the "h1" -- the rest must be at least one deeper.

    # Modify each heading tag
    for tag in headings:
        current_level = int(tag.name[1])  # Extract the current heading level
        new_level = min(
            max(current_level + n + delta, 1), 6
        )  # Ensure new level is between 1 and 6
        tag.name = f"h{new_level}"
        if delta == 0:
            tag.attrs["id"] = f"{article_id}-header"
        delta = 1


def clean_img_src(soup: BeautifulSoup) -> None:
    """
    Find all image tags in the given HTML content and remove any leading dots and slashes
    """
    for img_tag in soup.find_all("img"):
        src = img_tag.get("src")
        if src:
            new_src = src.lstrip("./")
            img_tag["src"] = new_src


def remove_paths(data: Union[dict, list], paths: List[List[str]]) -> Union[dict, list]:
    if isinstance(data, dict):
        for key in list(
            data.keys()
        ):  # Clone to avoid problems with mutation during iteration
            # Check if this key matches any of the first keys in paths
            matching_paths = [path for path in paths if path and path[0] == key]
            if matching_paths:
                if len(matching_paths[0]) == 1:
                    del data[key]  # Full path matches; remove this key
                else:  # Recurse into the value
                    data[key] = remove_paths(
                        data[key], [path[1:] for path in matching_paths]
                    )
                    if not data[key]:  # If the value is now empty, remove the key
                        del data[key]
    elif isinstance(data, list):
        for item in data:
            remove_paths(item, paths)
        data = [
            item for item in data if item
        ]  # Remove any empty dictionaries from the list
    return data


def parse_mkdocs_yml(yml_file: str, remove: List[List[str]]) -> dict:
    """
    Read and parse the mkdocs.yml files, with options to exclude
    elements from the nav-section based on key paths.
    """
    yaml = YAML()
    with open(yml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    if "nav" in data and remove:
        data["nav"] = remove_paths(data["nav"], remove)

    return data


def extract_html_h1(data: str) -> str:
    """
    Some files will have a raw HTML <h1> for styling reasons.
    """
    soup = BeautifulSoup(data, "html.parser")
    if h1 := soup.find("h1"):
        if name_span := h1.find("span", class_="name"):
            name = name_span.get_text() if name_span else None
            if name:
                return name.strip().replace('"', "").replace("`", "")
        else:
            return h1.get_text().strip().replace('"', "").replace("`", "")
    return ""


def extract_h1(filename: str) -> str:
    """
    Find the H1, either markdown or HTML-style
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    if h1 := extract_html_h1(data):
        return h1

    if h1 := re.findall(r"^#\s+(.+)$", data):
        return h1[0]

    return ""


def find_source_files(
    prefix: str, nav: NavType, path: List[str] = None
) -> Generator[Tuple[List[str], str], None, None]:
    if path is None:
        path = []

    if isinstance(nav, dict):
        for key, value in nav.items():
            current_path = path + [key]
            if isinstance(value, str):
                yield current_path, value
            else:
                yield current_path, ""  # Represent the key-path to an empty string
                yield from find_source_files(prefix, value, current_path)
    elif isinstance(nav, list):
        for item in nav:
            yield from find_source_files(prefix, item, path)
    elif isinstance(nav, str):
        # No key. Pick the H1.
        key = extract_h1(os.path.join(prefix, "docs", nav))
        current_path = path + [key]
        yield current_path, nav


def expand_macros(data: str, macros: dict) -> str:
    """
    The mkdocs macro extension makes use of templates of the type {{ macro-id }} where
    the substitution value is stored in the "extra:" section in the mkdocs.yml file.
    """

    def replace(match):
        key = match.group(1).strip()
        value = macros.get(key)
        return str(value) if not isinstance(value, dict) else match.group(0)

    return re.sub(r"\{\{\s*(.*?)\s*}}", replace, data)


def slug(text: str) -> str:
    return re.sub(r"\W+", "-", text).lower()


def print_footnotes(soup: BeautifulSoup) -> None:
    """
    Convert to CSS-only footnotes style.
    """
    from bs4.element import NavigableString, Tag

    # First, convert bare URLs in footnote content to clickable links
    footnote_div = soup.find("div", class_="footnote")
    if footnote_div and isinstance(footnote_div, Tag):
        # Pattern to match URLs (http, https, ftp)
        url_pattern = re.compile(
            r'(https?://[^\s<>"{}|\\^`\[\]]+|ftp://[^\s<>"{}|\\^`\[\]]+)',
            re.IGNORECASE
        )

        # Find all <p> tags within footnotes
        for p_tag in footnote_div.find_all("p"):
            if not isinstance(p_tag, Tag):
                continue

            # Process text nodes to find bare URLs
            contents_to_process = list(p_tag.contents)
            for content in contents_to_process:
                # Only process NavigableString (text) nodes, not tags
                if isinstance(content, NavigableString) and not isinstance(content, type(soup)):
                    text = str(content)
                    # Check if this text contains a URL
                    if url_pattern.search(text):
                        # Split the text by URLs and create new elements
                        new_contents = []
                        last_end = 0

                        for match in url_pattern.finditer(text):
                            url = match.group(0)
                            start, end = match.span()

                            # Add text before the URL
                            if start > last_end:
                                new_contents.append(text[last_end:start])

                            # Create a link for the URL
                            a_tag = soup.new_tag("a", href=url)
                            a_tag.string = url
                            new_contents.append(a_tag)

                            last_end = end

                        # Add any remaining text after the last URL
                        if last_end < len(text):
                            new_contents.append(text[last_end:])

                        # Replace the original text node with the new contents
                        content.replace_with(*new_contents)

    # Now extract footnote definitions, preserving HTML content
    footnote_defs = {}

    # Find all footnote definitions
    for footnote in soup.select("div.footnote ol li"):
        footnote_id = footnote.get("id")
        if footnote_id and footnote_id.startswith("fn:"):
            # Extract the content from the footnote definition, preserving HTML
            p_tag = footnote.find("p")
            if p_tag:
                # Get all contents except the backref link
                footnote_contents = [
                    c for c in p_tag.contents
                    if not (hasattr(c, 'get') and c.name == "a" and "footnote-backref" in c.get("class", []))
                ]
                footnote_defs[footnote_id] = footnote_contents

    # Find all footnote references
    footnote_refs = soup.find_all("sup", id=lambda x: x and x.startswith("fnref:"))

    # Replace footnote references with inlined footnotes
    for ref in footnote_refs:
        a_tag = ref.find("a")
        if a_tag:
            footnote_id = a_tag.get("href", "").lstrip("#")
            if footnote_id in footnote_defs:
                new_span = soup.new_tag("span", **{"class": "footnote"})
                # Append the HTML contents instead of setting string
                for content in footnote_defs[footnote_id]:
                    # Clone the content to avoid moving it
                    if isinstance(content, NavigableString):
                        new_span.append(type(content)(content))
                    elif isinstance(content, Tag):
                        new_span.append(content.__copy__())
                    else:
                        new_span.append(str(content))
                ref.replace_with(new_span)

    # Remove the original footnote definitions section
    footnote_div = soup.find("div", class_="footnote")
    if footnote_div:
        footnote_div.decompose()


def add_caption(soup, table, caption_text, table_seq) -> None:
    caption = soup.new_tag("caption", style="caption-side:top")
    strong = soup.new_tag("strong")
    strong.string = f"Table {table_seq}:"
    caption.append(strong)
    caption.append(" ")
    caption.append(caption_text)
    table.insert(0, caption)


def caption_tables(soup: BeautifulSoup) -> Dict[str, int]:
    def is_chapter(tag):
        return tag.name == "section" and tag.has_attr("data-chapter-seq")

    tables = soup.find_all("table")

    custom_id_caption_re = re.compile(r"^\s*Table:\s*([^{]+)\s*\{:\s*#([^ }]+)\s*}\s*$")
    normal_caption_re = re.compile(r"^\s*Table:\s*(. *)\s*$")

    table_refs: Dict[str, int] = {}

    for section in soup.find_all(is_chapter):
        table_seq = 1
        for table in section.find_all("table"):
            prev = table.find_previous_sibling()
            if prev and prev.name == "p" and "Table:" in prev.text:
                table_id: str = None
                tref = f'{section["data-chapter-seq"]}-{table_seq}'
                if match := custom_id_caption_re.match(prev.text):
                    caption_text = match.group(1).strip()
                    table_id = match.group(2).strip()
                    add_caption(soup, table, caption_text, tref)
                elif match := normal_caption_re.match(prev.text):
                    caption_text = match.group(1).strip()
                    table_id = f"_table-{tref}"
                    add_caption(soup, table, caption_text, tref)
                else:
                    continue

                if table_id in table_refs:
                    print(f"WARNING: recurring table id: {table_id}")

                table_refs[table_id] = tref
                prev.decompose()
                table_seq += 1
                table["id"] = table_id

    return table_refs


def convert_examples(soup: BeautifulSoup) -> None:
    headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"], class_="example")
    for header in headers:
        p_tag = soup.new_tag("p", **{"class": "example"})
        # Preserve the ID if it exists
        if "id" in header.attrs:
            p_tag["id"] = header["id"]
        p_tag.string = header.string
        header.replace_with(p_tag)


def update_seq_stack(seq_stack, s):
    for i in range(s + 1, len(seq_stack)):
        seq_stack[i] = 0
    seq_stack[s] += 1


def convert_to_html(
    filenames: Iterator[str],
    prefix: str,
    title: str,
    macros: dict,
    transforms: List[Callable[[str], str]],
    create_toc: bool = True,
    enumerate_sections: bool = True,
    syntax_hilite: bool = True,
    git_info="",
    build_date="",
) -> Tuple[Dict[str, str], str, Dict[str, str]]:
    """
    Markdown to HTML, using the same markdown extensions as our mkdocs site. Concatenate all converted files
    into a single HTML file, wrapping into <section>s of <article>s.
    """

    def process_markdown(file_path, article_id, remove_first_heading=False):
        """
        Convert Markdown to HTML, using the same extensions as used by our mkdocs setup.
        """
        extensions = [
            "admonition",  # https://python-markdown.github.io/extensions/admonition/
            "attr_list",  # https://python-markdown.github.io/extensions/attr_list/
            "footnotes",  # https://python-markdown.github.io/extensions/footnotes/
            "md_in_html",  # https://python-markdown.github.io/extensions/md_in_html/
            "markdown_tables_extended",  # https://github.com/fumbles/tables_extended
            "pymdownx.details",  # https://facelessuser.github.io/pymdown-extensions/extensions/details/
            "toc",  # https://python-markdown.github.io/extensions/toc/
        ]
        if syntax_hilite:
            extensions.append("pymdownx.superfences")
        else:
            extensions.append("fenced_code")

        def custom_slugify(value, separator):
            return article_id + "-" + slugify_unicode(value, separator)

        extension_configs = {"toc": {"slugify": custom_slugify}}

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()

        # Apply macros and any pre-html transforms
        md = expand_macros(md, macros)
        for fun in transforms:
            md = fun(md)

        # Convert to HTML
        body = markdown.markdown(
            md, extensions=extensions, extension_configs=extension_configs
        )
        soup = BeautifulSoup(body, "html.parser")

        # Optionally remove the first h1 heading
        if remove_first_heading:
            if h1 := soup.find("h1"):
                h1.decompose()

        # Apply standard processing
        print_footnotes(soup)
        clean_img_src(soup)
        convert_examples(soup)

        return str(soup).replace("``", "")

    # Initialise TOC and articles content
    toc = """
<article id="contents">
    <h2 class="contents">Contents</h2>
    <ul>
"""
    articles = ""
    section_stack = []
    chapter_number = 0
    front_matter = ' class="front-matter"'
    section_map = {}
    seq_stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    path_to_id = {}  # New mapping from file paths to article IDs

    # Process all files
    for keypath, file in filenames:
        # Close any sections that need to be closed
        while section_stack and len(section_stack[-1]) >= len(keypath):
            section_stack.pop()
            toc += "</ul></li>\n"
            articles += "</section>\n"

        # Case 1: Directory/Section entry
        if file == "":
            section_stack.append(keypath)
            heading_level = len(section_stack)
            heading_text = keypath[-1]
            section_id = "-".join(slug(part) for part in keypath)

            # Update section numbering
            update_seq_stack(seq_stack, len(section_stack) - 1)
            section_map[section_id] = ".".join(str(c) for c in seq_stack if c > 0)

            # Top-level section = chapter
            if heading_level == 1:
                chapter_number += 1
                front_matter = ""
                articles += f'<section id="{section_id}" data-chapter-seq="{chapter_number}">\n<h1 id="{section_id}-header" class="chapter">{heading_text}</h1>\n'
                toc += f'<li class="toc-chapter"><a href="#{section_id}-header" class="toc"></a><ul class="first-level">\n'
            else:
                articles += f'<section id="{section_id}">\n<h{heading_level} id="{section_id}-header">{heading_text}</h{heading_level}>\n'
                toc += f'<li{front_matter}><a href="#{section_id}-header" class="toc"></a><ul>\n'
            continue

        # Case 2: Top-level file (treat as chapter)
        is_top_level = len(keypath) == 1 and not section_stack

        if is_top_level:
            chapter_number += 1
            front_matter = ""
            heading_text = keypath[0]

            # Create section for this chapter
            section_id = slug(heading_text)
            heading_id = f"{section_id}-header"
            articles += (
                f'<section id="{section_id}" data-chapter-seq="{chapter_number}">\n'
            )
            articles += f'<h1 id="{heading_id}" class="chapter">{heading_text}</h1>\n'

            # Add to TOC
            toc += f'<li class="toc-chapter"><a href="#{heading_id}" class="toc"></a><ul class="first-level">\n'

            # Update section stack and numbering
            section_stack.append(keypath)
            update_seq_stack(seq_stack, 0)
            section_map[section_id] = str(chapter_number)
        elif front_matter == "":
            update_seq_stack(seq_stack, len(section_stack))

        # Create article
        article_id = file.replace("/", "-").replace(".md", "")
        tie_breaker = 0
        test_id = article_id
        while test_id in section_map:
            tie_breaker += 1
            test_id = article_id + f"-{tie_breaker}"
        article_id = test_id

        # Update mappings
        section_map[article_id] = ".".join(str(c) for c in seq_stack if c > 0)
        path_to_id[file] = article_id  # Map file path to article ID

        # Add to TOC (except for top-level file articles since they're already in TOC)
        if not is_top_level:
            # Use the YAML key text if available, otherwise empty
            toc_text = keypath[-1] if keypath else ""
            toc += f'<li{front_matter}><a href="#{article_id}-header" class="toc">{toc_text}</a></li>\n'

        # Process and add article content
        articles += f'<article id="{article_id}">\n'
        html_content = process_markdown(
            os.path.join(prefix, file),
            article_id,  # Pass article_id to process_markdown
            remove_first_heading=is_top_level,
        )

        # For non-top-level files, handle headings
        if not is_top_level:
            soup = BeautifulSoup(html_content, "html.parser")
            shift_headings(soup, len(section_stack), article_id)
            html_content = str(soup)

        articles += html_content
        articles += "\n</article>\n"

        # For top-level files, we're done with this file
        if is_top_level:
            continue

    # Close any remaining open sections
    while section_stack:
        section_stack.pop()
        toc += "</ul></li>\n"
        articles += "</section>\n"

    # Finish TOC
    toc += """
    </ul>
</article>
"""

    # Assemble final HTML
    result = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/styles/pdf.css">
    <link rel="stylesheet" href="assets/styles/admonitions.css">
    <link rel="stylesheet" href="assets/styles/codeblocks.css">
    {'<link rel="stylesheet" href="assets/styles/toc.css">' if create_toc else ''}
    {'<link rel="stylesheet" href="assets/styles/sections.css">' if enumerate_sections else ''}
    <title>{title}</title>
</head>
<body>
    <div id="title">{title}</div>
    <div style="string-set: build-info '{build_date} ({git_info})'"></div>
    {'<section>' + toc + '</section>' if create_toc else ''}
    {articles}
</body>
</html>
"""
    return section_map, result, path_to_id  # Return path_to_id


def copy_directory(src, dst):
    """
    Copy a directory and all its content from src to dst.
    """
    if not os.path.exists(src):
        raise ValueError(f"Source directory '{src}' does not exist")

    if os.path.exists(dst):
        raise ValueError(f"Destination directory '{dst}' already exists")

    shutil.copytree(src, dst)


def static_assets(src_dir="assets", project="project") -> None:
    """
    Copy the entire 'assets' directory into the project directory
    """
    dest_dir = os.path.join(project, "assets")

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    shutil.copytree(src_dir, dest_dir)


def fix_links(b: str) -> str:
    """
    Links in the mkdocs source are "clean URLs" -- the renderer will remove the .md extensions
    on link targets. We have to do that transformation ourselves -- or rather, change to .htm.

    Three cases:

    1. Intra-doc links present with link targets ending in ".md" -- they go to other pages
    defined within the same mkdocs.yml sub-site. Fix those by changing suffix to ".htm".

    2. Inter-doc links have a target presenting with (potentially several) leading "../" and no
    extension. The first actual component (not "../") of the path will be the name of one of the other
    sub-sites. Make the link absolute, and add the ".htm" extension.

    3. Off-site links start with "http" -- return those unchanged.
    """

    def link_transform(match: re.Match) -> str:
        link_text = match.group(1)
        link_target = match.group(2)

        # Links referencing tables are empty, and expected to be
        # filled out by the captioning plugin. We have to do this
        # as a post-conversion step. Peel off any page reference
        # prior to the id. We're now dealing with a single page.
        # Let's hope table ids are unique.
        if link_text == "":
            return f"[TABLE-REFERENCE]({re.sub(r'^[^#]+', '', link_target)})"

        if link_target.startswith("http"):  # Off-site link: return unchanged
            return f"[{link_text}]({link_target})"

        # If the link contains an internal anchor (#), return unchanged
        if "#" in link_target:
            return f"[{link_text}]({link_target})"

        path, name = os.path.split(link_target)
        base, ext = os.path.splitext(name)
        htm_target = f"{os.path.join(path, base)}.htm"

        if ext == ".md":  # Intra-doc link: change extension to ".htm"
            return f"[{link_text}]({htm_target})"

        if ext == "":  # Inter-doc link: make absolute, change extension
            # Replace any number of leading ../ with a single /
            no_slashdot = re.sub(r"^[/.]+", "/", htm_target)
            return f"[{link_text}]({no_slashdot})"

        # Something else; leave alone
        return f"[{link_text}]({link_target})"

    # Exclude markdown images (which start with !)
    return re.sub(r"(?<!!)\[([^]]*)]\(([^)]+)\)", link_transform, b)


def normalise_links(
    soup: BeautifulSoup,
    documents: Dict[str, str],
    table_refs: Dict[str, int],
    section_map: Dict[str, str],
    path_to_id: Dict[str, str],
    rewrite_links: bool = True,
) -> None:
    """
    Rewrite internal links to point to correct article IDs within the single HTML file using file path resolution.
    Optionally rewrite link text to section numbers for print-friendliness.
    """

    def in_table(tag):
        # Check if a tag is nested inside a table
        while tag:
            if tag.name == "table":
                return True
            tag = tag.parent
        return False

    def extract_components(href):
        # Remove leading ../ and .htm or .html extension. Split on '/'
        href = re.sub(r"^[/.]+", "", href)
        href = re.sub(r"\.html?$", "", href)
        return [comp for comp in href.split("/") if comp]

    def unslug(text):
        # Convert slug to readable text
        return text.replace("-", " ").title()

    # Create inverse mapping from article IDs to file paths
    id_to_path = {v: k for k, v in path_to_id.items()}

    # Find all articles and their IDs, excluding copyright page
    articles = soup.find_all("article")
    article_ids = {
        article["id"]
        for article in articles
        if not article.get("class") or "copyright-page" not in article.get("class")
    }

    # Process all <a> tags
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if "noprint" in a_tag.get("class", []):
            a_tag.decompose()
            continue

        a_text = a_tag.get_text()
        if a_text == "TABLE-REFERENCE":
            if table_id := table_refs.get(href[1:]):
                a_tag.string = f"Table {table_id}"
                if "class" in a_tag.attrs:
                    a_tag["class"].append("internal-link")
                else:
                    a_tag["class"] = ["internal-link"]
            else:
                print(f'--> Warning: could not find a matching table for id "{href}"')
            continue

        if not href.startswith("http"):
            # Split off anchor if present
            path_parts = href.split("#", maxsplit=1)
            path = path_parts[0]
            anchor = path_parts[1] if len(path_parts) > 1 else None

            if not path:
                # This is an anchor-only link within the same document
                # But skip TOC links which are handled elsewhere
                if anchor and "toc" not in a_tag.get("class", []):
                    parent_article = a_tag.find_parent("article")
                    if parent_article and "id" in parent_article.attrs:
                        article_id = parent_article["id"]
                        new_href = f"#{article_id}-{anchor}"
                        a_tag["href"] = new_href
                continue

            if path.startswith("/"):
                # Handle potential inter-document links
                components = extract_components(path)
                # Handle renamed documents
                if components and components[0] == "net-framework-interface-guide":
                    components[0] = "dotnet-framework-interface"
                if components and components[0] in documents:
                    new_tag = soup.new_tag("i")
                    text_parts = [documents[components[0]]]
                    if len(components) > 1:
                        text_parts.append(unslug(components[-1]))
                    new_tag.string = ": ".join(text_parts)
                    a_tag.replace_with(new_tag)
                else:
                    # For unresolvable absolute links, replace with italics
                    new_tag = soup.new_tag("i")
                    new_tag.string = a_text
                    a_tag.replace_with(new_tag)
                    print(f"--> Warning: can't resolve absolute link '{href}'")
            else:
                # Internal link: resolve using source file path
                parent_article = a_tag.find_parent("article")
                if parent_article and "id" in parent_article.attrs:
                    source_id = parent_article["id"]
                    if source_id in id_to_path:
                        source_path = id_to_path[source_id]
                        source_dir = os.path.dirname(source_path)
                        target_rel_path = (
                            os.path.normpath(os.path.join(source_dir, path))
                            .replace(".htm", ".md")
                            .replace(".html", ".md")
                        )
                        if target_rel_path in path_to_id:
                            target_id = path_to_id[target_rel_path]
                            if anchor:
                                new_href = f"#{target_id}-{anchor}"
                            else:
                                new_href = f"#{target_id}-header"
                            a_tag["href"] = new_href
                            if rewrite_links:
                                if "class" in a_tag.attrs:
                                    a_tag["class"].append("internal-link")
                                else:
                                    a_tag["class"] = ["internal-link"]
                                if not in_table(a_tag):
                                    if reference := section_map.get(target_id):
                                        if "." in reference:
                                            a_tag.string = f"Section {reference}"
                                        else:
                                            a_tag.string = f"Chapter {reference}"
                        else:
                            # Replace unresolvable link with italics
                            new_tag = soup.new_tag("i")
                            new_tag.string = a_text
                            a_tag.replace_with(new_tag)
                            print(
                                f'--> Warning: target path "{target_rel_path}" not found'
                            )
                    else:
                        # Replace link with italics if source ID not found
                        new_tag = soup.new_tag("i")
                        new_tag.string = a_text
                        a_tag.replace_with(new_tag)
                        print(f'--> Warning: source article ID "{source_id}" not found')
                else:
                    # Replace link with italics if no parent article found
                    new_tag = soup.new_tag("i")
                    new_tag.string = a_text
                    a_tag.replace_with(new_tag)
                    print(f'--> Warning: no parent article found for link "{href}"')


def toc_friendly_headings(soup: BeautifulSoup) -> None:
    # Find all headings with class "heading"
    for heading in soup.find_all(class_="heading"):
        # Ensure it has the specific structure we're looking for
        name_span = heading.find("span", class_="name")
        command_span = heading.find("span", class_="command")

        if name_span and command_span:
            # Create the new structure
            heading_container = soup.new_tag("div", **{"class": "heading-container"})
            new_heading = soup.new_tag(heading.name, **heading.attrs)
            new_heading.string = name_span.text
            command_div = soup.new_tag("div", **{"class": "command"})
            command_div.string = command_span.text

            # Assemble the new structure
            heading_container.append(new_heading)
            heading_container.append(command_div)

            # Replace the old heading with the new structure
            heading.replace_with(heading_container)


def toplevel_docs(nav: List[Dict[str, str]]) -> Dict[str, str]:
    result = {}
    
    def process_nav_value(doc_name, value):
        """Process a nav value which could be a string or a list (section group)."""
        if isinstance(value, str):
            if "!include" in value:
                # This is a directory include
                path = value.split(' ')[1]
                first_component = path.split('/')[1]
                result[first_component] = doc_name
            else:
                # This is a direct file reference
                path_parts = value.split('/')
                # Use the filename without extension as the key
                if len(path_parts) > 0:
                    filename = path_parts[-1]
                    file_base = os.path.splitext(filename)[0]
                    result[file_base] = doc_name
        elif isinstance(value, list):
            # This is a section group - process each item in the group
            for item in value:
                if isinstance(item, dict):
                    for sub_name, sub_value in item.items():
                        process_nav_value(sub_name, sub_value)
    
    for entry in nav:
        for doc_name, value in entry.items():
            process_nav_value(doc_name, value)
    
    return result


def process_document(document_path):
    """Process a single document directory."""
    if document_path.endswith("/"):
        document_path = document_path[:-1]

    # Get document metadata if using config file
    doc_metadata = None
    if args.config:
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)
            if isinstance(config.get("documents"), dict):
                doc_metadata = config["documents"].get(document_path)

    # If there is a print-specific yml file, use that. Otherwise, use the normal mkdocs.yml file.
    doc_mkdocs_file = str(
        os.path.join(
            os.path.abspath(os.path.dirname(args.mkdocs_yml)),
            document_path,
            "print_mkdocs.yml",
        )
    )
    if not os.path.isfile(doc_mkdocs_file):
        doc_mkdocs_file = str(
            os.path.join(
                os.path.abspath(os.path.dirname(args.mkdocs_yml)),
                document_path,
                "mkdocs.yml",
            )
        )
        if not os.path.isfile(doc_mkdocs_file):
            sys.exit(f'--> document mkdocs.yml file "{doc_mkdocs_file}" not found.')

    # Parse the mkdocs.yml file of our actual document
    yml_data = parse_mkdocs_yml(doc_mkdocs_file, remove=excludes)

    # Find all source Markdown files in depth-first traversal order
    md_files = find_source_files(os.path.dirname(doc_mkdocs_file), yml_data["nav"])

    # Copy img dir for this document
    img_src_dir = str(os.path.join(os.path.dirname(doc_mkdocs_file), "docs", "img"))
    img_dest_dir = str(os.path.join(args.project_dir, "img"))
    
    if os.path.exists(img_src_dir):
        if os.path.exists(img_dest_dir):
            shutil.rmtree(img_dest_dir)
        copy_directory(img_src_dir, img_dest_dir)

    # Convert each Markdown file to HTML, and concatenate to a single string
    source = f"{args.project_dir}/{document_path}.htm"
    section_map, html_content, path_to_id = convert_to_html(  # Receive path_to_id
        md_files,
        prefix=os.path.join(os.path.dirname(doc_mkdocs_file), "docs"),
        title=yml_data["site_name"],
        macros=top_mkdocs_data.get("extra", {}),
        transforms=[fix_links],
        create_toc=args.toc,
        enumerate_sections=args.enumerate_sections,
        syntax_hilite=args.syntax_hilite,
        git_info=git_info,
        build_date=build_date,
    )

    # Global transforms on the unified HTML-file.
    soup = BeautifulSoup(html_content, "html.parser")

    # Add the title page if metadata is available
    if doc_metadata:
        version_majmin = top_mkdocs_data["extra"].get("version_majmin", "")
        title_page = create_title_page(
            soup,
            doc_metadata.get("title"),
            doc_metadata.get("subtitle"),
            version_majmin,
        )

        # Insert title page at the start of the body
        soup.body.insert(0, title_page)

        # Add copyright page
        copyright_html = format_copyright(
            f"{doc_metadata.get('title')} {doc_metadata.get('subtitle', '')}",
            top_mkdocs_data["extra"].get("version_majmin", ""),
            f"{build_date} {git_info}",
        )
        copyright_soup = BeautifulSoup(copyright_html, "html.parser")

        # Create a section for the copyright page
        copyright_section = soup.new_tag("section", **{"class": "copyright-section"})
        copyright_article = soup.new_tag("article", **{"class": "copyright-page"})
        copyright_article.append(copyright_soup)
        copyright_section.append(copyright_article)

        # Insert copyright section after the title page
        title_page.insert_after(copyright_section)

    table_refs = caption_tables(soup)
    normalise_links(
        soup,
        documents,
        table_refs,
        section_map,
        path_to_id,
        rewrite_links=args.link_rewrite,
    )  # Pass path_to_id
    toc_friendly_headings(soup)

    # Insert link to title page CSS
    css_link = soup.new_tag(
        "link", rel="stylesheet", href="assets/styles/title-page.css"
    )
    soup.head.append(css_link)

    html_content = str(soup)

    with open(source, "w", encoding="utf-8") as f:
        f.write(html_content)

    if not args.html_only:
        output_filename = (
            doc_metadata.get("filename", f"{document_path}.pdf")
            if doc_metadata
            else f"{document_path}.pdf"
        )

        cmd = ["weasyprint", f"{document_path}.htm", output_filename]
        if not args.verbose:
            cmd.append("--quiet")

        output = Popen(cmd, cwd=args.project_dir)
        output.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF-files from mkdocs sites")
    parser.add_argument(
        "--mkdocs-yml",
        type=str,
        default="../mkdocs.yml",
        help="Path to the toplevel mkdocs.yml file",
    )
    parser.add_argument(
        "--document",
        type=str,
        help="Name of dir containing /docs to be converted to PDF",
    )
    parser.add_argument(
        "--config", type=str, help="JSON config file specifying documents and settings"
    )
    parser.add_argument(
        "--project-dir",
        type=str,
        default="project",
        help="Name of output directory",
    )
    parser.add_argument(
        "--assets-dir",
        type=str,
        default="assets",
        help="Name of assets directory",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument(
        "--exclude", type=str, help="Name of json file with ToC exclusions"
    )
    parser.add_argument(
        "--disable-toc",
        action="store_false",
        dest="toc",
        help="Disable print-style table of contents listing",
    )
    parser.add_argument(
        "--disable-link-rewriting",
        action="store_false",
        dest="link_rewrite",
        help="Disable print-style section numbering of links",
    )
    parser.add_argument(
        "--disable-syntax-highlighting",
        action="store_false",
        dest="syntax_hilite",
        help="Disable syntax highlighting",
    )
    parser.add_argument(
        "--disable-section-numbers",
        action="store_false",
        dest="enumerate_sections",
        help="Disable print-style section numbers",
    )
    parser.add_argument(
        "--screen",
        action="store_true",
        help="Make screen-oriented PDF (no ToC, no section numbers)",
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Generate unified HTML-file, but not PDF-conversion",
    )

    args = parser.parse_args()

    # Validate that either --document or --config is provided, but not both
    if bool(args.document) == bool(args.config):
        sys.exit("Error: Exactly one of --document or --config must be specified")

    if args.screen:
        args.toc = False
        args.link_rewrite = False
        args.enumerate_sections = False
        args.syntax_hilite = True

    if not args.enumerate_sections:
        args.link_rewrite = False

    if not args.mkdocs_yml.endswith("mkdocs.yml"):
        sys.exit('--> expected a "mkdocs.yml" file')

    if not os.path.isfile(args.mkdocs_yml):
        sys.exit(f'--> toplevel mkdocs.yml file "{args.mkdocs_yml}" not found.')

    if not os.path.exists(args.assets_dir):
        sys.exit(f'--> assets directory "{args.assets_dir}" not found.')

    # Load config file if provided
    config = {}
    if args.config:
        try:
            with open(args.config, "r", encoding="utf-8") as f:
                config = json.load(f)
        except json.JSONDecodeError:
            sys.exit(f'--> config file "{args.config}" is not valid JSON')
        except FileNotFoundError:
            sys.exit(f'--> config file "{args.config}" not found')

        # Override CLI arguments with config settings if present
        if "settings" in config:
            args.toc = not config["settings"].get("disable_toc", not args.toc)
            args.link_rewrite = not config["settings"].get(
                "disable_link_rewriting", not args.link_rewrite
            )
            args.syntax_hilite = not config["settings"].get(
                "disable_syntax_highlighting", not args.syntax_hilite
            )
            args.enumerate_sections = not config["settings"].get(
                "disable_section_numbers", not args.enumerate_sections
            )
            args.screen = config["settings"].get("screen", args.screen)
            args.html_only = config["settings"].get("html_only", args.html_only)

    git_info = get_git_info(os.path.dirname(args.mkdocs_yml))
    build_date = get_build_date()

    # Parse the top-level config
    top_mkdocs_data = parse_mkdocs_yml(args.mkdocs_yml, remove=args.exclude)

    version = top_mkdocs_data["extra"].get("version_majmin")
    if not version:
        sys.exit(f"--> source {args.mkdocs_yml} has no Dyalog version set")

    documents = toplevel_docs(top_mkdocs_data.get("nav", {}))

    excludes = []
    if args.exclude:
        with open(args.exclude, "r", encoding="utf-8") as file:
            excludes = json.load(file)

    # Prepare static assets (done once for all documents)
    os.makedirs(args.project_dir, exist_ok=True)
    static_assets(args.assets_dir, args.project_dir)

    # Process documents
    if args.config:
        if not isinstance(config.get("documents"), dict):
            sys.exit('--> config file must contain a "documents" dictionary')
        for doc in config["documents"]:
            print(f"=== building: {doc} ===")
            process_document(doc)
    else:
        process_document(args.document)
