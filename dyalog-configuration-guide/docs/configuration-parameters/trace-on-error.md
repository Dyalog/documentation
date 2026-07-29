# Trace_On_Error

Whether the Tracer is deployed automatically when execution of a defined function halts with an untrapped error. When enabled, a stack of Trace windows is displayed immediately, with the top window receiving the input focus.

Valid values are:

- `0` : the Tracer is not deployed automatically
- `1` : the Tracer is deployed automatically on an untrapped error

Default depends on operating system:

- Microsoft Windows: `0`
- UNIX and macOS: `1`

Related parameters: [Trace_Level_Warn](trace-level-warn.md).

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab) of the Windows Configuration Dialog.
