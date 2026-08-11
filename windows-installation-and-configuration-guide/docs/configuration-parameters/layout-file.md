# LAYOUT_FILE

This parameter specifies the path (absolute or relative to the working directory) and name of the Session layout file. The name must include the __.layout__ extension; it is not assumed.

The Session layout file records the docking layout of the Session, that is, the position of the Editor, the Debugger, and the other tools that can be docked in the Session window. It is loaded when Dyalog starts, and the current layout is written back to it when Dyalog exits. A layout selected from the [**Layout** menu](../../../windows-ui-guide/session-menubar#the-layout-menu) is, therefore, still in effect the next time Dyalog starts, without the session file having to be saved.

A layout file contains no APL code.

!!! Info "Information"
    If a user-defined Form is docked in the Session, its docking state cannot be recorded in the layout file; the session file must be saved to preserve it.

The default is **default.layout** in the relevant **Dyalog** folder of your **Documents** directory, for example, **C:\Users\Bob\Documents\Dyalog APL-64 21.0 Unicode Files\default.layout**.

Layout files supplied with Dyalog, such as __classic.layout__ and __Bottom.layout__, are installed in the directory identified by the [dyalog](./dyalog.md) configuration parameter, for example, __C:\Program Files\Dyalog\Dyalog APL-64 21.0 Unicode__.

See also [Session_File](./session-file.md) and [Log_File](./log-file.md).
