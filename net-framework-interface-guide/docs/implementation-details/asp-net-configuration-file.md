<h1 class="heading"><span class="name">The web.config file</span></h1>

ASP.NET configuration parameters are defined in a file named `web.config` located in or above the root directory of an ASP.NET application. Parameters defined in these files supplement or override ASP.NET parameters which are defined system-wide.

The `web.config` file provided with Dyalog is located in the Dyalog sub-directory `samples\asp.net` and applies to all the examples residing in child directories of this directory. If you create a Dyalog ASP.NET application elsewhere on your system, you will need to copy this `web.config` into the application root directory. The parameters defined in the Dyalog `web.config` file are described below. Further details are provided in comments in the file.

## DyalogBinDirectory

This specifies the full path to the Dyalog binaries (DLLs and script compiler).

## dyalog (compiler)

This section defines an ASP.NET language named `dyalog` so that the expression  `Language = "dyalog"` in a script file associates that script with the Dyalog APLScript compiler dyalogc.exe. Subsidiary parameters and keys for the dyalog compiler are:

|-------------------------|----------------------------------------------------------------------------------------------------|
|debug                    |"true" (default) or "false" to bind the script to the Development DLL or the Run-time DLL           |
|DyalogCompilerEncoding   |"classic" or "unicode"..                                                                            |
|DyalogCompilerOptions    |This is used to define options for the script compiler. For example, to set `[]WX` to 1 use "/wx:1".|
|DyalogCompilerEmitPragmas|Must be "true" if you are using workspace behind.                                                   |

## DyalogIsolationMode

This parameter specifies the isolation method. See [Isolation Mode](isolation-mode.md) for further details.

DyalogCacheDirectory may be used to define the directory used to save the cached files.
