<h1 class="heading"><span class="name">Introduction</span></h1>

The Dyalog DLL is the Dyalog APL *engine* that hosts the execution of all .NET classes that have been written in Dyalog APL, including APL Web Pages and APL Web Services. The Dyalog DLL provides the interface between client applications (such as ASP.NET) and your APL code. It receives calls from client applications, and executes the appropriate APL code. It also works the other way, providing the interface between your APL code and any .NET classes that you may call.

The Development DLL (the full developer version of the Dyalog DLL) contains the APL Session, Editor, Tracer and so forth, and may be used to develop and debug an APL .NET class while it is executing. Note that to gain access to the various workspace tools, such as the Workspace Explorer and the Search/Replace Dialog, the corresponding DyaRes DLL must be present alongside (in the same directory as) the Development DLL.

The Run-Time DLL (the re-distributable run-time version of the Dyalog DLL) contains no debugging facilities.

For the names of these files corresponding to the version of Dyalog that you are using, see [Files](../../../windows-installation-and-configuration-guide/files-and-directories).
