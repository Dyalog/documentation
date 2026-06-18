<h1 class="heading"><span class="name">Isolation Mode</span></h1>

For each application that uses a class written in Dyalog, at least one copy of the development or run-time version of the Dyalog DLL will be started to host and execute the appropriate APL code. Each of these _engines_ will have an APL workspace associated with it, and this workspace will contain classes and instances of these classes. The number of engines (and associated workspaces) that are started depends on the _isolation mode_ that was selected when the APL assemblies used by the application were generated. When running under IIS, it is also possible to specify the isolation mode by setting the <code class="language-nonAPL">DyalogIsolationMode</code> key to the appropriate value in the <code class="language-nonAPL">AppSettings</code> part of the **web.config** file for the web application.

For example:
```nonAPL
<appSettings>
.
.
.
<add key="DyalogIsolationMode" value="DyalogIsolationProcess" />
.
.
.
</appSettings>
```

The possible isolation modes (and their <code class="language-nonAPL">DyalogIsolationMode</code> values) are:

- <code class="language-nonAPL">DyalogIsolationAssembly</code> – each assembly has its own Dyalog DLL and workspace. This means that a new engine is started for each assembly containing APL classes.
- <code class="language-nonAPL">DyalogIsolationApplication</code> – each web application/AppDomain has its own Dyalog DLL and workspace. This means that, when running in IIS, a new engine is started for each ASP.NET application. In this context, Microsoft Internet Information Services (IIS) is a single process, even though it might be hosting a large number of different web pages. Each ASP.NET application will run in a separate AppDomain, a mechanism used by .NET to provide isolation within an application. Other .NET applications might also be divided into different AppDomains.
- <code class="language-nonAPL">DyalogIsolationProcess</code> – each process has its own Dyalog DLL and workspace (this is the default). This means that all classes and instances used by any IIS web page will be hosted in the same workspace and share a single copy of the interpreter.
- <code class="language-nonAPL">DyalogIsolationLocal</code> – each assembly attempts to use the local bridge and interpreter libraries.
