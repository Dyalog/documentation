# v21 Branch Strategy — Steps Performed

Tracking document for all tasks performed as part of the v21 branch strategy implementation. See `plan21.md` for the full plan.

---

## Phase 1: Implementation (on `v21-branch-strategy` branch)

### 1.1 Rewrite `mkdocs-publish.yml` (Plan Step 3)
- Replaced manual `version` input with auto-detection from `mkdocs.yml` via `yq`
- Added `version_override` optional input for edge cases
- Added `set_as_latest` boolean input (controls mike aliases)
- Added concurrency group (`docs-publish`, cancel-in-progress: false)
- Changed "Copy Jenkins files to gh-pages" to always source from `origin/main` (not the triggering branch)
- Pinned `yq` to v4.44.1

### 1.2 Update `Jenkinsfile` (Plan Step 4)
- Replaced `DOCSVERSION = '20.0'` with `PRODUCTION_VERSIONS = '20.0'` and `TRUNK_VERSION = '21.0'`
- Removed hardcoded `SVNDOCURL` and `SVNREADMEURL` env vars
- Added `getSvnDocbinUrl(version)` helper — trunk for TRUNK_VERSION, branches/{version} otherwise
- Added `getSvnReadmeUrl(version)` helper — same convention
- Added `getVersionedReleaseAssets(repo, targetDir, version)` — replaces `ghGetReleaseAssets`, filters releases by `v{version}.*` tag prefix
- Replaced `Checkout from svndocs` stage with per-version loop
- Replaced `Get files from svn/docbin etc` stage with per-version loop
- Replaced `Deploy site` stage with PRODUCTION_VERSIONS loop, source verification before touching production, deployed-count tracking
- Replaced `Verify deployment` stage with per-version index.html check
- Updated `Backup current site` to backup only PRODUCTION_VERSIONS directories
- Added PRODUCTION_VERSIONS and TRUNK_VERSION to Debug Environment output

### 1.3 Update `.rsync-exclude` (Plan Step 5)
- Added `21.0` line as defence-in-depth against accidental v21 production deployment

### 1.4 Create `mkdocs-offline.yml` workflow
- New dedicated offline build workflow for v21+
- Produces `documentation-{version}-offline.zip`
- Removes `navigation.instant` via `yq` (incompatible with `file://` URLs)
- Creates draft GitHub release with tag `v{version}.{commit_count}`
- Cleans up old drafts (keeps 5)

### 1.5 Commit and push to fork
- Committed as `3889fda` "Implement v21 branch strategy file changes"
- Pushed to `xpqz` remote only (git@github.com:xpqz/dyalog-docs.git)
- Origin (Dyalog/documentation) NOT touched

---

## Phase 2: Fork Setup for Testing

### 2.1 Setup (completed in prior session)
- Added fork as remote: `git remote add xpqz git@github.com:xpqz/dyalog-docs.git`
- Pushed `v21-branch-strategy` branch to fork
- Enabled GitHub Pages on fork (Settings → Pages → source: gh-pages)

### 2.2 Test 1: Baseline v20 publish (completed in prior session)
- Ran `mkdocs-publish.yml` from `main` on fork with version `20.0`
- Populated gh-pages with known-good v20 baseline

### 2.3 Test 2: Create branches and apply changes
- Created `v20.0` branch on fork from current `main` (pre-merge state)
- Merged `v21-branch-strategy` into fork's `main`, then:
  - Bumped version to 21.0 (`version_maj: 21`, `version_majmin: "21.0"`, `version_condensed: 210`)
  - Committed as `7cfc945` "Bump version to 21.0 on main"
- Merged `v21-branch-strategy` into fork's `v20.0`, then:
  - Quoted `version_majmin: "20.0"` (prevent YAML float coercion)
  - Changed submodule update from `--remote` to `--init` (pin v20 assets)
  - Committed as `dec0eaa` "Apply v20-specific tweaks"
- All pushes to `xpqz` remote only

**Fork state after Test 2:**
| Branch | Version | Submodule | Top commit |
|--------|---------|-----------|------------|
| `main` | 21.0 | `--remote` (latest) | `7cfc945` |
| `v20.0` | "20.0" | `--init` (pinned) | `dec0eaa` |
| `v21-branch-strategy` | 20.0 (unchanged) | — | `3889fda` |
| `gh-pages` | — | — | Baseline v20 from Test 1 |

---

## Phase 3: Fork Testing (pending)

### Test 3: Publish v20 from v20.0 branch
_Not yet started._ Run `mkdocs-publish.yml` from `v20.0` on fork. Verify:
- Version auto-detected as 20.0
- Mike deploys 20.0/ to gh-pages
- Jenkinsfile on gh-pages comes from origin/main (has PRODUCTION_VERSIONS)
- Site works at xpqz.github.io/documentation/20.0/

### Test 4: Publish v21 from main
_Not yet started._ Run `mkdocs-publish.yml` from `main` on fork. Verify:
- Version auto-detected as 21.0
- Mike deploys 21.0/ alongside 20.0/ on gh-pages
- versions.json shows both versions
- Site works at xpqz.github.io/documentation/21.0/

### Test 5: Jenkins simulation
_Not yet started._ Run `test-jenkins-simulation.yml` with:
- `production_versions: "20.0"` — should deploy only 20.0
- `production_versions: "20.0 21.0"` — should deploy both

### Test 6: Offline build
_Not yet started._ Run `mkdocs-offline.yml` from `main` on fork. Verify:
- Draft release created with `documentation-21.0-offline.zip`
- Zip contains working offline site

### Test 7: Concurrency
_Not yet started._ Trigger two publishes simultaneously. Confirm queuing.
