# Session_File

The name of the file from which the Session (`⎕SE`) is loaded when Dyalog starts. If no extension is given, `.dse` is assumed. The session file holds the `⎕SE` object last saved in it, which defines the appearance and behaviour of the Session menu bar, tool bars, and status bar, together with any functions and variables held in the `⎕SE` namespace.

Default is `[DYALOG]/default.dse` (the `default.dse` file in the Dyalog installation directory).

<!-- REVIEW(default): confirmed for UNIX/macOS from the Unix guide ($DYALOG/default.dse); confirm the Microsoft Windows default. -->

See also the [Session tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-session-tab) of the Windows Configuration Dialog.
