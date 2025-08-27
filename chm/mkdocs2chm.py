"""
mkdocs2chm.py

Convert a mkdocs site to a Windows CHM help file bundle.

Stefan Kruger <stefan@dyalog.com>

python mkdocs2chm.py \
    --mkdocs-yml ../mkdocs.yml \
    --project-dir project \
    --assets-dir assets \
    --config config.json

with a config.json:

{
    "exclude": [
        "UNIX Installation",
        "UNIX User Guide"
    ]
}

will read the top-level "mkdocs.yml" file and make a CHM file

    dyalog.chm

in the ./project/ directory.

Notes:

You need the tool "chmcmd" installed, which is part of Free Pascal. See

    https://wiki.freepascal.org/htmlhelp_compiler

You also need 'pygments' to highlight code.

If a directory 'assets' is found, any .css and .ttf files discovered will be included.
"""

import argparse
from dataclasses import dataclass, field
import itertools
import json
import logging
import os
from csscompressor import compress as css_compress
import cssutils
from htmlmin import minify as html_minify
import re
import shutil
from subprocess import Popen
import sys
from typing import Callable, IO, List, Tuple
import warnings
from xml.dom.minidom import getDOMImplementation

from caption import TableCaptionExtension
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
import markdown
from ruamel.yaml import YAML

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

cssutils.log.setLevel(logging.CRITICAL)


HEADER = """
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
<head>
<meta name="GENERATOR" content="Microsoft&reg; HTML Help Workshop 4.1">
</head><body>
<object type="text/site properties">
    <param name="SiteType" value="toc">
    <param name="Window Styles" value="0x800401">
    <param name="ExWindow Styles" value="0x200">
</object>
"""

DIR_ENTRY = """<li><object type="text/sitemap">
        <param name="Name" value="{name}">
    </object>
"""

FILE_ENTRY = """<li><object type="text/sitemap">
        <param name="Name" value="{name}">
        <param name="Local" value="{file}">
    </object>
"""


@dataclass
class Node:
    name: str = ""
    value: str | List[str] = None
    depth: int = 0
    parent: "Node" = None
    children: List["Node"] = field(default_factory=list)
    html_name: str = field(default=None, init=False)

    def __post_init__(self):
        if isinstance(self.value, str) and self.value.endswith(".md"):
            self.html_name = self.value.replace(".md", ".htm")

    def isdir(self):
        return len(self.children) > 0


def _process_nav_item(item: dict | str, parent: Node, project="project") -> None:
    """
    Process a single nav item -- either a dict, which has either a string
    value (leaf node), or a list value -- of other nav items, or a string
    referencing a file, from which the name needs to be picked up from the
    H1 later.
    """
    if isinstance(item, dict):
        ((key, value),) = item.items()
        # Navigation titles are already cleaned in parse_mkdocs_yml
    else:  # No name in the yml -- name should be picked up from the H1 in the file
        key = ""
        value = item  # item is the filename -- swap to .htm to parse
        if item.endswith(".md"):
            html_file = os.path.join(project, item.replace(".md", ".htm"))
            # Check if the HTML file exists (it might have been excluded)
            if os.path.exists(html_file):
                with open(html_file, "r", encoding="utf-8") as f:
                    data = f.read()
                if h1 := extract_h1(data):
                    key = h1
            else:
                # File was excluded, skip this nav item
                return

            # Special case for welcome.md - override the H1 title
            if item == "welcome.md":
                key = "Welcome"

    node = Node(key, value, parent.depth + 1, parent)
    parent.children.append(node)

    if isinstance(value, list):
        for sub_item in value:
            _process_nav_item(sub_item, node, project)


def _traverse(node: Node, toc: IO[str]) -> None:
    # Just clean up quotes and backticks (HTML tags and quad already removed during parsing)
    title = node.name.replace("`", "").replace('"', "")
    
    # Check if this directory has an "Introduction" child that should be used as its link
    intro_file = None
    if node.children:
        for child in node.children:
            if child.name == "Introduction" and not child.isdir() and child.html_name:
                intro_file = child.html_name
                break
    
    # Write the entry with or without a Local parameter
    if intro_file:
        toc.write(FILE_ENTRY.format(name=title, file=intro_file))
    else:
        toc.write(DIR_ENTRY.format(name=title))
    
    if node.children:  # Only write <ul> if there are children
        toc.write("<ul>\n")
        for child in node.children:
            if child.isdir():
                _traverse(child, toc)
            else:
                # Just clean up quotes and backticks
                child_name = child.name.replace("`", "").replace('"', "")
                toc.write(
                    FILE_ENTRY.format(
                        name=child_name,
                        file=child.html_name,
                    )
                )
        toc.write("</ul>\n")


def modify_paths(navdata, base_path: str):
    """
    In the monorepo, included documents must have the
    top-level prepended (here known as the `base_path`)
    """
    if isinstance(navdata, dict):
        for key, value in navdata.items():
            if isinstance(value, (dict, list)):
                navdata[key] = modify_paths(value, base_path)
            elif isinstance(value, str) and value.endswith(".md"):
                navdata[key] = os.path.join(base_path, value)
    elif isinstance(navdata, list):
        navdata = [modify_paths(item, base_path) for item in navdata]
    elif isinstance(navdata, str):
        navdata = os.path.join(base_path, navdata)
    return navdata


