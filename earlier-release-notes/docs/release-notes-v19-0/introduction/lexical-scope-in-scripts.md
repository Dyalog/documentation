<h1 class="heading"><span class="name">Lexical Scope in Scripts</span></h1>

## Historical Note

Lexical scope in scripts has been part of Dyalog since the implementation of Object Oriented Programming in Version 11.0, and is only partially documented.  See [Namespace Scripts](https://help.dyalog.com/19.0/index.htm#Language/Object%20Oriented%20Programming/Namespace%20Scripts/Namespace%20Scripts.htm#NamespaceScripts). This section provides additional explanation and extends the discussion to Classes.

## Introduction

Objects (Namespaces and Classes) that are defined using scripts, either in the workspace or in script files, may include nested objects (sub-namespaces and sub-classes). If so, Dyalog applies a form of lexical scope to all these objects to allow them to reference one another. Dyalog otherwise uses dynamic scope  – see [https://en.wikipedia.org/wiki/Scope_(computer_science)](https://en.wikipedia.org/wiki/Scope_(computer_science)).

This feature makes it possible to implement a class structure, in which members of the class tree may access one another, and it provides a way for classes to share data stored in a namespace.

When Dyalog fixes nested classes and namespaces in a script, references between parent and child objects are inserted to allow them to reference one another, preventing what would otherwise be `VALUE ERROR`. For example:
```apl
:Class Parent
:Access Public

    :Namespace Data
    :EndNamespace

    ∇ new name
      :Access Public
      :Implements Constructor
      Data.Name←name
    ∇

    :Class Child
    :Access Public
        :Field Public Name

        ∇ new name
          :Access Public
          :Implements Constructor
          Name←name
          Name,' is a child of ',Data.Name
        ∇
    :EndClass
:EndClass
```
```apl

      pete←⎕NEW Parent 'Pete'
      andy←⎕NEW pete.Child 'Andy'
Andy is a child of Pete

```

In this example, the namespace `Data` is accessible from the `Parent` class, and from any sub-classes within it and can therefore be used to share information between them. A more realistic example might be to share the value of the tie number of a component file.

Note that this is not possible using variables or Fields; **data to be shared between nested classes must be stored in a namespace**.
```apl
:Class Parent
:Access Public
:Field Private NameAsField←''
NameAsVariable←''            

    :Namespace Data
    :Endnamespace

    ∇ new name
      :Access Public
      :Implements Constructor
      Data.Name←name
      NameAsField←name
      NameAsVariable←name
    ∇

    :Class Child
    :Access Public
        :Field Public Name

        ∇ new name
          :Access Public
          :Implements Constructor
          Name←name
          Name,' is a child of ',Data.Name
          (0=⎕NC 'NameAsField')/Name, ' cannot see NameAsField'
          (0=⎕NC 'NameAsVariable')/Name,' cannot see NameAsVariable'
        ∇
    :EndClass
:EndClass

```
```apl
            pete←⎕NEW Parent 'Pete'
            andy←⎕NEW pete.Child 'Andy'
Andy is a child of Pete
Andy cannot see NameAsField
Andy cannot see NameAsVariable

```

## Variant Options for `⎕FIX`

Despite the essential benefits of lexical scope, there are circumstances in which it is undesirable and `⎕FIX`  provides fine control over the insertion of references. See [InjectReferences Option](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/fix.htm#InjectReferences).

Note that the ability to control lexical scope in this way applies only to `⎕FIX`. When a nested script is fixed by the Editor, the default lexical scope (InClasses) is applied. If, after fixing a script from the Editor, you wish to apply a different option (All or None) it is necessary to re-fix the script using `⎕FIX 62 ATX 'name'`.
