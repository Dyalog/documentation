---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STACK STACK
</div>






<h1 class="heading"><span class="name">State Indicator Stack</span> <span class="command">R←⎕STACK</span></h1>



`R` is a two-column matrix, with one row per entry in the state indicator.


Column 1 :`⎕OR` form of user defined functions or operators on the state indicator.  Space (`⎕UCS 32`) for entries that are not user defined functions or operators.


Column 2 :Indication of the type of the item on the stack.


|-------|---------------------------------|
|`space`|user defined function or operator|
|`⍎`    |execute level                    |
|`⎕`    |evaluated input                  |
|`*`    |desk calculator level            |
|`⎕DQ`  |in callback function             |
|`other`|primitive operator               |


<h2 class="example">Example</h2>
```apl

      )SI
#.PLUS[2]*
.
#.MATDIV[4]
#.FOO[1]*
⍎

      ⎕STACK
         *
∇PLUS
         .
∇MATDIV
         *
∇FOO
         ⍎
         *

      ⍴⎕STACK
8 2

      (⍴⎕LC)=1↑⍴⎕STACK
0
```


Pendent defined functions and operators may be edited in Dyalog APL with no resulting SI damage.  However, only the visible definition is changed; the pendent version on the stack is retained until its execution is complete.  When the function or operator is displayed, only the visible version is seen.  Hence `⎕STACK` is a tool which allows the user to display the form of the actual function or operator being executed.

<h2 class="example">Example</h2>


To display the version of `MATDIV` currently pendent on the stack:
```apl

      ⊃⎕STACK[4;1]
     ∇ R←A MATDIV B
[1]   ⍝ Divide matrix A by matrix B
[2]    C←A⌹B
[3]   ⍝ Check accuracy
[4]    D←⌊0.5+A PLUS.TIMES B
     ∇
```


