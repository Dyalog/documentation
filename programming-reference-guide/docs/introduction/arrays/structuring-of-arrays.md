# Structuring of Arrays

Primitive functions that restructure arrays:

|symbol|monadic|dyadic|
|----|---|---|
|`⍴` ||[reshape](../../../language-reference-guide/primitive-functions/reshape.md)|
|`,` |[ravel](../../../language-reference-guide/primitive-functions/ravel/index.md)|[laminate and catenate](../../../language-reference-guide/primitive-functions/catenate-laminate.md)|
|`⍪` |[table](../../../language-reference-guide/primitive-functions/table.md)|[catenate first](../../../language-reference-guide/primitive-functions/catenate-first.md)|
|`⌽⍟`|[reverse](../../../language-reference-guide/primitive-functions/reverse.md)|[rotate](../../../language-reference-guide/primitive-functions/rotate.md)|
|`⍉` |[transpose](../../../language-reference-guide/primitive-functions/transpose.md)||
|`↑` |[mix](../../../language-reference-guide/primitive-functions/mix.md)|[take](../../../language-reference-guide/primitive-functions/take/index.md)|
|`↓` |[split](../../../language-reference-guide/primitive-functions/split.md)|[drop](../../../language-reference-guide/primitive-functions/drop/index.md)|
|`∊` |[enlist](../../../language-reference-guide/primitive-functions/enlist.md)| |
|`⊂` |[enclose](../../../language-reference-guide/primitive-functions/enclose/index.md)|[partitioned enclose](../../../language-reference-guide/primitive-functions/partitioned-enclose.md)|
|`⊆` |[nest](../../../language-reference-guide/primitive-functions/nest.md)|[partition](../../../language-reference-guide/primitive-functions/partition.md)|

<h2 class="example">Examples</h2>
```apl
      ⊢m←2 2⍴1 2 3 4                   ⍝ reshape
1 2
3 4

      2 2 4⍴'ABCDEFGHIJKLMNOP'
ABCD
EFGH

IJKL
MNOP
      ,m                               ⍝ ravel
1 2 3 4
      1 2 3,4                          ⍝ catenate
1 2 3 4
      1⌽1 2 3 4                        ⍝ rotate
2 3 4 1
      ⌽m                               ⍝ reverse
2 1
4 3
      ⊖m                               ⍝ reverse first
3 4
1 2
      ⍉m                               ⍝ transpose
1 3
2 4
      ↑(1 2 3)(4)                      ⍝ mix
1 2 3
4 0 0
      ↓2 4⍴'COWSHENS'                  ⍝ split
┌────┬────┐
│COWS│HENS│
└────┴────┘
      [ 1 2 3 ⋄ (4 5) 6 (7 8 9)]
┌───┬─┬─────┐
│1  │2│3    │
├───┼─┼─────┤
│4 5│6│7 8 9│
└───┴─┴─────┘
      ∊[ 1 2 3 ⋄ (4 5) 6 (7 8 9)]      ⍝ enlist
1 2 3 4 5 6 7 8 9
      ≢⎕←⊂1 2 3 4                      ⍝ enclose
┌───────┐
│1 2 3 4│
└───────┘
1
      2 0 1 3 0 2 0 1⊂'abcdefg'        ⍝ partitioned enclose
┌┬──┬─┬┬┬──┬┬──┬┐
││ab│c│││de││fg││
└┴──┴─┴┴┴──┴┴──┴┘
      1 1 2 2 2⊆1 2 3 4 5              ⍝ partition
┌───┬─────┐
│1 2│3 4 5│
└───┴─────┘
```
