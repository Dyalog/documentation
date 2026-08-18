---
search:
  boost: 2
---

# <span>Format (Monadic)</span> `R←⎕FMT Y`{{key}}

`Y` may be any array.  `R` is a simple character matrix which appears the same as the default display of `Y`.  If `Y` contains control characters from `⎕TC`, they will be resolved.

[`⎕PP`](../pp/) is an implicit argument of `⎕FMT`.

<h2 class="example">Examples</h2>
```apl
      A←⎕FMT '∩' ,⎕TC[1],'∘'
 
      ⍴A
1 1
      A
⍝
 
      A←⎕VR 'FOO'
 
      A
     ∇ R←FOO
[1]    R←10
     ∇
 
      ⍴A
31
      B←⎕FMT A
 
      B
     ∇ R←FOO
[1]    R←10
     ∇
 
      ⍴B
3 12
```

## See Also

- [Display of Arrays](../../../programming-reference-guide/introduction/arrays/display-of-arrays/) – how arrays appear in the session
- [`⍕`](../primitive-functions/format.md) – Format: returns a character array (vector or matrix depending on input rank)

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>
