# Log_File

The path (absolute, or relative to the working directory) and name of the Session log file.

Session log files are not interchangeable between different versions, editions, or widths of Dyalog. Starting a second instance of the same interpreter with the same log file name would normally fail to create a log for that instance, so the default name includes a `*` character: at start-up Dyalog replaces the `*` with an increasing integer, beginning at `000`, and opens and locks the first name it can (for example `log*.dlfx` yields `log000.dlfx`, `log001.dlfx`, and so on). Closing an instance frees its number for reuse. The process fails, and no log is used, if the number would exceed `999`.

The `LogFile` property of `⎕SE` reports the name of the log file in use.

Default depends on operating system:

- Microsoft Windows: `<DocumentsDirectory>\Dyalog APL-<bits> <DyalogMajor><DyalogMinor> <Unicode|Classic> Files\default_*.dlfx`, for example `C:\Users\Bob\Documents\Dyalog APL-64 21.0 Unicode Files\default_*.dlfx`
- UNIX and macOS: `$HOME/.dyalog/session_log_<DyalogMajor><DyalogMinor><U|C><bits>_*.dlf`, for example `$HOME/.dyalog/session_log_210U64_*.dlf`

Related parameters: [Log_File_InUse](log-file-inuse.md), [Log_Size](log-size.md).

See also the [Session tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-session-tab.md) of the Windows Configuration Dialog.
