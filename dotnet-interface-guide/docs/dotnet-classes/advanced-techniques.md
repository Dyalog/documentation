<h1 class="heading"><span class="name">Advanced Techniques</span></h1>

## Shared Members

Certain .NET classes provide methods, fields, and properties that can be called directly without the need to create an instance of the class first. These _members_ are known as _shared_, because they have the same definition for the class and for any instance of the class.

The methods <code class="language-nonAPL">Now</code> and <code class="language-nonAPL">IsLeapYear</code> exported by <code class="language-nonAPL">System.DateTime</code> fall into this category.

<h4 class="example">Example</h4>
```apl
     ⎕USING←,⊂'System'
			 
     DateTime.Now
18/03/2020 11:14:05
			 
     DateTime.IsLeapYear 2000
1
```

## APL Language Extensions for .NET Projects

.NET provides a set of standard operators (methods) that are supported by certain classes, for example, methods to add and subtract .NET objects and methods to compare two .NET objects.

<h4 class="example">Example 1: DateTime – Adding and subtracting</h4>

The <code class="language-nonAPL">op_Addition</code> and <code class="language-nonAPL">op_Subtraction</code> operators add and subtract <code class="language-nonAPL">TimeSpan</code> objects to <code class="language-nonAPL">DateTime</code> objects:
```apl
      DT3←System.DateTime.Now
      DT3
15/02/2024 10:35:35
```
```apl
      TS←⎕NEW TimeSpan (1 1 1)
      TS
01:01:01
```
```apl
      DateTime.op_Addition DT3 TS
15/02/2024 11:36:36
```
```apl
      DateTime.op_Subtraction DT3 TS
15/02/2024 09:34:34
```

<h4 class="example">Example 2: DateTime – Comparing</h4>

The <code class="language-nonAPL">op_Equality</code> and <code class="language-nonAPL">op_Inequality</code> operators  compare two <code class="language-nonAPL">DateTime</code> objects:
```apl
      DT1←⎕NEW DateTime (2024 4 30)
      DT2←⎕NEW DateTime (2024 1 1)

      ⍝ Is DT1 equal to DT2?
      DateTime.op_Equality DT1 DT2
0
```

Some corresponding APL primitive functions have been extended to accept .NET objects as arguments and call these standard .NET methods internally. The methods and the corresponding APL primitives that are currently available are:

|.NET Method  |APL Primitive Function|
|-------------|----------------------|
|<code class="language-nonAPL">op_Equality</code>  |[`=`](../../../language-reference-guide/primitive-functions/equal-to/) and `≡`           |
|<code class="language-nonAPL">op_Inequality</code>|[`≠`](../../../language-reference-guide/primitive-functions/not-equal-to/) and `≢`           |

This means that Example 2 becomes:
```apl
      DT1←⎕NEW DateTime (2024 4 30)
      DT2←⎕NEW DateTime (2024 1 1)

      ⍝ Is DT1 equal to DT2?
      DT1 = DT2
0
```

!!! Info "Information"
    Calculations and comparisons performed by .NET methods are performed independently from the values of APL system variables (such as `⎕FR` and `⎕CT`).

## Exceptions

When a .NET object generates an error, it does so by _throwing an exception_. An _exception_ is a .NET class whose ultimate base class is <code class="language-nonAPL">System.Exception</code>.

The system constant [`⎕EXCEPTION`](../../../language-reference-guide/system-functions/exception/) returns a reference to the most recently generated exception object.

For example, if you attempt to create an instance of a <code class="language-nonAPL">DateTime</code> object with a year that is outside its range, the constructor throws an exception. This causes APL to report a (trappable) `EXCEPTION` error (error number 90) and access to the exception object is provided by `⎕EXCEPTION`.
```apl
      ⎕USING←'System'
      DT←⎕NEW DateTime (100000 0 0)
EXCEPTION: Year, Month, and Day parameters describe an un-representable DateTime.
      DT←⎕NEW DateTime (100000 0 0)
         ^		 
      ⎕EN
90
      ⎕EXCEPTION.Message
Year, Month, and Day parameters describe an un-representable DateTime.
			 
      ⎕EXCEPTION.Source
System.Private.CoreLib
			 
      ⎕EXCEPTION.StackTrace
at System.DateTime.DateToTicks(Int32 year, Int32 month, Int32 day)
at System.DateTime..ctor(Int32 year, Int32 month, Int32 day)
```

!!! Info "Information"
    The result of `⎕EXCEPTION.StackTrace` can depend on the exact version of .NET – your result might look different, but if it includes `System.DateTime..ctor(Int32 year, Int32 month, Int32 day)` then it is showing the correct exception for this example.

## Specifying Overloads

If a .NET function is overloaded in terms of the types of arguments that it accepts, then Dyalog chooses which overload to call depending on the data types of the arguments passed to it. For example, if a .NET function <code class="language-nonAPL">foo()</code> is declared to take a single argument either of type <code class="language-nonAPL">int</code> or of type <code class="language-nonAPL">double</code>, Dyalog would call the first version if you called it with an integer value and the second version if you called it with a floating-point value.

