<div style="display: none;">
  ↑
</div>






<h1 class="heading"><span class="name">Take with Axes</span> <span class="command">R←X↑[K]Y</span></h1>



`Y` may be any non-scalar array.  `X` must be a simple integer scalar or vector.  `K` is a vector of zero or more axes of `Y`.


`R` is an array of the first or last elements of `Y` taken along the axes `K` depending on whether the corresponding element of `X` is positive or negative respectively.


The rank of `R` is the same as the rank of `Y`:
```apl
      ⍴⍴R ←→ ⍴⍴Y
```


The size of each axis of `R` is determined by the corresponding element of `X`:
```apl
      (⍴R)[,K] ←→ |,X
```


<h2 class="example">Examples</h2>
```apl
      ⎕←M←2 3 4⍴⍳24
 1  2  3  4
 5  6  7  8
 9 10 11 12
 
13 14 15 16
17 18 19 20
21 22 23 24
 
      2↑[2]M
 1  2  3  4
 5  6  7  8
 
13 14 15 16
17 18 19 20
 
      2↑[3]M
 1  2
 5  6
 9 10
 
13 14
17 18
21 22
 
 
      2 ¯2↑[3 2]M
 5  6
 9 10
 
17 18
21 22
```


