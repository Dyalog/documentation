# <span>GetCommandLine</span> <span>Method 145</span>

**Applies To:** [Root](../objects/root.md)

**Description**

The GetCommandLine method returns the command line that was used to start the current Dyalog APL session or application.

The GetCommandLine method is niladic.

The result is a character vector.

<h2 class="example">Examples</h2>
```apl
      GetCommandLine
"C:\Program Files\Dyalog\Dyalog APL-64 13.2 Unicode\dyalog.exe"
```
```apl
      ⎕←2 ⎕NQ '.' 'GetCommandLine'
"C:\Program Files\Dyalog\Dyalog APL-64 13.2 Unicode\dyalog.exe"
```

## Note

GetCommandLine only works on Windows, and its use is deprecated in favour of [GetCommandLineArgs](getcommandlineargs.md), which works on all platforms.
