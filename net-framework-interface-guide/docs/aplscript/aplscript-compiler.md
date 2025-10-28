<h1 class="heading"><span class="name">The APLScript Compiler</span></h1>

APLScript files are *compiled* into executable code by the APLScript compiler whose name is given in the table below.

|&nbsp;    |Unicode Edition        |Classic Edition|
|----------|-----------------------|---------------|
|**32-Bit**|`dyalogc_unicode.exe`  |`dyalogc.exe`  |
|**64-Bit**|`dyalogc64_unicode.exe`|`dyalogc64.exe`|

This program is called automatically by `ASP.NET` when a client application requests a Web Page (.aspx) or Web Service (.asmx) and in these circumstances always generates the corresponding .NET class. However, the Script Compiler may also be used to:

- Compile an APLScript into a workspace (`.dws`) that you may subsequently run using `dyalog.exe` or `dyalogrt.exe` in the traditional manner.
- Compile an APLScript into a .NET class (`.dll`) which may subsequently be used by any other .NET compatible host language such as C# or Visual Basic.
- Compile an APLScript into a native Windows executable program (`.exe`), which may be run as a stand-alone executable. This program may be distributed, along with the Dyalog runtime DLL, as a packaged application, and does not require any of the additional support files and registry entries that are typically needed by the Dyalog run-time `dyalogrt.exe`. Note too that the Dyalog dynamic link library does not use MAXWS but instead allocates workspace dynamically as required. See the *Dyalog for Microsoft Windows Installation and Configuration Guide: Run-Time Applications and Components* for further details.
- Compile a Dyalog workspace (.dws) into a native Microsoft Windows executable program, with the same characteristics and advantages described above.

The Script is designed to be run from a command prompt. If in the 64-bit Unicode Edition change to the appropriate directory and type `dyalogc64_unicode /?` (to query its usage) the following output is displayed:

```other
c:\Program Files\Dyalog\Dyalog APL-64 18.0 Unicode>dyalogc64_unicode /?
Dyalog APLScript compiler 64 bit. Unicode Mode. Version 18.0.38524.0
Copyright Dyalog Ltd 2000-2020

dyalogc.exe command line options:

/?                Usage
/r:file           Add reference to assembly
/o[ut]:file       Output file name
/res:file         Add resource to output file
/icon:file        File containing main program icon
/q                Operate quietly
/v                Verbose
/s                Treat warnings as errors
/nonet            Creates a binary that does not use Microsoft .Net
/runtime          Build a non-debuggable binary
/lx:expression    Specify entry point (Latent Expression)
/t:library        Build .Net library (.dll)
/t:nativeexe      Build native executable (.exe). Default
/t:workspace      Build dyalog workspace (.dws)
/nomessages       Process does not use windows messages. Use when creating
                  a process to run under IIS
/console          Creates a console application
/c                Creates a console application
/multihost        Support multi-hosted interpreters
/unicode          Creates an application that runs in a Unicode intepreter
/wx:[0|1|3]       Sets ⎕WX for default code
/a:file           Specifies a JSON file containing attributes to be attached
       to the binary
/i:Process        Set the isolation mode of a .NET Assembly
/i:Assembly       Set the isolation mode of a .NET Assembly
/i:AppDomain      Set the isolation mode of a .NET Assembly
/i:Local          Set the isolation mode of a .NET Assembly
```

Note that the isolation mode specified by the `/i` option overrides the setting in `web.config`. See [DyalogIsolationMode](../implementation-details/asp-net-configuration-file.md).

The `/a` option is used to specify the name of a JSON file that contains assembly info. For example:
```
dyalogc64_unicode.exe /t:library j:/ws/attributetest.dws /a:c:/tmp/atts.json
```

where `c:/tmp/atts.json` contains:
```json
{
   "AssemblyVersion": "1.2.2.2",
   "AssemblyFileVersion": "2.1.1.4",
   "AssemblyProduct": "My Application",
   "AssemblyCompany": "My Company",
   "AssemblyCopyright": "Copyright 2020",
   "AssemblyDescription": "Provides a text description for an assembly.",
   "AssemblyTitle": "My Assembly Title",
   "AssemblyTrademark": "Your Legal Trademarks"
}
```
