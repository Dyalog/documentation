# DYALOG_INITSESSION

Whether Dyalog performs [Session Initialisation](../../../windows-ui-guide/the-session-object/session-initialisation) on start-up. Session initialisation makes Link, SALT, and other features available.

Valid values are:

- `0` : the Session is not initialised
- `1` : the Session is initialised

Default is `1` for interactive sessions, and `0` for executable scripts and run-time versions.
