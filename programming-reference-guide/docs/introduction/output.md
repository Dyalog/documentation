# Output

Dyalog APL produces output through several distinct mechanisms. This page defines the terminology for those mechanisms and describes where each kind of output goes, both in the interactive Session and when the interpreter is attached to operating-system streams.

## Kinds of Output

*Implicit output* is the display of the result of an expression that is not assigned to a name, passed as an argument to a function or operator, or otherwise suppressed. It arises at the Session prompt and from unassigned values in traditional functions and operators. Earlier documentation referred to this variously as "default output", "direct output", and "numeric output"; the term used throughout this documentation is *implicit output*.

Output can also be produced explicitly:

- Assignment to `⎕` displays an array in the same form as implicit output. See [Evaluated Input/Output](../../../language-reference-guide/system-functions/evaluated-input-output).
- Assignment to `⍞` displays characters without a trailing new-line and independently of the print width. See [Character Input/Output](../../../language-reference-guide/system-functions/character-input-output).

Further categories of output are the error messages reported for untrapped errors, the output of system commands (those beginning with `)`), and the messages reported by the function editor.

## Output in the Interactive Session

In the interactive Session, whether the native GUI or a Ride connection, all output appears in the Session log. The *stdout* and *stderr* streams described below do not apply.

Implicit output and output through `⎕` are folded according to the print width `⎕PW`. Output through `⍞` ignores `⎕PW`.

The Session reports a `SessionPrint` event immediately before a value is displayed, whether that value is implicit output or output through `⎕`. A callback attached to this event intercepts the display and may reformat or suppress it. The event is not reported for error messages or for the output of system commands. See [SessionPrint](../../../object-reference/methodorevents/sessionprint).

## Output to Operating-System Streams

When the interpreter is attached to operating-system streams, running under `dyalogscript` or started from a terminal with its streams redirected, each kind of output is written to either standard output (*stdout*) or standard error (*stderr*):

| Output | Stream |
|---|---|
| Implicit output | *stdout* |
| Output through `⎕` | *stdout* |
| Output through `⍞` | *stderr* |
| Untrapped error messages | *stderr* |
| System command output | *stderr* |
| Function editor messages | *stderr* |

<h3 class="example">Example</h3>

Given the script:
```apl
#!/usr/local/bin/dyalogscript
⎕←'to stdout'
⍞←'to stderr'
```
redirecting the two streams to separate destinations sends each message to its own destination.

!!! Info "Information"
    In a non-interactive shell script, implicit output is suppressed: only output through `⎕` and `⍞` is written. When the interpreter is attached to a terminal interactively, implicit output is written to *stdout*. See [Shell Scripts](../../../windows-installation-and-configuration-guide/shell-scripts) for the behaviour of `dyalogscript`.

## Print Width and Streams

`⎕PW` sets the width at which output is folded. It applies only to implicit output and to output through `⎕`; it does not affect output through `⍞`, nor the result of Format (`⍕`), `⎕FMT`, `⎕ARBOUT`, or `⎕ARBIN`. Because `⍞` is the only value-bearing output written to *stderr*, `⎕PW` governs *stdout* alone. See [Print Width](../../../language-reference-guide/system-functions/pw).
