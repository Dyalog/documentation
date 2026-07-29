# Functions

A function is an operation which is performed on zero, one or two array arguments and may produce an array result.  Three forms are permitted:

- NILADIC defined for no arguments
- MONADIC defined for a right but not a left argument
- DYADIC defined for a left and a right argument

The number of arguments is referred to as its VALENCE.

The name of a non-niladic function is AMBIVALENT; that is, it potentially represents both a monadic and a dyadic function, though it might not be defined for both.  The usage in an expression is determined by syntactical context.  If the usage is not defined an error results.

Functions have long SCOPE on the right; that is, the right argument of the function is the result of the entire expression to its right which must be an array.  A dyadic function has short scope on the left; that is, the left argument of the function is the array immediately to its left.  Left scope may be extended by enclosing an expression in parentheses whence the result must be an array.

For some functions, the explicit result is suppressed if it would otherwise be displayed on completion of evaluation of the expression. This applies on assignment to a variable name.  It applies for certain system functions, and may also apply for defined functions.

<h2 class="example">Examples</h2>
```apl
      10×5-2×4
¯30
      2×4
8
      5-8
¯3
      10×¯3
¯30
      (10×5)-2×4
42
```

## Defined Functions

Functions may be defined with the system function `⎕FX`, or with the function editor. A function consists of a HEADER which identifies the syntax of the function, and a BODY in which one or more APL statements are specified.

The header syntax identifies the function name, its (optional) result and its (optional) arguments. If a function is ambivalent, it is defined with two arguments but with the left argument within braces (`{}`).  If an ambivalent function is called monadically, the left argument has no value inside the function.  If the explicit result is to be suppressed for display purposes, the result is shown within braces.  A function need not produce an explicit result.  Refer to *Chapter 2* for further details.

<h3 class="example">Example</h3>
```apl
     ∇ R←{A} FOO B
[1]    R←⊃'MONADIC' 'DYADIC'[⎕IO+0≠⎕NC'A']
[2]  ∇
 
      FOO 1
MONADIC
 
      'X' FOO 'Y'
DYADIC
```

Functions may also be created by using assignment (`←`).

## Function Assignment & Display

The result of a function-expression may be given a name.  This is known as FUNCTION ASSIGNMENT (see also [Dfns & Dops](../defined-functions-and-operators/dfns-and-dops/dynamic-functions-and-operators.md)).  If the result of a function-expression is not given a name, its value is displayed.  This is termed FUNCTION DISPLAY.

<h3 class="example">Examples</h3>
```apl
      PLUS←+
      PLUS
+
      SUM←+/
      SUM
+/
```

Function expressions may include defined functions and operators. These are displayed as a `∇` followed by their name.

<h3 class="example">Example</h3>
```apl
      ∇ R←MEAN X    ⍝ Arithmetic mean
[1]     R←(+/X)÷⍴X
      ∇

      MEAN
 ∇MEAN
      AVERAGE←MEAN
      AVERAGE
 ∇MEAN
      AVG←MEAN∘,
      AVG
 ∇MEAN ∘,
```
