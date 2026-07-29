

# <span>VALUE ERROR</span> `6`

This report is given when either:

- There is no active definition for a name encountered in an expression.
- A function does not return a result in a context where a result is required.

<h2 class="example">Examples</h2>
```apl
     X
VALUE ERROR
     X
     ^
 
     ∇ HELLO
[1]    'HI THERE'
[2]  ∇
 
     2+HELLO
HI THERE
VALUE ERROR
     2+HELLO
      ^
```
