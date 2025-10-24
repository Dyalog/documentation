<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment (Selective Modified)</span> <span class="command">{R}←(EXP X)f←Y</span></h1>

`f` may be any dyadic function which returns an explicit result.  `Y` may be any array whose items are appropriate to function `f`.  `X` must be the *name* of an existing array.  `EXP` is an expression that **selects** elements of `X`. (See [Assignment (Selective)](assignment-selective.md) for a list of allowed selection functions.)  The selected elements of `X` must be appropriate to function `f`.

`Y` is either an array of the same shape as the selected elements of `X` or a scalar that is notionally extended to be the same shape as the selection.

The operator loops through the selected elements of `X` in ravel order. For each selected element `X[i]`,     it calculates the result of `X[i]fY[i]` and assigns it back to the same element `X[i]`.

`R` is the "pass-through" value, that is, the value of `Y`.  If the result of the derived function is not assigned or used, there is no explicit result.

<h2 class="example">Example</h2>
```apl
      A
12 36 23 78 30
 
      ((A>30)/A) ×← 100
      A
12 3600 23 7800 30
```

As the operator performs a loop, if an element of `X` is selected more than once,  function `f` will be applied the corresponding number of times and successively to the same element of `X`.
```apl
      a←3⍴0
      (5⍴a)+←1
      a
2 2 1
```
