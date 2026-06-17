<h1 class="heading"><span class="name">Locating .NET Classes and Assemblies</span></h1>

Unlike COM objects, which are referenced through the Mictrosoft Windows Registry, .NET assemblies and the classes they contain are generally self-contained independent entities (although they can be based upon classes in other assemblies). This means that a class can be installed by copying the assembly file onto hard disk and uninstalled by erasing the file.

Although classes are arranged physically into assemblies, they are also arranged logically into namespaces. These are not related to Dyalog's namespaces and, to avoid confusion, are referred to in this document as .NET namespaces.

A single .NET namespace can map onto a single assembly. In this situation, the name of the .NET namespace and the name of its assembly file are usually the same; for example, the .NET namespace <code class="language-nonAPL">System.Windows.Forms</code> is contained in an assembly named **System.Windows.Forms.dll**. However, it is possible for a .NET namespace to be implemented by more than one assembly; there is not a one-to-one-mapping between .NET Namespaces and assemblies. For example, the main top-level .NET namespace, <code class="language-nonAPL">System</code>, is spread over a number of different assembly files.

Within a single .NET namespace there can be numerous classes, each with its own unique name. The full name of a class is the name of the class prefixed by the name of the .NET namespace and a dot (the namespace name can also be delimited by dots). For example, the full name of the <code class="language-nonAPL">DateTime</code> class in the .NET namespace <code class="language-nonAPL">System</code> is <code class="language-nonAPL">System.DateTime</code>. Any number of different versions of an assembly can be installed on a single computer, and there can be multiple .NET namespaces with the same name, implemented in different sets of assembly files.

To use a .NET class, it is necessary to tell the system to load the assembly (**.dll** file) in which it is defined. In many languages (including C#) this is done by supplying the _names_ of the assemblies. To avoid having to refer to full class names, the C# and Visual Basic languages allow the .NET namespace prefix to be elided. In this case, you must declare a list of .NET namespaces with <code class="language-nonAPL">Using</code> (C#) and <code class="language-nonAPL">Imports</code> (Visual Basic) declaration statements. This list is then used to resolve unqualified class names referred to in the code. In either language, when the compiler encounters the unqualified name of a class, it searches the specified .NET namespaces for that class. In Dyalog, this mechanism is implemented by the `⎕USING` system variable. `⎕USING` performs the same two tasks that <code class="language-nonAPL">Using</code>/<code class="language-nonAPL">Imports</code> declarations and compiler directives provide in C# and Visual Basic; that is, to give a list of .NET namespaces to be searched for unqualified class names and to specify the assemblies that are to be loaded.

`⎕USING` is a vector of character vectors, each element of which contains 1 or 2 comma‑delimited strings. The first string specifies the name of a .NET namespace; the second specifies the pathname of the assembly. The pathname can be fully-qualified or ralative, but must include the file extension (**.dll**). If just the filename is specified, then Dyalog assumes that it is located in the standard .NET Framework directory that was specified when .NET Framework was installed (for example, **C:\Windows\Microsoft.NET\Framework64\v4.0.30319**).

It is convenient to treat .NET namespaces and assemblies in pairs. For example:
```apl
⎕USING←'System,mscorlib.dll'
```
```apl
⎕USING,←⊂'System.Windows.Forms,System.Windows.Forms.dll'
⎕USING,←⊂'System.Drawing,System.Drawing.dll'
```

!!! Info "Information"
    Dyalog automatically loads **mscorlib.dll** (which contains the most commonly used classes in the <code class="language-nonAPL">System</code> namespace), so it is not necessary to specify it explicitly in `⎕USING`.

`⎕USING` has namespace scope, that is, each Dyalog namespace, class or instance has its own value of `⎕USING` that is initially inherited from its parent space but can be separately modified. `⎕USING` can also be localised in a function header so that different functions can declare different search paths for .NET namespaces/assemblies.

If `⎕USING` is empty (`⎕USING←0⍴⊂''`), then Dyalog does not search for .NET classes to resolve names that would otherwise give a `VALUE ERROR`.

Assigning a simple character vector to `⎕USING` is equivalent to setting it to the enclose of that vector. The statement (`⎕USING←'')` does not empty `⎕USING`, but rather sets it to a single empty element, which gives access to **mscorlib.dll** and the Bridge library without a namespace prefix.

Within a Class script, you can employ one or more `:Using` statements to specify the .NET search path. Each of these statements is equivalent to appending an enclosed character vector to `⎕USING`. For example:
```apl
      :Using System,mscorlib.dll
      :Using System.Windows.Forms,System.Windows.Forms.dll
      :Using System.Drawing,System.Drawing.dll
```

Classes also inherit from the namespace that they are contained in. This means that the following statement:
```apl
      :Using
```

is equivalent to:
```apl
      ⎕USING←0⍴⊂''
```

and allows a class to clear the inherited value before appending to `⎕USING`, or to state that no .NET assemblies should be loaded.

The equivalent to `⎕USING←''` is a `:Using` statement followed by a comma separator with no namespace prefix and no assembly name:
```apl
      :Using ,
```
