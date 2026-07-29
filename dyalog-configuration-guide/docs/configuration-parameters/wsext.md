# WSEXT

Workspace filename extensions. Together with [`WSPath`](wspath.md) this determines the file search order for `)LOAD` and `)COPY`, and it specifies the extension added by `)SAVE` or `)CONTINUE` when none is given.

Valid values are a colon-separated list of one or more extensions, each including the leading period (`.`) that separates it from the basename. When `)SAVE` or `⎕SAVE` is used without an extension, the first extension in the list is applied.

Default depends on operating system:

- Microsoft Windows and macOS: `.dws:`
- other platforms: `:.dws:.DWS`

For example, on Windows `)LOAD myws` searches first for `myws.dws`, then for `myws` with no extension (and, as Windows file names are not case-sensitive, finds `myws.DWS`, `MyWs.Dws`, and so on). On other platforms `)LOAD myws` searches for `myws`, then `myws.dws`, then `myws.DWS`.

Related parameters: [WSPath](wspath.md), [CFEXT](cfext.md).
