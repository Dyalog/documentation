<h1 class="heading"><span class="name">The Dyalog .NET Compiler</span></h1>

APL Source files are compiled into executable code by the Dyalog .NET Compiler identified in [](#Compilers).

Table: Version-specific Dyalog .NET Compilers { #Compilers }

| |Unicode Edition      |Classic Edition|
|------|---------------------|---------------|
|32-Bit|**dyalogc_unicode.exe**  |**dyalogc.exe**    |
|64-Bit|**dyalogc64_unicode.exe**|**dyalogc64.exe** |

This program is called automatically by ASP.NET when a client application requests a web page (**.aspx**) or web service (.asmx) and, in these circumstances, always generates the corresponding .NET class. However, the Dyalog .NET Compiler can also be used to:

- compile an APL source file into a workspace (**.dws**) – this can sunsequently be run using **dyalog.exe** or **dyalogrt.exe**.
- compile an APL source file into a .NET class (**.dll**) – this can subsequently be used by any other .NET-compatible host language, such as C# or Visual Basic.
- compile an APL source file into a native Microsoft Windows executable program (**.exe**), which can be run as a stand-alone executable. This program can be distributed (along with the Dyalog APL runtime DLL) as a packaged application, and does not require any of the additional support files and registry entries that are typically needed by the Dyalog run-time **dyalogrt.exe**. For more information, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_.
    
	!!! Info "Information"
        The Dyalog APL dynamic link library does not use MAXWS, but instead allocates workspace dynamically as required.
		
- compile an APL workspace (**.dws**) into a native Microsoft Windows executable program, with the same characteristics and advantages described above.

The script is designed to be run from a command prompt. For example, if using the 64-bit Unicode edition, navigate to the appropriate directory and type `dyalogc64_unicode /?` to query its usage; the following output is displayed:
```nonAPL
c:\Program Files\Dyalog\Dyalog APL-64 18.0 Unicode>dyalogc64_unicode /?
Dyalog .NET Compiler 64 bit. Unicode Mode. Version 18.0.38524.0
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

The <code class="language-nonAPL">/i</code> option specifies the [isolation mode](../implementation-details/isolation-mode/) – this overrides the setting in **web.config**.

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
