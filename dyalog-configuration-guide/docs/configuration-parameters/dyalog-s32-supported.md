# DYALOG_S32_SUPPORTED

Whether support for small-span (32-bit) component files is enabled. When support is disabled, a small-span component file cannot be tied. Small-span component files have been deprecated; disabling support identifies whether an application still depends on them.

Valid values are:

- `0` : support for small-span component files is disabled
- `1` : support for small-span component files is enabled

Default is `1`.

Related parameters: [DYALOG_EXTVAR_SUPPORTED](dyalog-extvar-supported.md).

See also [File Share Tie](../../../language-reference-guide/system-functions/fstie) and [Exclusive File Tie](../../../language-reference-guide/system-functions/ftie).
