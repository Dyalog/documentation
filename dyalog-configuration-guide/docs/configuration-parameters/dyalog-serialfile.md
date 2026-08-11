# DYALOG_SERIALFILE

!!! Info "Information"
    This configuration parameter is only relevant on the UNIX and macOS operating systems.

The full path to the text file that contains your Dyalog serial number. If it is not set, the default location `$HOME/.dyalog/serial` is used. When Dyalog starts, if [`DYALOG_SERIAL`](dyalog-serial.md) is not already set it is set to the contents of this file. Setting this parameter is useful in a multi-user environment: a system administrator can maintain a single serial number file for all users.

Valid values are a file path.

Default is unset.

Related parameters: [DYALOG_SERIAL](dyalog-serial.md).
