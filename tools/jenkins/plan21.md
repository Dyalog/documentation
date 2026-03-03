# Plan: v21 Documentation Branch Strategy

This document describes the concrete steps to enable parallel development of v20.0 (maintenance) and v21.0 (new development) documentation, with v21 visible only on GitHub Pages staging until production release.

Executive summary at the end.
---

## Current State

### Documentation Repository Structure
- `main` contains v20.0 documentation
- `gh-pages` is the built site with mike versioning, monitored by Jenkins

### Action Workflows
| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `mkdocs-pdf.yml` | Manual dispatch | Generates PDF/CHM, creates draft GitHub release |
| `mkdocs-publish.yml` | Manual dispatch (version param) | Runs `mike deploy --push <version>` |

### Jenkins Behaviour
- Monitors `gh-pages` branch
- Deploys all content from `gh-pages` to `docs.dyalog.com`
- Hardcoded `DOCSVERSION = '20.0'` for SVN file fetching

Jenkins deploys everything on `gh-pages`, meaning if we publish v21 via `mike`, it would immediately appear on production.

The Dyalog Jenkins utility library can be found in https://git.bramley.dyalog.com/Systems/Jenkins-Library

---

## Target State

| Version | Source Branch | Staging (GitHub Pages) | Production (docs.dyalog.com) |
|---------|---------------|------------------------|------------------------------|
| 20.0 | `v20.0` | Visible | Visible |
| 21.0 | `main` | Visible | Not visible (until release) |

---

## Implementation

### Step 1: Create v20.0 Maintenance Branch

```bash
git switch main
git pull origin main
git switch -c v20.0
git push -u origin v20.0
```

Branch `v20.0` created, identical to current `main`.

---

### Step 2: Update `main` Branch for v21

In `mkdocs.yml` (on `main` branch only), change:
```yaml
extra:
  version_maj: 20
  version_min: 0
  version_majmin: 20.0
  version_condensed: 200
```

To (note: values must be quoted strings to prevent YAML number coercion):
```yaml
extra:
  version_maj: 21
  version_min: 0
  version_majmin: "21.0"
  version_condensed: 210
```

Quote `version_majmin` as a string. YAML parsers (including `yq`) treat unquoted `20.0` as a float and may drop the trailing `.0`, resulting in `20` instead of `20.0`. This might cause mike to deploy to `/20` instead of `/20.0`.

Also update `v20.0` branch to quote the value:
```yaml
  version_majmin: "20.0"
```

Additional changes on `main`:
- Create `release-notes-21/` directory structure (or update existing)

---

### Step 3: Modify `.github/workflows/mkdocs-publish.yml`

**This is important**: auto-detect version from `mkdocs.yml` to prevent human error.

Replace the entire file with:

```yaml
name: Publish MkDocs Documentation

on:
  workflow_dispatch:
    inputs:
      version_override:
        description: 'Version override (leave empty to use mkdocs.yml value)'
        required: false
        default: ''
        type: string
      set_as_latest:
        description: 'Set this version as the default/latest'
        required: false
        default: false
        type: boolean

permissions:
  contents: write
  pages: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
      with:
        submodules: recursive
        fetch-depth: 0

    - name: Update Assets
      run: git submodule update --remote --recursive documentation-assets

    - name: Install yq
      run: |
        sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
        sudo chmod +x /usr/local/bin/yq

    - name: Determine Version
      id: version
      run: |
        if [ -n "${{ inputs.version_override }}" ]; then
          VERSION="${{ inputs.version_override }}"
          echo "Using override version: ${VERSION}"
        else
          # Use -r for raw output (no quotes) and ensure string format
          VERSION=$(yq -r '.extra.version_majmin | tostring' mkdocs.yml)
          # Validate version format (X.Y)
          if ! echo "${VERSION}" | grep -qE '^[0-9]+\.[0-9]+$'; then
            echo "ERROR: Invalid version format '${VERSION}'. Expected X.Y (e.g., 20.0, 21.0)"
            exit 1
          fi
          echo "Using mkdocs.yml version: ${VERSION}"
        fi
        echo "VERSION=${VERSION}" >> $GITHUB_OUTPUT

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Set up Git
      run: |
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@users.noreply.github.com"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install \
          mike \
          mkdocs-material \
          mkdocs-macros-plugin \
          mkdocs-monorepo-plugin \
          mkdocs-site-urls \
          mkdocs-caption \
          markdown-tables-extended \
          mkdocs-minify-plugin

    - name: Get Git Info
      id: git-info
      run: |
        BRANCH=$(git rev-parse --abbrev-ref HEAD)
        HASH=$(git rev-parse --short HEAD)
        echo "GIT_INFO=${BRANCH}:${HASH}" >> $GITHUB_OUTPUT
        echo "DATE=$(date +'%Y-%m-%d')" >> $GITHUB_OUTPUT
        echo "CURRENT_YEAR=$(date +'%Y')" >> $GITHUB_OUTPUT

    - name: Substitute env variables in mkdocs.yml
      env:
        GIT_INFO: ${{ steps.git-info.outputs.GIT_INFO }}
        BUILD_DATE: ${{ steps.git-info.outputs.DATE }}
        CURRENT_YEAR: ${{ steps.git-info.outputs.CURRENT_YEAR }}
      run: |
        cp mkdocs.yml mkdocs.yml.bak
        envsubst '$BUILD_DATE $GIT_INFO $CURRENT_YEAR' < mkdocs.yml.bak > mkdocs.yml
        echo "--- Checking substituted content ---"
        cat mkdocs.yml | grep -A5 copyright

    - name: Move Styles into docs
      run: |
        mv documentation-assets docs

    - name: Deploy documentation
      run: |
        VERSION="${{ steps.version.outputs.VERSION }}"
        if [ "${{ inputs.set_as_latest }}" = "true" ]; then
          mike deploy --push --update-aliases ${VERSION} latest
          mike set-default --push latest
        else
          mike deploy --push ${VERSION}
        fi

    - name: Copy Jenkins files to gh-pages
      run: |
        git checkout -- mkdocs.yml
        git checkout gh-pages
        git checkout ${{ github.sha }} -- tools/jenkins/Jenkinsfile tools/jenkins/service.yml tools/jenkins/.rsync-exclude tools/jenkins/get_svn_docbin
        mv tools/jenkins/Jenkinsfile .
        mv tools/jenkins/service.yml .
        mv tools/jenkins/.rsync-exclude .
        mv tools/jenkins/get_svn_docbin .
        git rm -r tools
        git add Jenkinsfile service.yml .rsync-exclude get_svn_docbin
        if git diff --staged --quiet; then
          echo "No changes to Jenkins files"
        else
          git commit -m "Update Jenkins deployment files"
          git push origin gh-pages
        fi
```

