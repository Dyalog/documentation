# v21 Docs: What We Need From IT

We're splitting the documentation repo into two branches: `v20.0` (maintenance) and `main` (v21 development). The Jenkinsfile and GitHub Actions workflows have been updated and tested on a fork. See `plan21.md` for full details, `steps21.md` for test results.

## What changes in the Jenkinsfile

The Jenkinsfile on `gh-pages` (which Jenkins monitors) will be updated automatically by the publish workflow. Key differences:

- **`PRODUCTION_VERSIONS = '20.0'`** replaces `DOCSVERSION = '20.0'`. Deploy/backup/verify stages now loop over this space-separated list instead of hardcoding `20.0`.
- **`TRUNK_VERSION = '21.0'`** — controls SVN path routing (see below).
- **`getVersionedReleaseAssets()`** — new local function replacing `ghGetReleaseAssets()` from the shared library. Filters GitHub releases by version tag prefix (`v20.0.*`, `v21.0.*`) so each version gets its own assets. Same auth pattern (`getCredentialsId('github')`), same `buildinfo.json` output.
- SVN paths are now computed per-version via helper functions instead of hardcoded env vars.

## SVN: nothing to do right now

v21 is the current development version, so it reads from trunk — same paths Jenkins already uses:
- `docbin/trunk/documentation`
- `dyalog/trunk/svn/docs/readmes`

v20.0 reads from branches (already exist):
- `docbin/branches/20.0/documentation`
- `dyalog/branches/20.0/svn/docs/readmes`

**Future action (when v21 releases and v22 development starts):**
Create these SVN branches before updating `TRUNK_VERSION` to `22.0`:
- `docbin/branches/21.0/documentation`
- `dyalog/branches/21.0/svn/docs/readmes`

## gitdocs2svn

The `gitdocs2svn` script in `Dyalog/JenkinsBuild` currently handles a single version. With multi-version support, release assets are now downloaded per-version into `git_docs/{version}/` and SVN checkouts go into `svn_docs/{version}/`.

Options:
1. **Simplest**: leave `gitdocs2svn` as-is, limit `PRODUCTION_VERSIONS` to `'20.0'` until the script is updated. v21 still publishes to GitHub Pages staging; it just won't go through the SVN update path.
2. **When ready**: update `gitdocs2svn` to accept a version parameter or loop over versions. The directory structure is already set up.

## What we don't need from IT

- No Jenkins job configuration changes — the Jenkinsfile is self-contained on `gh-pages`
- No new credentials — uses existing `github` and `svn` credential IDs
- No infrastructure changes — same agents, same Docker image, same swarm

## Risk

The deploy stage now verifies source directories exist before touching production. If a version directory is missing from `gh-pages`, it skips rather than wipes. The `.rsync-exclude` also blocks `21.0` as a backstop.

Rollback: revert `gh-pages` Jenkinsfile to previous commit. The old single-version logic is one `git revert` away.

## Questions for IT

1. Can you confirm `docbin/branches/20.0/documentation` and `dyalog/branches/20.0/svn/docs/readmes` exist in SVN? (They should — v20 is the current release.)
2. Any concerns with the `getVersionedReleaseAssets` function replacing `ghGetReleaseAssets` for this pipeline? It uses the same credential ID and auth flow.
3. Timeline for `gitdocs2svn` multi-version support — or are you happy to defer?
