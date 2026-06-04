# Release Runbook

Operator procedures for publishing the documentation to staging and to the
live site. This is the durable, version-agnostic companion to
[`README.md`](README.md) (which describes the Jenkins pipeline architecture).
The version-specific `plan21.md` / `steps21.md` are kept only as a historical
record of the original v20/v21 split — **use this file for day-to-day
releases.**

Throughout, **N** is the *development* version that lives on `main` (currently
`21.0`) and **M** is the *current released* version that lives on its own
maintenance branch (currently `20.0` on branch `v20.0`). Substitute the real
numbers for the cycle you are in.

---

## How it fits together

| Layer | Where | Holds |
|-------|-------|-------|
| Source | `main` branch | Version **N** (the upcoming/development version), `version_majmin` in `mkdocs.yml` |
| Source | `vM.0` branch | Version **M** (the current released version) |
| Staging | `gh-pages` branch | Every version that `mike` has deployed — visible at `dyalog.github.io/documentation/<ver>/` |
| Production | `docs.dyalog.com` | Only the versions Jenkins is told to deploy |

Two stages, two different gates:

1. **`mike` → `gh-pages`** is driven by the GitHub Action
   [`mkdocs-publish.yml`](../../.github/workflows/mkdocs-publish.yml). Anything
   you publish lands on staging. Publishing **N** here never touches
   production.
2. **`gh-pages` → `docs.dyalog.com`** is driven by Jenkins
   ([`Jenkinsfile`](Jenkinsfile)). Jenkins deploys **only** the versions listed
   in `PRODUCTION_VERSIONS`, so a version can sit on staging indefinitely
   without reaching the live site.

