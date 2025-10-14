<div style="display: none;">
  ¨
</div>






<h1 class="heading"><span class="name">Each (with Dyadic Operand)</span> <span class="command">{R}←Xf¨Y</span></h1>



`f` may be any dyadic function.  `X` and `Y` may be any arrays whose corresponding items (after scalar extension) are appropriate to function `f` when applied separately.


The derived function is applied separately to each pair of corresponding elements of `X` and `Y`.  If `X` or `Y` is a scalar or single-element array, it will be extended to conform with the other argument.  The derived function need not produce an explicit result.  If a result is returned, `R` has the same shape as `Y` (after possible scalar extension) whose elements are the items produced by the application of the derived function to the corresponding items of `X` and `Y`.


If `X` or `Y` is empty, the operand function is applied *once* between the prototypes of `X` and `Y` to determine the prototype of `R`.


<h2 class="example">Examples</h2>
```apl
      +G←(1 (2 3))(4 (5 6))(8 9)10
   1  2 3   4  5 6   8 9  10
      1⌽¨G
  2 3  1   5 6  4  9 8  10
 
      1⌽¨¨G
 1  3 2   4  6 5   8 9  10
 
      1⌽¨¨¨G
 1  2 3   4  5 6   8 9  10
 
      1 2 3 4↑¨G
 1  4  5 6   8 9 0  10 0 0 0
 
      'ABC',¨'XYZ'
 AX  BY  CZ
```


