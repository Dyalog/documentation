<h1 class="heading"><span class="name">Advanced Techniques</span></h1>

## Shared Members

Certain .NET Classes provide methods, fields and properties, that can be called directly without the need to create an instance of the Class first. These *members* are known as shared, because they have the same definition for the class and for any instance of the class.

The methods `Now` and `IsLeapYear` exported by System.DateTime fall into this category. For example:
```apl
      ⎕USING←,⊂'System'
 
      DateTime.Now
07/11/2008 11:30:48
 
      DateTime.IsLeapYear 2000
1
```

## APL language extensions for .NET objects

The .NET Framework provides a set of standard operators (methods) that are supported by certain classes. These operators include methods to compare two .NET objects and methods to add and subtract objects.

In the case of the `DateTime` Class, there are operators to compare two `DateTime` objects. For example:
```apl
      DT1←⎕NEW DateTime (2008 4 30)
      DT2←⎕NEW DateTime (2008 1 1)
 
     ⍝ Is DT1 equal to DT2 ?
      DateTime.op_Equality DT1 DT2
0
```

The `op_Addition` and `op_Subtraction` operators add and subtract `TimeSpan` objects to `DateTime` objects. For example:
```apl
      DT3←DateTime.Now
      DT3
07/11/2008 11:33:45
 
      TS←⎕NEW TimeSpan (1 1 1)
      TS
01:01:01
 
```
```apl

      DateTime.op_Addition DT3 TS
07/11/2008 12:34:46
 
      DateTime.op_Subtraction DT3 TS
07/11/2008 10:32:44
```

The corresponding APL primitive functions have been extended to accept .NET objects as arguments and simply call these standard .NET methods internally. The methods and the corresponding APL primitives are shown in the table below.

Note that calculations and comparisons performed by .NET methods are performed independently from the values of APL system variables (such as `⎕FR` and `⎕CT`).

|.NET Method          |APL Primitive Function|
|---------------------|----------------------|
|op_Addition          |`+`                   |
|op_Subtraction       |`-`                   |
|op_Multiply          |`×`                   |
|op_Division          |`÷`                   |
|op_Equality          |`=`                   |
|op_Inequality        |`≠`                   |
|op_LessThan          |`<`                   |
|op_LessThanOrEqual   |`≤`                   |
|op_GreaterThan       |`>`                   |
|op_GreaterThanOrEqual|`≥`                   |

So instead of calling the appropriate .NET method to compare two objects, you can use the familiar APL primitive instead. For example:
```apl
      DT1=DT2
0
      DT1>DT2
1
      DT3+TS
07/11/2008 12:34:46
      DT3-TS
07/11/2008 10:32:44
```

Apart from being easier to use, the primitive functions automatically handle arrays and support scalar extension; for example:
```apl
      DT1>DT2 DT3
1 0
```

In addition, the monadic form of Grade Up (`⍋`) and Grade Down (`⍒`), and the Minimum (`⌊`) and Maximum (`⌈`) primitive functions have been extended to work on arrays of references to .NET objects. Note that the argument(s) must be a homogeneous set of references to objects of the same .NET class, and in the case of Grade Up and Grade Down, the argument must be a vector. For example:
```apl
      ⍋DT1 DT2 DT3
2 1 3
      ⌊/DT1 DT2 DT3
01/01/2008 00:00:00
 
```

## Exceptions

When a .NET object generates an error, it does so by *throwing an exception*. An exception is in fact a .NET class whose ultimate base class is `System.Exception`.

The system constant `⎕EXCEPTION` returns a reference to the most recently generated exception object.

For example, if you attempt to create an instance of a `DateTime` object with a year that is outside its range, the constructor throws an exception. This causes APL to report a (trappable) `EXCEPTION` error (error number 90) and access to the exception object is provided by `⎕EXCEPTION`.
```apl
      ⎕USING←'System'
      DT←⎕NEW DateTime (100000 0 0)
EXCEPTION
      DT←⎕NEW DateTime (100000 0 0)
 
      ⎕EN
90
      ⎕EXCEPTION.Message
Year, Month, and Day parameters describe an un-representable DateTime.
 
      ⎕EXCEPTION.Source
mscorlib
 
      ⎕EXCEPTION.StackTrace
   at System.DateTime.DateToTicks(Int32 year,
                                  Int32 month,
                                  Int32 day)
 
   at System.DateTime..ctor(Int32 year,
                            Int32 month,
                            Int32 day)
```

