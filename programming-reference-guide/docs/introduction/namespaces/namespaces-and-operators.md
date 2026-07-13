# Namespaces and Operators

A function passed as operand to a primitive or defined operator, carries its namespace context with it. This means that if subsequently, the function operand is applied to an argument, it executes in its home namespace, irrespective of the namespace from which the operator was invoked or defined.

<h2 class="example">Examples</h2>
```apl
      VAR←99                     ⍝ #.VAR
 
      )NS X
#.X
      X.VAR←77                   ⍝ X.VAR
      X.⎕FX'Z←FN R' 'Z←R,VAR'
 
      )NS Y
#.Y
      Y.VAR←88                   ⍝ Y.VAR
      Y.⎕FX'Z←(F OP)R' 'Z←F R'

      X.FN¨⍳3
 1 77  2 77  3 77

      X.FN 'VAR:'
 VAR: 77
 
      X.FN Y.OP 'VAR:'
 VAR: 77
      ⍎ Y.OP'VAR'
99
```
