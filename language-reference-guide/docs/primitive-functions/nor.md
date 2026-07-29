---
search:
  boost: 2
---

# <span>NOR</span> `R←X⍱Y`{{key}}

`Y` must be a Boolean array. `X` must be a Boolean array. `R` is Boolean. The value of `R` is the truth value of the proposition "neither `X` nor `Y`", and is determined as follows:
```apl
             X   Y     R
      
             0   0     1
             0   1     0
             1   0     0
             1   1     0
```

<h2 class="example">Example</h2>
```apl
      0 0 1 1 ⍱ 0 1 0 1
1 0 0 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍱ nor
</div>
