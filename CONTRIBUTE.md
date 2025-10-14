# Contribution process

The purpose of this document is to outline how documentation authors should contribute material to the Dyalog documentation.
When working with the Dyalog documentation, we follow common `git` workflows, preferring to think about treating [documentation as code](https://www.writethedocs.org/guide/docs-as-code/). Please consult the [Dyalog Documentation Guidelines](https://dyalog.github.io/documentation-guidelines) for the style and language conventions we adopt.

> **Note:** In order to be a Dyalog documentation contributor, you need basic `git` and GitHub proficiency and a GitHub account. You need to be fluent in Markdown and at least somewhat familiar with YAML.

There are slight process variations depending on if you're a member of the Dyalog GitHub organisation or not.

## Issue

All documentation work should start with a GitHub _issue_. As a rule of thumb, an issue should refer to a single logical aspect where practical. For example, an issue may be raised to "Document ⎕SHELL" -- an example of a single, logical aspect. "Document ⎕SHELL, and fix the formatting in the example for the session gutter in the UI guide" is not.

Think of issues as the "meaningful undo unit" -- if you need to revert the work for the issue, you don't want to then also have to revert unrelated work that happened to be tied up in it. A narrow issue scope also helps with reducing the likelihood of merge conflicts.

If you want to contribute some documentation -- be it new work, or fixes to existing, create an issue on the GitHub website, and make a note of the issue id. If you create an issue for yourself, assign yourself to the issue, too. Never work on an issue assigned to someone else without discussing it with them first. 

The issue title should be brief, but sufficiently descriptive so that anyone in the team is able to understand the issue's purpose from the title. 

The issue's body describes what the work entails. Note that an issue may evolve over its lifetime. Keep it updated if there are material changes. It is helpful to others if the issue describes which part of the documentation will be affected. 

## Branch

> **Note:** If you're not a member of the Dyalog GitHub organisation, you cannot push branches to the repository directly. Instead you must first _fork_ the documentation repository into your own GitHub account, and then follow the process outlined below. PRs can then be raised from your fork.

Each issue should be accompanied by a single branch off the main. These branches should conform to a very specific naming scheme:

```
X-name-derived-from-issue-title
```
where X is the issue id. Note: dashes for spaces, no other non-alpha-numerics, no capitals. Thus, if the issue is "Document ⎕SHELL", and its id is 5, we branch to `5-document-shell` or something along those lines.

We use this specific so that when we use `git log` we can at a glance see which tickets are being worked on, and also so that if several branches end up referring to the same issue, they will be grouped in the output: let's say that we subsequently discover that more work needs to go towards issue 5, a new branch is created for those fixes, for example `5-outline-windows-issues-for-shell`.

## Do the work in the branch

Once you have created the branch, write your documentation. Your work needs to be that described in the issue only. This requires discipline: it's not uncommon to discover something unrelated that needs fixing when you start writing. When this happens, create a new issue instead. 

If you find once you start working that the issue is not adequately describing what needs doing, don't be afraid to update the issue. The important thing is that the issue adequately describes the work at the point of merging. If the issue was not raised by you, discuss any changes with the originator first.

Commit your work to the branch, crafting a good commit message, describing what has been changed or added. Don't auto-close the ticket with `Closes #X` (if `X` is the ticket id) -- this is reserved for the _merge message_; see below. 

Once you have committed, push your branch to the upstream repository, for example:

```
git push origin 5-document-shell
```

If your push succeeds, you should be presented with a link to open a _pull request_ (PR). Open this in a browser.

## PR

A PR means a request to merge in some changes into the main branch. A PR should never be merged unless it's been reviewed: the PR screen on the GitHub website will normally suggest a reviewer -- you can either accept the suggestion, or add your own, or leave it blank: you can add a review request after the PR has been opened. 

> **Note:** If you're a contributor from outside Dyalog, leave the reviewer field blank.

When requesting a review, discuss this with the person -- again, GitHub notifications have a tendency to drown in the flow. It is polite to send the reviewer the link to the PR, with the _files changed_ tab open. This means they can get right into it.

```
Hi Alex --

thanks for agreeing to review my PR for the ⎕SHELL system function.

The issue is here: https://github.com/Dyalog/documentation/issues/4

PR: https://github.com/Dyalog/documentation/pull/3/files

Kind regards,

Sam
```

## Review and Merge

A review is a two-way conversation. Do use the GitHub interface for PR review so that we have a log. Most doc reviews will involve a lot of changes. It is most helpful to leave those inline -- in the diff view on GitHub, locate the line where the paragraph or section begins, and hover just to the right of the line number. You should see a "+" appearing. Clicking this gives you a text field into which you can type your comment. If you're proposing a stylistic rewording, a nice touch is to provide the complete replacement for the paragraph. This means that the author, if they agree with your suggestion, can lift the whole thing as-is. If you're querying the correctness or validity, write a concise question. 

Sometimes, it can be more productive to do a review "live", over a shared screen. If your review takes this form, the reviewer should approve the PR via the green button towards the top-right, and leave a comment "This was reviewed in person".

Doing reviews well is an art form and requires practice on both sides. Be respectful: as the reviewee, you have requested the time and effort from someone to help you with your work. Respect their input. As the reviewer, the reviewee has committed their time and effort to improve the Dyalog product by providing documentation for an area of their expertise. Respect _their_ work. Focus on correctness, clarity and completeness before formatting and style: it's not the reviewer's role to force the writing into _their_ particular tastes and preferences. 

Do not underestimate the effort being a reviewer requires -- the reviewer must ensure they understand the feature being documented so they can assess correctness. Before you accept a request to become a reviewer, indicate a timeline to the reviewee: if your earliest convenience is three weeks from now, it may be better to let someone else do the review. 

As the reviewee, you're not _obligated_ to accept every suggestion made by the reviewer (and the reviewer should be prepared for this). However, a PR will not be merged until the review has been marked as approved jointly by reviewee and reviewer(s). 

A review typically involves several changes. The reviewee should commit and push any agreed changes to PR branch, never the reviewer. 

Once a review is approved, if the reviewee is a Dyalog member, they should merge it, marking the PR branch for deletion. If the reviewee is external, the reviewer should merge it (marking the PR branch for deletion). In the merge message, auto-close the issue, for example:

```
Closes #5
```

## Pull Main

As you merge, your local main branch is now out of date, and your issue branch is irrelevant: it should be removed locally (we already deleted the remote branch after merging upstream, if you recall) after it has been merged. Pull the main branch in _fast forward only_ mode:

```
git switch main
git pull origin main --ff-only
git branch -d 5-document-shell  # or whatever your issue branch was called
```

The `--ff-only` will protect you from unintended consequences, meaning that git will terminate instead of generating merge conflicts. Together with always branching before making modifications, this should mean you never see a merge conflict.

