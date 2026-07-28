# Output

Dyalog APL produces output through several distinct mechanisms. This page defines the terminology for those mechanisms and describes where each kind of output goes, both in the interactive Session and when the interpreter is attached to operating-system streams.

## Kinds of Output

*Implicit output* is the display of the result of an expression that is not assigned to a name, passed as an argument to a function or operator, or otherwise suppressed. This is also known as "default output", "direct output", or "numeric output". It arises at the Session prompt and from unassigned values in traditional functions and operators.

Output is also produced explicitly by assignment to [`⎕`](../../../language-reference-guide/system-functions/evaluated-input-output), which displays an array in the same form as implicit output, or to [`⍞`](../../../language-reference-guide/system-functions/character-input-output), which displays characters without a trailing new-line. Error messages, the output of [system commands](../../../language-reference-guide/system-commands/), and the messages reported by the function editor are all directed in the same way as output through `⍞`.

## Output in the Interactive Session

In the interactive Session, whether the native GUI or a Ride connection, all output appears in the Session log; the stdout and stderr streams described below do not apply.

Implicit output and output through `⎕` are folded according to the print width [`⎕PW`](../../../language-reference-guide/system-functions/pw). Output through `⍞` ignores `⎕PW` and instead folds at the width of the window or terminal.

The Session reports a [SessionPrint](../../../object-reference/methodorevents/sessionprint) event immediately before a value is displayed, whether that value is implicit output or output through `⎕`. A callback attached to this event takes over the display entirely: it may output anything, or nothing at all, by any means, whether through `⎕`, `⍞`, or otherwise. The event is not reported for error messages or for the output of system commands.

## Output to Operating-System Streams

When the interpreter is attached to operating-system streams, running as a [shell script](../../../windows-installation-and-configuration-guide/shell-scripts) or started from a terminal with its streams redirected, each kind of output is written to either standard output (stdout) or standard error (stderr):

| Output | Stream |
|---|---|
| Implicit output | stdout |
| Output through `⎕` | stdout |
| Output through `⍞` | stderr |
| Error messages | stderr |
| System command output | stderr |
| Function editor messages | stderr |

<h3 class="example">Example</h3>

Given the script:
```apl
#!/usr/local/bin/dyalogscript
⎕←'to stdout'
⍞←'to stderr'
```
redirecting the two streams to separate destinations sends each message to its own destination.

!!! Info "Information"
    In a non-interactive shell script, implicit output is suppressed: only output through `⎕` and `⍞` is written. When the interpreter is attached to a terminal interactively, implicit output is written to stdout.

## Print Width and Streams

`⎕PW` sets the width at which output is folded. It applies only to implicit output and to output through `⎕`; it does not affect output through `⍞`, nor the result of [Format (`⍕`)](../../../language-reference-guide/primitive-functions/format), [`⎕FMT`](../../../language-reference-guide/system-functions/fmt), [`⎕ARBOUT`](../../../language-reference-guide/system-functions/arbout), or [`⎕ARBIN`](../../../language-reference-guide/system-functions/arbin). Because `⍞` is the only value-bearing output written to stderr, `⎕PW` governs stdout alone.
