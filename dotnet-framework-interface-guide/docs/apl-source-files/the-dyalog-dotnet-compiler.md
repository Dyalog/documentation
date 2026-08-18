# The Dyalog .NET Compiler

APL Source files are compiled into executable code by the Dyalog .NET Compiler identified in [](#Compilers).

Table: Version-specific Dyalog .NET Compilers { #Compilers }

| |Unicode Edition      |Classic Edition|
|------|---------------------|---------------|
|32-Bit|**dyalogc_unicode.exe**  |**dyalogc.exe**    |
|64-Bit|**dyalogc64_unicode.exe**|**dyalogc64.exe** |

This program is called automatically by ASP.NET when a client application requests a web page (**.aspx**) or web service (.asmx) and, in these circumstances, always generates the corresponding .NET class. However, the Dyalog .NET Compiler can also be used to:

- compile an APL source file into a workspace (**.dws**) – this can subsequently be run using **dyalog.exe** or **dyalogrt.exe**.
- compile an APL source file into a .NET class (**.dll**) – this can subsequently be used by any other .NET-compatible host language, such as C# or Visual Basic.
- compile an APL source file into a native Microsoft Windows executable program (**.exe**), which can be run as a stand-alone executable. This program can be distributed (along with the Dyalog APL runtime DLL) as a packaged application, and does not require any of the additional support files and registry entries that are typically needed by the Dyalog run-time **dyalogrt.exe**. For more information, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_.
    
	!!! Info "Information"
        The Dyalog APL dynamic link library does not use MAXWS, but instead allocates workspace dynamically as required.
		
- compile an APL workspace (**.dws**) into a native Microsoft Windows executable program, with the same characteristics and advantages described above.

The script is designed to be run from a command prompt. For example, if using the 64-bit Unicode edition, navigate to the appropriate directory and type `dyalogc64_unicode /?` to query its usage; the following output is displayed:
```nonAPL
C:\Program Files\Dyalog\Dyalog APL-64 21.0 Unicode>dyalogc64_unicode /?
Dyalog .NET component compiler 64 bit. Unicode Mode. Version 21.0.54393.0
Copyright Dyalog Ltd 2000-2026

dyalogc.exe command line options:

-?                Usage
-r:<file>         Add reference to assembly
-o[ut]:<file>               Output file name
-res:<file>                 Add resource to output file
-icon:<file>                File containing main program icon
-q                          Operate quietly
-v                          Verbose
-v2                         More verbose
-s                          Treat warnings as errors
-nonet                      Creates a binary that does not use Microsoft .NET
-net                        Creates a binary that targets .NET Version>=5
-framework                  Creates a binary that targets .NET Framework
-runtime                    Build a non-debuggable binary
-t:library                  Build .NET library (.dll)
-t:workspace                Build dyalog workspace (.dws)
-t:nativeexe                (Windows only) Build native executable (.exe). Default
-t:standalonenativeexe      (Windows only) Build native executable (.exe). Default
-lx:<text>                  (Windows only) Specify entry point (Latent Expression)
-cmdline:<text>             Specify a command line to pass to the interpreter
-nomessages                 (.NET Framework Only) Process does not use windows messages. Use when creating a process to run under IIS
-console|-c                 Creates a console application
-multihost                  Support multi-hosted interpreters
-unicode                    Creates an application that runs in a Unicode interpreter
-wx:[0|1|3]                 Sets ⎕WX for default code
-a:file                     (.NET Framework Only) Specifies a JSON file containing attributes to be attached to the binary
-i:Process                  (.NET Framework Only) Set the isolation mode of a .NET Assembly
-i:Assembly                 (.NET Framework Only) Set the isolation mode of a .NET Assembly
-i:AppDomain                (.NET Framework Only) Set the isolation mode of a .NET Assembly
-i:Local                    (.NET Framework Only) Set the isolation mode of a .NET Assembly
```

The <code class="language-nonAPL">/i</code> option specifies the [isolation mode](../implementation-details/isolation-mode.md) – this overrides the setting in **web.config**.

The <code class="language-nonAPL">/a</code> option specifies the name of a JSON file that contains assembly information. For example:
```nonAPL
dyalogc64_unicode.exe /t:library j:/ws/attributetest.dws /a:c:/tmp/atts.json
```

where <code class="language-nonAPL">c:/tmp/atts.json</code> contains:
```nonAPL
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
