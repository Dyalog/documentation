




# <span>SYNTAX ERROR</span> `2`



This report is given when a line of characters does not constitute a meaningful statement.  This condition occurs when either:

- An illegal symbol is found in an expression.
- Brackets, parentheses or quotes in an expression are not matched.
- Parentheses in an expression are not matched.
- Quotes in an expression are not matched.
- A value is assigned to a function, label, constant or system constant.
- A strictly dyadic function (or derived function) is used monadically.
- A monadic function (or derived function) is used dyadically.
- A monadic or dyadic function (or derived function) is used without any arguments.
- The operand of an operator is not an array when an array is required.
- The operand of an operator is not a function (or derived function) when a function is required.
- The operand of an operator is a function (or derived function) with incorrect valency.
- A dyadic operator is used with only a single operand.
- An operator is used without any operands.

<h2 class="example">Examples</h2>
```apl
      A>10)/A
SYNTAX ERROR
      A>10)/A
      ^
 
      ⊤2 4 8
SYNTAX ERROR
      ⊤2 4 8
      ^
 
      A.+1 2 3
SYNTAX ERROR
      A.+1 2 3
      ^
```