Key changes:
1. Version auto-detected from `mkdocs.yml` using `yq -r ... | tostring` to handle both quoted and unquoted values
2. Validation step ensures version matches `X.Y` format before proceeding
3. Optional `version_override` parameter for edge cases
4. Optional `set_as_latest` to control mike aliases

---

### Step 4: Modify `tools/jenkins/Jenkinsfile`

Goal: Only deploy specified versions to production, ignoring others on `gh-pages`.

Replace the entire `environment` block (lines 32-47) with:

```groovy
    environment {
        GITHUB_REPO     = 'https://github.com/dyalog/documentation.git'
        WEB_ROOT        = '/DockerVolumes/websites/docs.dyalog.com/'
        WEB_URL         = 'docs.dyalog.com'
        HASH_SAME       = 'unknown'
        SWARM_NAME      = "docsweb"

        // ============================================================
        // PRODUCTION_VERSIONS: Space-separated list of versions to deploy
        // Add '21.0' when v21 is ready for production release
        // ============================================================
        PRODUCTION_VERSIONS = '20.0'

        // The "development" version currently on trunk in SVN.
        // When v21 is released and v22 development starts, update this to '22.0'.
        TRUNK_VERSION = '21.0'

        GITDOCURL       = 'documentation'

        // Version-agnostic SVN paths
        SVNSHARPPLOTURL = "dyalogtools/Causeway/trunk/release"

        SVNDOCDIR       = 'svn_docs'
        GITDOCDIR       = 'git_docs'
    }
```

Add helper functions at the top of the pipeline (after `def hashSame = null`):

```groovy
// Per-version SVN path configuration.
// Convention: trunk is always the current development version;
// released versions live under branches/{version}/.

def getSvnDocbinUrl(String version) {
    if (version == env.TRUNK_VERSION) {
        return "docbin/trunk/documentation"
    }
    return "docbin/branches/${version}/documentation"
}

def getSvnReadmeUrl(String version) {
    return "dyalog/branches/${version}/svn/docs/readmes"
}
```

**SVN prerequisites:** `dyalog/branches/21.0/svn/docs/readmes` does not yet exist in SVN and must be created before v21 goes to production. This is not a blocker for the initial branch setup (v21 is staging-only and Jenkins skips non-production versions), but it must be in place before adding `21.0` to `PRODUCTION_VERSIONS`.

Replace the `Get files from svn/docbin etc` stage (lines 117-129) with:

```groovy
                stage('Get files from svn/docbin etc') {
                    steps {
                        script {
                            def versions = env.PRODUCTION_VERSIONS.split(' ')
                            versions.each { version ->
                                dir("${version}/files") {
                                    deleteDir()
                                }
                                dir("${version}") {
                                    doSvnCheckout(getSvnDocbinUrl(version), "files", true, 'svncom')
                                    doSvnCheckout(env.SVNSHARPPLOTURL, "files/sharpplot", true, 'svncom')
                                    doSvnCheckout(getSvnReadmeUrl(version), "files/readmes", true, 'svncom')
                                    sh "\$WORKSPACE/get_svn_docbin ${version}"
                                }
                            }
                        }
                    }
                }
```

Each version now fetches from its own SVN paths:

| Version | `docbin` | `readmes` | `sharpplot` |
|---------|----------|-----------|-------------|
| 20.0 | `docbin/branches/20.0/documentation` | `dyalog/branches/20.0/svn/docs/readmes` | `dyalogtools/Causeway/trunk/release` (shared) |
| 21.0 | `docbin/trunk/documentation` | `dyalog/branches/21.0/svn/docs/readmes` | `dyalogtools/Causeway/trunk/release` (shared) |

The `TRUNK_VERSION` environment variable controls which version maps to trunk. When v21 is released and v22 development begins, update `TRUNK_VERSION` to `'22.0'` and the paths will automatically adjust.

Replace the `Deploy site` stage (lines 235-289) with:

