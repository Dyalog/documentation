<h1 class="heading"><span class="name">Workspace Size</span></h1>

By default, there is no limit on the size of the workspace used by the Dyalog DLL, and it will grow (and shrink) according to user demand.

The maximum workspace size can be specified by the MAXWS configuration parameter in both the development and run-time versions of Dyalog. The difference is that MAXWS must be specified for the host application, the application in which the Dyalog DLL is embedded.

This is achieved by defining a Registry key named:
```
HKLM\Software\Dyalog\Embedded\<appname>
```

or, for 32-bit Dyalog on 64-bit Windows only:
```
HKLM\Software\Wow6432Node\Dyalog\Embedded\<appname>
```

where `<appname>` is the name of the application, containing a string value `maxws` that is set to the desired size.

The name of the ASP.NET application is **aspnet_wp.exe** (IIS 5.1 and earlier) or **w3wp.exe** (IIS 6.0 and later).

An additional way to set MAXWS is on the command line of the assembly at export time. This is convenient if you know that you are only using one Dyalog assembly or what the [IsolationMode](isolation-mode.md) is for each assembly.
