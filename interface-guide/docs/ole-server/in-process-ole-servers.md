# In-process OLE Servers

## Exporting

When you use File/Export to create an *in-process* OLE Server, the following steps are performed.

APL first saves your workspace to a *temporary* file. Then it creates a *temporary* Type Library File that describes each of the OLEServer objects in the workspace. Next, it creates a Dynamic Link Library (DLL) file (whose name defaults to the name of your workspace but with a .DLL extension) by merging  the workspace saved in the temporary file with the file dllstub.dll. Finally, it registers your OLE Server by updating the Windows Registry. Your OLE Server DLL is self-contained and is independent of your workspace. The temporary files are then deleted.

## Execution

In-process OLEServers are hosted (executed) by the Dyalog APL DLL. If you export your OLE Server with *Runtime application* checked, it will be bound with the run-time version, If this checkbox is cleared, your OLE Server will be bound by the development version.

If an in-process OLE Server, that is bound with the run-time Dyalog APL DLL generates an untrapped error, an OLE Automation error will be reported.

If an in-process OLE Server, that is bound with the development Dyalog APL DLL generates an untrapped error, the APL Session will appear and you can use it to debug the problem and continue. Note that at this point, the development DLL will load your Session file so that all of your session tools are available during debugging. If your Session file runs any initialisation code that references external files, remember that this code will be executed in the current working directory of the host process.

For further details, see Dyalog for Microsoft Windows Installation and Configuration Guide.

## Registering and Unregistering In-Process OLE Servers

During development, an in-process OLE Server is automatically registered when you create it using *File/Export*.

The Windows utility regsvr32.exe should be used to register an *in-process* OLE Server independently, or to install a runtime in-process OLE Server on a target computer. For example:

```
C:\WINDOWS\System32>regsvr32 c:\MyWS\mysvr.dll
```

regsvr32 should also be used (with the */u* flag) to unregister an in-process OLE Server. For example:

```
C:\WINDOWS\System32>regsvr32 /u c:\MyWS\mysvr.dll
```

Note that in both cases, regsvr32 actually starts the OLE Server. This in turn loads the appropriate Dyalog APL DLL. If you are using the development DLL, note that if your session start-up code fails for any reason, the regsvr32 process will hang and have to be terminated using the Task Manager.