Occasionally it might be desirable to override this mechanism and explicitly specify which overload to use. This can be done by calling the function and specifying the _variant_ operator ([`⍠`](../../../language-reference-guide/primitive-operators/variant/)) with the `OverloadTypes` option. This takes an array of references to .NET types, of the same length as the number of parameters to the function.

<h4 class="example">Example</h4>

To force APL to call the double version of function <code class="language-nonAPL">foo()</code> irrespective of the type of the argument <code class="language-nonAPL">val</code>, enter:
```apl
      (foo ⍠('OverloadTypes'Double))val
```

or (more simply):
```apl
      (foo ⍠Double)val
```

where `Double` is a reference to the .NET type <code class="language-nonAPL">System.Double</code>.
```apl
      ⎕USING←'System'
      Double
(System.Double)
		
```

Taking this a stage further, suppose that <code class="language-nonAPL">foo()</code> is defined with five overloads as follows:
```nonAPL
foo()
foo(int i)
foo(double d)
foo(double d, int i)
foo(double[] d)

```

The following statements will call the niladic, double, (double, int) and double`[]` overloads respectively:
```
(foo ⍠ (⊂⍬)) ⍬                               ⍝ niladic
(foo ⍠ Double) 1                             ⍝ double
(foo ⍠(⊂Double Int32))1 1                    ⍝ double,int
(foo ⍠(Type.GetType ⊂'System.Double[]'))⊂1 1 ⍝ double[]
```

### Overloaded Constructors

If a class provides constructor overloads, then a similar mechanism is used to specify which of the constructors is to be used when an instance of the class is created using `⎕NEW`.

For example, if <code class="language-nonAPL">MyClass</code> is a .NET class with an overloaded constructor, and one of its constructors is defined to take two parameters; a <code class="language-nonAPL">double</code> and an <code class="language-nonAPL">int</code>, then the following statement would create an instance of the class by calling that specific constructor overload:
```apl
      (⎕NEW ⍠ (⊂Double Int32)) MyClass (1 1)
```

## Generics

The .NET interface supports creating concrete versions of _generic classes_, instantiating them, and calling generic methods. This is done by calling `43⌶` with a right argument of `632` (for more information on `43⌶`, see the _Dyalog APL Language Reference Guide_). Note that this I-beam will be replaced with something that is better integrated into the language in a future Dyalog version.

A generic class is a class that has type parameters, which must be given values to create a concrete version of the class. Similarly, a generic method has type parameters that must be specified before the method can be called.

The result of `43⌶632` is a monadic operator, which is used to apply the type arguments of generic classes or methods.

### Creating a Concrete Version of a Generic Class

The class <code class="language-nonAPL">System.Collections.Generic.List</code> is a generic class with one type parameter, which is the type of the elements of the list.

A concrete version of the <code class="language-nonAPL">List</code> class can be created using `43⌶632`. For example, a list class that contains integers can be created as follows:
```apl
     IntList←System.Collections.Generic.List(43⌶632)System.Int32
     IntList
(System.Collections.Generic.List`1[System.Int32])
```

The shared members of the <code class="language-nonAPL">IntList</code> class can then be accessed, and the class instantiated using `⎕NEW`. It is not necessary to give the constructed class a name.

The operations can also be combined and multiple type argument specified. For example:
```apl
    types←System.Char System.Int32
    ⎕NEW System.Collections.Generic.Dictionary (43⌶632) types
System.Collections.Generic.Dictionary`2[System.Char,System.Int32]

```

Attempting to instantiate a generic class without the expected number of type arguments generates an exception. For example:
```apl
    ⎕USING←''
    ⎕NEW System.Collections.Generic.List
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    ⎕NEW System.Collections.Generic.List
    ∧
```

### Calling a Generic Method

Generic methods have a display form with a generic type parameter list shown in square brackets. For example:
```apl
    ⎕USING←''
    System.Decimal.CreateChecked
System.Decimal CreateChecked[TOther](TOther)
```

The <code class="language-nonAPL">CreateChecked</code> function has one type parameter, shown in square brackets, and one regular parameter, shown in parentheses.

The generic type argument can be applied using  `43⌶632`. When the monadic operator `43⌶632` is run with a .NET method as its left argument, and a scalar type or a vector of .NET types as its right argument, the result is a derived function that calls the specified .NET method with both the generic type arguments and regular arguments applied. For example:
```apl
    fn←System.Decimal.CreateChecked (43⌶632) System.Int32
    fn 123
123
```

Attempting to call a method without specifying the type argument generates an exception. For example:
```apl
    System.Decimal.CreateChecked 123
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    System.Decimal.CreateChecked 123
                   ∧
```

### Calling a Niladic Generic Method

.NET methods that only export overloads with zero parameters are exported as niladic functions, which means they cannot be passed as an operand to `43⌶632` without being evaluated.  To accomodate this, `43⌶632` also accepts a character vector as its left argument. In this case, it runs the .NET method with that name, with the generic type arguments applied. For example:
```apl
    r←'System.Array.Empty'(43⌶632)System.Int32
    r≡⍬
1
```

Attempting to evaluate the niladic function without calling `43⌶632`  generates an exception. For example:
```apl
    System.Array.Empty
EXCEPTION: Invalid number of generic type arguments applied (expected 1, got 0)
    System.Array.Empty
    ∧
```
