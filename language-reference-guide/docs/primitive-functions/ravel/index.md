<div style="display: none;">
  ,
</div>

<h1 class="heading"><span class="name">Ravel</span> <span class="command">R←,Y</span></h1>

`Y` may be any array.  `R` is a vector of the elements of `Y` taken in row-major order.

<h2 class="example">Examples</h2>
```apl
      M
1 2 3
4 5 6
 
      ,M
1 2 3 4 5 6
 
      A
ABC
DEF
GHI
JKL
      ,A
ABCDEFGHIJKL
 
      ⍴,10
1
```

See also: [Ravel with Axes](ravel-with-axes.md).



