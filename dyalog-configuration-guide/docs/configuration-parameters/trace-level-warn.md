# Trace_Level_Warn

The maximum number of Trace windows displayed when an error occurs and [`Trace_On_Error`](trace-on-error.md) is `1`. If the state indicator holds more functions than this, a warning message box is displayed instead of the stack of Trace windows, avoiding a lengthy delay. This parameter is ignored when the Tracer is invoked explicitly, and applies only in Classic Dyalog mode.

Valid values are a positive integer.

Default is `16`.

Related parameters: [Trace_On_Error](trace-on-error.md).

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab) of the Windows Configuration Dialog.
