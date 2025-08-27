<h1 class="heading"><span class="name">DyalogStartupSE</span></h1>

This parameter specifies one or more *Session initialisation* directories that contain APL code to be installed in `⎕SE`.  If this parameter is not specified, the default is a directory named `StartupSession` located in three standard locations.

Under Windows these might be:

1. `C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode`

2. `C:\Users\Pete\Documents\Dyalog APL Files`

3. `C:\Users\Pete\Documents\Dyalog APL-64 19.0 Unicode Files`

The version-specific name is :
```apl
     Dyalog APL{bit} {version} {edition}
```

where:

- {bit} is "`-64`" if 64-bit version, otherwise nothing
- {version} is the main and secondary version numbers of dyalog.exe separated by ".".
- {edition} is "`Unicode`" for the Unicode Edition, otherwise nothing

The parameter is a string containing the list of directory names separated by ";" on Windows, ":" elsewhere.

If DyalogStartupSE begins with the specified separator, the default list is *extended* rather than *replaced*.

Note that the effective sequence of directories specified by this parameter is converted to a vector of character vectors and stored in  `⎕SE.Dyalog.StartupSession.AllPaths`.

If unset or extended (that is, starts with a : separator):

- the effective StartupSession directory in [DYALOG] is available as `⎕SE.Dyalog.StartupSession.Dyalog`.
- the StartupSession directory in the version-agnostic directory is available as `⎕SE.Dyalog.StartupSession.VerAgno`.
- the StartupSession directory in the version-specific directory is available as `⎕SE.Dyalog.StartupSession.VerSpec`.

See also [Implementation](https://help.dyalog.com/19.0/index.htm#UserGuide/The%20APL%20Environment/Session%20Initialisation.htm).
