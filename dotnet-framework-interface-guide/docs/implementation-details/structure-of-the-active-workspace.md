<h1 class="heading"><span class="name">Structure of the Active Workspace</span></h1>

Each engine has a workspace associated with it that contains all the APL objects it is currently hosting.

Unless the highest isolation mode (DyalogIsolationAssembly – see [Isolation Mode](isolation-mode.md)) has been selected, the workspace will contain one or more namespaces associated with .NET AppDomains. When the .NET Framework calls Dyalog to process an APL class, it specifies the AppDomain in which it is to be executed. To maintain AppDomain isolation and scope, Dyalog associates each different AppDomain with a namespace whose name is that of the AppDomain, prefixed by `AppDomain_`.

Within each `AppDomain_` namespace, there will be one or more namespaces associated with the different assemblies from which the APL classes have been loaded. These namespaces are named by the assembly name and prefixed by `Assembly_`. If the APL class is a web page or a web service, the corresponding assembly is created dynamically when the page is first loaded. In this case, the name of the assembly itself is manufactured by .NET. Below the `Assembly_` namespace is a namespace that corresponds to the .NET namespace representing the container of your class. If the APL class is a web page or web service, this namespace is called `ASP`. Finally, the namespace tree ends with a namespace that represents the APL class. This will have the same name as the class. In the case of a web page or web service, this is the name of the **.aspx** or **.asmx** file.

!!! Info "Information"
    In the manufactured namespace names, characters that would be invalid symbols in a namespace name are replaced by underscores.

The image below shows the namespace tree that exists in the Dyalog DLL workspace when the example in [Tutorial: Example 1](../../writing-dotnet-classes/tutorial/#example-1) is executed under Visual Studio. To cause the suspension, an error has been introduced in the method `IndexGen`. In this example, there is a single AppDomain involved whose name (**DyApp_vshost_exe**) is specified by .NET. APL has made a corresponding namespace called **AppDomain_DyApp_vshost_exe**. Next, there is a namespace associated with the assembly 'aplclasses', called `Assembly_aplclasses`. Beneath this is a namespace called `APLClasses` associated with the .NET namespace of the same name. Finally, there is the APL Class called `Primitives`.

The state indicator displays the entire .NET calling structure, not just the APL stack. In this example, the state indicator shows that `IndexGen` was called from `MainClass.Main`, which combines the class and method names specified in **aplfns.cs**. .NET calls are slightly indented.

`IndexGen` has been started on APL thread 1 which, in this case, is associated with system thread 8752. If the client application called `IndexGen` on multiple system threads, this would be reflected by multiple APL threads in the workspace – see [Threading](threading.md) for more information.

The possibility for the client to execute code in several instances of an object at the same time requires that each executing instance is separated from all the others. Each instance will be created as an _unnamed_ object in the workspace, within the relevant appdomain and assembly namespaces.

![Structure when each host process has a single workspace](../img/s-ws-structure.png)

The image below shows the workspace structure when the assembly was generated with isolation mode set to "Each assembly has its own workspace". In this case, the AppDomain and Assembly structure is not created above the classes in the workspace, so the workspace structure is simpler.

![Structure when each assembly has its own workspace](../img/s-ws-structure-simple.png)
