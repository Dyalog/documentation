---
search:
  boost: 2
---
<div style="display: none;">
  ⌊ floor
</div>

# <span>Floor</span> `R←⌊Y`{{key}}

`Y` must be numeric.

For real numbers, `R` is the largest integer value less than or equal to `Y` within the comparison tolerance `⎕CT`.

<h2 class="example">Examples</h2>
```apl
      ⌊¯2.3 0.1 100 3.3
¯3 0 100 3
 
      ⌊0.5 + 0.4 0.5 0.6
0 1 1
```

For complex numbers, `R` depends on the relationship between the real and imaginary parts of the numbers in `Y`.
```apl
      ⌊1j3.2 3.3j2.5 ¯3.3j¯2.5
1J3 3J2 ¯3J¯3
```

## Complex Floor

The following (deliberately) simple function illustrates one way to express the rules for evaluating complex Floor.
```apl
     ∇ fl←CpxFloor cpxs;a;b
[1]   ⍝ Complex floor of scalar complex number (a+ib)
[2]    a b←9 11○cpxs
[3]    :If 1>(a-⌊a)+b-⌊b
[4]        fl←(⌊a)+0J1×⌊b
[5]    :Else
[6]        :If (a-⌊a)<b-⌊b
[7]            fl←(⌊a)+0J1×1+⌊b
[8]        :Else
[9]            fl←(1+⌊a)+0J1×⌊b
[10]       :EndIf
[11]   :EndIf
     ∇
 
      CpxFloor¨1j3.2 3.3j2.5 ¯3.3j¯2.5
1J3 3J2 ¯3J¯3
```

`⎕CT` and `⎕DCT` are  implicit arguments of Floor.