## Specifying Overloads and Casts

If a .NET function is overloaded in terms of the types of arguments it accepts, Dyalog chooses which overload to call depending upon the data types of the arguments passed to it. For example, if a .NET function `foo()` is declared to take a single argument either of type `int` or of type `double` APL would call the first version if you called it with an integer value and the second version if you called it with a non-integer value.

In some circumstances it may be desirable to override this mechanism and explicitly specify which overload to use.

A second requirement is to be able to specify to what .NET types APL should coerce arrays before calling a .NET function. For example, if a parameter to a .NET function is declared as type `System.Object`, it might be necessary to force the APL argument to be cast to a particular  *type* of `Object` before the function is called.

Both these requirements are met by calling the function via the Variant operator `⍠`. There are two options, **OverloadTypes** (the Principle Option) and **CastToTypes**. Each option takes an array of refs to .NET types, the same length as the number of parameters to the function.

## OverloadTypes Examples

To force APL to call the double version of function `foo()` regardless of the type of the argument `val`:
```apl
      (foo ⍠('OverloadTypes'Double))val
```

or more simply:
```apl
      (foo ⍠Double)val
```

Note that `Double` is a ref to the .NET type `System.Double`.
```apl
      ⎕USING←'System'
      Double
(System.Double)

```

Taking this a stage further, suppose that `foo()` is defined with 5 overloads as follows:
```apl
foo()
foo(int i)
foo(double d)
foo(double d, int i)
foo(double[] d)

```

The following statements will call the niladic, double, (double, int) and double[] overloads respectively.

```apl

(foo ⍠ (⊂⍬)) ⍬                              ⍝ niladic
(foo ⍠ Double) 1                            ⍝ double
(foo ⍠(⊂Double Int32))1 1                   ⍝ double,int
(foo ⍠(Type.GetType ⊂'System.Double[]'))⊂1 1 ⍝ double[]
```

Note that in the niladic case, an enclosed empty vector is used to represent a null reference to a .NET type.

## CastToTypes Example

The .NET function `Array.SetValue()` sets the value of a specified element (or elements) of an array. The first argument, the new value, is declared as `System.Object`, but the value supplied must correspond to the type of the `Array` in question. APL has no means to know what this is and will therefore pass the value *as is*, that is, in whatever internal format it happens to be at the time. For example:
```apl
      ⎕USING←'System'

      ⍝ create a Boolean  array with 2 elements
      BA←Array.CreateInstance Boolean 2
      BA.GetValue 0 ⍝ get the 0th element
0
```
```apl
      ⍝ attempt to set the 0th element to 1 (AKA true)
```
```apl

      BA.SetValue 1 0
EXCEPTION: Cannot widen from source type to target type
either because the source type is a not a primitive type or the conversion cannot be accomplished.
test[5] BA.SetValue 1 0
       ∧ 
```

The above expression failed because APL passed the first argument 1 ,unchanged from its current internal representation, as a 1-byte integer which does not fit into a Boolean element.

To rectify the situation, APL must be told to cast the argument to a Boolean as follows:
```apl
      (BA.SetValue ⍠ ('CastToTypes'(Boolean Int32)))1 0
      BA.GetValue 0 ⍝ get the 0th element
1
```

## Overloaded Constructors

If a class provides constructor overloads, a similar mechanism is used to specify which of the constructors is to be used when an instance of the class is created using `⎕NEW`.

For example, if `MyClass` is a .NET class with an overloaded constructor, and one of its constructors is defined to take two parameters; a `double` and an `int`, the following statement would create an instance of the class by calling that specific constructor overload:
```apl
      (⎕NEW ⍠ (⊂Double Int32)) MyClass (1 1)
```
