# Session Initialisation

## Introduction

Each time Dyalog starts it loads and loads an initialisation file whose name is defined by the **DyalogStartup** parameter. The code defined in this file performs Session initialisation. If **DyalogStartup** is undefined, the system uses the first file it finds named `StartupSession` with file extension `.aplf`, `.apln` or `.aplc` in the Dyalog directory. If the file has the `.aplf` extension, it is executed. If it has a `.apln` or `.aplc` extension, the system instantiates the namespace or class and executes its `Run` function (if it exists).

At the end of the initialisation, the function defined by the `.aplf` file (or the `Run` function of the namespace or class) becomes the niladic function `⎕SE.StartupSession`, which be called to re-run the session initialisation procedures.

## Implementation

Code to be installed in `⎕SE` is specified in APL source code files contained in *Session initialisation* directories identified by the **DyalogStartupSE** parameter. If this parameter is not specified, the default is a directory named `StartupSession` located in three standard locations as described below. See  [DyalogStartupSE](../../../windows-installation-and-configuration-guide/configuration-parameters/dyalogstartupse) for more details. 

Only content stored in files matching the wildcard patterns `*.dyalog` and `*.apl?` will be loaded. All such files must be appropriate for `⎕FIX`.

For each subdirectory in a Session initialisation directory, a corresponding namespace is created in `⎕SE`. Any source code files in these subdirectories will be fixed in their respective corresponding namespaces, and nested subdirectories become nested namespaces, recursively

Every top-level directory that is loaded as a namespace in `⎕SE` can have a `Run` function which (depending on the value of the **DyalogStartup_X** parameter, will be called after everything has been loaded. This does not apply to sub-namespaces. See [DyalogStartup_X](../../../windows-installation-and-configuration-guide/configuration-parameters/dyalogstartup-x).

This requires Link which is available by default. A custom version of Link can be used. See [DyalogLink](../../../windows-installation-and-configuration-guide/configuration-parameters/dyaloglink).

The Session initialisation directories are processed in alphabetical order and code defined in each directory will replace code with the same name defined previously. In effect, this means that user-supplied content can replace content supplied by Dyalog Ltd. and version-specific content can replace version-agnostic content.

## Default Session Initialisation Directories

If the **DyalogStartupSE** parameter is undefined, APL looks for Session initialisation directories named `StartupSession` in the following three locations, and processes them in that order:

1. The Dyalog installation directory (which contains the dyalog executable)
2. A version-agnostic subdirectory in the user directory (the standard directory for user-related Dyalog APL files)
3. A version-specific subdirectory in the user directory, whose name is derived as described below.

Under Windows these might be:

1. `C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode`

2. `C:\Users\Pete\Documents\Dyalog APL Files`

3. `C:\Users\Pete\Documents\Dyalog APL-64 19.0 Unicode Files`

The version-specific name is :
```
     Dyalog APL{bit} {version} {edition}
```

where:

- {bit} is "`-64`" if 64-bit version, otherwise nothing
- {version} is the main and secondary version numbers of dyalog.exe separated by ".".
- {edition} is "`Unicode`" for the Unicode Edition, otherwise nothing
