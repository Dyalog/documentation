# DyalogStartupSE

One or more *Session initialisation* directories containing APL code to be installed in `⎕SE`.

Valid values are a list of directory names, separated by `;` (Windows) or `:` (UNIX and macOS). If the value begins with the separator, the default list is *extended* rather than *replaced*.

Default is a directory named `StartupSession` in the standard locations. On Windows these might be:

1. `C:\Program Files\Dyalog\Dyalog APL-64 21.0 Unicode`
2. `C:\Users\Bob\Documents\Dyalog APL Files`
3. `C:\Users\Bob\Documents\Dyalog APL-64 21.0 Unicode Files`

where the version-specific name has the form `Dyalog APL{bit} {version} {edition}` (`{bit}` is `-64` for a 64-bit version, otherwise nothing; `{version}` is the major and secondary version numbers separated by a period; `{edition}` is `Unicode` for the Unicode edition, otherwise nothing).

The effective sequence of directories is stored as a vector of character vectors in `⎕SE.Dyalog.StartupSession.AllPaths`. When the parameter is unset or extended, the `StartupSession` directory in the installation directory, the version-agnostic directory, and the version-specific directory are available as `⎕SE.Dyalog.StartupSession.Dyalog`, `.VerAgno`, and `.VerSpec` respectively.

Related parameters: [DyalogStartup_X](dyalogstartup-x.md).

For more information, see [Session Initialisation](../../../windows-ui-guide/the-session-object/session-initialisation).
