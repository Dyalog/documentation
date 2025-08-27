<div style="display: none;">
  ∘
</div>






<h1 class="heading"><span class="name">Beside</span> <span class="command">{R}←{X}f∘gY</span></h1>



`g` can be any monadic function which returns a result.  `Y` can be any array appropriate to function `g` with `gY` being suitable as the right argument to function `f`.


If `X` is omitted, `f` must be a monadic function. If `X` is specified, `f` must be a dyadic function and `X` can be any array that is suitable as the left argument to function `f`.


The derived function is equivalent to `fgY` or `XfgY` and need not return a result.


The Beside operator allows functions to be glued together to build up more complex functions. For further information, see [Function Composition](../operator-syntax#function-composition).


<h2 class="example">Examples</h2>
```apl
      RANK ← ⍴∘⍴
      RANK ¨ 'JOANNE' (2 3⍴⍳6)
 1  2
```
```apl
      +/∘⍳¨2 4 6
3 10 21
 
 
      ⎕VR'SUM'
     ∇ R←SUM X
[1]    R←+/X
     ∇
 
      SUM∘⍳¨2 4 6
3 10 21
```
```apl
      +∘÷/40⍴1       ⍝ Golden Ratio! (Bob Smith)
1.618033989
 
      0,∘⍳¨⍳5
0 1  0 1 2  0 1 2 3  0 1 2 3 4  0 1 2 3 4 5
```


