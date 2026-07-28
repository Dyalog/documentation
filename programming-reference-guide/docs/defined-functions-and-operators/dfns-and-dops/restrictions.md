# Restrictions

A dfn or dop is subject to the following restrictions.

- A dfn need not return a [result](../../introduction/results.md), but any expression that does not produce a result still terminates the dfn. You therefore cannot call a no-result function from the middle of a dfn and carry on, because evaluation stops at that expression.
- Normal tracing (`<TC>`) steps over a single-line dfn, executing it atomically like an [Execute](../../../../language-reference-guide/primitive-functions/execute) (`⍎`) expression. This deliberate restriction avoids the confusion of tracing a line and seeing nothing change. Inline Tracing (`<IT>`) can step through the functions called within a single-line dfn, and a multi-line dfn traces normally.
- [`⎕CS`](../../../../language-reference-guide/system-functions/cs) is not supported inside a dfn and signals a `NONCE ERROR`.
- [`⎕MONITOR`](../../../../language-reference-guide/system-functions/set-monitor), [`⎕TRACE`](../../../../language-reference-guide/system-functions/set-trace), and [`⎕LOCK`](../../../../language-reference-guide/system-functions/lock) do not apply to dfns or dops.
- [`⎕SHADOW`](../../../../language-reference-guide/system-functions/shadow) skips dfns when looking down the stack for a tradfn in which to make a new local name.
- Control structures and other `:`-keywords, such as `:If` and `:Return`, are unavailable; a dfn expresses conditions through guards instead.
- Monadic branch (`→` given a line number, equivalent to `:GoTo`) is not supported. Niladic branch, that is [abort](../../../../language-reference-guide/other-syntax/abort) (`→`), does work: it clears the most recently suspended statement and all of its pendent statements from the state indicator.
- Modified assignment (`X f←Y`) and use of the pass-through value of an assignment (as in `X f Y←Z`) behave as expected when `f` is a primitive, but in a dfn a named function is instead read as part of a multiple assignment, so `X plus←10` assigns `10` to both `X` and `plus`. Insert `∘⊢` to force the intended reading: `X plus∘⊢←10` for the modified assignment, and `1 plus∘⊢a←10` (or simply `1 plus⊢a←10`) for the pass-through.

## Supplied Workspaces

You can find many samples of dfns and dops in utility workspace `dfns.dws` in the `ws` sub-directory.

Additional examples are in workspaces: `min.dws`, `max.dws`, `tube.dws` and `eval.dws`.
