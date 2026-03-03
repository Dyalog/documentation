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

## Phase 3: Fork Testing (complete)

### Test 3: Publish v20 from v20.0 branch — PASSED
Run ID: 22628673123 (27m52s, success)
- Version auto-detected as 20.0 — `Using mkdocs.yml version: 20.0`
- Mike deployed 20.0/ to gh-pages
- Jenkinsfile on gh-pages sourced from `origin/main` — confirmed `PRODUCTION_VERSIONS = '20.0'`, `TRUNK_VERSION = '21.0'`, all helper functions present
- Jenkins files committed to gh-pages as `e130526`
- Site: https://xpqz.github.io/dyalog-docs/20.0/

### Test 4: Publish v21 from main — PASSED
Run ID: 22630553925 (27m33s, success)
- Version auto-detected as 21.0 — `Using mkdocs.yml version: 21.0`
- Mike deployed 21.0/ alongside 20.0/ on gh-pages
- `versions.json` shows both: `21.0` and `20.0` (20.0 retains `latest` alias, correct)
- Site: https://xpqz.github.io/dyalog-docs/21.0/

### Test 5: Jenkins simulation — PASSED
Run ID 22632056281 (56s, success): `production_versions: "20.0"`
- Processed 20.0 only → Deployed 1 version

Run ID 22632116644 (1m3s, success): `production_versions: "20.0 21.0"`
- Processed 20.0 + 21.0 → Deployed 2 versions

### Test 6: Offline build — PASSED
Run ID: 22632414277 (28m54s, success)
- Draft release created: `v21.0.1187`
- Asset: `documentation-21.0-offline.zip` (153MB)
- Download and verify offline viewing manually if desired

### Test 7: Concurrency
Skipped (non-critical). The concurrency group is configured; behaviour is standard GitHub Actions.

---

## Summary

All implementation and fork testing is complete. The `v21-branch-strategy` branch contains all file changes. Tests 3–6 passed on the xpqz/dyalog-docs fork, confirming:

- Version auto-detection works from both branches
- Both versions coexist on gh-pages (`versions.json` lists 20.0 and 21.0)
- Jenkins files on gh-pages are always sourced from `origin/main`
- The PRODUCTION_VERSIONS deploy loop correctly filters versions
- The offline build produces a versioned zip in a draft release

### What's been built

| File | Change |
|------|--------|
| `mkdocs-publish.yml` | Auto-detects version from `mkdocs.yml`, concurrency group, `set_as_latest` option, Jenkins files always sourced from `origin/main` |
| `Jenkinsfile` | `PRODUCTION_VERSIONS` / `TRUNK_VERSION`, version-aware SVN paths, `getVersionedReleaseAssets` (replaces shared library call), per-version deploy loop with source verification |
| `.rsync-exclude` | `21.0` exclusion as defence-in-depth |
| `mkdocs-offline.yml` | New offline zip workflow for v21+ (replaces CHM/PDF on main) |
| `mkdocs-pdf.yml` | Offline bundle option added (from earlier chm-replacement work) |
| `mkdocs.yml` | Offline plugin added |

---

## Phase 4: Go Live (pending)

### On Dyalog/documentation

1. **Merge `v21-branch-strategy` into `main`** — PR review, then merge
2. **Create `v20.0` branch from `main`** (before or after merge, same as fork test)
3. **On `main`**: bump version to 21.0, quote `version_majmin`
4. **On `v20.0`**: quote `version_majmin` as `"20.0"`, change submodule update to `--init`
5. **Publish v20 from `v20.0`** — first real publish using new workflow
6. **Publish v21 from `main`** — appears on GitHub Pages staging only

### Outside this repo

- **`gitdocs2svn`** (in Dyalog/JenkinsBuild): may need a version parameter or loop to handle per-version SVN paths. Not a blocker for initial deployment — the `Update svndocs` stage can be limited to v20 initially.
- **SVN branches**: no new SVN branches needed for v21 (it uses trunk). When v21 is eventually released and v22 starts, `docbin/branches/21.0/` and `dyalog/branches/21.0/` must exist before updating `TRUNK_VERSION`.

### When v21 goes to production

1. Change `PRODUCTION_VERSIONS = '20.0'` → `'20.0 21.0'` in Jenkinsfile
2. Remove `21.0` from `.rsync-exclude`
3. Publish from main with `set_as_latest` checked
4. Handle root redirect (`index.html` on production) — either extend deploy stage or manual step
