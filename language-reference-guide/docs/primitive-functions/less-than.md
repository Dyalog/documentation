<div style="display: none;">
  <
</div>

<h1 class="heading"><span class="name">Less Than</span> <span class="command">R←X&lt;Y</span></h1>

`Y` may be any numeric array. `X` may be any numeric array. `R` is Boolean. `R` is 1 if `X` is less than `Y` and `X=Y` is 0. Otherwise `R` is 0.

`⎕CT` and `⎕DCT` are  implicit arguments of Less Than.

<h2 class="example">Examples</h2>
```apl
      (2 4) (6 8 10) < 6
 1 1  0 0 0
 
      ⎕CT←1E¯10
 
      1 0.99999999999 0.9999999999<1
0 0 1
```
