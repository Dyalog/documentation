# Locating .NET Classes and Assemblies

.NET assemblies and the classes they contain are generally self-contained independent entities (although they can be based upon classes in other assemblies). This means that a class can be installed by copying the assembly file onto hard disk and uninstalled by erasing the file.

Microsoft supplies a tool for browsing .NET class libraries called **ildasm.exe** (Intermediate Language Disassembler). On Microsoft Windows, ILDASM has a GUI front end; it can be found in the .NET SDK and is distributed with Visual Studio. For other platforms, ILDASM is available as a command line tool that can be downloaded from [https://www.nuget.org/packages/runtime.linux-x64.Microsoft.NETCore.ILDAsm/](https://www.nuget.org/packages/runtime.linux-x64.Microsoft.NETCore.ILDAsm/).

Although classes are arranged physically into assemblies, they are also arranged logically into namespaces. These are not related to Dyalog's namespaces and, to avoid confusion, are referred to in this document as .NET namespaces.

A single .NET namespace can map onto a single assembly. For example, the .NET namespace System.IO is contained in an assembly named **System.IO.FileSystem.dll**. However, a .NET namespace can be implemented by more than one assembly, removing the one-to-one-mapping between .NET namespaces and assemblies. For example, the main top-level .NET namespace, **System**, spans a number of different assembly files.

Within a single .NET namespace there can be numerous classes, each with its own unique name. The full name of a class is the name of the class prefixed by the name of the .NET namespace and a dot (the namespace name can also be delimited by dots). For example, the full name of the DateTime class in the .NET namespace System is System.DateTime. Any number of different versions of an assembly can be installed on a single computer, and there can be multiple .NET namespaces with the same name, implemented in different sets of assembly files.

To use a .NET class, it is necessary to tell the system to load the assembly in which it is defined. In many languages (including C#) this is done by supplying the names of the assemblies. To avoid having to refer to full class names, C# allows the .NET namespace prefix to be elided. In this case, the programmer must declare a list of .NET namespaces with `using` declaration statements. This list is then used to resolve unqualified class names referred to in the code. In either language, when the compiler encounters the unqualified name of a class, it searches the specified .NET namespaces for that class. In Dyalog, this mechanism is implemented by the `⎕USING` system variable. `⎕USING` performs the same two tasks that `using/imports` declarations provide in C#; that is, to give a list of .NET namespaces to be searched for unqualified class names and to specify the assemblies that are to be loaded.

`⎕USING` is a vector of character vectors, each element of which contains 1 or 2 comma‑delimited strings. The first string specifies the name of a .NET namespace; the second specifies the assembly either with a file name (the string ends with the extension **.dll**) or with an assembly name. If an assembly name is given, standard .NET rules are used to locate the assembly.

It is convenient to treat .NET namespaces and assemblies in pairs. For example, the System.IO namespace is located within the System.IO.FileSystem assembly.

`⎕USING` has namespace scope, that is, each Dyalog namespace, class or instance has its own value of `⎕USING` that is initially inherited from its parent space but can be separately modified. `⎕USING` can also be localised in a function header so that different functions can declare different search paths for .NET namespaces/assemblies.

If `⎕USING` is empty (`⎕USING←0⍴⊂''`), then Dyalog does not search for .NET classes to resolve names that would otherwise give a `VALUE ERROR`.

Assigning a simple character vector to `⎕USING` is equivalent to setting it to the enclose of that vector. The statement (`⎕USING←'')` does not empty `⎕USING`, but rather sets it to a single empty element, which gives access to the **System.Runtime** and **System.Private.CoreLib** assembly files without a namespace prefix.
