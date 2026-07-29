# Tools for Dyalog documentation authors

The `tools/` directory contains Docker-based tools for Dyalog's documentation authors. You will need a working installation of [Docker](https://www.docker.com/products/docker-desktop/). We use the `docker compose` orchestration tool to bundle up a set of containers that are useful for documentation authors who do not wish to keep a local Python environment.

Note: the directory settings can be stashed in a `.env` file; see [below](#the-env-file).

## Available Docker Services

- **`mkdocs-server`** - Live preview server with hot-reload (port 8000)
- **`docs-nginx`** - Build static site and serve via nginx (port 8080) - **much faster, but no live reload**
- **`utils`** - Utility scripts for validation, checking links, finding orphans, etc.

## Live preview

A "sub-site" is one of the component documents as defined by the nav section in the top-level `mkdocs.yml` file, currently:

- release-notes
- earlier-release-notes
- language-reference-guide
- programming-reference-guide
- windows-installation-and-configuration-guide
- windows-ui-guide
- object-reference
- interface-guide
- dotnet-framework-interface
- unix-installation-and-configuration-guide
- unix-user-guide

> **Note:** When using the Docker-based tools, you need to give `docker compose` the **full command name**, _not_ a bare `docker compose up`. 

To preview a mkdocs site, do:

```shell
export DOCS_DIR=path-to-dir-containing-docs  # or use a .env file; see below
docker compose up [--build][--remove-orphans] mkdocs-server
```
Note the full command name. For example, for the whole lot, do:
```shell
export DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation
docker compose up mkdocs-server
```
and for a particular sub-site, e.g the `language-reference-guide` (see list above):
```shell
export DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation/language-reference-guide/
docker compose up mkdocs-server
```

> **Note**: The first time you run `docker compose`, the various containers will be built. Subsequent runs will reuse the containers, and will be quicker to start.

Visit [the preview page](http://localhost:8000/) on http://localhost:8000/

For individual documents, this is pretty swift, and subsequent source changes will be reflected live.

Note that building the complete set takes several minutes. Consider previewing the specific document you're working on for the best experience.

Note also that you'll see many screens of warnings about links referencing files that do not exist -- this is expected, and a consequence of the [monorepo plugin](https://backstage.github.io/mkdocs-monorepo-plugin/). Links referencing pages across sub-sites will only be valid _after_ the final rendering is complete.

The docker image will consume resources, so when you're finished, be sure to quit with <kbd>Ctrl</kbd>-<kbd>c</kbd>, and tidy up with 
```shell
docker compose down
```

### Preview a remote branch

If, for example, you're asked to review a PR branch, checkout the remote branch, and run the preview as described above. If you're using the commandline version of git, simply do

```shell
git checkout -b branch-name-here origin/branch-name-here
cd tools
export DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation/language-reference-guide/
docker compose up mkdocs-server  # Note: full command name
```

If you're using a GUI tool for git, like [GitHub Desktop](https://github.com/apps/desktop), 

1. In the menu, select `Repository > Fetch`
2. Set "Current branch" to the branch to be reviewed

See [CONTRIBUTE](../CONTRIBUTE.md) for how to leave a PR review.

## Utility Scripts

The `utils` service provides access to various documentation maintenance scripts:

Edit `.env` to contain:

```
DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation
ASSETS_DIR=/Users/stefan/work/dyalog-docs/documentation/documentation-assets
```

From the tools/ directory:

### Live Markdown Renderer

`render.py` is a live markdown renderer with auto-reload functionality. It renders a markdown file to HTML and automatically refreshes the browser view when the source file changes. This is perfect for testing markdown files before building the full site.

**Features:**
- Live preview with auto-reload on file changes
- Uses the same CSS as the live MkDocs site (from `documentation-assets`)
- Uses the same Markdown extensions as MkDocs (pymdownx, tables, admonitions, etc.)
- Built-in HTTP server

#### Docker Usage (Recommended)

```bash
# Make sure .env has ASSETS_DIR set (see above)
docker compose run --rm utils python /utils/render.py /docs/tools/primitive-functions-by-category.md --no-browser
```

The rendered HTML will be created in the same directory as the source Markdown file.

#### Local Usage

```bash
cd tools
source ../docs-venv/bin/activate
python utils/render.py primitive-functions-by-category.md
```

This will open your browser automatically and watch for changes.

#### Options

```bash
# Custom output file
python utils/render.py /path/to/input.md --output /docs/custom.html

# Custom port (if 8000 is in use)
python utils/render.py /path/to/input.md --port 8080

# Don't open browser (useful for Docker)
python utils/render.py /path/to/input.md --no-browser
```

#### CSS Sources

The script automatically loads CSS in this priority:

1. **External CSS (preferred)**: Loads `main.css` and `extra.css` from `documentation-assets`
   - In Docker: mounted at `/docs/docs/documentation-assets`
   - Locally: auto-detected relative to the script location
   - Gives you the same styling as the live site
   - Shows message: `Loaded CSS from /path/to/documentation-assets`

2. **Embedded CSS (fallback)**: Uses built-in CSS if `documentation-assets` not found
   - Shows warning: `Warning: documentation-assets not found, using embedded CSS`
   - Still provides good styling but may not match live site exactly

**Tip:** To ensure you see the same rendering as the live site, make sure `ASSETS_DIR` is set in your `.env` file (see [The `.env` file](#the-env-file) section below).

#### What Gets Rendered

The script renders markdown using the same extensions as MkDocs:
- Extended tables with column/row spans and alignment (`:--:`, `---:`, etc.)
- Admonition blocks (note, warning, info, tip, etc.)
- Collapsible sections (details/summary)
- Syntax-highlighted code blocks
- Keyboard key combinations
- Footnotes

For detailed documentation:
```bash
# Quick help
python /utils/render.py --help

# Full documentation (local)
cd tools/utils && pydoc3 render

# Or view the comprehensive docstring at the top of utils/render.py
```

### Finding Orphaned Pages

`find_orphans.py`: Find truly orphaned Markdown files across ALL output formats:

```bash
# Docker
docker compose run --rm utils python /utils/find_orphans.py --root /docs/mkdocs.yml

# Local
python utils/find_orphans.py --root ../mkdocs.yml --verbose

# With YAML output
python utils/find_orphans.py --root ../mkdocs.yml --output orphans.yaml

# Exclude specific subsites (comma-separated)
python utils/find_orphans.py --root ../mkdocs.yml --exclude object-reference,unix-user-guide

# Exclude CHM disambiguation pages
python utils/find_orphans.py --root ../mkdocs.yml --output orphans.yaml --help_urls path/to/svn/help_urls.h
```

This locates files that are invisible in ALL formats:
- Not in any `mkdocs.yml` nav (standard or `print_mkdocs.yml`)
- Not referenced by any markdown links
- Not referenced by any HTML links
- Not used by CHM (`welcome.md`) or PDF builds

**Note:** Files in object-reference/ that are only accessible via links (not in nav) are correctly identified as NON-orphans.

### Ghost pages
`find_ghost_pages.py`: list pages not referenced by any `nav` section (simpler, faster):
```
docker compose run --rm utils python /utils/find_ghost_pages.py --root /docs/mkdocs.yml
```

### Link validation

#### Deployed Link Checker

Check links on a deployed site by testing actual HTTP responses.

Using [nginx](https://nginx.org/) (serves pre-built static site; fast!):
```bash
docker compose up docs-nginx

# in a different terminal:
docker compose run --rm utils python /utils/check_links.py \
                   --base-url http://docs-nginx:8080 \
                   --output /docs/tools/broken_links.yaml

docker compose down docs-nginx
```

Local:
```bash
mkdocs build
python tools/utils/check_links.py \
    --base-url http://localhost:8080 \ 
    --output tools/broken_links.yaml
```

Note: local is slower than Docker to Docker.

#### Source-based Link Validation

Check for dangling links via the Markdown source -- note, this can be unreliable:

```
docker compose run --rm utils python /utils/dangling_links.py
```

Find links containing specific text in the URL:

```
docker compose run --rm utils python /utils/findlinks.py --target "json" --root /docs
```

Check that all files in nav exist:
```
docker compose run --rm utils python /utils/check_yml_files.py
```

Validate image references in markdown files (detects both markdown `![](path)` and HTML `<img>` tags):
```
docker compose run --rm utils python /utils/validate_images.py --output /docs/tools/broken_images.yaml
```

If you're running outside Docker:

```
python utils/validate_images.py --output broken_images.yaml --root-dir ..
```

This script automatically uses ripgrep to verify unreferenced images and detects cross-document image references. The YAML report includes:
- `broken_references`: Markdown files with broken image links
- `cross_document_references`: Images referenced across document boundaries (bad practice that breaks isolated builds)
- `unreferenced_images`: Truly unreferenced images (safe to delete - verified with ripgrep)

**Important**: This script requires ripgrep (`rg`) to be installed. If ripgrep is not found, the script will exit with an error. To fix:
```
docker compose build utils
```

Remove unreferenced images identified by validate_images.py:
```
cd tools
./utils/remove-unused-images.sh broken_images.yaml           # Dry-run (shows what would be deleted)
./utils/remove-unused-images.sh broken_images.yaml --execute # Actually delete files
```

**Note**: This script must be run locally (not via Docker). The script:
- Must be run from the `tools/` directory
- Processes the `unreferenced_images:` section from the YAML output
- Uses `git rm` to remove files from both filesystem and git index
- Runs in dry-run mode by default for safety
- Requires explicit `--execute` flag to actually delete files
- Prompts for confirmation when running in execute mode

After running with `--execute`, review the staged deletions with `git status` and commit when ready.

Report all image references (not just broken ones):
```
docker compose run --rm utils python /utils/validate_images.py --all --output /docs/tools/all_images.yaml
```

Find and report all admonitions (note, info, warning, hint, etc.):
```
docker compose run --rm utils python /utils/find_admonitions.py --output /docs/tools/admonitions.yaml
```

Filter by admonition type:
```
docker compose run --rm utils python /utils/find_admonitions.py --type "warning,note" --output /docs/tools/warnings_notes.yaml
```

Filter admonitions by content (case-insensitive by default):
```
docker compose run --rm utils python /utils/find_admonitions.py --contains "strong INTERRUPT" --output /docs/tools/filtered.yaml
```

Combine type and content filters:
```
docker compose run --rm utils python /utils/find_admonitions.py --type info --contains "deprecated" --output /docs/tools/deprecated_info.yaml
```

Case-sensitive search:
```
docker compose run --rm utils python /utils/find_admonitions.py --contains "INTERRUPT" --case-sensitive --output /docs/tools/filtered.yaml
```

This script scans all markdown files and reports:
- Total count and breakdown by type (note, info, warning, hint, legacy, OS-specific)
- Files containing admonitions with line numbers and body content
- Usage statistics grouped by type
- Unknown admonition types that may lack styling in admonitions.css
- Optional filtering by type (e.g., `--type warning,note`) and/or content (e.g., `--contains "deprecated"`)

Admonition types supported in PDF generation:
- `note`, `info`, `warning`, `hint`, `legacy` (general purpose)
- `linux`, `unix`, `macos`, `windows` (OS-specific)

Add APL symbol synonyms:
```
docker compose run --rm utils python /utils/add_synonyms.py /docs/language-reference-guide/docs/primitive-functions [--dry-run]
```

Spider the deployed site to check for broken links and images (images are checked by default):
```
docker compose run --rm utils python /utils/check_deployed_links.py \
                   --base-url https://dyalog.github.io/documentation/20.0 \
                   --output /docs/tools/broken_links.yaml
```

If you're checking against a local site build running in Docker, use Docker's internal network:
```
docker compose run --rm utils python /utils/check_deployed_links.py \
                   --base-url http://mkdocs-server:8000 \
                   --output /docs/tools/broken_links.yaml
```

Key points:

- The `--rm` flag removes the container after it exits
- `/docs` inside the container is mapped to your `DOCS_DIR` from the `.env` file
- `/utils` inside the container contains all the utility scripts
- The scripts expect paths relative to the *container's* filesystem, not your host

`http://mkdocs-server:8000` works because:

1. Both containers are in the same Docker Compose network
2. Docker provides automatic DNS resolution for service names
3. `mkdocs-server` resolves to the internal IP of the mkdocs container

### Shared Utilities (`doc_utils.py`)

The `tools/utils/doc_utils.py` module provides reusable classes for working with the documentation:

**Core Classes:**
- `YAMLLoader` - Load YAML files with mkdocs custom tag support
- `NavTraverser` - Traverse and extract files from mkdocs nav structures
- `MkDocsRepo` - Represent and navigate the monorepo structure
- `LinkExtractor` - Extract markdown and HTML links from content
- `PathResolver` - Resolve file paths in the monorepo structure
- `LinkValidator` - Validate internal and cross-subsite links

**Specialized Parsers:**
- `HelpUrlsParser` - Parse C header files containing `HELP_URL()` macros
  - `parse_help_urls(file_path)` - Extract (symbol, url) tuples from `.h` files
  - `url_to_markdown_path(url, root_dir)` - Convert help URLs to source file paths
- `ImageReference` - Represent image references with line numbers
- `AdmonitionExtractor` - Extract and validate admonition blocks

These classes are used by multiple utility scripts to maintain consistency in how the documentation structure is processed.

### Additional Scripts

Exclude pages from search:
```
docker compose run --rm utils python /utils/exclude_from_search.py --exclude-file ghost.txt
```

Generate system function tables (for Language Reference Guide):
```
docker compose run --rm utils python /utils/sysfns.py
docker compose run --rm utils python /utils/sysfntables.py
docker compose run --rm utils python /utils/ibeams.py
```

### Adding New Utils

To add a new utility script:

1. Add the script to `tools/utils/`
2. If it requires additional Python packages, update the Dockerfile in `tools/utils/Dockerfile`
3. Rebuild the Docker image: `docker compose build utils`

## The `.env` file

You can gather the environment variable settings into a `.env` file which will be read by `docker compose`. Create a file called `.env` in the `tools/` directory. There is a file `.env.template` included in the repository. It should look like this:

```
DOCS_DIR={YOUR_REPO}
ASSETS_DIR={PATH_TO}/documentation-assets
```

Here is mine:

```
DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation/
ASSETS_DIR=/Users/stefan/work/dyalog-docs/documentation/documentation-assets
```

and for a specific sub-site, in this case `language-reference-guide`:

```
DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation/language-reference-guide
ASSETS_DIR=/Users/stefan/work/dyalog-docs/documentation/documentation-assets
```

If you're on Windows, you _must_ use backslashes:

```
DOCS_DIR=C:\devt\documentation
...
```

## Running Docker on Windows

To run `docker compose` on Windows, you'll need to have `Docker Desktop` for Windows installed and
running. `Docker Desktop` includes both `Docker` and `Docker Compose`.

**Install Docker Desktop for Windows**

> **Warning:** If you're using Microsoft Windows 10, you cannot use WSL2 with Docker. Choose HyperV instead during installation.

1. Download and run the [Docker Desktop installer](https://docs.docker.com/desktop/install/windows-install/) and follow
   the prompts to complete the installation.
2. `Docker Desktop` will recommend you to enable the [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) feature
   and potentially install a Linux kernel update package. Follow the installation guide provided by
   the `Docker` installer. 
3. After installation, run `Docker Desktop`. You might need to log in with your Docker account.

**Open a terminal**

1. You can use either Command Prompt (cmd) or PowerShell to run Docker commands on Windows.
2. Use the `cd` command to go to the directory containing the `docker-compose.yml` file.
3. Run `docker compose up`. This command reads the `docker compose.yml` file in the current directory, builds the images
   if they don't exist, and starts the containers as specified in the file.
4. If you've made changes to your `Dockerfile` or Docker Compose configuration and want to rebuild the images, you can
   use `docker compose up --build mkdocs-server`.
   
## APL-based tools

### BuildGUI

Note:

1. This code has been exported from the workspace `Core/ws/GUIMaint.dws`.
2. The code can only be run on Windows.

The main purpose of the code herein is to generate the cross-reference tables present in the `Object Reference Guide`. In
all likelihood, this is now fairly static, but changes do still occasionally happen. The code was written a long time ago, before Dyalog contained, for example, `⎕XML`. There are a few other, related functions in present, but only the cross-references generation has been ported to the new format for now.

The code has been left as-is, with the following exceptions:

1. The workspace has been exported to text, so that it can be versioned.
2. The function `WriteFile` now ensures that any directories not present in its path are created.

Additionally, two new functions have been added:

1. `NewBuildGUI`: the new entry point, serving the same purpose as `BuildGUI`, but not writing entries into a
   Table-of-Contents file, and not writing stubbed entries of new object.
2. `NewWriteMembers`: analogous to `WriteMembers`, creating the actual cross-reference tables, but writing
   Markdown instead of XML. This function will sort the tables it generates in col-major order. The old code generated
   tables that were occasionally not sorted at all.

To run this code, say

```apl
files ← NewBuildGUI '/some/path/to/your/chosen/dir/here'
```

Note that the old `BuildGUI` also takes a left arg 0 for "run" and 1 for "dry run". Write out the files to a fresh directory, do a diff against the existing, and integrate manually in the rare cases that something changed. 

We don't envisage that this will need doing as part of the day-to-day documentation authoring process, but something that will be run once per major version release.
