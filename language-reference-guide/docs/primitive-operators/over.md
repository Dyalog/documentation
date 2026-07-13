---
search:
  boost: 2
---
<div style="display: none;">
  ⍥
  over
</div>

# <span>Over</span> `{R}←{X}f⍥gY`{{key}}

!!! Info "Information"
    The `⍥` glyph is not available in Classic Edition, and the _behind_ operator is instead represented by `⎕U2365`.

The _over_ operator allows functions to be *glued* together to build up more complex functions. For further information, see [Function Composition](./function-composition.md).

`g` can be any monadic function which returns a result.  `Y` can be any array that is suitable as the argument to function `g` with `gY` being suitable as the right argument to function `f`.

If `X` is omitted, `f` must be a monadic function. If `X` is specified, `f` must be a dyadic function and `X` can be any array that is suitable as argument to function `g` with `gX` being suitable as the left argument to function `f`.

The derived function is equivalent to `fgY` or `(gX)f(gY)` and need not return a result.

<h2 class="example">Examples</h2>
```apl
      2 3 ,⍥⊂ 'text'   ⍝ ,⍥⊂  ←→  {⍺⍵}
┌───┬────┐
│2 3│text│
└───┴────┘
 
     scores←82 90 76
     weights←20 35 45
     (weights×scores)÷⍥(+/)weights ⍝ Weighted average
82.1
```
