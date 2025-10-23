<h1 class="heading"><span class="name">Multi-line Session Input</span></h1>

The Session allows multi-line input. This feature is optional, and is controlled by the value of the **Dyalog_LineEditor_Mode** configuration parameter (default is `1`, meaning that multi-line input is enabled). To disable multi-line input, set **Dyalog_LineEditor_Mode** to `0`.

See [Dyalog_LineEditor_Mode.](../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-lineeditor-mode)

On Microsoft Windows, multi-line input can be enabled and disabled using the **Enable Multiline Input** checkbox on the **Session** tab of the **Configuration** dialog box. See [Dyalog_LineEditor_Mode](../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-session-tab).

## When Multi-line Input is Enabled

- The session considers all related lines to be a *group*.
- Grouped lines are syntax coloured as a whole.
- If a change is made to one or more lines in a group then the whole group is marked to be re-executed when **&lt;ER>** is pressed.
- Lines can be inserted into a group with the **&lt;IL>** keystroke.
- The current line can be cleared with the **&lt;EL>** keystroke. (It is not possible to UNDO a delete line in the session).
- if the interpreter detects an un-terminated control structure or dfn on a single line of input it:
  - enters a new multi-line mode which accumulates lines until the control structure or dfn is terminated.
  - executes a completed block of lines as if it were within a niladic defined function.
- enters a new multi-line mode which accumulates lines until the control structure or dfn is terminated.
- executes a completed block of lines as if it were within a niladic defined function.

Multi-line input can be terminated by correctly terminating the input. For example, if you started a block of multi-line input with a `{` character, then a matching and similarly nested `}` character terminates it. Similarly, if you started a block of multi-line input with `:If` then a matching and similarly nested `:EndIf` terminates it. Issuing a weak interrupt aborts the multi-line input and all changes are lost.

On Microsoft Windows and in Ride, one or more lines from a group can be executed separately by selecting the entire line or lines before pressing **&lt;ER>**.
