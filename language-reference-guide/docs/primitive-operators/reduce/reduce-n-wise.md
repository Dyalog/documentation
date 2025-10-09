<div style="display: none;">
  /
</div>

<h1 class="heading"><span class="name">Reduce N-Wise</span> <span class="command">R←Xf/[K]Y</span></h1>

`f` must be a dyadic function. `X` must be a simple scalar or one-item integer array. `Y` may be any array whose sub-arrays along the `K`th axis are appropriate to function `f`.

The axis specification is optional. If present, `K` must identify an axis of `Y`. If absent, the last axis of `Y` is implied. The form `R←Xf⌿Y` implies the first axis of `Y`.

`R` is an array formed by applying function `f` between items of sub-vectors of length `X` taken from vectors along the `K`th (or implied) axis of `Y`.

`X` can be thought of as the width of a "window" which moves along vectors drawn from the `K`th axis of `Y`.

If `X` is zero, the result is a `(⍴Y)+(-⍴⍴Y)↑1` array of identity elements for the function `f`. See [Identity Elements](index.md/#IdentityElements).

If `X` is negative, each sub-vector is reversed before being reduced.

<h2 class="example">Examples</h2>

```apl
      ⍳4
1 2 3 4
 
      3+/⍳4    ⍝ (1+2+3) (2+3+4)
6 9
      2+/⍳4    ⍝ (1+2) (2+3) (3+4)
3 5 7
      1+/⍳4    ⍝ (1) (2) (3) (4)
1 2 3 4
 
      0+/⍳4    ⍝ Identity element for +
0 0 0 0 0
      0×/⍳4    ⍝ Identity element for ×
1 1 1 1 1
 
      2,/⍳4    ⍝ (1,2) (2,3) (3,4)
 1 2  2 3  3 4 
      ¯2,/⍳4   ⍝ (2,1) (3,2) (4,3)
 2 1  3 2  4 3 
```
