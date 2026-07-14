

# <span>If Statement</span> `:If bexp`

[Formal Definition](if-statement-definition.md){: .noprint }

The simplest `:If` control structure is a single condition of the form:
```apl
[1]   :If AGE<21
[2]       expr 1
[3]       expr 2
[5]   :EndIf
```

If the test condition (in this case `AGE<21`) is true, the statements between the `:If` and the `:EndIf` will be executed.  If the condition is false, none of these statements will be run and execution resumes after the `:EndIf`.  Note that the test condition to the right of `:If` must return a single element Boolean value 1 (true) or 0 (false).

`:If` control structures may be considerably more complex.  For example, the following code will execute the statements on lines `[2-3]` if `AGE<21` is 1 (true), **or alternatively**, the statement on line `[6]` if `AGE<21` is 0 (false).
```apl
[1]   :If AGE<21
[2]       expr 1    
[3]       expr 2
[5]   :Else
[6]       expr 3
[7]   :EndIf
```

Instead of a single condition, it is possible to have multiple conditions using the `:ElseIf` control word.  For example:
```apl
[1]   :If WINEAGE<5
[2]       'Too young to drink'
[5]   :ElseIf WINEAGE<10
[6]       'Just Right'
[7]   :ElseIf WINEAGE<15
[8]       'A bit past its prime'
[9]   :Else
[10]     'Definitely over the hill'
[11]  :EndIf
```

Notice that APL executes the expression(s) associated with the **first** condition that is true or those following the `:Else` if **none** of the conditions are true.

The `:AndIf` and `:OrIf` control words may be used to define a block of conditions and so refine the logic still further.  You may qualify an `:If` or an `:ElseIf` with one or more `:AndIf` statements **or** with one or more `:OrIf` statements.  You may not however mix `:AndIf` and `:OrIf` in the same conditional block.  For example:
```apl
[1]   :If WINE.NAME≡'Chateau Lafitte'
[2]   :AndIf WINE.YEAR∊1962 1967 1970
[3]       'The greatest?'
[4]   :ElseIf WINE.NAME≡'Chateau Latour'
[5]   :Orif WINE.NAME≡'Chateau Margaux'
[6]   :Orif WINE.PRICE>100    
[7]       'Almost as good'
[8]   :Else
```
```apl
[9]       'Everyday stuff'
[10]  :EndIf
```

Please note that in a `:If` control structure, the conditions associated with each of the condition blocks are executed in order until an entire condition block evaluates to true.  At that point, the APL statements following this condition block are executed.  None of the conditions associated with any other condition block are executed.  Furthermore, if an `:AndIf` condition yields 0 (false), it means that the entire block must evaluate to false so the system moves immediately on to the next block without executing the other conditions following the failing `:AndIf`.  Likewise, if an `:OrIf` condition yields 1 (true), the entire block is at that point deemed to yield true and none of the following `:OrIf` conditions in the same block are executed.
