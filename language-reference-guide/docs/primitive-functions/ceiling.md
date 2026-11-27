---
search:
  boost: 2
---

# <span>Ceiling</span> `R←⌈Y`{{key}}

_Ceiling_ is defined in terms of _floor_ as `⌈Y←→-⌊-Y`

`Y` must be numeric.

If an element of `Y` is real, the corresponding element of `R` is the least integer greater than or equal to the value of `Y`.

If an element of `Y` is complex, the corresponding element of `R` depends on the relationship between the real and imaginary parts of the numbers in `Y`.

<h2 class="example">Examples</h2>
```apl
      ⌈¯2.3  0.1  100  3.3
¯2 1 100 4
 
      ⌈1.2j2.5 1.2j¯2.5
1J3 1J¯2
```

For further explanation, see [Floor](floor.md).

`⎕CT` is an implied argument of _ceiling_.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⌈ ceiling
</div>
