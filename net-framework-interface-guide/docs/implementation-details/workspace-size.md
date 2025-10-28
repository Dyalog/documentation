<h1 class="heading"><span class="name">Workspace Size</span></h1>

By default, there is no limit placed upon the size of the workspace  used by the Dyalog DLL and it will grow (and shrink) according to user demand.

The maximum workspace size may be specified by the **maxws** parameter that is used to control the workspace size in the development and run-time versions of the Dyalog program. The difference is that the **maxws** parameter must be specified for the **host application**, the application in which the Dyalog DLL is embedded.

This is achieved by defining a Registry key named:
```apl
HKLM\Software\Dyalog\Embedded\<appname>
```

or on 64-bit Windows:
```apl
HKLM\Software\Wow6432Node\Dyalog\Embedded\<appname>
```

where `<appname>` is the name of the application, containing a String Value named `maxws` set to the desired size.

The name of the ASP.NET application is aspnet_wp.exe or w3wp.exe ((IIS 6 and above).

An additional way is to set the **maxws** parameter on the command line of the Assembly at export time. That might be be useful if you know that you are only using one Dyalog assembly or the IsolationMode is "Each Assembly". For more information, see [Isolation Mode](isolation-mode.md).
