<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment (Indexed Modified)</span> <span class="command">{R}←X[I]f←Y</span></h1>

`f` may be any dyadic function which returns an explicit result.  `Y` may be any array whose items are appropriate to function `f`.  `X` must be the *name* of an existing array.  `I` must be a valid index specification.  The items of the indexed portion of `X` must be appropriate to function `f`.

`Y` is either an array of the same shape as the indices specified by `I` or a scalar that is notionally extended to be the same shape as those indices.

The operator loops through the indices specified by `I` in ravel order. For each successive index `i` in the set specified by `I`,     it calculates the result of `X[i]fY[i]` and assigns it back to `X[i]`.

`R` is the "pass-through" value, that is, the value of `Y`.  If the result of the derived function is not assigned or used, there is no explicit result.

<h2 class="example">Examples</h2>
```apl
      A
1 2 3 4 5
 
      +A[2 4]+←1
1
 
      A
1 3 3 5 5
 
      A[3]÷←2
 
      A
1 3 1.5 5 5
```


As the operator performs a loop, if an index in `I` is repeated, function `f` will be applied that number of times and successively to the same item of `X`.

<h2 class="example">Example</h2>
```apl
      B←3 5⍴0
      B[1 1 3;1 3 3 5]+←1
      B
2 0 4 0 2
0 0 0 0 0
1 0 2 0 1

```
