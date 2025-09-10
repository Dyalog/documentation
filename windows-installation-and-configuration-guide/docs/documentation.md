<h1 class="heading"><span class="name">Documentation</span></h1>

The documentation set for Dyalog is installed in the `help` sub-directory of the main Dyalog installation directory.

The latter is given by the expression:
```apl
      ⎕←2 ⎕NQ'.' 'GetEnvironment' 'DYALOG'
C:\Program Files\Dyalog\Dyalog APL-64 15.0 Unicode
```

<h2 class="example">Example</h2>
```apl

      dyalog←2⎕NQ'.' 'GetEnvironment' 'DYALOG'
      ⎕CMD 'dir "',dyalog,'/help"'
 Volume in drive C is OS
 Volume Serial Number is 3013-866E

 Directory of C:\Program Files\Dyalog\Dyalog APL-64 15.0 Unicode\help

18/01/2016  11:53    <DIR>          .
18/01/2016  11:53    <DIR>          ..
11/01/2016  17:20           182,965 APL Workspace Transfer Guide.pdf
11/01/2016  17:20           467,005 Application Tuning Guide.pdf
11/01/2016  17:20           587,605 Code Libraries Reference Guide.pdf
11/01/2016  17:20           249,461 Compiler User Guide.pdf
11/01/2016  17:20           451,949 Conga User Guide.pdf
...
```
