<h1 class="heading"><span class="name">Execution</span></h1>

When your Web Service (or Page) is invoked, ASP.NET requests an instance of the corresponding Class from the Assembly (DLL) that was created when it was compiled. The first time this happens for any Dyalog Web Service or Web Page, the Dyalog dynamic link library  is loaded into the ASP.NET host process and the namespace corresponding to your Web Service class is `)COPYed` from the Assembly. The Dyalog dynamic link library then delivers an instance of this namespace to the client (calling) process. See [Introduction](../implementation-details/introduction.md) for further details.

In general, every call on a method in a Web Service causes a new instance of the Web Server class to be created. If you need to maintain/update variables between calls, you need to write them to permanent storage.

If a client invokes a different Dyalog Web Service or Web Page, its class is `)COPY`ed from its Assembly into the workspace managed by the Dyalog dynamic link library. When you export a class, you can select one of three Isolation Modes:

1. Each host process has a single workspace
2. Each AppDomain has its own workspace
3. Each Assembly has its own workspace

In this context, "workspace" is synonymous with "Dyalog process": Each workspace is managed by a separate process running dyalog.dll. Under option 1, all Dyalog APL Web Services (and Web Pages) hosted by the IIS host process share the same workspace when they are invoked.

The isolation mode selected has implications for the way that you access and manage global resources such as component files. Finer isolation modes may be implemented in future versions of Dyalog.
