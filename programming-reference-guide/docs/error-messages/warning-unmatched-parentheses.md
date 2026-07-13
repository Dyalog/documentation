




# warning unmatched parentheses



This report is given after adding or editing a function line in definition mode when it is found that there is not an opening parenthesis to match a closing parenthesis, or vice versa, in an expression.  This is a warning message only.  The function line will be accepted even though syntactically incorrect.

<h2 class="example">Example</h2>
```apl
[4]   X←(E>2)^E<10)⌿A
warning unmatched parentheses
[5]
```