```groovy
                stage('Deploy site') {
                    when {
                        expression { hashSame == false }
                    }
                    options {
                        lock('docs-deploy')
                    }
                    steps {
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Starting deployment to ${WEB_ROOT}."

                            if [ -z "${WEB_ROOT}" ]; then
                                echo "ERROR: WEB_ROOT NOT SET"
                                exit 1
                            fi

                            # Create WEB_ROOT if it doesn't exist
                            if [ ! -d "${WEB_ROOT}" ]; then
                                mkdir -p "${WEB_ROOT}"
                            fi

                            # Track deployment success
                            DEPLOYED_COUNT=0

                            # Deploy only PRODUCTION_VERSIONS
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                echo "Processing version: ${VERSION}"

                                # CRITICAL: Verify source exists before touching production
                                if [ ! -d "${WORKSPACE}/${VERSION}" ]; then
                                    echo "  ERROR: Source ${WORKSPACE}/${VERSION} does not exist!"
                                    echo "  This version may not have been published to gh-pages."
                                    echo "  Skipping to avoid wiping production."
                                    continue
                                fi

                                if [ ! -f "${WORKSPACE}/${VERSION}/index.html" ]; then
                                    echo "  ERROR: ${WORKSPACE}/${VERSION}/index.html missing!"
                                    echo "  Source appears incomplete. Skipping to avoid corruption."
                                    continue
                                fi

                                # Source verified - safe to deploy
                                echo "  Source verified, deploying..."

                                # Clear existing version directory (only now that source is verified)
                                if [ -d "${WEB_ROOT}/${VERSION}" ]; then
                                    rm -rf "${WEB_ROOT}/${VERSION:?}"/*
                                fi

                                # Sync this version
                                rsync -rl --delete --exclude-from="${WORKSPACE}/.rsync-exclude" "${WORKSPACE}/${VERSION}" "${WEB_ROOT}"
                                echo "  Deployed ${VERSION} successfully"
                                DEPLOYED_COUNT=$((DEPLOYED_COUNT + 1))
                            done

                            # Only update git hash if at least one version was deployed
                            if [ $DEPLOYED_COUNT -eq 0 ]; then
                                echo "ERROR: No versions were deployed! Not updating .git-hash"
                                exit 1
                            fi

                            # Update git hash
                            echo "Storing new git hash (${LATEST_HASH})."
                            echo "${LATEST_HASH}" | tee "${WEB_ROOT}/.git-hash" >/dev/null

                            echo "Deployment completed successfully. Deployed ${DEPLOYED_COUNT} version(s)."
                        '''
                        script {
                            env.DEPLOYMENT_EXECUTED = 'true'
                        }
                    }
                    post {
                        failure {
                            echo "ERROR: Deployment failed at ${env.WEB_ROOT}"
                        }
                    }
                }
```

Safety:

1. Verifies source directory exists AND contains `index.html` before touching production
2. Only deletes production directory after source verification passes
3. Tracks deployment count; fails if zero versions deployed (prevents `.git-hash` update masking failure)
4. Uses `${VERSION:?}` in `rm` to prevent catastrophic deletion if `VERSION` is somehow empty

Replace the `Verify deployment` stage (lines 291-315) with:

```groovy
                stage('Verify deployment') {
                    when {
                        expression { hashSame == false }
                    }
                    steps {
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Verifying deployment at ${WEB_ROOT}..."

                            FAILED=0
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                if ! test -f "${WEB_ROOT}/${VERSION}/index.html"; then
                                    echo "ERROR: ${VERSION}/index.html not found"
                                    FAILED=1
                                else
                                    echo "  ${VERSION}/index.html OK"
                                fi
                            done

                            if [ $FAILED -eq 1 ]; then
                                exit 1
                            fi

                            echo "Deployment verified successfully."
                            echo "Site location: ${WEB_ROOT}"
                            echo "Deployed Git hash: $(cat "${WEB_ROOT}/.git-hash" 2>/dev/null || echo 'unknown')"
                        '''
                    }
                    post {
                        failure {
                            echo "ERROR: Deployment verification failed - site may be in inconsistent state"
                        }
                    }
                }
```

Update the `Backup current site` stage (lines 189-233):

Change the backup command to handle missing directories gracefully:
```groovy
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Backing up current site at ${WEB_ROOT} before deployment."

                            echo "Creating compressed backup: ${BACKUP_FILE}"
                            cd "${WEB_ROOT}"

                            # Build list of existing directories to backup
                            BACKUP_TARGETS=""
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                if [ -d "${VERSION}" ]; then
                                    BACKUP_TARGETS="${BACKUP_TARGETS} ${VERSION}"
                                else
                                    echo "  Note: ${VERSION} does not exist yet, skipping from backup"
                                fi
                            done

                            # Add .git-hash if it exists
                            if [ -f ".git-hash" ]; then
                                BACKUP_TARGETS="${BACKUP_TARGETS} .git-hash"
                            fi

                            # Only create backup if we have something to backup
                            if [ -z "${BACKUP_TARGETS}" ]; then
                                echo "WARNING: Nothing to backup (no existing production versions)"
                                # Create empty marker file so archiveArtifacts doesn't fail
                                touch "${WORKSPACE}/${BACKUP_FILE}.empty"
                            else
                                echo "Backing up:${BACKUP_TARGETS}"
                                tar -czf "${WORKSPACE}/${BACKUP_FILE}" ${BACKUP_TARGETS}
                                BACKUP_SIZE=$(ls -lh "${WORKSPACE}/${BACKUP_FILE}" | awk '{print $5}')
                                echo "Backup created successfully. Size: ${BACKUP_SIZE}"
                            fi

                            cd "${WORKSPACE}"
                        '''
```

