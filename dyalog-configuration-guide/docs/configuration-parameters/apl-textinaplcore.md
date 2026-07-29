# APL_TextInAplCore

Whether certain information is written to an *aplcore* file when a [system error](../../../programming-reference-guide/error-messages/system-errors) occurs.

Valid values are:

- `0` : the information is omitted
- `1` : the information is included

Default is `1` (the interpreter's own default is `0`, but on UNIX and macOS the supplied startup script sets it to `1`).

Related parameters: [AplCoreName](aplcorename.md).
