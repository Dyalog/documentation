# Contributing to the Dyalog documentation

The documentation repo has two active branches:

- **`main`** — v21 (new content, in development)
- **`v20.0`** — v20 (maintenance)

Your PRs need to target the right one. Pick the scenario that matches your change.

## (1) Fixing something v20-specific

Examples: typo in a v20 release note, broken link in existing v20 content, clarifying a v20-only quirk.

**Shape:** branch from `v20.0`, commit your fix, PR against `v20.0`.

**Via GitHub UI (easiest for small edits):**

1. Before editing, make sure you're viewing the file on the `v20.0` branch (the URL will contain `/blob/v20.0/`, not `/blob/main/`). Use the branch dropdown at the top-left of the file tree to switch.
2. Click the pencil icon, edit, commit to a new branch.
3. The PR form opens. **Check the base branch dropdown — it must be `v20.0`, not `main`.** Submit.

**Via command line:**

```
git checkout v20.0
git pull
git checkout -b fix-typo-v20
# edit files
git add -u && git commit -m "Fix typo in foo.md"
git push -u origin fix-typo-v20
```

On the PR form on GitHub, change the base branch dropdown from `main` to `v20.0` before submitting.

## (2) Fixing something relevant to both v20 and v21

Examples: typo in shared content, fix to an API description that both versions document.

**Shape:** make the change commit on `main` (where v21 development lives), then apply the same commit to `v20.0` via a cherry-pick. Two PRs — one against each branch — and the v20 PR contains the exact commit that was merged to `main`.

**Step 1:** make the change on `main` as in scenario (3). Merge it.

**Step 2:** once step 1 is merged, apply the same commit to `v20.0`:

```
git checkout v20.0
git pull
git checkout -b fix-typo-v20
git cherry-pick <hash-of-the-main-merge-commit>
git push -u origin fix-typo-v20
```

To find the hash: on the merged `main` PR, copy the merge-commit SHA shown in the conversation view. Or run `git log --oneline origin/main -5`.

Then open a PR **against `v20.0`** (remember to change the base branch dropdown).

**If the cherry-pick conflicts** (because v20 content has drifted from v21), either resolve the conflict and continue (`git cherry-pick --continue`), or abort (`git cherry-pick --abort`) and just apply the change manually on a fresh branch from `v20.0`.

## (3) Writing something only for v21

Examples: new feature documentation, new language reference content, anything not relevant to v20.

**Shape:** branch from `main`, PR against `main`. This is the workflow you already know.

```
git checkout main
git pull
git checkout -b feature-xyz
# write content
git add -u && git commit -m "Document feature xyz"
git push -u origin feature-xyz
```

PR base defaults to `main`, so nothing special to set.

## Quick reference

| What you're changing | Branch from | PR base |
|---|---|---|
| v20 only | `v20.0` | `v20.0` |
| Both v20 and v21 | `main` then cherry-pick to `v20.0` | two PRs: one against each |
| v21 only | `main` | `main` |

## Common mistakes to watch for

- **PRing the wrong base.** GitHub's PR form defaults the base to `main`. For a v20 fix you must change it to `v20.0` before submitting — there's no warning if you get it wrong, it'll just merge into the wrong version.
- **Branching from the wrong base.** `git checkout -b my-fix` branches off whatever you're currently on. Always `git checkout <base> && git pull` first.
- **Editing a file on `main` when you meant `v20.0` (or vice versa).** When using the GitHub UI to edit, verify the branch in the file URL before clicking the pencil.

## If in doubt

Raise the PR against whatever seems closest, and say in the PR description that you're unsure whether the change should also go to the other branch. We can sort it out in review.
