




# <span>Repeat Statement</span> `:Repeat`



[Formal Definition](repeat-statement-definition.md){: .noprint }


The simplest type of `:Repeat` loop is as follows.  This example executes lines `[3-5]` 100 times.  Notice that as there is no conditional test at the beginning of a `:Repeat` structure, its code statements are executed at least once.
```apl
[1]   I←0
[2]   :Repeat
[3]       expr1
[4]       expr2
[5]       I←I+1
[6]   :Until I=100
```



You can have multiple conditional tests at the end of the loop by adding `:AndIf` or `:OrIf` expressions.  The following example will read data from a native file as 80-character records until it reaches one beginning with the text string `'Widget'` or reaches the end of the file.
```apl
[1]   :Repeat
[2]       REC←⎕NREAD ¯1 82 80
[3]   :Until 'Widget'≡6⍴REC
[4]   :OrIf 0=⍴REC
```


A `:Repeat` structure may be terminated by an `:EndRepeat` (or `:End`) statement in place of a conditional expression.  If so, your code must explicitly jump out of the loop using a `:Leave` statement or by branching.  For example:
```apl
[1]   :Repeat
[2]       REC←⎕NREAD ¯1 82 80
[3]      :If 0=⍴REC
[4]      :OrIf 'Widget'≡6⍴REC
[5]         :Leave
[6]      :EndIf
[7]   :EndRepeat
```





