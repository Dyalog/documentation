<div style="display: none;">
  >
</div>






<h1 class="heading"><span class="name">Greater Than</span> <span class="command">R←X>Y</span></h1>



`Y` must be numeric. `X` must be numeric. `R` is Boolean. `R` is 1 if `X` is greater than `Y` and `X=Y` is 0. Otherwise `R` is 0.


`⎕CT` and `⎕DCT` are  implicit arguments of Greater Than.

<h2 class="example">Examples</h2>
```apl
      1 2 3 4 5 > 2
0 0 1 1 1
 
      ⎕CT←1E¯10
 
      1 1.00000000001 1.000000001 > 1
0 0 1
```



