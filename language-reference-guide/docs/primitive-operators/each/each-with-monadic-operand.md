<div style="display: none;">
  ¨
</div>






<h1 class="heading"><span class="name">Each (with Monadic Operand)</span> <span class="command">{R}←f¨Y</span></h1>



`f` may be any monadic function.  `Y` may be any array, each of whose items are separately appropriate to function `f`.


The derived function applies function `f` separately to each item of `Y`.  The derived function need not return a result.  If a result is returned, `R` has the same shape as `Y`, and its elements are the items produced by the application of function `f` to the corresponding items of `Y`.


If `Y` is empty, the prototype of `R` is determined by applying the operand function *once* to the prototype of `Y`.


<h2 class="example">Examples</h2>
```apl
      G←('TOM' (⍳3))('DICK' (⍳4))('HARRY' (⍳5))
      ⍴G
3
      ⍴¨G
 2  2  2
 
      ⍴¨¨G
  3  3    4  4    5  5
 
      +⎕FX¨('FOO1' 'A←1')('FOO2' 'A←2')
 FOO1 FOO2
```


