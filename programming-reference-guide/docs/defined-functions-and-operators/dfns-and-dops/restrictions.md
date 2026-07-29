# Restrictions

- Dfns need not return a result. However even a non-result-returning expression will terminate the function, so you can't, for example, call a non-result-returning function from the middle of a dfn.
- You can trace a dfn **only** if it is defined on more than one line. Otherwise it is executed atomically in the same way as an execute (`⍎`) expression. This deliberate restriction is intended to avoid the confusion caused by tracing a line and seeing nothing change on the screen.
- dfns do not currently support `⎕CS` which, if used, generates a `NONCE ERROR`.
- `⎕SHADOW` ignores dfns when looking down the stack for a traditional function (tradfn) in which to make a new local name.
- dfns do not support control structures or branch.
- dfns do not support modified assignment such as  `X plus←10` where `X` is an array and `plus` is a function. In this example, both `X` and `plus` would be assigned the value 10.
- `⎕MONITOR` does not apply to dfns and dops.

## Supplied Workspaces

You can find many samples of dfns and dops in utility workspace `dfns.dws` in the `ws` sub-directory.

Additional examples are in workspaces: `min.dws`, `max.dws`, `tube.dws` and `eval.dws`.
