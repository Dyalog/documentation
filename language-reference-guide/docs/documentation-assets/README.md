# Documentation Assets
Central respository of stylesheets, assets and tools used across documentation of Dyalog projects

## How to include in another project
Futher explanation in [github.blog/open-source/git/working-with-submodules/](https://github.blog/open-source/git/working-with-submodules/).

These assets are for inclusion in Dyalog projects that use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for their documentation to enforce a consistent style and allow updating styles from a single source.

1. Clone the repository for the project.
2. Open a terminal (with Git installed) and navigate (`cd`) to the repository directory.
3. Run the following command to add this repository as a Git submodule.
    ```shell
    git submodule add https://github.com/Dyalog/documentation-assets
    ```

> **NOTE:**
> 
> If you are working on multiple projects, instead of doing a recursive clone you might prefer to clone this repository separately. Recursive cloning each project will result in having a copy of the documentation assets inside every project you clone.
> 
> The documentation can be previewed using the Docker configuration in the **tools** directory. The assets are included by setting the `STYLES_DIR` variable in the **.env** file in the **tools** directory.
