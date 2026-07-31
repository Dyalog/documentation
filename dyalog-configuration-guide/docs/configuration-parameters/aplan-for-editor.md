# APLAN_FOR_EDITOR

Whether new **Edit** windows containing arrays open using [array notation](../../../programming-reference-guide/introduction/arrays/array-notation/) when possible.

Valid values are:

- `0` : arrays open in the usual display form
- `1` : arrays open using array notation; [`⎕PP`](../../../language-reference-guide/system-functions/pp) does not then apply to numbers shown in the editor

Default is `0`.

The setting can be toggled with the `]APLAN.Editor` user command. In Ride and the Microsoft Windows IDE, an open **Edit** window's mode can be toggled with the ![array notation](../img/object_arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon in the editor's toolbar.

Related parameters: [APLAN_FOR_OUTPUT](aplan-for-output.md).
