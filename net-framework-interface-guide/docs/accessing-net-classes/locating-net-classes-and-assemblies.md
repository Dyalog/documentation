<h1 class="heading"><span class="name">Locating .NET Classes and Assemblies</span></h1>

Unlike COM objects, which are referenced via the Windows Registry, .NET assemblies and the classes they contain, are generally self-contained independent entities (they can be based upon classes in other assemblies). In simple terms, you can install a class on your system by copying the assembly file onto your hard disk and you can de-install it by erasing the file.

Although classes are arranged physically into assemblies, they are also arranged logically into namespaces. These have nothing to do with Dyalog namespaces and, to avoid confusion, are henceforth referred to in this document as .NET namespaces.

Often, a single .NET namespace maps onto a single assembly and usually, the name of the .NET namespace and the name of its assembly file are the same; for example, the .NET namespace `System.Windows.Forms` is contained in an assembly named `System.Windows.Forms.dll`.

However, it is possible for a .NET Namespace to be implemented by more than one assembly; there is not a one-to-one-mapping between .NET Namespaces and assemblies. Indeed, the main top-level .NET Namespace, `System`, is spread over a number of different assembly files.

Within a single .NET Namespace there can be any number of classes, but each has its own unique name. The full name of a class is the name of the class itself, prefixed by the name of the .NET namespace and a dot. For example, the full name of the `DateTime` class in the .NET namespace `System` is `System.DateTime`.

There can be any number of different versions of an assembly installed on your computer, and there can be several .NET namespaces with the same name, implemented in different sets of assembly files; for example, written by different authors.

To use a .NET Class, it is necessary to tell the system to load the assembly (`dll`) in which it is defined. In many languages (including C#) this is done by supplying the *names* of the assemblies or the *pathnames* of the assembly files as a compiler directive.

Secondly, to avoid the verbosity of programmers having to always refer to full class names, the C# and Visual Basic languages allow the .NET namespace prefix to be elided. In this case, the programmer must declare a list of .NET namespaces with `Using` (C#) and `Imports` (Visual Basic) declaration statements. This list is then used to resolve unqualified class names referred to in the code.

In either language, when the compiler encounters the unqualified name of a class, it searches the specified .NET namespaces for that class.

In Dyalog, this mechanism is implemented by the `⎕USING` system variable. `⎕USING` performs the same two tasks that `Using/Imports` declarations and compiler directives provide in C# and Visual Basic; namely to give a list of .NET namespaces to be searched for unqualified class names, and to specify the assemblies which are to be loaded.

`⎕USING` is a vector of character vectors each element of which contains 1 or 2 comma-delimited strings. The first string specifies the name of a .NET namespace; the second specifies the *pathname* of an assembly file. This may be a full pathname or a relative one, but must include the file extension (`.dll`). If just the file name is specified, it is assumed to be located in the standard  .NET Framework directory that was specified when the .NET Framework was installed (for example, `C:\Windows\Microsoft.NET\Framework64\v4.0.30319`)

It is convenient to treat .NET namespaces and assemblies in pairs. For example:
```apl
⎕USING←'System,mscorlib.dll'
⎕USING,←⊂'System.Windows.Forms,System.Windows.Forms.dll'
⎕USING,←⊂'System.Drawing,System.Drawing.dll'
```

Note that because Dyalog APL automatically loads `mscorlib.dll` (which contains the most commonly used classes in the `System` Namespace), it is not actually necessary to specify it explicitly in `⎕USING`.

`⎕USING` has Namespace scope, that is, each Dyalog namespace, class or instance has its own value of `⎕USING` that is initially inherited from its parent space but which may be separately modified. `⎕USING` may also be localised in a function header, so that different functions can declare different search paths for .NET namespaces/assemblies.

If `⎕USING` is empty (`⎕USING←0⍴⊂''`), APL will not search for .NET classes in order to resolve names which would otherwise give a `VALUE ERROR`.

Assigning a simple character vector to `⎕USING` is equivalent to setting it to the enclose of that vector. The statement (`⎕USING←'')` does not empty `⎕USING`, it sets it to a single empty element, which gives access to `mscorlib.dll` and the  Bridge DLL without a namespace prefix.

Within a Class script, you may instead employ one or more `:Using` statements to specify the .NET search path. Each of these statements is equivalent to appending an enclosed character vector to `⎕USING`.
```apl
     :Using System,mscorlib.dll
     :Using System.Windows.Forms,System.Windows.Forms.dll
     :Using System.Drawing,System.Drawing.dll
```

Classes also inherit from the namespace they are contained in. The statement
```apl
     :Using
```

Is equivalent to
```apl
     ⎕USING←0⍴⊂''
```

…and allows a class to clear the inherited value before appending to `⎕USING`, or to state that no .NET assemblies should be loaded.

The equivalent to `⎕USING←''` is a `:Using` statement followed by a comma separator but no namespace prefix and no assembly name:
```apl
    :Using ,
```