---

### Step 5: Update `.rsync-exclude`

File: `tools/jenkins/.rsync-exclude`

Current contents:
```
.git
Jenkinsfile
service.yml
.rsync-exclude
*.tar.gz
get_svn_docbin
```

Add exclusion for non-production versions. Change to:
```
.git
Jenkinsfile
service.yml
.rsync-exclude
*.tar.gz
get_svn_docbin
21.0
```

When v21 goes to production, remove `21.0` from this file.

This exclusion is a safety backstop. The Jenkinsfile changes in Step 4 explicitly deploy only `PRODUCTION_VERSIONS`, so even without this exclusion, v21 would not be deployed. However, defence-in-depth is valuable.

---

## Operational Procedures

### Publishing v20.0 Updates

1. Create PR against `v20.0` branch
2. Merge PR
3. If PDF/CHM updates needed:
   - Go to Actions → "Convert MkDocs to PDF and CHM"
   - Click "Run workflow" → Select branch `v20.0`
   - Wait for completion, then publish the draft release
4. Publish to staging and production:
   - Go to Actions → "Publish MkDocs Documentation"
   - Click "Run workflow" → Select branch `v20.0`
   - Leave version_override empty (will use `20.0` from mkdocs.yml)
   - Leave `set_as_latest` unchecked
5. Jenkins automatically deploys to `docs.dyalog.com`

### Publishing v21.0 to Staging Only

1. Create PR against `main` branch
2. Merge PR
3. Publish to staging:
   - Go to Actions → "Publish MkDocs Documentation"
   - Click "Run workflow" → Select branch `main`
   - Leave version_override empty (will use `21.0` from mkdocs.yml)
   - Leave set_as_latest unchecked
4. Site appears at https://dyalog.github.io/documentation/21.0/
5. Jenkins runs but **does not deploy** 21.0 (not in PRODUCTION_VERSIONS)

### Releasing v21.0 to Production

When v21 is ready for production release:

1. Generate final PDF/CHM:
   - Run `mkdocs-pdf.yml` from `main` branch
   - Publish the GitHub release (not draft)

2. Update Jenkins configuration:
   - Edit `tools/jenkins/Jenkinsfile` on `main` branch
   - Change: `PRODUCTION_VERSIONS = '20.0'`
   - To: `PRODUCTION_VERSIONS = '20.0 21.0'`

3. Update `.rsync-exclude`:
   - Remove `21.0` line

4. Publish and set as default:
   - Run `mkdocs-publish.yml` from `main`
   - Check "Set this version as the default/latest"

5. Verify:
   - https://docs.dyalog.com/21.0/ should now be live
   - Version dropdown should show both 20.0 and 21.0

---

## Testing the Changes

The pipeline can't be run locally as a Jenkins pipeline (it needs the Jenkins agent, Docker swarm, SVN, credential store, etc.), but most of the moving parts can be validated independently.

### 1. GitHub Actions Workflows (local)

The `mkdocs-publish.yml` and offline build workflows can be tested locally since `mkdocs`, `mike`, `yq`, and `gh` are all available in the local venv/homebrew:

```bash
# Activate the docs venv
source docs-venv/bin/activate

# Test version detection (the core of the publish workflow)
VERSION=$(yq -r '.extra.version_majmin | tostring' mkdocs.yml)
echo "Detected version: ${VERSION}"
echo "${VERSION}" | grep -qE '^[0-9]+\.[0-9]+$' && echo "PASS: format valid" || echo "FAIL"

# Test mike deploy (locally, does not push)
mike deploy ${VERSION}
mike list

# Test offline build
OFFLINE=true mkdocs build
ls -lh site/index.html  # verify output exists
(cd site && zip -r ../documentation-${VERSION}-offline.zip .)
ls -lh documentation-${VERSION}-offline.zip

# Test that navigation.instant is removed for offline
yq -i 'del(.theme.features[] | select(. == "navigation.instant"))' mkdocs.yml
grep -c 'navigation.instant' mkdocs.yml  # should be 0

# Clean up
git checkout mkdocs.yml
rm -rf site/ documentation-*-offline.zip
```

### 2. Release Asset Filtering (local)

The `getVersionedReleaseAssets` logic is just `gh` + `jq`. Test the query directly:

```bash
# This is the exact query the Jenkinsfile helper runs
TAG=$(gh release list --repo dyalog/documentation --exclude-drafts \
    --json tagName,createdAt \
    | jq -r '[.[] | select(.tagName | startswith("v20.0."))]
             | sort_by(.createdAt) | last | .tagName')
echo "Latest v20.0 release: ${TAG}"
# Expected: v20.0.1175

# Verify it downloads correctly
mkdir -p /tmp/test-assets
gh release download "${TAG}" --repo dyalog/documentation --dir /tmp/test-assets
ls /tmp/test-assets
rm -rf /tmp/test-assets

# Test that a non-existent version returns null (not an error)
TAG21=$(gh release list --repo dyalog/documentation --exclude-drafts \
    --json tagName,createdAt \
    | jq -r '[.[] | select(.tagName | startswith("v21.0."))]
             | sort_by(.createdAt) | last | .tagName')
echo "Latest v21.0 release: '${TAG21}'"
# Expected: 'null' (no v21 releases yet)
```

