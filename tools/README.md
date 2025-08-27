# Tools for Dyalog documentation authors

The `tools/` directory contains Docker-based tools for Dyalog's documentation authors. You will need a working installation of [Docker](https://www.docker.com/products/docker-desktop/). We use the `docker compose` orchestration tool to bundle up a set of containers that are useful for documentation authors who do not wish to keep a local Python environment.

Note: the directory settings can be stashed in a `.env` file; see [below](#the-env-file).

## Live preview

A "sub-site" is one of the component documents as defined by the nav section in the top-level `mkdocs.yml` file, currently:

- release-notes-v19-0
- windows-installation-and-configuration-guide
- unix-installation-and-configuration-guide
- programming-reference-guide
- language-reference-guide
- object-reference
- windows-ui-guide
- interface-guide
- dotnet-interface
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
```

From the tools/ directory:

`find_ghost_pages.py`: list pages not referenced by any `nav` section:
```
docker compose run --rm utils python /utils/find_ghost_pages.py --root /docs/mkdocs.yml
```

Check for dangling links:

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

Add APL symbol synonyms:
```
docker compose run --rm utils python /utils/add_synonyms.py /docs/language-reference-guide/docs/primitive-functions [--dry-run]
```

Spider the deployed site to check for broken links:
```
docker compose run --rm utils python /utils/check_deployed_links.py \
                   --base-url https://dyalog.github.io/documentation/20.0 \
                   --output broken_links.txt
```

Key points:

- The `--rm` flag removes the container after it exits
- `/docs` inside the container is mapped to your `DOCS_DIR` from the `.env` file
- `/utils` inside the container contains all the utility scripts
- The scripts expect paths relative to the *container's* filesystem, not your host

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
```

Here is mine:

```
DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation
```

and for a specific sub-site, in this case `language-reference-guide`:

```
DOCS_DIR=/Users/stefan/work/dyalog-docs/documentation/language-reference-guide
```

If you're on Windows, you _must_ use backslashes:

```
DOCS_DIR=C:\devt\documentation
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
