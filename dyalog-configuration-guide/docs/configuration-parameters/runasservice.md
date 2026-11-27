# RunAsService

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system.

Whether Dyalog runs as a service: it does not prompt for confirmation when the user logs off, and the interpreter continues to run across the logoff/logon process.

Valid values are:

- `0` : Dyalog does not run as a service
- `1` : Dyalog runs as a service
- `2` : as `1`, but graphical user-interface features are disabled to reduce resource use; `⎕WC` then fails with a `LIMIT ERROR` for every object except Timer

Default is `0`.
