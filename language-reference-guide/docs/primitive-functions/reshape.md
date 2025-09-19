<div style="display: none;">
  ⍴
</div>






<h1 class="heading"><span class="name">Reshape</span> <span class="command">R←X⍴Y</span></h1>



`Y` may be any array.  `X` must be a simple scalar or vector of non-negative integers.  `R` is an array of shape `X` whose elements are taken from `Y` in row-major sequence and repeated cyclically if required.  If `Y` is empty, `R` is composed of fill elements of `Y` (`⊂∊⊃Y` with `⎕ML←0`).  If `X` contains at least one zero, then `R` is empty.  If `X` is an empty vector, then `R` is scalar.

<h2 class="example">Examples</h2>
```apl
      2 3⍴⍳8
1 2 3
4 5 6
 
      2 3⍴⍳4
1 2 3
4 1 2
 
      2 3⍴⍳0
0 0 0
0 0 0
```



