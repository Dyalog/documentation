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

The .NET Framework provides a set of standard operators (methods) that are supported by certain classes. These operators include methods to compare two .NET objects and methods to add and subtract objects. In the case of the <code class="language-nonAPL">DateTime</code> class, there are operators to compare two <code class="language-nonAPL">DateTime objects</code>. For example:
```apl
      DT1←⎕NEW DateTime (2008 4 30)
      DT2←⎕NEW DateTime (2008 1 1)

      ⍝ Is DT1 equal to DT2 ?
      DateTime.op_Equality DT1 DT2
0
```

The <code class="language-nonAPL">op_Addition</code> and <code class="language-nonAPL">op_Subtraction</code> operators add and subtract <code class="language-nonAPL">TimeSpan</code> objects to <code class="language-nonAPL">DateTime</code> objects. For example:
```apl
      DT3←DateTime.Now
      DT3
18/03/2020 11:15:10

      TS←⎕NEW TimeSpan (1 1 1)
      TS
01:01:01

      DateTime.op_Addition DT3 TS
07/11/2008 12:34:46

      DateTime.op_Subtraction DT3 TS
07/11/2008 10:32:44
```

The corresponding APL primitive functions have been extended to accept .NET objects as arguments and call these standard .NET methods internally. The methods and the corresponding APL primitives are shown in [](#method-equivalents).

!!! Info "Information"
    Calculations and comparisons performed by .NET methods are performed independently from the values of APL system variables (such as `⎕FR` and `⎕CT`).

Table: .NET methods and their APL primitive function equivalents { #method-equivalents }

|.NET Method                                               |APL Primitive Function|
|----------------------------------------------------------|----------------------|
|<code class="language-nonAPL">op_Addition</code>          |`+`                   |
|<code class="language-nonAPL">op_Subtraction</code>       |`-`                   |
|<code class="language-nonAPL">op_Multiply</code>          |`×`                   |
|<code class="language-nonAPL">op_Division</code>          |`÷`                   |
|<code class="language-nonAPL">op_Equality</code>          |`=`                   |
|<code class="language-nonAPL">op_Inequality</code>        |`≠`                   |
|<code class="language-nonAPL">op_LessThan</code>          |`<`                   |
|<code class="language-nonAPL">op_LessThanOrEqual</code>   |`≤`                   |
|<code class="language-nonAPL">op_GreaterThan</code>       |`>`                   |
|<code class="language-nonAPL">op_GreaterThanOrEqual</code>|`≥`                   |

So instead of calling the appropriate .NET method to compare two objects, APL primitives can be used instead. For example:
```apl
      DT1=DT2
0
```
```apl

      DT1>DT2
1
```
```apl

      DT3+TS
07/11/2008 12:34:46
```
```apl

      DT3-TS
07/11/2008 10:32:44
```

In addition to being easier to use, the primitive functions automatically handle arrays and support scalar extension. For example:
```apl
      DT1>DT2 DT3
1 0
```

The monadic forms of the _grade up_ (`⍋`), _grade down_ (`⍒`), _minimum_ (`⌊`), and _maximum_ (`⌈`) primitive functions have been extended to work on arrays of references to .NET objects. For example:
```apl
      ⍋DT1 DT2 DT3
2 1 3
```
```apl

      ⌊/DT1 DT2 DT3
01/01/2008 00:00:00
```

!!! Info "Information"
    The argument(s) must be a homogeneous set of references to objects of the same .NET class and, for grade up and grade down, the argument must be a vector.

## Exceptions

When a .NET object generates an error, it does so by throwing an _exception_. An exception is a .NET class whose ultimate base class is <code class="language-nonAPL">System.Exception</code>.

The system constant `⎕EXCEPTION` returns a reference to the most recently generated exception object.

For example, if you attempt to create an instance of a <code class="language-nonAPL">DateTime</code> object with a year that is outside its range, the constructor throws an exception. This causes APL to report a (trappable) `EXCEPTION` error (error number `90`) and access to the exception object is provided by `⎕EXCEPTION`.
```apl
      ⎕USING←'System'
      DT←⎕NEW DateTime (100000 0 0)
EXCEPTION
      DT←⎕NEW DateTime (100000 0 0)
         ^

      ⎕EN
90
      ⎕EXCEPTION.Message
Year, Month, and Day parameters describe an un-representable DateTime.

      ⎕EXCEPTION.Source
mscorlib

      ⎕EXCEPTION.StackTrace
at System.DateTime.DateToTicks(Int32 year, Int32 month, Int32 day)
at System.DateTime..ctor(Int32 year, Int32 month, Int32 day)
```

## Specifying Overloads

If a .NET function is overloaded in terms of the types of arguments that it accepts, then Dyalog chooses which overload to call depending on the data types of the arguments passed to it. For example, if a .NET function <code class="language-nonAPL">foo()</code> is declared to take a single argument either of type <code class="language-nonAPL">int</code> or of type <code class="language-nonAPL">double</code>, Dyalog would call the first version if you called it with an integer value and the second version if you called it with a non-integer value.

Occasionally it might be desirable to override this mechanism and explicitly specify which overload to use or  the.NET types that APL should map arrays to before calling a .NET function. For example, if a parameter to a .NET function is declared as type <code class="language-nonAPL">System.Object</code>, it might be necessary to force the APL argument to be cast to a particular type of <code class="language-nonAPL">Object</code> before the function is called.

These requirements can be met by calling the function and specifying the _variant_ operator (`⍠`) with the `OverloadTypes` or the `CastToTypes` option respectively. Each option takes an array of references to .NET types, of the same length as the number of parameters to the function.

<h4 class="example">Example (using OverloadTypes option)</h4>

To force APL to call the double version of function `foo()` irrespective of the type of the argument `val`, enter:
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

Taking this a stage further, suppose that `foo()` is defined with 5 overloads, specifically:
```apl
foo()
foo(int i)
foo(double d)
foo(double d, int i)
foo(double[] d)

```

The following statements will call the `niladic`, `double`, `double,int`, and `double[]` overloads respectively:
```apl
(foo ⍠ (⊂⍬)) ⍬                               ⍝ niladic
(foo ⍠ Double) 1                             ⍝ double
(foo ⍠(⊂Double Int32))1 1                    ⍝ double,int
(foo ⍠(Type.GetType ⊂'System.Double[]'))⊂1 1 ⍝ double[]
```

!!! Info "Information"
    In the niladic case, an enclosed empty vector is used to represent a null reference to a .NET type.

<h4 class="example">Example (using CastToTypes option)</h4>

The .NET function <code class="language-nonAPL">Array.SetValue()</code> sets the value of a specified element (or elements) of an array. The first argument, the new value, is declared as <code class="language-nonAPL">System.Object</code>, but the value supplied must correspond to the type of the array. APL cannot determine what this is and passes the value unchanged, that is, in whatever internal format it happens to be. For example:
```apl
      ⎕USING←'System'

      ⍝ create a Boolean array with 2 elements
      BA←Array.CreateInstance Boolean 2
      BA.GetValue 0 ⍝ get the 0th element
0

      ⍝ attempt to set the 0th element to 1 (AKA true)
      BA.SetValue 1 0
EXCEPTION: Cannot widen from source type to target type
either because the source type is a not a primitive type or the conversion cannot be accomplished.
test[5] BA.SetValue 1 0
       ∧ 
```

The expression failed because APL passed the first argument `1`, unchanged from its internal representation, as a 1-byte integer – this does not fit into a Boolean element.

To rectify the situation, APL must be told to cast the argument to a Boolean:
```apl
      (BA.SetValue ⍠ ('CastToTypes'(Boolean Int32)))1 0
      BA.GetValue 0      ⍝ get the 0th element
1
```

### Overloaded Constructors

If a class provides constructor overloads, then a similar mechanism is used to specify which of the constructors is to be used when an instance of the class is created using `⎕NEW`.

For example, if <code class="language-nonAPL">MyClass</code> is a .NET class with an overloaded constructor, and one of its constructors is defined to take two parameters; a <code class="language-nonAPL">double</code> and an <code class="language-nonAPL">int</code>, then the following statement would create an instance of the class by calling that specific constructor overload:
```apl
      (⎕NEW ⍠ (⊂Double Int32)) MyClass (1 1)
```
