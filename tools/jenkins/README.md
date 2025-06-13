# Jenkins Pipelines: MkDocs Site Deployment and Restore

## Purpose

Deploy the [MkDocs](https://www.mkdocs.org/) website which uses the [mike](https://github.com/jimporter/mike) tool for versioning. 


## Overview

### Deployment Pipeline (`Jenkinsfile`)

Deployment Pipeline (`Jenkinsfile`): keeps a self-hosted version of the documentation site in sync with the `gh-pages` branch. The deployment pipeline mirrors the `gh-pages` branch to a target web server directory while maintaining all `mike` versioning features.

The deployment pipeline is triggered whenever a new build is triggered via the GitHub Action (see `mkdocs-publish.yml`).

1. Compares the latest commit against the currently deployed version
   - Only proceeds if changes are detected (skip-if-same optimisation)
2. Creates timestamped backup of current site (unless `SKIP_BACKUP` is set)
   - Archives as Jenkins artifact with fingerprinting
   - Jenkins manages retention (keeps 5)
3. Deploys new content to web server
   - Mirror content with `rsync --delete`
   - Stage-level locking prevents concurrent deployments
   - Sets proper ownership and permissions
4. Verifies the deployment succeeded
5. Automatic rollback on failure using `copyArtifacts` from last successful build
6. Optional debug mode to display environment variables and state

## Stages

### Deployment Pipeline

1. `Initialise`:
    * Generates BUILD_TIMESTAMP for backup naming
    * Bails if timestamp generation fails

2. `Check for Changes`:
    * Compares the latest commit hash with currently deployed version

3. `Debug Environment` (optional):
    * Only runs when `DEBUG` parameter is enabled
    * Shows internal state variables and environment

4. `Backup Current Site`:
    * Only runs if changes detected and site exists
    * Creates backup named: `docs.backup.YYYYMMDD_HHMMSS.{hash}.tar.gz` (UTC timestamp)
    * Archives as Jenkins artifact with fingerprinting
    * Jenkins handles retention via `buildDiscarder` (keeps 5 artifacts)
    * Can be skipped with `SKIP_BACKUP` parameter
    * 10-minute timeout

5. `Deploy Site`:
    * Protected by `lock('docs-deploy')` to prevent concurrent deployments
    * Clears existing content while preserving volume mount
    * Uses `rsync -a --delete` to mirror content exactly
    * Stores commit hash for future comparisons
    * Sets proper ownership and permissions
    * Stage-level error reporting

6. `Verify Deployment`:
    * Simple verification checking for `index.html`
    * Reports deployment location and git hash
    * Stage-level error reporting

## Jenkins Plugins

The pipelines use the following Jenkins plugins:

1. `pipeline`
2. `git`
3. `timestamper` (optional)
   - Adds timestamps to console output via `timestamps()`
4. `copyartifact`
   - Required for `archiveArtifacts` and `copyArtifacts` steps
   - Backup storage and cross-job artifact access

5. `lockable-resources`
   - Required for `lock('docs-deploy')` in deployment stage
   - Prevents concurrent deployments
