---
search:
  boost: 2
---

# <span>Assignment (Modified)</span> `{R}←Xf←Y`{{key}}

`f` may be any dyadic function which returns an explicit result.  `Y` may be any array  appropriate to function `f`.  `X` must be the *name* of an existing array appropriate to function `f`.

`R` is the “pass-through” value, that is, the value of `Y`.  If the result of the derived function is not assigned or used, there is no explicit result.

The effect of the derived function is to reset the value of the array named by `X` to the result of `XfY`.

!!! Info "Information"
    In a dfn or dop, modified assignment works only when `f` is a primitive. A named `f` is read as part of a multiple assignment, so `X plus←10` assigns `10` to both `X` and `plus`. Instead, modified assignment can be achieved by inserting `∘⊢`, that is, `X plus∘⊢←10`. 

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

<!-- Hidden search keywords -->
<div style="display: none;">
  ← gets
</div>
