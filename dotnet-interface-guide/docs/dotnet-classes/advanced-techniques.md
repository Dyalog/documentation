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

In .NET, a method, interface, or class can be _generic_, which means that it is a template or recipe for a _concrete_ method, interface, or class. What makes them generic is that they have a list of _type parameters_; the user must apply a matching number of _type arguments_ to create a concrete version. In the case of methods, it is not always necessary to apply type arguments, as the .NET interface can sometimes perform [type inference](#type-inference) to deduce the type arguments from the types of the method arguments.

### Syntax

The syntax used to apply type arguments to methods, classes, and interfaces, is square brackets, for example `G[T]` where `G` is the generic entity, and `T` is a .NET type or a vector of .NET types. The types could be the result of applying types to a generic .NET class.

The square bracket syntax means that working with generics in Dyalog APL and C# looks visually similar, except that C# uses angle brackets, as illustrated by the example below:

```C#
// Instantiate a concrete version of a generic class in C#
new System.Collections.Generic.List<System.Int32>();

// Call a concrete version of a generic method in C#
System.Decimal.CreateChecked<System.Int32>(5);
```

The corresponding APL is:
```apl
⍝ Instantiate a concrete version of a generic class in APL
⎕NEW System.Collections.Generic.List[System.Int32]

⍝ Call a concrete version of a generic method in APL
System.Decimal.CreateChecked[System.Int32] 5
```

### Creating a Concrete Version of a Generic Class

The class <code class="language-nonAPL">System.Collections.Generic.List</code> is a generic class with one type parameter, which is the type of the elements of the list. The display form of the type indicates that it is generic:

```apl
      ⎕USING←''
      System.Collections.Generic.List
(System.Collections.Generic.List[T])
```

A concrete version of the <code class="language-nonAPL">List</code> class can be created using square brackets. For example, a list class that contains integers can be created as follows:
```apl
	  ⎕USING←''
      IntList←System.Collections.Generic.List[System.Int32]
      IntList
(System.Collections.Generic.List[System.Int32])
```

The shared members of the `IntList` class can then be accessed, and the class instantiated using `⎕NEW`.

It is not necessary to give the constructed class a name before creating instances of it. Multiple type arguments can also be specified. For example:
```apl
	  ⎕USING←''
      types←System.Char System.Int32
      ⎕NEW System.Collections.Generic.Dictionary[types]
System.Collections.Generic.Dictionary`2[System.Char,System.Int32]
```

Attempting to instantiate a generic class without the expected number of type arguments generates an error. For example:
```apl
      ⎕USING←''
      ⎕NEW System.Collections.Generic.List
LENGTH ERROR: No overload of the type expects the given number (0) of generic type arguments
      ⎕NEW System.Collections.Generic.List
      ∧
```

Similarly, applying too many type arguments also results in an error:

```apl
      ⎕USING←''
      System.Collections.Generic.List[3⍴System.Int32]
LENGTH ERROR: No overload of the type expects the given number (3) of generic type arguments
      System.Collections.Generic.List[3⍴System.Int32]
```
### Creating a Concrete Version of a Generic Interface

Applying type arguments to generic interfaces closely resembles applying type arguments to generic classes. The example below defines a function `IsBoolCollection`. This checks whether a given .NET type implements the concrete version `ICollection[Boolean]` of the generic <code class="language-nonAPL">ICollection</code> interface, which is often implemented by data structures that act as collections of elements of a specific type.

```apl
      ⎕USING←'System' 'System.Collections.Generic'

      IsBoolCollection←{ICollection[Boolean]∊∊⎕CLASS ⍵}

      a←⎕NEW HashSet[Int32]
      b←⎕NEW List[Boolean]
      c←⎕NEW Dictionary[Int32 Boolean]

      IsBoolCollection¨a b c
0 1 0
```

### Multiple Overloads of .NET Classes and Interfaces
Some .NET classes and interfaces have multiple overloads, varying in the number of generic type parameters. The display form of the type makes this clear, and the .NET interface will automatically use the appropriate overload based on context.

```apl
      ⎕USING←'System'
      ValueTuple
(System.ValueTuple)
(System.ValueTuple[T1])
(System.ValueTuple[T1,T2])
(System.ValueTuple[T1,T2,T3])
(System.ValueTuple[T1,T2,T3,T4])
(System.ValueTuple[T1,T2,T3,T4,T5])
(System.ValueTuple[T1,T2,T3,T4,T5,T6])
(System.ValueTuple[T1,T2,T3,T4,T5,T6,T7])
(System.ValueTuple[T1,T2,T3,T4,T5,T6,T7,TRest])
```

The <code class="language-nonAPL">ValueTuple</code> class has one non-generic overload and eight generic overloads.

```apl
      ⎕USING←'System'
      ValueTuple[Int32]         ⍝ Create concrete version of overload with 1 generic parameter
(System.ValueTuple[System.Int32])

      ValueTuple[Int32 Boolean] ⍝ Create concrete version of overload with 2 generic parameters
(System.ValueTuple[System.Int32,System.Boolean])
```

### Calling a Generic Method

Generic methods have a display form with a generic type parameter list shown in square brackets. For example:
```apl
    ⎕USING←''
    System.Decimal.CreateChecked
System.Decimal CreateChecked[TOther](TOther)
```

The <code class="language-nonAPL">CreateChecked</code> function has one type parameter, shown in square brackets, and one regular parameter, shown in parentheses.

The generic type argument can be applied using square brackets, and the result is a concrete version of the generic method. The method can either be given a name or evaluated directly. The display form indicates that the type parameters have been replaced to form a concrete function.

```apl
      ⎕USING←'System'
      fn←Decimal.CreateChecked[Int32]
      fn
System.Decimal CreateChecked[Int32](Int32)
      fn 10
10
      Decimal.CreateChecked[Int32] 50
50
```

If a generic method has overloads with different numbers of type parameters, applying type arguments will narrow down the list of overloads that are applicable. For example, when having only one overload means that a single type argument is expected:

```apl
      ⎕USING←'System'
      ValueTuple.Create
System.ValueTuple Create()
System.ValueTuple`1[T1] Create[T1](T1)
System.ValueTuple`2[T1,T2] Create[T1,T2](T1, T2)
System.ValueTuple`3[T1,T2,T3] Create[T1,T2,T3](T1, T2, T3)
...

      ValueTuple.Create[Boolean]
System.ValueTuple`1[System.Boolean] Create[Boolean](Boolean)
```

.NET methods with only a single overload that expects no arguments are usually imported into APL as niladic functions. However, when they are generic, they are imported as monadic functions so that the type arguments can be applied. For example:

```apl
      ⎕USING←'System'
      Array.Empty
T[] Empty[T]()

      Array.Empty[Int32]
Int32[] Empty[Int32]()

      r←Array.Empty[Int32] ⍬
      r≡⍬
1
```

Applying an incorrect number of type arguments to a method will generate an error:

```apl
      ⎕USING←'System'
      Decimal.CreateChecked 50
LENGTH ERROR: No overload of the method expects the given number (0) of generic type arguments
      Decimal.CreateChecked 50
      ∧

      ValueTuple.Create[10⍴Int32]
LENGTH ERROR: No overload of the method expects the given number (10) of generic type arguments
      ValueTuple.Create[10⍴Int32]
                                ∧
```

#### Type Inference

If the arguments to a generic method have a concrete .NET type, then their type information might be sufficient for the .NET bridge to unambiguously select a method overload and to automatically apply the needed type arguments. If there is any ambiguity about the type, such as when the arguments are regular APL arrays (for example the scalar `0`, which can be converted into a number of different .NET types), type inference will not take place. For example:

```
      ⎕USING←'System' 'System.Threading.Tasks'
      Task.FromResult
System.Threading.Tasks.Task`1[TResult] FromResult[TResult](TResult)

      Task.FromResult 123
LENGTH ERROR: No overload of the method expects the given number (0) of generic type arguments
      Task.FromResult 123
      ∧

      ⍝ Explicitly apply type arguments
      Task.FromResult[Int128] 123
System.Threading.Tasks.Task`1[System.Int128]

      ⍝ Explicitly apply type arguments, and pass in a .NET object of that type
      i128←Int128.Parse ⊂'123'
      Task.FromResult[Int128] i128
System.Threading.Tasks.Task`1[System.Int128]

      ⍝ Let the bridge infer the type argument from argument's .NET type
      Task.FromResult i128
System.Threading.Tasks.Task`1[System.Int128]
```

Type inference can remove the need for additional code (as shown in the last lines of the example above), but manually applying type arguments is also permitted.

If the user has [specified an overload](#specifying-overloads), then the type information is taken into account. This means that an alternative way of coding the above would be:

```apl
      ⎕USING←'System' 'System.Threading.Tasks'
      Task.FromResult
System.Threading.Tasks.Task`1[TResult] FromResult[TResult](TResult)

      Task.FromResult⍠Int128⊢123
System.Threading.Tasks.Task`1[System.Int128]
```

This works because we tell the .NET bridge that we want the overload that takes an <code class="language-nonAPL">Int128</code> as its argument, which means the type parameter `TResult` *must* be <code class="language-nonAPL">Int128</code>; it is, therefore, not necessary to explicitly apply the type arguments using square brackets.