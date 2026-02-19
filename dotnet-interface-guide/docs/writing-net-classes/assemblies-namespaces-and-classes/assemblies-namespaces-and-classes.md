# Assemblies, Namespaces, and Classes

To create a .NET class in Dyalog, create a standard APL class and export the workspace as a .NET assembly (***.dll**).

Exporting APL code to .NET assemblies is only supported on 64-bit versions of Dyalog.

.NET classes are organised in .NET namespaces. If you wrap your class (or classes) within an APL namespace, the name of that namespace will be used to identify the name of the corresponding .NET namespace in your assembly.

If a class is to be based upon a specific .NET class, then the name of that .NET class must be specified as the base class in the `:Class` statement, and the `:Using` statements must correctly locate the base class. Otherwise, the class is assumed to be based on System.Object. If you use any .NET types within your class, you must ensure that these too are located by `:Using`.

Once you have defined the functionality of your .NET classes, you can save them in an assembly. This is achieved in one of the following ways:

- Select Export... from the Session's File menu. You will be prompted to specify the directory and name of the assembly (DLL), and it will then be created and saved.

- Use the Bind method (see [Section ](the-bind-method.md)).
- Use the Dyalog .NET Compiler (see [Section ](creating-dotnet-classes-with-apl-source-files.md)).

Your .NET class is now ready for use by any .NET development environment, including APL.

When a Dyalog .NET class is invoked by a host application, it automatically loads the Dyalog DLL, which is the developer/debug or run-time dynamic link library version of Dyalog. The Dyalog .NET class, and all the Dyalog DLLs on which it depends, reside in the same directory as the host program.

If you want to include a Dyalog .NET class in a Visual Studio application, Dyalog Ltd recommends that you add the bridge DLL as a reference in a Visual Studio .NET project.
If you want to repeat the most recent export after making changes to the class, you can click on the icon to the right of the save icon on the WS button bar at the top of the session. The workspace is not saved when you do an export, so if you want the export options to be remembered you must `)SAVE` the workspace after you have exported it.