def clean_nav_titles(navdata):
    """
    Clean navigation titles by removing HTML tags and the quad symbol.
    This ensures CHM compatibility by removing UTF-8 characters that don't display properly.
    """
    if isinstance(navdata, dict):
        cleaned = {}
        for key, value in navdata.items():
            # Clean the key if it's a navigation title
            if isinstance(value, (str, list, dict)) and not key.startswith('!'):
                # Remove HTML tags and quad symbol from navigation titles
                cleaned_key = re.sub(r'<[^>]+>', '', key).replace('⎕', '')
            else:
                cleaned_key = key
            # Recursively clean the value
            cleaned[cleaned_key] = clean_nav_titles(value)
        return cleaned
    elif isinstance(navdata, list):
        return [clean_nav_titles(item) for item in navdata]
    else:
        return navdata


def parse_mkdocs_yml(yml_file: str, remove: List[str]) -> dict:
    """
    Read and parse the mkdocs.yml files. The monorepo plugin references
    the sub-document mkdocs.yml files, which we expand in place to produce
    the complete state.
    """

    yaml = YAML()
    with open(yml_file, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    if remove:
        data["nav"] = [
            item for item in data["nav"] if not any(key in item for key in remove)
        ]

    def resolve_includes(data: dict, base_path: str) -> dict:
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = resolve_includes(value, base_path)
        elif isinstance(data, list):
            for i in range(len(data)):
                data[i] = resolve_includes(data[i], base_path)
        elif isinstance(data, str) and data.startswith("!include"):
            include_path = data.split(" ")[1]
            full_path = os.path.normpath(os.path.join(base_path, include_path))
            navdata = parse_mkdocs_yml(full_path, remove=[])["nav"]
            subdir = os.path.basename(os.path.dirname(include_path))
            return modify_paths(navdata, subdir)
        return data

    base_path = os.path.dirname(yml_file)
    data = resolve_includes(data, base_path)
    
    # Clean navigation titles after parsing
    if "nav" in data:
        data["nav"] = clean_nav_titles(data["nav"])
    
    return data


def generate_toc(yml_data: dict, project="project"):
    """
    Given the parsed and expanded mkdocs.yml -- specifically its "nav"
    section -- write out the corresponding CHM TOC XML with top-level items
    directly under the root <ul>.
    """
    root = Node()
    nav = yml_data.get("nav", [])
    for item in nav:
        _process_nav_item(item, root, project)

    # Post-process to add language reference disambiguation pages
    add_langref_disambiguation_pages(root, project)

    toc = open(os.path.join(project, "_table_of_contents.hhc"), "w", encoding="utf-8")
    toc.write(HEADER)
    toc.write("<ul>\n")

    # Write top-level children directly, skipping the empty root
    for child in root.children:
        if child.isdir():
            _traverse(child, toc)
        else:
            # Just clean up quotes and backticks (HTML tags and quad already removed during parsing)
            child_name = child.name.replace("`", "").replace('"', "")
            toc.write(
                FILE_ENTRY.format(
                    name=child_name,
                    file=child.html_name,
                )
            )

    toc.write("</ul>\n")
    toc.write("</body></html>\n")
    toc.close()


def find_source_files(topdir: str, subdirs: List[str]) -> Tuple[List[str], List[str]]:
    """
    Under `topdir`, recursively scan the subdirs defined by `subdirs`,
    and return full paths to all Markdown and image files.
    """
    markdown_files = []
    image_files = []
    excluded_print_files = []

    for subdir in subdirs:
        incldir = os.path.join(topdir, re.sub(r"^[./]+", "", os.path.dirname(subdir)))
        if not os.path.isdir(incldir):
            raise NotADirectoryError(f"Not a directory: {incldir}")
        for root, _, files in os.walk(incldir):
            for file in files:
                full_path = os.path.abspath(os.path.join(root, file))
                # If the markdown source has been used to build a site already, we need to
                # ensure we skip the target files
                if "/site/" in full_path:
                    continue
                extension = os.path.splitext(full_path)[-1]
                if extension == ".md":
                    # Skip -print.md files completely
                    if file.endswith("-print.md"):
                        excluded_print_files.append(full_path)
                    else:
                        markdown_files.append(full_path)
                elif extension in {".png", ".gif", ".jpg", ".bmp", ".jpeg"}:
                    image_files.append(full_path)

    if excluded_print_files:
        print(f"\nExcluded {len(excluded_print_files)} -print.md files from all processing:")
        for f in sorted(excluded_print_files):
            print(f"  - {os.path.basename(f)}")

    return markdown_files, image_files


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


def purge_css(css: str, html_content: str) -> str:
    """
    Simple CSS purger that removes unused selectors.
    Uses cssutils for parsing CSS and BeautifulSoup for HTML.
    Preserves selectors for important HTML structure elements.
    """
    # Parse the HTML to find all class names and IDs
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all class names in use
    classes_in_use = set()
    for tag in soup.find_all(class_=True):
        classes_in_use.update(tag.get("class"))

    # Find all IDs in use
    ids_in_use = {tag.get("id") for tag in soup.find_all(id=True)}

    # Find all tag names in use
    tags_in_use = {tag.name for tag in soup.find_all()}

    # Add essential HTML structure elements that might not appear in the parsed HTML
    # but are still needed for proper styling
    essential_tags = {
        "html",
        "head",
        "body",
        "main",
        "article",
        "section",
        "header",
        "footer",
    }
    tags_in_use.update(essential_tags)

    # Parse the CSS
    stylesheet = cssutils.parseString(css)

    # Track which rules to keep
    rules_to_keep = []

    # Process each rule
    for rule in stylesheet:
        if rule.type == rule.STYLE_RULE:
            selectors = rule.selectorText.split(",")
            matched_selectors = []

            for selector in selectors:
                selector = selector.strip()
                should_keep = False

                # Always keep essential structure selectors and their variants
                for tag in essential_tags:
                    if re.search(r"\b" + re.escape(tag) + r"\b", selector):
                        should_keep = True
                        break

                if not should_keep:
                    # Simple tag selectors like "div" or "p"
                    if selector in tags_in_use:
                        should_keep = True
                    # Class selectors like ".my-class"
                    elif selector.startswith(".") and selector[1:] in classes_in_use:
                        should_keep = True
                    # ID selectors like "#my-id"
                    elif selector.startswith("#") and selector[1:] in ids_in_use:
                        should_keep = True
                    # Universal selector
                    elif selector == "*":
                        should_keep = True
                    # Complex selectors - more conservative, keep these to avoid breaking things
                    elif any(c in selector for c in (":", ">", "+", "~", "[", "]")):
                        should_keep = True
                    # Selectors with tags, classes, or IDs that might be used
                    else:
                        # Check for tag names
                        for tag in tags_in_use:
                            if re.search(r"\b" + re.escape(tag) + r"\b", selector):
                                should_keep = True
                                break

                        # Check for class names
                        if not should_keep:
                            for cls in classes_in_use:
                                if re.search(r"\." + re.escape(cls) + r"\b", selector):
                                    should_keep = True
                                    break

                        # Check for IDs
                        if not should_keep:
                            for id_val in ids_in_use:
                                if re.search(
                                    r"#" + re.escape(id_val) + r"\b", selector
                                ):
                                    should_keep = True
                                    break

                if should_keep:
                    matched_selectors.append(selector)

            # If any selectors matched, keep this rule with only the matched selectors
            if matched_selectors:
                rule.selectorText = ", ".join(matched_selectors)
                rules_to_keep.append(rule)

        # Keep other types of rules (like @media, @keyframes, etc.)
        elif rule.type != rule.COMMENT:
            rules_to_keep.append(rule)

    # Create a new stylesheet with only the retained rules
    new_stylesheet = cssutils.css.CSSStyleSheet()
    for rule in rules_to_keep:
        new_stylesheet.add(rule)

    # Serialise the new stylesheet
    return new_stylesheet.cssText.decode("utf-8")


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content.
    Returns (frontmatter_dict, content_without_frontmatter)
    """
    frontmatter_pattern = r'^\s*---\n(.*?)\n---\n+'
    match = re.match(frontmatter_pattern, content, flags=re.DOTALL)
    
    if match:
        yaml = YAML()
        try:
            frontmatter = yaml.load(match.group(1))
            if frontmatter is None:
                frontmatter = {}
        except:
            frontmatter = {}
        content_without = re.sub(frontmatter_pattern, '', content, count=1, flags=re.DOTALL)
        return frontmatter, content_without
    return {}, content


def convert_to_html(
    filenames: List[str],
    css: str,
    macros: dict,
    transforms: List[Callable[[str], str]],
    project: str,
    top_level_files: List[str],
) -> Tuple[List[str], List[str]]:
    """
    Convert each Markdown file and convert to HTML, using the same rendering library as
    mkdocs, with the same set of extensions. We expand the mkdocs-macro {{ templates }}
    and optionally provide means for applying a set of transformations. Currently, we add
    all the CSS in the header - this is required as the HTML engine in the Windows CHM
    viewer does not understand <link ...>.

    As a mitigation, take steps to only add the actually used CSS bits.
    
    Returns: (converted_files, excluded_files)
    """
    converted: List[str] = []
    excluded: List[str] = []

    head_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
"""

    for file in filenames:
        if file in top_level_files:
            # Top-level files go directly in project/
            newname = os.path.basename(file).replace(".md", ".htm")
        elif "/docs/" in file:
            # Sub-site files go in project/sub-site/
            path, oldname = file.split("/docs/", maxsplit=1)
            sub_site = os.path.basename(path)
            newname = os.path.join(sub_site, oldname.replace(".md", ".htm"))
        else:
            # Fallback for files without /docs/
            newname = os.path.basename(file).replace(".md", ".htm")

        realpath_newname = str(os.path.join(project, newname))
        os.makedirs(os.path.dirname(realpath_newname), exist_ok=True)

        with open(file, "r", encoding="utf-8") as f:
            md = f.read()

        # Parse frontmatter and check for search exclusion
        frontmatter, md = parse_frontmatter(md)
        if frontmatter.get('search', {}).get('exclude', False):
            excluded.append(file)

        # Macros are defined in the "extra:" section in the mkdocs.yml file. In the Markdown
        # source, they are templates of the type
        #
        #    {{ macro-name }}
        md = expand_macros(md, macros)

        # Hook point for transforms we may want to apply to the source Markdown before it's
        # converted to HTML.
        for fun in transforms:
            md = fun(md)

        # Convert Markdown to HTML, using the same extensions as used by our mkdocs setup.
        body = markdown.markdown(
            md,
            extensions=[
                "admonition",  # https://python-markdown.github.io/extensions/admonition/
                "attr_list",  # https://python-markdown.github.io/extensions/attr_list/
                "footnotes",  # https://python-markdown.github.io/extensions/footnotes/
                "markdown_tables_extended",  # https://github.com/fumbles/tables_extended
                "pymdownx.details",  # https://facelessuser.github.io/pymdown-extensions/extensions/details/
                "pymdownx.superfences",  # https://facelessuser.github.io/pymdown-extensions/extensions/superfences/
                TableCaptionExtension(),  # https://github.com/flywire/caption
            ],
        )

        body = body.replace("``", "")  # Empty code blocks aren't rendered correctly

        body = fix_links_html(body)
        body = remove_footnote_links(body)
        body = fix_external_links(body)

        # Extract the H1 content for use in the title tag, setting for_title=True
        # to only extract the name part (excluding command span)
        title = extract_h1(body, for_title=True)

        # Use a default title if no H1 is found
        if not title:
            # Use the filename without extension as a fallback title
            title = (
                os.path.splitext(os.path.basename(file))[0].replace("_", " ").title()
            )

            # For special files like welcome.md, use a more appropriate title
            if file.endswith("welcome.md"):
                title = "Welcome to Dyalog APL"

        # Format the head with the title
        head = head_template.format(title=title)

        # Optimise CSS specifically for this page: only use selectors referring to
        # ids, classes and tags on the actual page.
        optimised_css = purge_css(css, body)

        # Minimise the CSS
        optimised_css = css_compress(optimised_css)

        # Construct and minimise the HTML
        final_html = (
            f"{head}<style>{optimised_css}</style></head><body>{body}</body></html>"
        )
        final_html = html_minify(
            final_html,
            remove_comments=True,
            remove_empty_space=True,
            remove_all_empty_space=False,
            reduce_boolean_attributes=True,
        )

        with open(realpath_newname, "w", encoding="utf-8") as f:
            f.write(final_html)

        converted.append(str(newname))
    return converted, excluded


def copy_images(filenames: List[str], project="project") -> List[str]:
    copied: List[str] = []
    for file in filenames:
        path, oldname = file.split("/docs/", maxsplit=1)
        newname = str(os.path.join(os.path.basename(path), oldname))
        realpath_newname = str(os.path.join(project, newname))
        os.makedirs(os.path.dirname(realpath_newname), exist_ok=True)
        shutil.copy(file, realpath_newname)
        copied.append(newname)
    return copied


def static_assets(
    src_dir="assets", project="project"
) -> Tuple[List[str], str, List[str]]:
    """
    Copy the items in the assets dir. There is no supported way to
    bundle css via a <link> tag in a CHM file, so we concatenate
    the css files we can find and return this as a string for
    injection into each page.
    """
    assets = []
    css_files = []  # Keep track of CSS files
    css = ""

    if not os.path.exists(src_dir):
        return assets, css, css_files

    os.makedirs(os.path.join(project, "assets"), exist_ok=True)

    for root, _, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, src_dir)
            dst_path = os.path.join(project, "assets", rel_path)

            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            if file.endswith(".css"):
                with open(src_path, "r", encoding="utf-8") as f:
                    data = f.read()
                css = css + data
                css_files.append(src_path)  # Add to list of CSS files
            else:
                shutil.copy(src_path, dst_path)
                assets.append(os.path.join("assets", rel_path))

    return assets, css, css_files


