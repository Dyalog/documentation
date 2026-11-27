# CFEXT

Component file filename extensions, determining the file search order when a component file is tied.

Valid values are a colon-separated list of one or more extensions, each including the leading period (`.`) that separates it from the basename.

Default depends on operating system:

- Microsoft Windows and macOS: `.dcf:`
- other platforms: `.dcf:.DCF:`

For example, on Windows `'myfile'⎕FTIE 0` searches first for `myfile.dcf`, then for `myfile` with no extension (and, as Windows file names are not case-sensitive, finds `myfile.DCF`, `MyFile.Dcf`, and so on). On other platforms it searches for `myfile`, then `myfile.dcf`, then `myfile.DCF`.

Related parameters: [WSEXT](wsext.md).
