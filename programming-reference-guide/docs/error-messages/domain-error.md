

# <span>DOMAIN ERROR</span> `11`

This report is given when either:

- An argument of a function is not of the correct type or its numeric value is outside the range of permitted values or its character value does not constitute valid name(s) in the context.
- An array operand of an operator is not an array, or it is not of the correct type, or its numeric value is outside the range of permitted values.  A function operand of an operator is not one of a prescribed set of functions.
- A value assigned to a system variable is not of the correct type, or its numeric value is outside the range of permitted values
- The result produced by a function includes numeric elements which cannot be fully represented.

<h2 class="example">Examples</h2>
```apl
      1÷0
DOMAIN ERROR
      1÷0
      ^
 
      (×∘'CAT')2 4 6
DOMAIN ERROR
      (×∘'CAT')2 4 6
      ^
 
      ⎕IO←5
DOMAIN ERROR
      ⎕IO←5
      ^
```
