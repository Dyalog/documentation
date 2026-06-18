<h1 class="heading"><span class="name">Assemblies, Namespaces, and Classes</span></h1>

To create a .NET class in Dyalog, create a standard APL class and export the workspace as a Microsoft .NET assembly (***.dll**).

.NET classes are organised in .NET namespaces. If you wrap your class (or classes) within an APL namespace, the name of that namespace will be used to identify the name of the corresponding .NET namespace in your assembly.

If a class is to be based upon a specific .NET class, then the name of that .NET class must be specified as the base class in the `:Class` statement, and the `:Using` statements must correctly locate the base class. Otherwise, the class is assumed to be based on <code class="language-nonAPL">System.Object</code>. If you use any .NET types within your class, you must ensure that these too are located by `:Using`.

Once you have defined the functionality of your .NET classes, you can save them in an assembly. This is achieved by doing one of the following:

- Selecting **Export...** from the **Session**'s **File** menu. You will be prompted to specify the directory and name of the assembly (DLL), and it will then be created and saved.

- Using the [Bind method](#the-bind-method).
- Using the [Dyalog .NET Compiler ](../../apl-source-files/the-dyalog-dotnet-compiler/).

Your .NET class is now ready for use by any .NET development environment, including APL.

When a Dyalog .NET class is invoked by a host application, it automatically loads the Dyalog DLL, which is the developer/debug or run-time dynamic link library version of Dyalog. You decide which of these DLLs is to be used according to the setting of the **Runtime application** checkbox in the **Create bound file** dialog box. The Dyalog .NET class, and all the Dyalog DLLs on which it depends, reside in the same directory as the host program.

!!! Info "Information"
    If you want to include a Dyalog .NET class in a Visual Studio application, Dyalog Ltd recommends that you add the bridge DLL as a reference in a Visual Studio .NET project.
	
If you want to repeat the most recent export after making changes to the class, you can click on the icon to the right of the save icon on the WS button bar at the top of the session. The workspace is not saved when you do an export, so if you want the export options to be remembered you must `)SAVE` the workspace after you have exported it.

## The Bind Method

The `Bind` method is described in the _Dyalog for Microsoft Windows Object Reference Guide_. A subset of the `Bind` method can be used on any supported platform to export .NET assemblies. Specifically, the expression:
```apl
      2 ⎕NQ '.' 'Bind' <filename> 'Library'
```
creates a .NET assembly (in `<filename>`) that contains the APL code in the classes in the active workspace

This use of the `Bind` method is similar to selecting **File** > **Export...** in the **Session**.
