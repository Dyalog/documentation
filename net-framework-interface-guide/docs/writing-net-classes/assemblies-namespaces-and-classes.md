<h1 class="heading"><span class="name">Assemblies, Namespaces and Classes</span></h1>

To create a .NET class in Dyalog, you simply create a standard APL Class and export the workspace as a *Microsoft .NET Assembly (*.dll)*.

.NET Classes are organised in .NET Namespaces. If you wrap your Class (or Classes) within an APL namespace, the name of that namespace will be used to identify the name of the corresponding .NET Namespace in your Assembly.

If a Class is to be based upon a specific .NET Class, the name of that .NET Class must be specified as the Base Class in the `:Class` statement, and the `:Using` statements must correctly locate the base class. If not, the Class is assumed to be based upon System.Object. If you use any .NET Types within your Class, you must ensure that these too are located by :Using.

Once you have defined the functionality of your .NET classes, you are ready to save them in an assembly. This is simply achieved by selecting *Export* from the Session *File* menu.

You will be prompted to specify the directory and name of the assembly (DLL) and it will then be created and saved. Your .NET class is now ready for use by any .NET development environment, including APL itself.

When a Dyalog .NET class is invoked by a host application, it automatically loads the Dyalog DLL, the developer/debug or run-time dynamic link library version of Dyalog. You decide which of these DLLs is to be used according to the setting of the *Runtime application* checkbox in the *Create bound file* dialog box. Note however that the Dyalog .NET class, and all the Dyalog DLLs on which it depends, reside in the same directory as the host program.

Note that if you wish to include a Dyalog .NET class in a Visual Studio application it is recommended that you add the  Bridge DLL as a reference in a  Visual Studio .NET project.

If you want to repeat the most recent export after making changes to the class, you can click on the icon to the right of the save icon on the WS button bar at the top of the session.  Note that the workspace itself is not saved when you do an export, so if you want the export options to be remembered you must `)SAVE` the workspace *after* you have exported it.
