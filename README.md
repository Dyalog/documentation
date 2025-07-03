# Dyalog APL documentation

> **Note** This is the source repository for the documentation for Dyalog APL. If you are looking for the actual published documentation, visit the [help section](https://help.dyalog.com/) on Dyalog's website instead. This repository is intended for documentation authors, not users.

If you want to contribute content to Dyalog's documentation, see the file [CONTRIBUTE.md](CONTRIBUTE.md) for an outline of the process we use.

Please consult the [Dyalog Documentation Guidelines](https://dyalog.github.io/documentation-guidelines) for the style and language conventions we adopt.

## Organisation

This is a mkdocs _monorepo_, using the Spotify [monorepo](https://github.com/backstage/mkdocs-monorepo-plugin) plugin. The top-level site is defined by the file `mkdocs.yml` in the root, and the `docs/` directory. The other directories are the respective sub-sites included in the `nav` section in `mkdocs.yml`, currently:

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

### Central Styles and Assets Submodule

Dyalog documentation uses the [Dyalog/documentation-styles](https://github.com/Dyalog/documentation-styles) repository as a submodule, included in `documentation-styles/`, to include CSS, fonts and images. Any additions or changes must be merged into that repository.

Using the [development tools](#tools) ensures that the styles are correctly included while developing, and the [GitHub Action to publish](./.github/workflows/mkdocs-publish.yml) handles them for publication.

Publication of the documentation updates the styles submodule to the latest commit. This repository will have a dependabot job that checks daily for updates and opens a pull request to update the submodule for this repository. Developers can update the submodule in their local checkout with `git submodule update --remote`.

## Tools

The `tools/` directory contains a `docker compose` configuration that can be used to preview our documentation documents in their rendered form. See its [README](tools/README.md) file for instructions on how to use the tooling.

## Getting started

1. Clone (or fork-clone if you are not a member of the Dyalog org) git@github.com:Dyalog/documentation.git
2. Set up a `{YOUR REPO}/tools/.env` file as indicated by [tools/README.md](tools/README.md)
3. Render the full site (if you have the patience, a sub-site if not) by running `docker-compose up mkdocs-server` in the `{YOUR REPO}/tools/` dir.

This is a large repository. If you're cloning using https, you may need to increase your buffer-size if the clone fails:

```
git config --global http.postBuffer 524288000"
```
   
## Publish

[For the person responsible for publishing]

```
mike set-default --push 20.0  # only needed once
mike deploy --push 20.0
```