### 3. Jenkinsfile Deploy Logic (local simulation)

The deploy stage is a shell script that can be tested against a temporary directory:

```bash
# Simulate the deploy stage locally
export WEB_ROOT=$(mktemp -d)
export PRODUCTION_VERSIONS='20.0'
export WORKSPACE=$(mktemp -d)
export LATEST_HASH=$(git rev-parse HEAD)

# Create a fake 20.0 source
mkdir -p "${WORKSPACE}/20.0"
echo '<html>test</html>' > "${WORKSPACE}/20.0/index.html"

# Create a fake 21.0 source (should NOT be deployed)
mkdir -p "${WORKSPACE}/21.0"
echo '<html>v21</html>' > "${WORKSPACE}/21.0/index.html"

# Run the deploy loop from the plan
DEPLOYED_COUNT=0
for VERSION in ${PRODUCTION_VERSIONS}; do
    if [ ! -d "${WORKSPACE}/${VERSION}" ]; then
        echo "SKIP: ${WORKSPACE}/${VERSION} does not exist"
        continue
    fi
    if [ ! -f "${WORKSPACE}/${VERSION}/index.html" ]; then
        echo "SKIP: index.html missing"
        continue
    fi
    mkdir -p "${WEB_ROOT}/${VERSION}"
    rsync -rl --delete "${WORKSPACE}/${VERSION}/" "${WEB_ROOT}/${VERSION}/"
    echo "Deployed ${VERSION}"
    DEPLOYED_COUNT=$((DEPLOYED_COUNT + 1))
done

# Verify: 20.0 deployed, 21.0 not deployed
echo "--- WEB_ROOT contents ---"
find "${WEB_ROOT}" -type f
# Expected: only 20.0/index.html, no 21.0/

# Clean up
rm -rf "${WEB_ROOT}" "${WORKSPACE}"
```

### 4. Mike Versioning (local)

Test that both versions coexist on gh-pages without interfering:

```bash
source docs-venv/bin/activate

# Deploy v20.0 (from current content)
mike deploy 20.0
mike list  # should show 20.0

# Temporarily tweak version and deploy v21.0
yq -i '.extra.version_majmin = "21.0"' mkdocs.yml
mike deploy 21.0
mike list  # should show 20.0 and 21.0

# Test setting latest alias
mike deploy --update-aliases 21.0 latest
mike set-default latest
mike list  # should show 20.0, 21.0 [latest]

# Clean up: delete test versions from local gh-pages
mike delete 21.0
mike delete 20.0
git checkout mkdocs.yml
```

Note: these `mike` commands modify the local `gh-pages` branch. Do **not** use `--push` during testing.

### 5. End-to-End: GitHub Actions on a Fork

For full integration testing of the workflows before merging:

1. Fork the repo (or use a test branch with a modified workflow trigger)
2. Push the `v21-branch-strategy` branch changes
3. Run `mkdocs-publish.yml` manually → verify mike deploys to gh-pages
4. Run the offline build workflow → verify the draft release contains `documentation-{version}-offline.zip`
5. Verify the Jenkinsfile and `.rsync-exclude` are correctly copied to gh-pages

The Jenkins pipeline itself can only be tested on the actual Jenkins server, but by that point the only untested logic is the `PRODUCTION_VERSIONS` loop and `rsync`, which have been validated locally in step 3.

---

## Rollback Procedures

### If v21 Accidentally Deploys to Production

```bash
# SSH to production server
cd /DockerVolumes/websites/docs.dyalog.com/
rm -rf 21.0/
# Also remove .git-hash to force redeployment on next Jenkins run
rm -f .git-hash
```

Then fix `PRODUCTION_VERSIONS` in Jenkinsfile and trigger a new publish from v20.0 branch.

Removing `.git-hash` is necessary because Jenkins uses it to detect changes. If left in place, Jenkins will see "no changes" and skip deployment even after fixing the config.

### If mike Versioning Breaks

```bash
# Remove problematic version from gh-pages
mike delete 21.0 --push

# Or reset gh-pages entirely (destructive!)
git checkout gh-pages
git reset --hard <known-good-commit>
git push --force origin gh-pages
```

### Revert to Single-Branch Workflow

1. Delete `v20.0` branch
2. Revert mkdocs.yml to 20.0 values
3. Revert Jenkinsfile to original
4. Run `mike delete 21.0 --push`

---

## GitHub Release Strategy for PDF/CHM/Offline Assets

### Problem

The `ghGetReleaseAssets` function in the `dyalog-scripts` shared library (`@Library('dyalog-scripts')`, source at `https://git.bramley.dyalog.com/Systems/Jenkins-Library`) fetches the single "latest" non-draft GitHub release, regardless of version. The actual implementation (from `Library/vars/ghGetReleaseAssets.groovy`):

```groovy
def call(String repository, directory="github_assets") {
    withCredentials([...]) {
        sh('echo ${GITHUB_PASS} | /usr/bin/gh auth login --with-token')
        r=sh(script: """
            ...
            GH_LATEST_RELEASE=\$(gh release list -R \$REPO --exclude-drafts \
                --json name,isPrerelease,isLatest,tagName \
                --jq '.[0] | select(.isLatest)|.tagName')
            if [ "x\$GH_LATEST_RELEASE" = "x" ]; then
                # Fallback: latest prerelease
                GH_LATEST_RELEASE=\$(gh release list -R \$REPO --exclude-drafts \
                    --json name,isPrerelease,isLatest,tagName \
                    --jq '.[0] | select(.isPrerelease)|.tagName')
            fi
            gh release -R \$REPO download -D $WORKSPACE/$directory \$GH_LATEST_RELEASE
            gh release view -R \$REPO --json ... \$GH_LATEST_RELEASE \
                > $WORKSPACE/$directory/buildinfo.json
        """, returnStdout: true).trim()
    }
}
```

