# Inheritance

If you want a Class to derive from another Class, you simply add the name of that Class to the `:Class` statement using colon+space as a separator.

The following example specifies that `CLASS2` derives from `CLASS1`.
```apl
:Class CLASS2: CLASS1
:EndClass
```

Note that `CLASS1` is referred to as the *Base Class* of `CLASS2`.

If a Class has a Base Class, it automatically acquires all of the **Public** Properties, Methods and Fields defined for its Base Class unless it replaces them with its own members of the same name. This principle of inheritance applies throughout the Class hierarchy. Note that **Private** members are **not** subject to inheritance.

!!! warning
    When a class is fixed, it keeps a reference (a pointer) to its base class. If the global name of the base class is expunged, the derived class will still have the base class reference, and the base class will therefore be kept *alive* in the workspace. The derived class will be fully functional, but attempts to edit it will fail when it attempts to locate the base class as the new definition is fixed.

At this point, if a new class with the original base class name is created, the derived class has no way of detecting this, and it will continue to use the *old and invisible* version of the base class. Only when the derived class is re-fixed, will the new base class be detected.

If you edit, re-fix or copy an existing base class, APL will take care to patch up the references, but if the base class is expunged first and recreated later, APL is unable to detect the substitution. You can recover from this situation by editing or re-fixing the derived class(es) after the base class has been substituted.

## Copying Classes

See [Dependent Objects](../../../../language-reference-guide/system-commands/copy) and [Referenced Objects](../../../../language-reference-guide/system-commands/copy).

## Classes that derive from .NET Types

You may define a Class that derives from any of the .NET Types by specifying the name of the .NET Type and including a `:USING` statement that provides a path to the .NET Assembly in which the .NET Type is located.

<h3 class="example">Example</h3>
```apl
:Class APLGreg: GregorianCalendar
:Using System.Globalization
...
:EndClass
```

## Classes that derive from the Dyalog GUI

You may define a Class that derives from any of the Dyalog APL GUI objects by specifying the *name* of the Dyalog APL GUI Class in quotes.

For example, to define a Class named `Duck` that derives from a `Poly` object, the Class specification would be:
```apl
:Class Duck:'Poly'
:EndClass
```

The Base Constructor for such a Class is the `⎕WC` system function.
