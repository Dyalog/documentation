# Expressions

An expression is a sequence of one or more syntactic tokens which may be symbols or constants or names representing arrays (variables) or functions.  An expression which produces an array is called an ARRAY EXPRESSION. An expression which produces a function is called a FUNCTION EXPRESSION. Some expressions do not produce a result.

An expression may be enclosed within parentheses.

Evaluation of an expression proceeds from right to left, unless modified by parentheses.  If an entire expression results in an array that is not assigned to a name, then that array value is displayed.  (Some system functions and defined functions return an array result only if the result is assigned to a name or if the result is the argument of a function or operator.)

<h2 class="example">Examples</h2>
```apl
      X←2×3-1
 
      2×3-1
4
      (2×3)-1
5
```

Either blanks or parentheses are required to separate constants, the names of variables, and the names of defined functions which are adjacent.  Excessive blanks or sets of parentheses are redundant, but permitted.  If `F` is a function, then:
```apl
      F 2←→ F(2) ←→ (F)2 ←→ (F) (2) ←→ F  (2) ←→ F ((2))
```

Blanks or parentheses are not needed to separate primitive functions from names or constants, but they are permitted:
```apl
      -2 ←→ (-)(2) ←→ (-) 2
```

Blanks or parentheses are not needed to separate operators from primitive functions, names or constants. They are permitted with the single exception that a dyadic operator must have its right argument available when encountered.  The following syntactical forms are accepted:
```apl
      (+.×) ←→ (+).× ←→ +.(×)
```

The use of parentheses in the following examples is not accepted:
```apl
      +(.)×  or     (+.)×
```