Current releases are all tagged `v20.0.*`:
```
v20.0.1175  (latest — assets: dyalog.chm + 8 PDFs)
v20.0.1092
v20.0.1078
...
```

Once v21 releases appear (tagged `v21.0.*`), the latest release will be a v21 offline zip, and v20 production would incorrectly receive it.

### Approach: Local Helper Function in Jenkinsfile

Rather than modifying the shared library (which affects other pipelines), add a local function in the Jenkinsfile that handles version-filtered downloads. This avoids shared library coordination and can be tested independently.

```groovy
/**
 * Download release assets for a specific documentation version.
 * Finds the latest non-draft release whose tag starts with "v{version}."
 * and downloads all assets to the target directory.
 */
def getVersionedReleaseAssets(String repo, String targetDir, String version) {
    withCredentials([
        usernamePassword(
            credentialsId: getCredentialsId('github'),
            usernameVariable: 'GITHUB_USER',
            passwordVariable: 'GITHUB_PASS'
        )
    ]) {
        sh """#!/bin/bash
            set -euo pipefail
            echo "\${GITHUB_PASS}" | /usr/bin/gh auth login --with-token

            REPO="Dyalog/${repo}"
            TAG=\$(gh release list -R "\$REPO" --exclude-drafts \\
                --json tagName,createdAt \\
                | jq -r '[.[] | select(.tagName | startswith("v${version}."))]
                         | sort_by(.createdAt) | last | .tagName')

            if [ -z "\$TAG" ] || [ "\$TAG" = "null" ]; then
                echo "ERROR: No release found matching v${version}.*"
                exit 1
            fi

            echo "Downloading assets from release \$TAG for version ${version}"
            rm -rf "\$WORKSPACE/${targetDir}"
            mkdir -p "\$WORKSPACE/${targetDir}"
            gh release download "\$TAG" -R "\$REPO" -D "\$WORKSPACE/${targetDir}"
            gh release view "\$TAG" -R "\$REPO" \\
                --json apiUrl,author,createdAt,id,isDraft,isPrerelease,name,publishedAt,tagName \\
                > "\$WORKSPACE/${targetDir}/buildinfo.json"
            echo "Downloaded:"
            ls "\$WORKSPACE/${targetDir}"
        """
    }
}
```

This mirrors the authentication and `buildinfo.json` generation from the shared library's `ghGetReleaseAssets`, so downstream stages that read `buildinfo.json` continue to work.

### Jenkinsfile Changes

Replace the current single call:
```groovy
r=ghGetReleaseAssets(GITDOCURL, GITDOCDIR)
```

With a per-version loop in the `Checkout from svndocs` stage:
```groovy
stage('Checkout from svndocs') {
    steps {
        script {
            sh '[ "x" != "x$WORKSPACE" ] && rm -rf $WORKSPACE/*'
            doGitCheckout('JenkinsBuild', 'Jenkins')

            // Fetch release assets for each production version
            def versions = env.PRODUCTION_VERSIONS.split(' ')
            versions.each { version ->
                getVersionedReleaseAssets(GITDOCURL, "${GITDOCDIR}/${version}", version)
            }

            doSvnCheckout(SVNDOCURL, SVNDOCDIR)
        }
    }
}
```

### Version-Specific Assets

| Version | Release tag pattern | Assets downloaded |
|---------|---------------------|-------------------|
| 20.0 | `v20.0.*` | `dyalog.chm`, `*.pdf` |
| 21.0 | `v21.0.*` | `documentation-21.0-offline.zip` |

The `get_svn_docbin` script validates against `filelist.txt` from SVN, so the different asset types don't conflict — each version's assets are in their own directory (`git_docs/20.0/`, `git_docs/21.0/`).

### Future: Shared Library Update

Once the local approach is validated in production, the shared library can optionally be updated with a `tagPattern` parameter for reuse by other pipelines. This is not a blocker.

---

## Documentation Assets Submodule

### Current Setup

