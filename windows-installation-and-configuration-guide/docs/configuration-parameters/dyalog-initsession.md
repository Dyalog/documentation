# DYALOG_INITSESSION

This Boolean parameter governs whether (`1`) or not (`0`) Dyalog performs Session Initialisation on start-up. See [Session Initialisation](../../../windows-ui-guide/the-session-object/session-initialisation).

The default is `1` for interactive sessions, and `0` for executable scripts and run-time versions.

Session initialisation makes Link, SALT and other things available. These features depend on DYALOG_INITSESSION being `1` (explicitly or by default).
