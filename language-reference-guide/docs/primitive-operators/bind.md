---
search:
  boost: 2
---
<div style="display: none;">
  ∘
  bind
</div>

# <span>Bind</span> <code>{R}←A∘fY<br>{R}←(f∘B)Y</code>{{key}}

The Bind operator binds an array `A` or `B` to a dyadic function `f` either as its left or its right argument respectively. The former may be described as left argument currying and the latter as right argument currying.

`A`, `B` and `Y` may be any arrays whose items are appropriate to function `f`. In the case where `B` is bound as the right argument of function `f`, the parentheses are required in order to distinguish between the operand `B` and the argument `Y`.

The derived function is equivalent to `AfY` or `YfB` and need not return a result.

<h2 class="example">Examples</h2>
```apl
      2 2∘⍴ ¨ 'AB'
 AA  BB
 AA  BB
 
      SINE ← 1∘○
 
      SINE 10 20 30
¯0.5440211109 0.9129452507 ¯0.9880316241
```
```apl
      (*∘0.5)4 16 25
2 4 5
 
      SQRT ← *∘.5
 
      SQRT 4 16 25
2 4 5
```

The following example uses both forms of Bind to list functions in the workspace:
```apl
      ⎕NL 3
ADD
PLUS
 
      ⎕∘←∘⎕VR¨↓⎕NL 3
     ∇ ADD X
[1]    →LAB⍴⍨0≠⎕NC'SUM' ⋄ SUM←0
[2]   LAB:SUM←SUM++/X
     ∇
     ∇ R←A PLUS B
[1]    R←A+B
     ∇
```
