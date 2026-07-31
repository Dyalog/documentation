# APLAN_FOR_OUTPUT

Whether Session output uses [array notation](../../../programming-reference-guide/introduction/arrays/array-notation/) when possible.

Valid values are:

- `0` : Session output uses the usual display form
- `1` : Session output uses array notation; [`⎕PP`](../../../language-reference-guide/system-functions/pp) does not then apply to numeric Session output

Default is `0`.

The setting can be toggled with the `]APLAN.Output` user command. In the Microsoft Windows IDE it can also be toggled with the ![array notation](../img/session_arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon in the Session toolbar.

Related parameters: [APLAN_FOR_EDITOR](aplan-for-editor.md).
