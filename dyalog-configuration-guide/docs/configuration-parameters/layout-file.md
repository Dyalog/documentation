# LAYOUT_FILE

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system.

The path (absolute, or relative to the working directory) and name of the Session layout file. The Session layout file records the docking layout of the Session, that is, the position of the Editor, the Debugger, and the other tools that can be docked in the Session window.

The file is read when Dyalog starts, and the current layout is written back to it when Dyalog exits, so a layout chosen from the [Layout menu](../../../windows-ui-guide/session-menubar#the-layout-menu) is still in effect the next time Dyalog starts, without the session file having to be saved. A layout file contains no APL code.

Valid values are a file path including the `.layout` extension, which is not assumed.

Default is `default.layout` in the Dyalog folder of your Documents directory, for example `C:\Users\Bob\Documents\Dyalog APL-64 21.0 Unicode Files\default.layout`. The folder name identifies the interpreter: `-64` is included for the 64-bit interpreter and `Unicode` for the Unicode edition, so the 32-bit Classic edition of Dyalog 19.0 uses `Dyalog APL 19.0 Files`.

The layout files supplied with Dyalog, such as `classic.layout` and `Bottom.layout`, are installed in the directory given by [`Dyalog`](dyalog.md), for example `C:\Program Files\Dyalog\Dyalog APL-64 21.0 Unicode`.

!!! Info "Information"
    The docking state of a user-defined Form docked in the Session cannot be recorded in the layout file; the session file must be saved to preserve it.

Related parameters: [Session_File](session-file.md), [Log_File](log-file.md).
