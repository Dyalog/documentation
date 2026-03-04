# Specifying Overloads

If a .NET function is overloaded in terms of the types of arguments that it accepts, then Dyalog chooses which overload to call depending on the data types of the arguments passed to it. For example, if a .NET function `foo()` is declared to take a single argument either of type `int` or of type `double`, Dyalog would call the first version if you called it with an integer value and the second version if you called it with a floating-point value.

Occasionally it might be desirable to override this mechanism and explicitly specify which overload to use. This can be done by calling the function and specifying the Variant operator `⍠` with the OverloadTypes option. This takes an array of references to .NET types, of the same length as the number of parameters to the function.

Example

To force APL to call the double version of function `foo()` irrespective of the type of the argument `val`, enter:
```apl
      (foo ⍠('OverloadTypes'Double))val
```

or (more simply):
```apl
      (foo ⍠Double)val
```

where `Double` is a reference to the .NET type System.Double.
```apl
      ⎕USING←'System'
      Double
(System.Double)
		
```

Taking this a stage further, suppose that `foo()` is defined with 5 overloads as follows:
```
foo()
foo(int i)
foo(double d)
foo(double d, int i)
foo(double[] d)

```

The following statements will call the niladic, double, (double, int) and double`[]` overloads respectively:
```apl
(foo ⍠ (⊂⍬)) ⍬                               ⍝ niladic
(foo ⍠ Double) 1                             ⍝ double
(foo ⍠(⊂Double Int32))1 1                    ⍝ double,int
(foo ⍠(Type.GetType ⊂'System.Double[]'))⊂1 1 ⍝ double[]
```
