---
search:
  boost: 2
---

# <span>Logarithm</span> `R←X⍟Y`{{key}}

`X` and `Y` must be numeric arrays. `X` cannot be 1 unless `Y` is also 1. `R` is the base `X` logarithm of `Y`.

Note that _logarithm_ (dyadic `⍟`) is defined in terms of _natural logarithm_ (monadic `⍟`) as:
```apl
      X⍟Y←→(⍟Y)÷⍟X
```

<h2 class="example">Examples</h2>
```apl
      10⍟100 2
2 0.3010299957
 
      2 10⍟0J1 1J2
0J2.266180071 0.3494850022J0.4808285788
 
      1 ⍟ 1
1
      2 ⍟ 1
0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍟ log logarithm
</div>
