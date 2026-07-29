# APLSTATUSFD

!!! Info "Information"
    This configuration parameter is only relevant on the UNIX and macOS operating systems.

The number of the output stream (file descriptor) on which messages for the Status window are written. Setting it allows this output to be redirected when Dyalog is started.

Valid values are a file descriptor number.

Default is unset, in which case the output appears in the same terminal window as the Session (although it is not part of the Session, and can be cleared with the Screen Redraw command key, often `Ctrl+L`).
