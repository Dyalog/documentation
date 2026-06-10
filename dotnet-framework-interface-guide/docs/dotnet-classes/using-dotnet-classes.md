<h1 class="heading"><span class="name">Using .NET Classes</span></h1>

To create a Dyalog object as an instance of a .NET class, the `⎕NEW` system function is used. The `⎕NEW` system function is monadic. It takes a 1 or 2-element argument, the first element of which is a class.

If the argument is a scalar or a 1-element vector, an instance of the class is created using the constructor overload that takes no argument.

If the argument is a 2-element vector, an instance of the class is created using the [constructor overload](#constructors-and-overloading)) whose argument matches the disclosed second element.

<h4 class="example">Example</h4>

To create a <code class="language-nonAPL">DateTime</code> object whose value is 30 April 2008:
```apl
      ⎕USING←'System'
      mydt←⎕NEW DateTime (2008 4 30)

```

The result of `⎕NEW` is an reference to the newly-created instance:
```apl
      ⎕NC ⊂'mydt'
9.2
```

When a reference to a .NET object is formatted, APL calls its <code class="language-nonAPL">ToString</code> method to obtain a useful description or identification of the object (this topic is discussed in more detail in [Displaying a .NET Object](#displaying-a-net-object)):
```apl
      mydt
30/04/2008 00:00:00
```

To use fully-qualified class names instead, one of the elements of `⎕USING` must be an empty vector. For example:
```apl
      ⎕USING←,⊂''
      mydt←⎕NEW System.DateTime (2008 4 30)
```

When creating an instance of the <code class="language-nonAPL">DateTime</code> class, two elements are needed in the argument – the class and the _constructor argument_ (in this example, the constructor argument is a 3-element vector representing the date). Many classes provide a default constructor that takes no arguments. In Dyalog, the _default constructor_ is called by calling `⎕NEW` with only a reference to the class in the argument. For example, the call to creata a default `Button` object is:
```apl
      mybtn←⎕NEW Button
```

This assumes that `⎕USING` has been defined correctly – there must be a reference to **System.Windows.Forms.dll**, and a namespace prefix that allows the name `Button` to be recognised as <code class="language-nonAPL">System.Windows.Forms.Button</code>.

The rest of this page describes the mechanism by which Dyalog associates the class name with a class in a .NET namespace.

## Constructors and Overloading

Each .NET class has one or more _constructor_ methods. These are called to initialise an instance of the class. Typically, a class will support several constructor methods, each with a different set of parameters. For example, <code class="language-nonAPL">System.DateTime</code> supports a constructor that takes three <code class="language-nonAPL">Int32</code> parameters (year, month, day), another that takes six <code class="language-nonAPL">Int32</code> parameters (year, month, day, hour, minute, second), and various other constructors. These different constructor methods are not distinguished by having different names but by the different sets of parameters that they accept.

This concept, which is known as _overloading_, may seem somewhat alien to the APL programmer, who will be accustomed to defining functions that accept an arbitrary array. However, type checking, which is fundamental to the.NET Framework, requires a method to be called with the correct number of parameters, and that each parameter is of a predefined type. Overloading solves this issue.

When creating an instance of a class in C#, the <code class="language-nonAPL">new</code> operator is used. At compile time, this is mapped to the appropriate constructor overload by matching the user-supplied parameters to the various forms of the constructor. A similar mechanism is implemented in Dyalog by the `⎕NEW` system function.

## Resolving References to .NET Objects

When Dyalog executes an expression such as
```apl
      mydt←⎕NEW DateTime (2008 4 30)
```

the following logic is used to resolve the reference to <code class="language-nonAPL">DateTime</code> correctly.

The first time that Dyalog encounters a reference to a non-existent name (that is, a name that would otherwise generate a `VALUE ERROR`), it searches the .NET namespaces/assemblies specified by `⎕USING` for a .NET class of that name. If found, the name (in this case, <code class="language-nonAPL">DateTime</code>) is recorded in the APL symbol table with a name class of `9.6` and is associated with the corresponding .NET namespace. If not found, then `VALUE ERROR` is reported as usual. This search ONLY takes place if `⎕USING` has been assigned a non-empty value.

Subsequent references to that symbol (in this example, <code class="language-nonAPL">DateTime</code>) are resolved directly and do not involve any assembly searching.

If `⎕NEW` is called with only a class as argument, then Dyalog attempts to call the overload of its constructor that is defined to take no arguments. If no such overload exists, then the call fails with a `LENGTH ERROR`.

If `⎕NEW` is called with a class as argument and a second element, then Dyalog calls the version of the constructor whose parameters match the second element supplied to `⎕NEW`. If no such overload exists, then the call will fail with either `LENGTH ERROR`.

!!! Info "Information"
    The value of `⎕USING` is only used when an object is instantiated. Changing the value of `⎕USING` has no effect on objects that have already been instantiated in the active workspace.

!!! Info "Information"
    When a workspace containing .NET objects is saved, the names of those objects are saved with it but they are not automatically re-instantiated when the workspace is loaded or copied. A reference to such an orphaned object will report `(NULL)`.

## Displaying a .NET Object

When you display a reference to a .NET object, APL calls the object's <code class="language-nonAPL">ToString</code> method and displays the result. All objects provide a <code class="language-nonAPL">ToString</code> method because all objects ultimately inherit from the .NET class <code class="language-nonAPL">System.Object</code>, which provides a default implementation. Many .NET classes provide their own <code class="language-nonAPL">ToString</code> that overrides the one inherited from <code class="language-nonAPL">System.Object</code> and returns a useful representation of the object in question. <code class="language-nonAPL">ToString</code> usually supports a range of calling parameters, but Dyalog always calls the version of <code class="language-nonAPL">ToString</code> that is defined to take no calling parameters. The monadic format function (`⍕`) and monadic `⎕FMT` have been extended to provide the same result and provide a shorthand method to call <code class="language-nonAPL">ToString</code>. The default <code class="language-nonAPL">ToString</code> supplied by <code class="language-nonAPL">System.Object</code> returns the name of the object's Type. For a particular object in the namespace, this can be changed using the system function `⎕DF`.

<h4 class="example">Example</h4>

```apl
      z←⎕NEW DateTime ⎕TS
      z.(⎕DF(⍕DayOfWeek),,'G< 99:99>'⎕FMT 100⊥Hour Minute)
      z
Saturday 09:17
```

The type of an object can be obtained using the <code class="language-nonAPL">GetType</code> method, which is supported by all .NET objects:
```apl
      z.GetType
System.DateTime
```

## Disposing of .NET Objects

.NET objects are managed by the [.NET Common Language Runtime (CLR)](https://learn.microsoft.com/en-us/dotnet/standard/clr). The CLR allocates memory for an object when it is created, and de-allocates this memory when it is no longer required.

When the (last) reference from Dyalog to a .NET object is expunged by `⎕EX` or by localisation, the system marks the object as unused, leaving it to the CLR to de-allocate the memory that it had previously allocated to it (when appropriate – even though Dyalog has dereferenced the APL name, the object could potentially still be referenced by another .NET class).

De-allocated memory might not be reused immediately and might never be reused,  depending on the algorithms used by the CLR garbage disposal.

Furthermore, a .NET object can allocate unmanaged resources (such as window handles) which are not automatically released by the CLR.

To allow you to control the freeing of resources associated with .NET objects in a standard way, many objects implement the <code class="language-nonAPL">IDisposable</code> interface which provides a <code class="language-nonAPL">Dispose()</code> method. The C# language provides a <code class="language-nonAPL">using</code> control structure that automates the freeing of resources. Crucially, it does so irrespective of how the flow of execution exits the control structure, even as a result of error handling. This obviates the need for the programmer to call <code class="language-nonAPL">Dispose()</code> explicitly wherever it may be required.

This programming convenience is provide in Dyalog by the [`:Disposable ... :EndDisposable`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/disposable/) control structure.
