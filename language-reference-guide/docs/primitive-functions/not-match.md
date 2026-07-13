---
search:
  boost: 2
---
<div style="display: none;">
  ≢
</div>






# <span>Not Match</span> `R←X≢Y`{{key}}



`Y` may be any array.  `X` may be any array.  `R` is a simple Boolean scalar.  If `X` is identical to `Y`, then `R` is 0.  Otherwise `R` is 1.


Non-empty arrays are identical if they have the same structure and the same values in all corresponding locations.  Empty arrays are identical if they have the same shape and the same prototype (disclosed nested structure).


`⎕CT` and `⎕DCT` are  implicit arguments of Not Match.


<h2 class="example">Examples</h2>
```apl
      ⍬≢⍳0
0
      ''≢⍳0
1
```
```apl

      ⊢A←⊂(⍳3) 'ABC'
  1 2 3  ABC
```
```apl

      A≢(⍳3)'ABC'
1
      A≢⊂(⍳3) 'ABC'
0
      ⍬≢0⍴A
1
      (1↑0⍴A)≢⊂(0 0 0) '   '
1
```