This decoupling is the key fact: **what is on `main` and what is live are
controlled independently.** You do not need a git/SVN branch for a version to
publish it to the live site — see [Procedure C](#c-publish-the-upcoming-version-to-live-as-a-preview).

### Control points

| Control | File (on `main`) | Effect |
|---------|------------------|--------|
| `PRODUCTION_VERSIONS` | `Jenkinsfile` | Space-separated list of versions Jenkins deploys to `docs.dyalog.com`. **The production gate.** |
| `TRUNK_VERSION` | `Jenkinsfile` | Which version maps to the SVN *trunk* (vs `branches/<ver>/`). Equals **N** while N is in development. |
| `.rsync-exclude` | `.rsync-exclude` | Defence-in-depth backstop. A version listed here is skipped by `rsync` even if it is in `PRODUCTION_VERSIONS`. |
| `set_as_latest` | workflow input | When ticked, `mike` repoints the default/`latest` alias (and the root redirect) to the version being published. |
| GitHub release `v<ver>.*` | (GitHub Releases) | Jenkins' `getVersionedReleaseAssets` downloads the release assets from the newest non-draft release whose tag starts `v<ver>.` (CHM for all versions; PDFs only on v20 and earlier). |

> The `Jenkinsfile` and `.rsync-exclude` that Jenkins actually runs live at the
> root of `gh-pages`, and [`mkdocs-publish.yml`](../../.github/workflows/mkdocs-publish.yml)
> copies them there **from `origin/main`** on every publish. So always edit
> these on `main`, and they take effect on the next publish — regardless of
> which branch triggered it.

---

## A. Publish a maintenance update (released version M)

Routine update to the version that is already live and the default.

1. Merge the content PR into the `vM.0` branch.
2. Publish from `vM.0`. Leave `set_as_latest` **ticked only if M is still the
   default** (normally yes, until N is promoted):
   - If the PDF/CHM assets changed, run **Full Release**. It rebuilds the
     assets, publishes them as a non-draft GitHub release, and republishes the
     site in one run.
   - If only content changed, run **Publish MkDocs Documentation** (leave
     `version_override` empty, auto-detected as `M`) to republish the site
     against the existing release assets.
3. Jenkins deploys to `docs.dyalog.com/M/` because **M** is in
   `PRODUCTION_VERSIONS`.

---

## B. Publish the upcoming version (N) to staging only

For review on GitHub Pages without any production exposure.

1. Merge the content PR into `main`.
2. Run **Publish MkDocs Documentation** from `main`:
   - `version_override` empty (auto-detected as **N**);
   - `set_as_latest` **unticked**.
3. Result: `dyalog.github.io/documentation/N/` updates. Jenkins runs but does
   **not** deploy N (it is not in `PRODUCTION_VERSIONS`), so `docs.dyalog.com`
   is untouched.

---

## C. Publish the upcoming version (N) to live as a preview

Make **N** reachable at `docs.dyalog.com/N/` for early access, while **M**
remains the default. **No `vN.0` git or SVN branch is required** — N stays on
`main` as the trunk/development version.

**Prerequisites**

- A **non-draft** GitHub release tagged `vN.*` exists with the CHM asset.
  Without it, Jenkins' `getVersionedReleaseAssets` aborts the build with
  `No release found matching vN.*`. Produce one via **Full Release** from
  `main` and publish it.
- The SVN trunk docbin (`docbin/trunk/documentation`) is fully populated for N
  — `filelist.txt`, `theme/`, plus the sharpplot and readmes checkouts. The
  `Get files from svn/docbin` stage bails if the filelist and checkout disagree.
  (`get_svn_docbin` itself is version-agnostic; this is a content check.)

**Steps** (on `main`)

1. Add N to the production gate in `Jenkinsfile`:
   ```groovy
   PRODUCTION_VERSIONS = 'M N'      // e.g. '20.0 21.0'
   ```
2. Remove the `N` line from `.rsync-exclude` (otherwise the `rsync` filter
   skips the directory even though it is listed for deployment).
3. Run **Publish MkDocs Documentation** (or **Full Release**) from `main` with
   `set_as_latest` **unticked**. This pushes `N/` to `gh-pages` and copies the
   updated `Jenkinsfile` + `.rsync-exclude` to `gh-pages`.
4. Jenkins now deploys `docs.dyalog.com/N/`.

**What "preview" gets you for free:** because `set_as_latest` is off, `mike`
does not change the default — `docs.dyalog.com/` keeps redirecting to **M** and
the root redirect is untouched. You avoid the root-redirect handling that a
full release needs (see [Procedure D](#d-promote-the-upcoming-version-to-full-production)).

**Caveats**

- **Dropdown / discoverability:** the deploy stage only syncs version
  directories, *not* the root `versions.json` that the `mike` version selector
  reads on production. So the preview works by **direct URL** (`/N/`) but does
  not appear in the version dropdown on the live site unless the production-root
  `versions.json` is updated separately.
- **Reversible:** to pull the preview, revert `PRODUCTION_VERSIONS`, restore the
  `N` line in `.rsync-exclude`, and on the server
  `rm -rf N/ && rm .git-hash` (removing `.git-hash` forces Jenkins to redeploy;
  otherwise it sees "no changes" and skips).

---

## D. Promote the upcoming version (N) to full production

When N becomes the released default. Builds on [Procedure C](#c-publish-the-upcoming-version-to-live-as-a-preview)
(N is already, or now becomes, part of `PRODUCTION_VERSIONS`).

1. Produce the final GitHub release for `vN.*` (non-draft).
2. Ensure `PRODUCTION_VERSIONS` contains both `M` and `N`, and that
   `.rsync-exclude` no longer lists `N`.
3. Run **Publish MkDocs Documentation** from `main` with `set_as_latest`
   **ticked**. `mike` repoints `latest` and the root redirect on `gh-pages` to
   `N/`.
4. **Deploy the root redirect to production.** The deploy stage only syncs
   version directories, so the root files (`index.html`, `versions.json`,
   `latest/`) are **not** deployed automatically. Either extend the deploy
   stage to also sync the root-level files from `gh-pages`, or update the
   redirect / `versions.json` on the production server manually.
5. Verify: `docs.dyalog.com/N/` is live, `docs.dyalog.com/` redirects to N, and
   the version dropdown shows both M and N.

---

## E. Start the next development cycle (rotation)

When N is released and N+1 development begins. This is the heavyweight
"branching" step — do it only at this point, not for a preview.

1. Cut a maintenance branch `vN.0` from `main` (freezes N's content). On that
   branch, quote `version_majmin: "N"` and change the submodule update in
   `mkdocs-publish.yml` from `--remote` to `--init` to pin its assets.
2. On `main`, bump `mkdocs.yml` to N+1 (`version_maj`, `version_majmin` quoted,
   `version_condensed`).
3. In `Jenkinsfile`, set `TRUNK_VERSION = 'N+1'`. The SVN helpers then resolve
   N+1 to trunk and N to `branches/N/`.
4. **Before** this switch, the SVN branches for the now-released N must exist:
   `docbin/branches/N/documentation` and `dyalog/branches/N/svn/docs/readmes`.
5. Add `N+1` to `.rsync-exclude` as the new development version's backstop.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Jenkins: `No release found matching v<ver>.*` | No non-draft GitHub release for that version | Publish a `v<ver>.*` release (not draft) |
| Jenkins `get_svn_docbin` bails: `SVN includes files that are not in ./filelist.txt` (lists a file) | A file was added to that version's SVN docbin but not to its `filelist.txt` (common on `trunk` when promoting the dev version) | Add the listed file to `filelist.txt` in the version's docbin (`docbin/trunk/documentation` for the trunk version, `docbin/branches/<ver>/documentation` otherwise) as a **tab-separated** line, e.g. `./File.pdf<TAB>web` (`web` = publish; non-`web` = keep out of the site). Commit to SVN, then re-run the build. |
| Jenkins `get_svn_docbin` bails: `filelist.txt includes files which are not in SVN` (lists a file) | `filelist.txt` references a file that was removed from the docbin | Remove the stale entry from `filelist.txt` (or restore the file in SVN). Commit, then re-run the build. |
| Version deployed but missing from live dropdown | Production-root `versions.json` not synced (expected for previews) | Update root `versions.json` on the server, or promote via [Procedure D](#d-promote-the-upcoming-version-to-full-production) |
| Version published to staging but not live | Not in `PRODUCTION_VERSIONS`, or still listed in `.rsync-exclude` | Add to `PRODUCTION_VERSIONS` / remove from `.rsync-exclude` on `main`, then publish |
| Fixed config but Jenkins still skips deploy | `.git-hash` on server matches last commit ("no changes") | `rm .git-hash` in `WEB_ROOT` to force redeploy |
