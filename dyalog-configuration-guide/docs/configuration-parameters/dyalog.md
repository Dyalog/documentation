# Dyalog

The directory in which Dyalog is installed. It is used to form the default values of parameters such as [`APLKeys`](aplkeys.md), [`APLTrans`](apltrans.md), and [`WSPath`](wspath.md).

Valid values are a directory path.

Default is the directory from which the Dyalog program was loaded.

!!! Info "Information"
    On UNIX and macOS this parameter is set by the supplied startup script (`mapl`). To find the location of the Dyalog executable itself, read it from the process information (for example `/proc/<process-id>/` on Linux, or the output of `ps`) rather than from this parameter.

Related parameters: [DyalogInstallDir](dyaloginstalldir.md).