The `documentation-assets` submodule (https://github.com/Dyalog/documentation-assets) contains shared CSS and images. Currently:

- Single branch: `main`
- Submodule reference in `.gitmodules` points to the repo without a branch specifier
- The workflow runs `git submodule update --remote --recursive documentation-assets` which always pulls latest from `main`

### Problem

If v20 and v21 need different styles (e.g., v21 has new CSS for new features), pulling "latest" for both versions would give v20 builds potentially broken or inappropriate v21 styles.

### Solution: Pin the v20.0 branch to a specific commit

No version branches needed in `documentation-assets`. The submodule pointer on the `v20.0` documentation branch is simply frozen at the commit that was current when the branch was created. This is the default git submodule behaviour — the recorded commit doesn't change unless someone explicitly updates it.

The key is to **remove `--remote`** from the workflow on the `v20.0` branch. The `--remote` flag overrides the recorded commit and fetches latest from the remote branch, which is exactly what we want to avoid.

**On the `v20.0` documentation branch**, change the workflow step from:
```yaml
- name: Update Assets
  run: git submodule update --remote --recursive documentation-assets
```

To:
```yaml
- name: Update Assets
  run: git submodule update --init --recursive documentation-assets
```

This checks out the exact commit recorded in the submodule pointer, giving v20 a frozen set of styles.

**On `main`**, keep `--remote` so v21 builds always use the latest assets:
```yaml
- name: Update Assets
  run: git submodule update --remote --recursive documentation-assets
```

No changes to `.gitmodules` or the `documentation-assets` repo are required.

---

## Offline Documentation: Replacing CHM and PDF with MkDocs Offline Build

Starting with v21, we are abandoning CHM and PDF generation in favour of Material for MkDocs' built-in offline plugin. This produces a self-contained site that can be downloaded as a zip file and viewed directly in a browser without a server.

The `chm-replacement` branch contains prior work on this: the offline plugin is already integrated into `mkdocs.yml` and the `mkdocs-pdf.yml` workflow has a `generate_offline` input. The changes below build on that foundation.

### What Changes

For v21 onwards:
- The `mkdocs-pdf.yml` workflow on `main` is replaced with a dedicated offline build workflow
- No more CHM compilation or PDF generation from `main`
- The only generated asset is `documentation-{version}-offline.zip`

For v20 maintenance:
- The `mkdocs-pdf.yml` workflow continues to run from the `v20.0` branch
- CHM and PDF releases continue to be published for v20
- Jenkins continues to fetch v20 release assets as before

### Configuration Changes for v21

The `chm-replacement` branch already has the correct plugin setup in `mkdocs.yml`:

```yaml
plugins:
  - privacy      # Downloads external assets for offline use (already present)
  - offline:     # Enables offline site search
      enabled: !ENV [OFFLINE, false]
```

The `privacy` plugin automatically downloads external assets (fonts, scripts) so the offline build is fully self-contained. The `offline` plugin is gated behind the `OFFLINE` environment variable so it does not affect normal site builds or mike deployments.

**Disabling incompatible features for offline builds:**

`navigation.instant` (currently enabled in `mkdocs.yml` line 10) uses fetch API calls that browsers block from `file://` URLs. This must be conditionally disabled when building offline. Options:

1. **Recommended: environment override in mkdocs.yml** — Material for MkDocs does not support `!ENV` toggles on individual theme features. Instead, use a `mkdocs-offline.yml` overlay or a build script that patches the config:
   ```bash
   # In the offline build step, remove navigation.instant before building
   yq -i 'del(.theme.features[] | select(. == "navigation.instant"))' mkdocs.yml
   ```

2. Analytics and version switcher: not currently configured, so no action needed. If added later, they must also be disabled for offline builds.

### Workflow Changes

Replace `mkdocs-pdf.yml` on the `main` branch with a workflow that produces only the offline zip. The `chm-replacement` branch already has the core build step; the changes below adapt it to be the sole asset generator:

```yaml
name: Build Offline Documentation

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-offline:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
      with:
        submodules: recursive
        fetch-depth: 0

    - name: Update Assets
      run: git submodule update --remote --recursive documentation-assets

    - name: Get Git Info
      id: git-info
      run: |
        BRANCH=$(git rev-parse --abbrev-ref HEAD)
        HASH=$(git rev-parse --short HEAD)
        echo "GIT_INFO=${BRANCH}:${HASH}" >> $GITHUB_OUTPUT
        echo "DATE=$(date +'%Y-%m-%d')" >> $GITHUB_OUTPUT
        echo "CURRENT_YEAR=$(date +'%Y')" >> $GITHUB_OUTPUT

    - name: Install yq
      run: |
        sudo wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/v4.44.1/yq_linux_amd64
        sudo chmod +x /usr/local/bin/yq

    - name: Determine Version
      id: version
      run: |
        VERSION=$(yq -r '.extra.version_majmin | tostring' mkdocs.yml)
        if ! echo "${VERSION}" | grep -qE '^[0-9]+\.[0-9]+$'; then
          echo "ERROR: Invalid version format '${VERSION}'. Expected X.Y"
          exit 1
        fi
        echo "VERSION=${VERSION}" >> $GITHUB_OUTPUT

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install \
          mkdocs-material \
          mkdocs-macros-plugin \
          mkdocs-monorepo-plugin \
          mkdocs-site-urls \
          mkdocs-caption \
          mkdocs-minify-plugin

    - name: Build offline site
      env:
        OFFLINE: 'true'
        GIT_INFO: ${{ steps.git-info.outputs.GIT_INFO }}
        BUILD_DATE: ${{ steps.git-info.outputs.DATE }}
        CURRENT_YEAR: ${{ steps.git-info.outputs.CURRENT_YEAR }}
      run: |
        VERSION="${{ steps.version.outputs.VERSION }}"

        # Substitute env variables in mkdocs.yml
        cp mkdocs.yml mkdocs.yml.bak
        envsubst '$BUILD_DATE $GIT_INFO $CURRENT_YEAR' < mkdocs.yml.bak > mkdocs.yml

        # Disable features incompatible with offline viewing
        yq -i 'del(.theme.features[] | select(. == "navigation.instant"))' mkdocs.yml

        mv documentation-assets docs/documentation-assets
        mkdocs build
        cd site && zip -r "../documentation-${VERSION}-offline.zip" .

    - name: Create draft release
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        VERSION="${{ steps.version.outputs.VERSION }}"
        COMMIT_COUNT=$(git rev-list --count HEAD)
        RELEASE_TAG="v${VERSION}.${COMMIT_COUNT}"

        # Clean up old drafts (keep 5)
        MAX_DRAFTS=5
        DRAFTS=$(gh release list --json tagName,isDraft,createdAt \
          --jq '.[] | select(.isDraft==true) | [.tagName,.createdAt] | @tsv' \
          | sort -k2 | awk '{print $1}')
        DRAFT_COUNT=$(echo "$DRAFTS" | grep -c "^" || true)
        if [ $DRAFT_COUNT -gt $MAX_DRAFTS ]; then
          TO_DELETE=$((DRAFT_COUNT - MAX_DRAFTS + 1))
          echo "$DRAFTS" | head -n $TO_DELETE | while read -r tag; do
            gh release delete "$tag" --yes
          done
        fi

        # Handle tag collisions
        TAG="$RELEASE_TAG"
        LETTER="a"
        while gh release view "$TAG" &>/dev/null; do
          TAG="${RELEASE_TAG}${LETTER}"
          LETTER=$(echo "$LETTER" | tr "a-y" "b-z")
        done

        gh release create "$TAG" \
          "documentation-${VERSION}-offline.zip" \
          --draft \
          --title "Documentation Offline ${TAG}" \
          --notes "Offline documentation generated from ${{ steps.git-info.outputs.GIT_INFO }}"
```

Key differences from the `chm-replacement` branch:
1. **Versioned zip filename**: `documentation-{version}-offline.zip` instead of `site.zip`
2. **No PDF/CHM steps or inputs**: this workflow only produces the offline zip
3. **`navigation.instant` removed** via `yq` before building, preventing broken navigation in offline mode
4. **Pinned `yq` version** (`v4.44.1`) instead of fetching latest
5. **Submodule checkout in the actions/checkout step** rather than a separate `git submodule update --init`

### Jenkins Implications

The `ghGetReleaseAssets` modification described earlier still applies. For v21, the release asset is `documentation-{version}-offline.zip` instead of CHM/PDF files. The Jenkins pipeline downloads and deploys this to the `/files` directory just as it does for v20 CHM/PDF files.

The `get_svn_docbin` script may need minor adjustments to handle a single zip file instead of multiple CHM/PDF files.

### Version-Specific Behaviour

| Version | Offline Format | Workflow | Release Assets |
|---------|----------------|----------|----------------|
| 20.0 | CHM + PDF | mkdocs-pdf.yml (on v20.0 branch) | *.chm, *.pdf |
| 21.0 | Offline zip | mkdocs-offline.yml (on main) | documentation-21.0-offline.zip |

This means the shared library changes for version-filtered release assets are essential: v20 must fetch CHM/PDF releases (tagged `v20.0.*`) while v21 fetches zip releases (tagged `v21.0.*`).

---

## Summary

We need to enable parallel maintenance of v20 documentation alongside new v21 development. The core strategy is that v20 content lives on a new v20.0 branch while v21 development continues on main.

The existing GitHub Actions publish workflow is modified to automatically detect the version from the mkdocs configuration file rather than requiring manual input. This prevents accidental cross-version deployments.

The Jenkins pipeline is changed from deploying everything on the gh-pages branch to deploying only explicitly listed production versions. A new environment variable controls which versions are deployed to the live site. Initially this is set to v20 only, meaning v21 can be published to GitHub Pages staging without appearing on the production site. SVN paths are now version-aware: released versions fetch from `docbin/branches/{version}/documentation`, while the current development version fetches from `docbin/trunk/documentation`. A `TRUNK_VERSION` variable controls the trunk mapping. Readmes follow the same pattern via `dyalog/branches/{version}/svn/docs/readmes`; SharpPlot remains on trunk (version-agnostic). The SVN branch `dyalog/branches/21.0/svn/docs/readmes` must be created before v21 goes to production.

The shared Jenkins library function `ghGetReleaseAssets` (in `dyalog-scripts` at `git.bramley.dyalog.com/Systems/Jenkins-Library`) currently fetches the single latest release regardless of version. Rather than modifying the shared library, a local helper function `getVersionedReleaseAssets` is added to the Jenkinsfile. It uses the same `gh` CLI and authentication pattern but filters releases by version tag prefix (e.g., `v20.0.*`), so each version fetches its own assets independently. The shared library can be updated later if other pipelines need the same capability.

The documentation-assets submodule is handled simply: the v20.0 branch pins the submodule to the commit that was current at branch creation by removing the `--remote` flag from the workflow's submodule update step. The main branch continues to pull latest assets. No version branches or `.gitmodules` changes are needed in the assets repo.

Starting with v21, CHM and PDF generation is replaced by a single offline zip bundle (`documentation-{version}-offline.zip`) built using Material for MkDocs' offline plugin. The `chm-replacement` branch contains prior work on this; the plan incorporates and refines it. The v20.0 branch retains the existing `mkdocs-pdf.yml` workflow for CHM/PDF. The offline build disables `navigation.instant` (incompatible with `file://` URLs) via `yq` before invoking `mkdocs build`.

Safety: the deploy stage verifies source directories exist before deleting production content, the backup stage handles missing directories gracefully, and the rsync exclude file provides defence against accidental v21 deployment.

On staging (github pages), v21 becomes the default version immediately upon first publish. On production, the root URL redirect to v21 requires a separate web server configuration change when v21 goes live.
