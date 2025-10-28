<h1 class="heading"><span class="name">Using .NET Classes</span></h1>

To create a Dyalog object as an instance of a .NET class, you use the `⎕NEW` system function. The `⎕NEW` system function is monadic. It takes a 1 or 2-element argument, the first element being a *class*.

If the argument is a scalar or a 1-element vector, an instance of the class is created using the *constructor* that takes NO argument.

If the argument is a 2-element vector, an instance of the class is created using the *constructor* whose argument matches the disclosed second element.

For example, to create a `DateTime` object whose value is the 30<sup>th</sup> April 2008:
```apl
      ⎕USING←'System'
 
      mydt←⎕NEW DateTime (2008 4 30)
 
```

The result of  `⎕NEW` is an reference to the newly created instance:
```apl
      ⎕NC ⊂'mydt'
9.2
```

If you format a reference to a .NET Object, APL calls its `ToString` method to obtain a useful description or identification of the object. This topic is discussed in more detail later in this chapter.
```apl
      mydt
30/04/2008 00:00:00
```

If you want to use fully qualified class names instead, one of the elements of `⎕USING` must be an empty vector. For example:
```apl
      ⎕USING←,⊂''
 
      mydt←⎕NEW System.DateTime (2008 4 30)
```

When creating an instance of the `DateTime` class, you are required to provide an argument with two elements: (the class and the *constructor argument*, in our case a 3-element vector representing the date). Many classes provide a default constructor which takes no arguments. From Dyalog, the *default constructor* is called by calling `⎕NEW` with only a reference to the class in the argument. For example, to obtain a default `Button` object, we only need to write:
```apl
      mybtn←⎕NEW Button
```

The above statement assumes that you have defined `⎕USING` correctly; there must be a reference to `System.Windows.Forms.dll`, and a namespace prefix which allows the name `Button` to be recognised as `System.Windows.Forms.Button`.

The mechanism by which APL associates the class name with a class in a .NET namespace is described below.

## Constructors and Overloading

Each .NET Class has one or more *constructor* methods. A constructor is a method which is called to initialise an instance of the Class. Typically, a Class will support several constructor methods - each with a different set of parameters. For example, `System.DateTime` supports a constructor that takes three `Int32` parameters (year, month, day), another that takes six `Int32` parameters (year, month, day, hour, minute, second), and so forth. These different constructor methods are not distinguished by having different names but by the different sets of parameters they accept.

This concept, which is known as *overloading*, may seem somewhat alien to the APL programmer. After all, we are used to defining functions that accept a whole range of different arguments. However, type checking, which is fundamental to the .NET Framework, requires that a method is called with the correct number of parameters, and that each parameter is of a predefined type. Overloading solves this issue.

When you create an instance of a class in C#, you do so using the `new` operator. This is automatically mapped to the appropriate constructor method by matching the parameters you supply to the various forms of the constructor. A similar mechanism is implemented in Dyalog using the `⎕NEW` system function.

## How the `⎕NEW` System Function is implemented

When APL executes an expression such as:
```apl
      mydt←⎕NEW DateTime (2008 4 30)
```

the following logic is used to resolve the reference to `DateTime` correctly.

The first time that APL encounters a reference to a non-existent name (that is, a name that would otherwise generate a `VALUE ERROR`), it searches the .NET namespaces/assemblies specified by `⎕USING` for a .NET class of that name. If found, the name (in this case `DateTime`) is recorded in the APL symbol table with a name class of 9.6 and is associated with the corresponding .NET namespace. If not, `VALUE ERROR` is reported as usual. Note that this search ONLY takes place if `⎕USING` has been assigned a value.

Subsequent references to that symbol (in this case `DateTime`) are resolved directly and do not involve any assembly searching.

If you use `⎕NEW` with only a class as argument, APL will attempt to call the version of its constructor that is defined to take no arguments. If no such version of the constructor exists, the call will fail with a `LENGTH ERROR`.

Otherwise, if you use `⎕NEW` with a class as argument and a second element, APL will call the version of the constructor whose parameters match the second element you have supplied to `⎕NEW`. If no such version of the constructor exists, the call will fail with a `LENGTH ERROR`.

## Notes

- The value of `⎕USING` is only used when an object is instantiated. Changing the value of `⎕USING` has no effect on objects that have already been instantiated in the active workspace.
- When a workspace containing .Net objects is saved, the names of the Net objects are saved with it but they are not automatically re-instantiated when the workspace is loaded or copied. A reference to such an orphaned object will report `(NULL)`. 
- Some functionality might work with .NET Framework or .NET but not both, for example, SharpPlot requires the .NET Framework and does not work with .NET itself.

## Displaying a .NET Object

When you display a reference to a .NET object, APL calls the object's `ToString` method and displays the result. All objects provide a `ToString` method because all objects ultimately inherit from the .NET class `System.Object`. Many .NET classes will provide their own `ToString` that overrides the one inherited from `System.Object`, and return a useful description or identifier for the object in question. `ToString` usually supports a range of calling parameters, but APL always calls the version of `ToString` that is defined to take no calling parameters. Monadic format (`⍕`) and monadic `⎕FMT` have been extended to provide the same result, and provides a quick shorthand method to call `ToString` in this way. The default `ToString` supplied by `System.Object` returns the name of the object's Type. This can be changed using the system function `⎕DF`. For example,
```apl
     z←⎕NEW DateTime ⎕TS
     z.(⎕DF(⍕DayOfWeek),,'G< 99:99>'⎕FMT 100⊥Hour Minute)
     z
Saturday 09:17

```

Note that if you want to check the type of an object, this can be obtained using the `GetType` method, which is supported by all .NET objects.

## Disposing of .NET Objects

.NET objects are managed by the .NET Common Language Runtime (CLR). The CLR allocates memory for an object when it is created, and de-allocates this memory when it is no longer required.

When the (last) reference from Dyalog to a .NET object is expunged by `⎕EX` or by localisation, the system marks the object as unused, leaving it to the CLR to de-allocate the memory that it had previously allocated to it, when appropriate. Note that even though Dyalog has de-referenced the APL name, the object could potentially still be referenced by another .NET class.

De-allocated memory may not actually be re-used immediately and may indeed never be re-used,  depending upon the algorithms used by the CLR garbage disposal.

Furthermore, a .NET object may allocate unmanaged resources (such as window handles) which are not automatically released by the CLR.

To allow the programmer to control the freeing of resources associated with .NET objects in a standard way, objects implement the IDisposable interface which provides a Dispose() method. The C# language provides a `using` control structure that automates the freeing of resources. Crucially, it does so however the flow of execution exits the control structure, even as a result of error handling. This obviates the need for the programmer to call Dispose() explicitly wherever it may be required.

This programming convenience is provide in Dyalog by the `:Disposable ... :EndDisposable` control structure. For further information, see [Disposable Statement](../../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/disposable/)