def extract_h1(data: str, for_title: bool = False) -> str:
    """
    Extract text from the first h1 tag, handling special styling with spans.
    """
    soup = BeautifulSoup(data, "html.parser")
    if h1 := soup.find("h1"):
        if name_span := h1.find("span", class_="name"):
            # If for_title is True, return only the name
            if for_title:
                return name_span.get_text().strip().replace('"', "").replace("`", "")

            # Otherwise, return name + command if command exists
            command_span = h1.find("span", class_="command")
            if command_span:
                return f"{name_span.get_text()} {command_span.get_text()}".strip()
            else:
                return name_span.get_text().strip().replace('"', "").replace("`", "")
        else:
            # No special spans, just return the full h1 text
            return h1.get_text().strip().replace('"', "").replace("`", "")
    return ""


def extract_headers(filename: str) -> List[str]:
    """
    Find all headers -- Markdown headers are lines that start with one or more '#'.
    Some files will also have a raw HTML <h1> for styling reasons. The headers will
    be used as entries in the CHM index file.
    """
    results: List[str] = []

    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()

    # Note: extract headers, but discard the command span, as the Windows search
    # results list display cannot cope with UTF8...
    h1 = extract_h1(data, for_title=True)
    if h1:
        results.append(h1)

    headers = re.findall(r"^#+\s+(.+)$", data)
    results.extend(headers)

    return results


