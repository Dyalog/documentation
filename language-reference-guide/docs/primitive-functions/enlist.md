---
search:
  boost: 2
---
<div style="display: none;">
  ∊ enlist
</div>

# <span>Enlist</span> `(⎕ML≥1) R←∊Y`{{key}}

Migration level must be such that `⎕ML≥1` (otherwise see [Type](type.md)).

`Y` may be any array, `R` is a simple vector created from all the elements of `Y` in ravel order.

<h2 class="example">Examples</h2>
```apl

      ⎕ML←1         ⍝  Migration level 1
      MAT←2 2⍴'MISS' 'IS' 'SIP' 'PI' ⋄ MAT
 MISS  IS
 SIP   PI
      ∊MAT
MISSISSIPPI
 
      M←1 (2 2⍴2 3 4 5) (6(7 8))
      M
1  2 3  6  7 8
   4 5
      ∊M
1 2 3 4 5 6 7 8
```



