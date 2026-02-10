# The Dyalog .NET Compiler

APL Source files are compiled into executable code by the Dyalog .NET Compiler, which is called **dyalogc.exe**.

By default, **dyalogc.exe** compiles to .NET. If the `-framework` option is set, it will instead compile to .NET Framework.
For backwards compatibility, the Dyalog .NET Compiler is also distributed on Microsoft Windows with the names identified in the table below.
        
|&nbsp;|Unicode Edition      |Classic Edition|
|------|---------------------|---------------|
|32-Bit|dyalogc_unicode.exe  |dyalogc.exe    |
|64-Bit|dyalogc64_unicode.exe|dyalogc64.exe  |

The Dyalog .NET Compiler can be used to:

- compile APL Source files into a workspace (**.dws**) – this can subsequently be run using **dyalog.exe** or **dyalogrt.exe**.
- compile APL Source files into a .NET class (**.dll**) – this can subsequently be used by any other .NET-compatible host language, such as C#.

The script is designed to be run from a command prompt. Navigate to the appropriate directory and type `dyalogc /?` to query its usage; the following output is displayed (the output displayed here is for Microsoft Windows; the command line options are not all applicable on other platforms):
```
c:/Program Files/Dyalog/Dyalog APL-64 19.0 Unicode>dyalogc /?
Dyalog .NET Compiler 64 bit. Unicode Mode. Version 19.0.48745.0
Copyright Dyalog Ltd 2000-2024

dyalogc.exe command line options:

-?                      Usage
-r:<file>               Add reference to assembly
-o[ut]:<file>           Output file name
-res:<file>             Add resource to output file
-icon:<file>            File containing main program icon
-q                      Operate quietly
-v                      Verbose
-v2                     More verbose
-s                      Treat warnings as errors
-nonet                  Creates a binary that does not use Microsoft .NET
-net                    Creates a binary that targets .NET Version >=5
-framework              Creates a binary that targets .NET Framework
-runtime                Build a non-debuggable binary
-t:library              Build .NET library (.dll)
-t:workspace            Build dyalog workspace (.dws)
-t:nativeexe            (Windows only) Build native executable (.exe). Default
-t:standalonenativeexe  (Windows only) Build native executable (.exe). Default
-lx:<text>              (Windows only) Specify entry point (Latent Expression)
-cmdline:<text>         Specify a command line to pass to the interpreter
-nomessages             (.NET Framework only) Process does not use windows messages. Use when creating a process to run under IIS  
-console|c              Creates a console application
-multihost              Support multi-hosted interpreters
-unicode                Creates an application that runs in a Unicode interpreter
-wx:[0|1|3]             Sets ⎕WX for default code
-a:file                 (.NET Framework only) Specifies a JSON file containing attributes to be attached to the binary
-i:Process              (.NET Framework only) Set the isolation mode of a .NET Assembly
-i:Assembly             (.NET Framework only) Set the isolation mode of a .NET Assembly
-i:AppDomain            (.NET Framework only) Set the isolation mode of a .NET Assembly
-i:Local                (.NET Framework only) Set the isolation mode of a .NET Assembly
```

The `-a` option specifies the name of a JSON file that contains assembly information. For example:
```
dyalogc.exe -t:library j:/ws/attributetest.dws -a:c:/tmp/atts.json
```

where `c:/tmp/atts.json` contains:
```
{
"AssemblyVersion":"1.2.2.2",
"AssemblyFileVersion":"2.1.1.4",
"AssemblyProduct":"My Application",
"AssemblyCompany":"My Company",
"AssemblyCopyright":"Copyright 2020",
"AssemblyDescription":"Provides a text description for an assembly.",
"AssemblyTitle":"My Assembly Title",
"AssemblyTrademark":"Your Legal Trademarks",
}
```
