## v21 Documentation: Branch Strategy

We need to start v21 documentation work while continuing to maintain the v20 docs. The goal is to let both versions coexist: v20 updates continue to flow to docs.dyalog.com as before, while v21 content is visible on GitHub Pages for internal review but does not appear on the production site until we're ready.

### What changes for authors

The documentation repo gets a new `v20.0` branch. Going forward:

- **v20 maintenance** (bug fixes, clarifications) → PR against `v20.0`
- **v21 new content** → PR against `main`

Publishing works the same way (manual dispatch in GitHub Actions), but the version is now auto-detected from `mkdocs.yml` — no need to type it in, no risk of publishing the wrong version from the wrong branch.

### What changes on the infrastructure side

The Jenkinsfile gains a `PRODUCTION_VERSIONS` variable (initially set to `'20.0'`). Jenkins only deploys the versions in that list. When v21 is ready for production, we add `'21.0'` to the list — that's the only change needed.

SVN paths are now computed per-version following the existing trunk/branches convention. v21 reads from trunk (same as today); v20 reads from its branches. No new SVN branches are needed right now.

The `gitdocs2svn` script is unchanged — the Jenkinsfile calls it once per version with the right environment variables.

Details of what's changing in the Jenkinsfile and what (little) we need from IT are in the attached `it.md`.

### What changes for offline documentation

Starting with v21, we're replacing CHM and PDF generation with a single offline zip built using MkDocs' offline plugin. The v20.0 branch retains the existing CHM/PDF workflow.

### What's been tested

All workflows have been tested end-to-end on a fork (see `steps21.md`). Version auto-detection, multi-version publishing, selective deployment, and the offline build all passed. The only thing not tested is the actual Jenkins pipeline against live infrastructure — the changes are designed to be safe (source verification before deployment, defence-in-depth exclusions) and trivially reversible.

### Next steps

1. Review the attached documents
2. Coordinate with IT (the `it.md` attachment covers this — it's minimal)
3. Merge and set up branches on the real repo
4. First publish from both branches to verify
