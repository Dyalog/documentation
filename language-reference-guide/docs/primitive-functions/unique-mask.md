---
search:
  boost: 2
---

# <span>Unique Mask</span> `R←≠Y`{{key}}

`Y` may be any array.

`R` is a Boolean vector whose length is the number of major cells
in `Y`. For each major cell of `Y`, the corresponding element of  `R` is 1 if it is the first occurrence of that value, and 0 if it is a duplicate of an earlier major cell.

`⎕CT` and `⎕DCT` are  implicit arguments of _unique_.

<h2 class="example">Examples</h2>
```apl
      ≠22 10 22 22 21 10 5 10
1 1 0 0 1 0 1 0

```
```apl

      ≠ v←'CAT' 'DOG' 'CAT' 'DUCK' 'DOG' 'DUCK'
1 1 0 1 0 0

      ⊢mat←↑v 
CAT 
DOG 
CAT 
DUCK
DOG 
DUCK
      ≠mat
1 1 0 1 0 0

```

<!-- Hidden search keywords -->
<div style="display: none;">
  ≠ nubsieve unique mask
</div>
