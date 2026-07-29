# Auto_PW

Whether the value of [`⎕PW`](../../../language-reference-guide/system-functions/pw) is derived automatically from the current width of the Session (Windows) or terminal (UNIX and macOS) window.

Valid values are:

- `0` : `⎕PW` is independent of the window width
- `1` : `⎕PW` changes whenever the window is resized, reflecting the number of characters that fit on one line

Default depends on operating system:

- Microsoft Windows: `0`
- UNIX and macOS: when unset, behaves as `1` (`⎕PW` tracks the terminal width, updated when the interpreter next checks for input)

Related parameters: [Default_PW](default-pw.md).

See also the [Session tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-session-tab) of the Windows Configuration Dialog.
