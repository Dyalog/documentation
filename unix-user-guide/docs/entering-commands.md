#  Entering Commands

Commands are either entered using the keys on the keyboard in conjunction with 0 or more metakeys, or when using the keyboard in different modes. A separate keystroke is used to move from one mode to the next; by default this is defined to be <kbd>Ctrl</kbd>+<kbd>x</kbd>. When Dyalog APL is started, you are in mode 0. Except Move/Resize in the editor/tracer, all mode changes are effective for one keystroke only.

**Example**

- assume that you have just started APL
- assume that the <kbd>Windows</kbd> key is used to enter APL characters
- `+` represents one keystroke, so <kbd>Ctrl</kbd>+<kbd>x</kbd><kbd>p</kbd> means: first hit <kbd>Ctrl</kbd> and <kbd>x</kbd> together, then <kbd>p</kbd>

| Keystrokes entered | How described in documentation | Outcome in Dyalog APL session                                                                                                                                                                                                                                        |
| --- | --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <kbd>p</kbd> | p | `p` appears in the session                                                                                                                                                                                                                                           |
| <kbd>Shift</kbd>+<kbd>p</kbd> | P | `P` appears in the session                                                                                                                                                                                                                                           |
| <kbd>Windows</kbd>+<kbd>p</kbd> | APL p | `*` appears in the session                                                                                                                                                                                                                                           |
| <kbd>Windows</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd> | APL P | `⍣` appears in the session                                                                                                                                                                                                                                           |
| <kbd>Ctrl</kbd>+<kbd>x</kbd><kbd>p</kbd> | Cmd-p | No noticeable effect. This is the command "Previous" (PV) used for search/replace. Note how Nrm in status line changes to Cmd when <kbd>Ctrl</kbd>+<kbd>x</kbd> is hit and then back to Nrm when the <kbd>p</kbd> is hit.                                            |
| <kbd>Ctrl</kbd>+<kbd>x</kbd><kbd>Ctrl</kbd>+<kbd>x</kbd><kbd>p</kbd> | CMD-p | No noticeable effect. This is the command "Paste" (PT). Note how Nrm in status line changes to Cmd when <kbd>Ctrl</kbd>+<kbd>x</kbd> is hit, and then changes to CMD when <kbd>Ctrl</kbd>+<kbd>x</kbd> hit again, and then back to Nrm when the <kbd>p</kbd> is hit. |
| <kbd>Ctrl</kbd>+<kbd>x</kbd><g> | N/A | Nothing; this is an invalid character in Cmd mode. Note how Nrm in status line changes to Cmd when <kbd>Ctrl</kbd>+<kbd>x</kbd> is hit, and then back to Nrm when the <kbd>g</kbd> is hit.                                                                           |

### Notes

1. the words "Nrm", "Cmd" and "CMD" are configurable.
2. in this example each mode is temporary, lasting for only one subsequent keystroke.
