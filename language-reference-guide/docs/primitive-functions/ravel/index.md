---
search:
  boost: 2
---

# <span>Ravel</span> `R←,Y`{{key}}

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

<!-- Hidden search keywords -->
<div style="display: none;">
  , ravel
</div>
