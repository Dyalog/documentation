<div style="display: none;">
  ≢
</div>

<h1 class="heading"><span class="name">Tally</span> <span class="command">R←≢Y</span></h1>

`Y` may be any array.  `R` is a simple numeric scalar.

Tally returns the number of major cells of `Y`. See [Cells and Sub-arrays](../../../programming-reference-guide/introduction/arrays/cells-and-subarrays).

This can also be expressed as the length of the leading axis or 1 if `Y` is a scalar. Tally is equivalent to the function `{⍬⍴(⍴⍵),1}`.

<h2 class="example">Examples</h2>
```apl
      ≢2 3 4⍴⍳10
2
      ≢2
1
      ≢⍬
0
```

Note that `≢V` is useful for returning the length of vector `V` as a scalar.  (In contrast, `⍴V` is a one-element vector.)



