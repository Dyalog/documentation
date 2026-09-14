---
search:
  boost: 2
---

# <span>Less Than Or Equal To</span> `R←X≤Y`{{key}}

`Y` may be any numeric array. `X` may be any numeric array. `R` is Boolean. `R` is 1 if `X` is less than `Y` or `X=Y`. Otherwise `R` is 0.

`⎕CT` and `⎕DCT` are  implicit arguments of _less than or equal to_.

<h2 class="example">Examples</h2>
```apl
      2 4 6 8 10 ≤ 6
1 1 1 0 0
 
      ⎕CT←1E¯10
 
      1  1.00000000001 1.00000001 ≤ 1
1 1 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ≤
</div>
