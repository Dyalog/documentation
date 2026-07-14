---
search:
  boost: 2
---
<div style="display: none;">
  ≡ match
</div>

# <span>Match</span> `R←X≡Y`{{key}}

`Y` may be any array.  `X` may be any array.  `R` is a simple Boolean scalar.  If `X` is identical to `Y`, then `R` is 1.  Otherwise `R` is 0.

Non-empty arrays are identical if they have the same structure and the same values in all corresponding locations.  Empty arrays are identical if they have the same shape and the same prototype (disclosed nested structure).

`⎕CT` and `⎕DCT` are  implicit arguments of Match.

<h2 class="example">Examples</h2>
```apl
      ⍬≡⍳0
1
      ''≡⍳0
0
      A
THIS
WORD
 
      A≡2 4⍴'THISWORD'
1
      A≡⍳10
0
      +B←A A
 THIS  THIS
 WORD  WORD
 
      A≡⊃B
1
 
      (0⍴A)≡0⍴B
0
 
      ' '=⊃0⍴B
1 1 1 1
1 1 1 1
 
      ' '=⊃0⍴A
1
```
