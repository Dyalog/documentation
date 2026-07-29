#  Out-of-process OLE Servers

## Exporting

When you use File/Export to create an *out-of-process* OLE Server, the following steps are performed.

APL first creates a single Type Library File that describes all the OLEServer objects in the workspace. It then registers your OLE Server by updating the Windows Registry with, among other things, the names and ClassIDs of your workspace and Type Library file.

Note that the type information is taken from your active workspace and not the saved workspace. It is up to you to ensure that your saved workspace (which will actually be used when the OLE Server is invoked) is kept in step.

For example, if you were subsequently to remove the OLEServer objects from your workspace and re-save it, or save a completely different workspace with the same pathname, your OLE Server would fail to start because the Type Library and Registry and no longer synchronised with your workspace.

## Execution

An out-of-process OLE Server is implemented by a separate Dyalog APL process (DYALOG.EXE or DYALOGRT.EXE) that loads your workspace when it starts.

If an out-of-process OLE Server, that is bound with the *run-time* Dyalog APL program, generates an untrapped error, an OLE Automation error will be reported.

If an out-of-process OLE Server, that is bound with the *development* Dyalog APL program, generates an untrapped error, the APL Session will appear, and you can use it to debug the problem and continue. In previous versions of Dyalog APL, the visibility of the APL Session for debugging was controlled by the ShowSession property. Setting ShowSession to 1 will cause the Session to be displayed immediately, when the OLE Server is started. However, setting ShowSession to 0 will not prevent the Session from appearing if an untrapped APL error occurs.

## Registering and Unregistering

During development, an out-of-process OLE Server is automatically registered when you create it using *File/Export*.

An out-of-process OLEServer may also be registered  by calling its OLERegister method. This performs the same tasks as *File/Export*, but without any user-interaction. OLERegister is the recommended way to install an *out-of-process* OLEServer on a target computer as a run-time application.

An out-of-process OLEServer may be unregistered by calling its OLEUnRegister method.

## Registry Entries

This section describes the entries that are written into the Windows Registry when APL registers an *out-of-process* OLEServer.

All registry entries are written as sub-keys of the primary key `HKEY_LOCAL_MACHINE\SOFTWARE\Classes` of which `HKEY_CLASSES_ROOT` is an alias. Four separate entries are created, although only the first of these applies to top-level OLEServers.

1. A sub-key named **dyalog.xxxx** where **xxxx** is the name of the OLEServer. This has a sub-key named **CLSID** whose *Default* value is a GUID corresponding to the ClassID property of the OLEServer.
2. A sub-key named **CLSID\xxxx** where **xxxx** is the GUID corresponding to the value of the ClassID property of the OLEServer. The *Default* value of this sub-key is the name of the OLEServer, and the sub-key itself contains sub-keys, namely **DyalogDispInterface**, **DyalogEventInterface, InProcHandler32**, **LocalServer32**, **ProgID**, **TypeLib**, and **VersionIndependentProgID**.
	1. **DyalogDispInterface** and **DyalogEventInterface** have their *Default* values set to the GUID for the Interface entry (see Paragraph 4). This GUID is generated internally by the registration of the Type Library.
	2. **InProcHandler32** has the *Default* value "OLE32.DLL".
	3. **LocalServer32** has its *Default* value set to the command line that is required to start the OLEServer. This is the full path-name of the appropriate DYALOG.EXE or DYALOGRT.EXE followed by the full path-name of the corresponding workspace plus any options that were specified in the *Create bound file* dialog box.
	4. **ProgID** has its *Default* value set to "dyalog.xxxx" where "xxxx" is the name of the OLEServer.
	5. **TypeLib** has its *Default* value set to the GUID corresponding to the TypeLibID property of the OLEServer.
	6. **VersionIndependentProgID** has its *Default* value set to "dyalog.xxxx" where "xxxx" is the name of the OLEServer (same as **ProgID**).
	7. Note that for a sub-object (an OLEServer that is a child of another OLEServer) only the **InProcHandler32** key is required, although the other entries are created and are in fact redundant.
3. A sub-key named **TypeLib\xxxx** where **xxxx** is the GUID corresponding to the value of the TypeLib property of the OLEServer. This contains a sub-key named **1.0** (which refers to its version number). The *Default* value of **1.0** is "Type Library for xxxx" where "xxxx" is the name of the OLEServer. **1.0** contains three further sub-keys named **0**, **FLAGS** and **HELPDIR**.
	1. **0** (this identifies the language id; 0 refers to *all* languages) contains a sub-key named **win32** whose *Default* value is the full path-name of the Type Library file associated with the OLE object; i.e. the value of the TypeLibFile property of the OLEServer.
	2. **FLAGS** has a *Default* value of "0".
	3. **HELPDIR** has its *Default* value set to the full path-name of the directory in which the corresponding workspace is saved.
4. Sub-keys named **Interface\xxxx** where **xxxx** is the GUID referenced by the value of **DyalogDispInterface** and **DyalogEventInterface** described in paragraph 2. The *Default* values of these sub-keys is "xxxxdisp" where "xxxx" is the name of the OLEServer. You may identify the correct **Interface** sub-key by searching the registry for this string. It has three sub-keys named **ProxyStubClsid**, **ProxyStubClsid32**, and **TypeLib**.
	1. **ProxyStubClsid** has a *Default* value of a GUID that references an interface of type PSDispatch.
	2. **ProxyStubClsid32** (same as **ProxyStubClsid**).
	3. **TypeLib** has two values. Its *Default* value is the GUID identified by the TypeLib property of the OLEServer object, or, for a child OLEServer, the TypeLib property if its parent OLEServer. Its *Version* value is "1.0".
