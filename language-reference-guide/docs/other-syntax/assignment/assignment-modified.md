<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment (Modified)</span> <span class="command">{R}←Xf←Y</span></h1>

`f` may be any dyadic function which returns an explicit result.  `Y` may be any array  appropriate to function `f`.  `X` must be the *name* of an existing array appropriate to function `f`.

`R` is the “pass-through” value, that is, the value of `Y`.  If the result of the derived function is not assigned or used, there is no explicit result.

The effect of the derived function is to reset the value of the array named by `X` to the result of `XfY`.

<h2 class="example">Examples</h2>
```apl
      A
1 2 3 4 5
 
      A+←10
 
      A
11 12 13 14 15
 
      ⎕←A×←2
2
      A
22 24 26 28 30
 
      vec←¯4+9?9 ⋄ vec
3 5 1 ¯1 ¯2 4 0 ¯3 2
      vec/⍨←vec>0 ⋄vec
3 5 1 4 2
```
