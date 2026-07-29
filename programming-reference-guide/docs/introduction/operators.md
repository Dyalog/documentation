# Operators

An operator is an operation on one or two operands which produces a function called a DERIVED FUNCTION. An operand may be a function or an array.  Operators are not ambivalent.  They require either one or two operands as applicable to the particular operator.  However, the derived function may be ambivalent.  The derived function need not return a result.  Operators have higher precedence than functions.  Operators have long scope on the left.  That is, the left operand is the longest function or array expression on its left.  The left operand may be terminated by:

1. the end of the expression
2. a function with a function to its left
3. a function with an array to its left
4. an array with a function to its left
5. an array or function to the right of a monadic operator.
6. A dyadic operator has short scope on the right.  That is, the right operand of an operator is the single function or array on its right. Right scope may be extended by enclosing an expression in parentheses.

<h2 class="example">Examples</h2>
```apl
      ⍴¨X←'WILLIAM' 'MARY' 'BELLE'
 7  4  5
 
      ⍴∘⍴¨X
 1  1  1
 
      (⍴∘⍴)¨X
 1  1  1
```
```apl

 
      ⎕∘←∘⎕VR¨'PLUS' 'MINUS'
     ∇ R←A PLUS B
[1]    R←A+B
     ∇
     ∇ R←A MINUS B
[1]    R←A-B
     ∇
 
      PLUS/1 2 3 4
10
```

## Defined Operators

Operators may be defined with the system function `⎕FX`, or with the function editor. A defined operator consists of a HEADER which identifies the syntax of the operator, and a BODY in which one or more APL statements are specified.

A defined operator may have one or two operands; and its derived function may have one or two arguments, and may or may not produce a result. The header syntax defines the operator name, its operand(s), the argument(s) to its derived function, and the result (if any) of its derived function. The names of the operator and its operand(s) are separated from the name(s) of the argument(s) to its derived function by parentheses.

<h3 class="example">Example</h3>
```apl
      ∇ R←A(F AND G)B
[1]     R←(A F B)(A G B)
      ∇
```

The above example shows a dyadic operator called AND with two operands (`F` and `G`). The operator produces a derived function which takes two arguments (`A` and `B`), and produces a result (`R`).
```apl
      12 +AND÷ 4
16 3
```

Operands passed to an operator may be either functions or arrays.
```apl
      12 (3 AND 5) 4
12 3 4  12 5 4
 
      12 (× AND 5) 4
48  12 5 4
```