def generate_index_data(files: List[str]) -> List[Tuple[str, str]]:
    """
    Note: we're generating the index data from the source Markdown, but we
    need to ensure that filenames refer to the converted HTML files.
    """
    entries = []
    for filename in files:
        headings = extract_headers(filename)
        if "/docs/" in filename:
            a, b = filename.split("/docs/", maxsplit=1)
            newname = f"{os.path.basename(a)}/{b.replace('.md', '.htm')}"
        else:
            # For root-level files, just use the basename
            newname = os.path.basename(filename).replace(".md", ".htm")

        for heading in headings:
            entries.append((heading, newname))

    # Sort the index alphabetically by entry (not filename!)
    entries.sort(key=lambda w: w[0])

    return entries


def write_index_data(entries: List[Tuple[str, str]], filename: str) -> None:
    """
    Write out the CHM index file.
    """
    with open(filename, "w", encoding="utf-8") as idxfh:
        idxfh.write(HEADER)
        idxfh.write("<ul>\n")
        for x in entries:
            idxfh.write(FILE_ENTRY.format(name=x[0], file=x[1]))
        idxfh.write("</ul>\n")
        idxfh.write("</body></html>\n")


def find_nav_files_and_dirs(
    filename: str, remove: List[str]
) -> Tuple[List[str], List[str]]:
    """
    Extract both top-level directories (from !include directives) and standalone Markdown files
    directly listed in the nav section of the mkdocs.yml file.

    Returns:
        Tuple[List[str], List[str]]: (included_dirs, standalone_files)
    """
    yaml = YAML()
    with open(filename, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    included_dirs = []
    standalone_files = []

    for d in data["nav"]:
        key, value = next(iter(d.items()))
        if key not in remove:
            if isinstance(value, str):
                if m := re.match(r'!include\s+([^"]+)', value):
                    included_dirs.append(m.group(1))  # Path from !include
                elif value.endswith(".md") and not value.endswith("-print.md"):
                    standalone_files.append(
                        os.path.join("docs", value)
                    )  # Direct .md file reference

    return included_dirs, standalone_files


def generate_hfp(
    project: str,
    chmfile: str,
    files: List[str],
    images: List[str],
    assets: List[str],
    title: str,
    codepage: int = 65001,
) -> None:
    """
    Generates a project .hfp file for the chmcmd chm compiler, listing all .htm-files
    in the directory tree, plus the _index.hhk and _table_of_contents.hhc files.
    """
    start_page = None
    base, chmext = os.path.splitext(chmfile)
    hfp = base + ".hfp"
    outfile = os.path.join(project, hfp)

    impl = getDOMImplementation()

    doc = impl.createDocument(None, "CONFIG", None)

    # Create the <CONFIG> base element
    cfg = doc.documentElement

    # Files section
    filegroup = doc.createElement("Files")
    cfg.appendChild(filegroup)

    count = doc.createElement("Count")
    count.setAttribute("Value", str(len(files) + len(images) + len(assets)))
    filegroup.appendChild(count)

    fcount = 0

    for file in itertools.chain(files, images, assets):
        f = doc.createElement("FileName" + str(fcount))
        f.setAttribute("Value", file)
        filegroup.appendChild(f)
        if start_page is None:
            _, ext = os.path.splitext(file)
            if ext == ".htm":
                start_page = file
        fcount = fcount + 1

    tcf = doc.createElement("IndexFile")
    tcf.setAttribute("Value", "_index.hhk")
    filegroup.appendChild(tcf)

    tcf = doc.createElement("TOCFile")
    tcf.setAttribute("Value", "_table_of_contents.hhc")
    filegroup.appendChild(tcf)

    settings = doc.createElement("Settings")
    cfg.appendChild(settings)

    searchable = doc.createElement("MakeSearchable")
    searchable.setAttribute("Value", "True")
    settings.appendChild(searchable)

    if start_page is None:
        start_page = "welcome.htm"
    dflt = doc.createElement("DefaultPage")
    dflt.setAttribute("Value", start_page)
    settings.appendChild(dflt)

    te = doc.createElement("Title")
    te.setAttribute("Value", title)
    settings.appendChild(te)

    ofn = doc.createElement("OutputFileName")
    ofn.setAttribute("Value", chmfile)
    settings.appendChild(ofn)

    fnt = doc.createElement("DefaultFont")
    fnt.setAttribute("Value", "")
    settings.appendChild(fnt)

    # Add CodePage setting
    cp = doc.createElement("CodePage")
    cp.setAttribute("Value", str(codepage))
    settings.appendChild(cp)

    # Hard-coded Language ID for UK English (0x0809)
    lang = doc.createElement("Language")
    lang.setAttribute("Value", "0x0809")
    settings.appendChild(lang)

    # Add additional CHM-specific settings that might help with search
    binary_index = doc.createElement("BinaryIndex")
    binary_index.setAttribute("Value", "True")
    settings.appendChild(binary_index)

    full_text_search = doc.createElement("FullTextSearch")
    full_text_search.setAttribute("Value", "True")
    settings.appendChild(full_text_search)

    with open(outfile, "w", encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  "))


def table_captions(body: str) -> str:
    """
    Find table captions and references. Adapt for use with

        https://github.com/flywire/caption

    Captions will have the format

        Table: caption_text {: #anchor_name }

    References are links to the anchor name, but without a link text:

        [](#anchor_name)

    The flywire/caption Markdown extension uses its own ids of the form

        _table-X

    so we need to rewrite our ids to theirs. Also, flywire/caption has
    no automatic renumbering of table _references_, so fill that out.
    """
    anchors = {}
    idx_list = []

    def replace_table_captions(match, idx_list):
        idx = len(idx_list) + 1  # ⎕IO ← 1
        caption_text, anchor_name = match.groups()
        idx_list.append(idx)
        anchors[anchor_name] = idx
        return f"Table: {caption_text}"

    # Update table references
    def replace_table_refs(match):
        anchor_name = match.group(1)
        if anchor_name in anchors:
            idx = anchors[anchor_name]
            return f"[Table {idx}](#_table-{idx})"
        return match.group(0)  # Return the original match if not in anchors

    # Rework caption ids.
    body = re.sub(
        r"Table:\s*(.*?)\s*\{:\s*#(\S+)\s*\}",
        lambda match: replace_table_captions(match, idx_list),
        body,
    )
    return re.sub(
        r"\[\]\(#(\S+)\)", replace_table_refs, body
    )  # Update table references


def fix_links_html(html: str) -> str:
    """
    Applies the link transformations to an HTML document:
    1. Links with targets ending in ".md" are changed to ".htm".
    2. Links without extensions and leading "../" are lifted one relative level, and suffixed with ".htm".
    3. Off-site links starting with "http" remain unchanged.

    Parameters:
        html (str): The HTML content as a string.

    Returns:
        str: The modified HTML content.
    """

    def transform_link(href: str) -> str:
        """
        Transforms an individual href link according to the rules.
        """
        if href.startswith("http"):  # Off-site link: leave unchanged
            return href

        path, name = os.path.split(href)
        base, ext = os.path.splitext(name)

        if ext == ".md":  # Link to another sub-site: change ".md" to ".htm"
            return os.path.join(path, f"{base}.htm")

        if (
            ext == ""
        ):  # Link within the same side -- lift one relative level, and add .htm
            target = re.sub(r"^\.\.\/", "", href, count=1)
            return f"{target}.htm"

        # Something else; leave unchanged
        return href

    # Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find and transform all <a> tags with href attributes
    for a_tag in soup.find_all("a", href=True):
        original_href = a_tag["href"]
        a_tag["href"] = transform_link(original_href)

    # Return the modified HTML as a string
    return str(soup)


def remove_footnote_links(html: str) -> str:
    """
    Remove linking aspects from footnotes:
    1. Convert footnote reference links to plain superscript text
    2. Remove backlinks from footnote text
    
    Parameters:
        html (str): The HTML content as a string.
        
    Returns:
        str: The modified HTML content.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # Find all footnote reference links and replace with plain superscript text
    for a_tag in soup.find_all("a", class_="footnote-ref"):
        # Get the footnote number/text
        footnote_text = a_tag.get_text()
        # Create a superscript element
        sup_tag = soup.new_tag("sup")
        sup_tag.string = footnote_text
        # Replace the link with the superscript
        a_tag.replace_with(sup_tag)
    
    # Find all footnote backlinks and remove them
    for a_tag in soup.find_all("a", class_="footnote-backref"):
        # Simply remove the backlink
        a_tag.decompose()
    
    return str(soup)


def fix_external_links(html: str) -> str:
    """
    Fix external links for CHM compatibility.
    The Windows CHM viewer can open external links with target="_blank".
    This function adds the target attribute to all external HTTP/HTTPS links.
    
    Parameters:
        html (str): The HTML content as a string.
        
    Returns:
        str: The modified HTML content.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # Find all external links
    for a_tag in soup.find_all("a", href=True):
        href = a_tag.get("href")
        if href and href.startswith(("http://", "https://")):
            # Add target="_blank" to open in external browser
            a_tag["target"] = "_blank"
    
    return str(soup)


def find_image_references_in_markdown(md_files: List[str]) -> set:
    """
    Find all image references in Markdown files.
    Returns set of image filenames.
    """
    image_refs = set()

    # Regular expression for Markdown image syntax: ![alt](path/image.png)
    md_img_pattern = r"!\[.*?\]\((.*?)\)"

    # Regular expression for HTML image tags in Markdown: <img src="path/image.png">
    html_img_pattern = r'<img[^>]*src=[\'"]([^\'"]+)[\'"][^>]*>'

    for file in md_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

                # Find Markdown-style image references
                for match in re.findall(md_img_pattern, content):
                    if not match.startswith(("http:", "https:", "data:")):
                        image_refs.add(os.path.basename(match))

                # Find HTML-style image references
                for match in re.findall(html_img_pattern, content):
                    if not match.startswith(("http:", "https:", "data:")):
                        image_refs.add(os.path.basename(match))
        except Exception as e:
            print(f"Warning: Could not check images in {file}: {e}")

    return image_refs


def find_image_references_in_css(css_files: List[str]) -> set:
    """
    Find all image references in CSS files.
    Returns set of image filenames.
    """
    image_refs = set()

    # Regular expression for CSS url() syntax: url('/path/image.png')
    css_img_pattern = r'url\([\'"]?([^\'"()]+)[\'"]?\)'

    for file in css_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

                # Find CSS url() references
                for match in re.findall(css_img_pattern, content):
                    if not match.startswith(("http:", "https:", "data:")):
                        # Extract just the filename from the path
                        image_refs.add(os.path.basename(match))
        except Exception as e:
            print(f"Warning: Could not check images in CSS file {file}: {e}")

    return image_refs


def filter_unused_images(
    md_files: List[str], css_files: List[str], image_files: List[str]
) -> List[str]:
    """
    Filter out images that are not referenced in any Markdown or CSS files.
    Returns filtered list of image files to include.
    """
    # Find all image references from Markdown and CSS
    md_referenced_images = find_image_references_in_markdown(md_files)
    css_referenced_images = find_image_references_in_css(css_files)

    referenced_images = md_referenced_images.union(css_referenced_images)

    # Filter image_files to only include referenced images
    used_images = []
    unused_images = []

    for img in image_files:
        if os.path.basename(img) in referenced_images:
            used_images.append(img)
        else:
            unused_images.append(img)

    # Report findings
    if unused_images:
        print("\nExcluding unused images:")
        for img in sorted(unused_images):
            print(f"  {os.path.basename(img)}")
        print(
            f"\nTotal: {len(unused_images)} unused images removed, keeping {len(used_images)} used images"
        )
    else:
        print("\nAll images are referenced in the documentation or CSS.")

    if css_referenced_images:
        print("\nImages referenced in CSS:")
        for img in sorted(css_referenced_images):
            print(f"  {img}")

    return used_images


def add_langref_disambiguation_pages(root: Node, project: str) -> None:
    """
    Add missing symbol files to the TOC as a post-processing step.
    This function finds all converted HTML files in the symbols directory
    and adds them to the "Symbols" node in the TOC if they aren't already there.

    Parameters:
        root (Node): The root node of the TOC tree
        project (str): The project directory
    """
    print("Post-processing TOC to add Language Reference disambiguation pages...")

    # First find the "Language Reference" node
    lang_ref_node = None
    for child in root.children:
        if child.name == "Language Reference":
            lang_ref_node = child
            break

    if not lang_ref_node:
        print("  Warning: Language Reference node not found in TOC")
        return

    # Then find the "Symbols" node under "Language Reference"
    symbols_node = None
    for child in lang_ref_node.children:
        if child.name == "Symbols":
            symbols_node = child
            break

    if not symbols_node:
        print("  Warning: Symbols node not found under Language Reference in TOC")
        return

    print(
        f"  Found Symbols node in TOC with {len(symbols_node.children)} existing entries"
    )

    # Get the symbol html files from the project directory
    symbols_dir = os.path.join(project, "language-reference-guide", "symbols")
    if not os.path.isdir(symbols_dir):
        print(f"  Warning: Symbols directory not found at {symbols_dir}")
        return

    # Get all HTML files in the symbols directory
    html_files = [f for f in os.listdir(symbols_dir) if f.endswith(".htm")]
    print(f"  Found {len(html_files)} HTML files in symbols directory")

    # Find which ones are already in the TOC
    existing_files = set()
    for child in symbols_node.children:
        if child.html_name:
            existing_files.add(os.path.basename(child.html_name))

    print(f"  Found {len(existing_files)} files already in TOC")

    # For each HTML file not in the TOC, extract its title and add it
    added_count = 0
    for html_file in html_files:
        # Skip if already in TOC
        if html_file in existing_files:
            continue

        # Read the HTML file to extract its title
        html_path = os.path.join(symbols_dir, html_file)
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            # Extract the title from the HTML
            soup = BeautifulSoup(html_content, "html.parser")
            title = ""

            # Try to find title in the head first
            if title_tag := soup.find("title"):
                title = title_tag.string.strip()

            # If no title or title is too generic, try to find the name span in h1
            if not title or title == "Dyalog APL":
                if h1 := soup.find("h1", class_="heading"):
                    if name_span := h1.find("span", class_="name"):
                        title = name_span.string.strip()

            # If still no title, use filename
            if not title:
                title = os.path.splitext(html_file)[0].replace("-", " ").title()

            # Create a new node and add it to the Symbols node
            node = Node(
                title, f"symbols/{html_file}", symbols_node.depth + 1, symbols_node
            )
            node.html_name = f"language-reference-guide/symbols/{html_file}"
            symbols_node.children.append(node)
            added_count += 1
            print(f"    Added: {title} -> {node.html_name}")

        except Exception as e:
            print(f"  Warning: Error processing {html_file}: {e}")

    if added_count > 0:
        print(f"  Added {added_count} additional symbol files to TOC")
    else:
        print("  No additional symbol files needed to be added")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a CHM bundle from a mkdocs site"
    )
    parser.add_argument(
        "--mkdocs-yml", type=str, required=True, help="Path to the mkdocs.yml file"
    )
    parser.add_argument(
        "--project-dir", type=str, required=True, help="Name of output directory"
    )
    parser.add_argument(
        "--assets-dir", type=str, default="assets", help="Name of assets directory"
    )
    parser.add_argument(
        "--welcome", type=str, default="welcome.md", help="Path to welcome.md file"
    )
    parser.add_argument(
        "--config", type=str, help="JSON config file for additional options"
    )
    parser.add_argument("--git-info", type=str, help="Git branch and commit info")
    parser.add_argument("--build-date", type=str, help="Build date")
    parser.add_argument(
        "--codepage",
        type=int,
        default=65001,
        help="CodePage to use (default: 65001 for UTF-8)",
    )

    args = parser.parse_args()

    if not args.mkdocs_yml.endswith("mkdocs.yml"):
        sys.exit('--> expected a "mkdocs.yml" file')

    if not os.path.isfile(args.mkdocs_yml):
        sys.exit(f"--> file {args.mkdocs_yml} not found.")

    if not os.path.isfile(args.welcome):
        sys.exit(f"--> welcome file {args.welcome} not found.")

    os.makedirs(args.project_dir, exist_ok=True)

    # Parse config for excludes
    excludes = []
    if args.config:
        try:
            with open(args.config, "r", encoding="utf-8") as f:
                config = json.load(f)
                excludes = config.get("exclude", [])
        except (json.JSONDecodeError, FileNotFoundError) as e:
            sys.exit(f"--> Error reading config file: {e}")

    # Parse mkdocs.yml
    yml_data = parse_mkdocs_yml(args.mkdocs_yml, remove=excludes)

    # Find top-level dirs and standalone files from nav
    included_dirs, standalone_files = find_nav_files_and_dirs(
        args.mkdocs_yml, remove=excludes
    )

    version = yml_data["extra"].get("version_majmin")
    if not version:
        sys.exit(f"--> source mkdocs.yml has no Dyalog version set")

    # Find all source Markdown files from included directories
    md_files_from_dirs, image_files = find_source_files(
        os.path.dirname(args.mkdocs_yml), included_dirs
    )

    # Add standalone Markdown files from nav, with absolute paths
    standalone_files_abs = [
        os.path.abspath(os.path.join(os.path.dirname(args.mkdocs_yml), f))
        for f in standalone_files
    ]
    
    # Filter out -print.md files from standalone files
    excluded_print_standalone = [f for f in standalone_files_abs if f.endswith("-print.md")]
    standalone_files_abs = [f for f in standalone_files_abs if not f.endswith("-print.md")]
    
    if excluded_print_standalone:
        print(f"\nExcluded {len(excluded_print_standalone)} -print.md standalone files:")
        for f in sorted(excluded_print_standalone):
            print(f"  - {os.path.basename(f)}")
    
    md_files = md_files_from_dirs + standalone_files_abs

    # Add welcome.md to the start of the files list
    md_files.insert(0, os.path.abspath(args.welcome))

    # Modify nav to include welcome page at the start
    yml_data["nav"].insert(0, "welcome.md")

    # Copy images and other static assets into the project
    assets, css, css_files = static_assets(args.assets_dir, args.project_dir)

    # Filter out unused images, considering both MD and CSS references
    image_files = filter_unused_images(md_files, css_files, image_files)
    copied_images = copy_images(image_files, project=args.project_dir)

    # Add git info and build date to macros
    macros = yml_data.get("extra", {})
    if args.git_info:
        macros["git_info"] = args.git_info
    if args.build_date:
        macros["build_date"] = args.build_date

    # Convert to HTML
    html_files, excluded_files = convert_to_html(
        md_files,
        css,
        macros=macros,
        transforms=[table_captions],
        project=args.project_dir,
        top_level_files=standalone_files_abs,
    )
    
    # Remove excluded files from md_files for indexing
    md_files = [f for f in md_files if f not in excluded_files]
    
    if excluded_files:
        print(f"\nExcluded {len(excluded_files)} files from search index due to 'search: exclude: true':")
        for f in excluded_files:
            print(f"  - {os.path.basename(f)}")

    # Generate the CHM ToC
    generate_toc(yml_data, project=args.project_dir)

    # Generate the index
    idx = generate_index_data(md_files)
    write_index_data(idx, f"{args.project_dir}/_index.hhk")

    print(f"Converted {len(md_files)} Markdown files to HTML.")

    # Generate the CHM project config file
    chm_name = "dyalog.chm"
    generate_hfp(
        args.project_dir,
        chm_name,
        html_files,
        copied_images,
        assets,
        title=f"Dyalog version {version}",
        codepage=args.codepage,
    )

    # Run the compiler
    output = Popen(["chmcmd", "dyalog.hfp"], cwd=args.project_dir)
    output.wait()
