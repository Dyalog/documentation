<div style="display: none;">
  ↓
</div>






<h1 class="heading"><span class="name">Drop with Axes</span> <span class="command">R←X↓[K]Y</span></h1>



`Y` may be any non-scalar array.  `X` must be a simple integer scalar or vector.  `K` is a vector of zero or more axes of `Y`.


`R` is an array of the elements of `Y` with the first or last `X`[i] elements removed. Elements are removed from the beginning or end of `Y` according to the sign of `X`[i].


The rank of `R` is the same as the rank of `Y`:
```apl
       ⍴⍴R ←→ ⍴⍴Y
```


The size of each axis of `R` is determined by the corresponding element of `X`:
```apl
      (⍴R)[,K] ←→ 0⌈(⍴Y)[,K]-|,X
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
 
      1↓[2]M
 5  6  7  8
 9 10 11 12
           
17 18 19 20
21 22 23 24
 
      2↓[3]M
 3  4
 7  8
11 12
     
15 16
19 20
23 24
 
      2 1↓[3 2]M
 7  8
11 12
     
19 20
23 24
```


