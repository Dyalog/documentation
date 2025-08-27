<div style="display: none;">
  ⍷
</div>






<h1 class="heading"><span class="name">Find</span> <span class="command">R←X⍷Y</span></h1>



`X` and `Y` may be any arrays.  `R` is a simple Boolean array the same shape as Y which identifies occurrences of `X` within `Y`.


If the rank of `X` is smaller than the rank of `Y`, `X` is treated as if it were the same rank with leading axes of size 1.  For example a vector is treated as a 1-row matrix.


If the rank of `X` is larger than the rank of `Y`, no occurrences of `X` are found in `Y`.


`⎕CT` and `⎕DCT` are implicit arguments of Find.


<h2 class="example">Examples</h2>
```apl
      'AN'⍷'BANANA'
0 1 0 1 0 0
 
      'ANA'⍷'BANANA'
0 1 0 1 0 0
 
      'BIRDS' 'NEST'⍷'BIRDS' 'NEST' 'SOUP'
1 0 0
 
      MAT
IS YOU IS
OR IS YOU
ISN'T
      'IS'⍷MAT
1 0 0 0 0 0 0 1 0
0 0 0 1 0 0 0 0 0
1 0 0 0 0 0 0 0 0
      'IS YOU'⍷MAT
1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```


