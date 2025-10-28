<h1 class="heading"><span class="name">Isolation Mode</span></h1>

For *each* application which uses a class written in Dyalog APL, at least one copy of the development or run-time version of the Dyalog DLL   will be started in order to host and execute the appropriate APL code. Each of these *engines* will have an APL workspace associated with it, and this workspace will contain classes and instances of these classes. The number of engines (and associated workspaces) which are started will depend on the Isolation Mode which was selected when the APL assemblies used by the application were generated. Isolation modes are:

- Each host process has a single workspace
- Each appdomain has its own workspace
- Each assembly has its own workspace 

Note that, in this context, Microsoft Internet Information Services (IIS) is a *single process*, even though it may be hosting a large number of different web pages. Each ASP.NET application will be running in a separate *AppDomain*, a mechanism used by .NET to provide isolation within an application. Other .NET applications may also be divided into different AppDomains.

In other words, if you use the first option, ALL classes and instances used by any IIS web page will be hosted in the same workspace and share a single copy of the interpreter. The second option will start a new Dyalog engine for each ASP.NET application; the final option an engine for each assembly containing APL classes.
