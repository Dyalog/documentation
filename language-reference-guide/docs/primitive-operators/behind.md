<div style="display: none;">
  ⍛
</div>

<h1 class="heading"><span class="name">Behind</span> <span class="command">{R}←{X}f⍛gY</span></h1>

!!! Info "Information"
    The `⍛` glyph is not available in Classic Edition, and the _behind_ operator is instead represented by `⎕U235B`.

`f` can be any monadic function that returns a result; the result must be suitable as the left argument to the function `g`.

`g` can be any dyadic function; it does not need to return a result.

`Y` can be any array that is suitable as the right argument to the function `g`.
If `X` is omitted, `Y` must also be suitable as the right argument to the function `f`.

`X` can be any array that is suitable as the right argument to the function `f`.

The derived function is equivalent to either `(f Y) g Y` or `(f X) g Y`, depending on whether `X` is specified or not.

The _behind_ operator allows functions to be *glued* together to build up more complex functions. For further information, see [Function Composition](./operator-syntax.md).

<h2 class="example">Examples</h2>
```apl
      ⍝ Is it a palindrome?
      ⌽⍛≡ 'Dyalog' 
0
      ⌽⍛≡ 'racecar'
1

      ⍝ Drop from the right
      4-⍛↓'Dyalog APL'
Dyalog
```
