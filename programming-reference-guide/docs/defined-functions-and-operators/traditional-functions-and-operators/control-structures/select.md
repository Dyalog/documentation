




# <span>Select Statement</span> `:Select aexp`



[Formal Definition](select-statement-definition.md){: .noprint }


A `:Select` structure is used to execute alternative blocks of code depending upon the value of an array.  For example, the following displays `'I is 1'` if the variable `I` has the value 1, `'I is 2'` if it is 2, or `'I is neither 1 nor 2'` if it has some other value.
```apl
[1]   :Select I
[2]   :Case 1
[3]       'I is 1'
[4]   :Case 2
[5]       'I is 2'
[6]   :Else
[7]       'I is neither 1 nor 2'
[8]   :EndSelect
```



In this case, the system compares the value of the array expression to the right of the `:Select` statement with each of the expressions to the right of the `:Case` statements and executes the block of code following the one that matches.  If none match, it executes the code following the `:Else` (which is optional).  Note that comparisons are performed using the `≡` primitive function, so the arrays must match exactly.  Note also that not all of the `:Case` expressions are necessarily evaluated because the process stops as soon as a matching expression is found.


Instead of a `:Case` statement, you may also use a `:CaseList` statement.  If so, the *enclose of* the array expression to the right of `:Select` is tested for membership of the array expression to the right of the `:CaseList` using the `∊` primitive function.


Note also that any code placed between the `:Select` and the first `:Case` or `:CaseList` statements are unreachable; future versions of Dyalog APL may generate an error when attempting to fix functions which include such code.

<h2 class="example">Example</h2>
```apl
[1]   :Select ?6 6
[2]   :Case 6 6
[3]       'Box Cars'
[4]   :Case 1 1
[5]       'Snake Eyes'
[6]   :CaseList 2⍴¨⍳6
[7]       'Pair'
[8]   :CaseList (⍳6),¨⌽⍳6
[9]       'Seven'
[10]  :Else
[11]      'Unlucky'
[12]  :EndSelect



```


