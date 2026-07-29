# DYALOG_SHELL_SUBPROCESS

!!! Info "Information"
    This configuration parameter is only relevant on the AIX operating system.

Whether the interpreter starts a small child process to handle calls to [`⎕SHELL`](../../../language-reference-guide/system-functions/shell). This improves the performance of `⎕SHELL` on AIX.

Valid values are:

- `0` : calls to `⎕SHELL` are handled without a child process
- `1` : the interpreter starts a child process to handle calls to `⎕SHELL`

Default is `1`.
