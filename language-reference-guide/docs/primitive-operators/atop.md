---
search:
  boost: 2
---

# <span>Atop</span> `{R}←{X}f⍤gY`{{key}}

!!! Info "Information"
    The `⍤` glyph is not available in Classic Edition, and the _atop_ operator is instead represented by `⎕U2364`.

The _atop_ operator allows functions to be *glued* together to build up more complex functions. For further information, see [Function Composition](./function-composition.md).

`f` can be any monadic function.  `Y` can be any array that is suitable as the right argument to function `g` with the result of `g` being appropriate to function `f`.

If `X` is omitted, `g` must be a monadic function. If `X` is specified, `g` must be a dyadic function and `X` can be any array that is suitable as the left argument to function `g`.

The derived function is equivalent to `fgY` or `fXgY` and need not return a result.

<h2 class="example">Examples</h2>
```apl

      -⍤÷ 4      ⍝ (  f⍤g y) ≡  f   g y
¯0.25
      12 -⍤÷ 4   ⍝ (x f⍤g y) ≡ (f x g y)
¯3
      3 1 4 1 5 ~⍤∊ 1 2 3
0 0 1 0 1

```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍤
  atop
</div>
