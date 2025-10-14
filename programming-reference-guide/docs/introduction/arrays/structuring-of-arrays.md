<h1 class="heading"><span class="name">Structuring of Arrays</span></h1>

Primitive functions that restructure arrays:

|symbol|monadic|dyadic|
|----|---|---|
|`⍴` ||[reshape](../../../../language-reference-guide/primitive-functions/reshape)|
|`,` |[ravel](../../../../language-reference-guide/primitive-functions/ravel)|[laminate and catenate](../../../../language-reference-guide/primitive-functions/catenate-laminate)|
|`⍪` |[table](../../../../language-reference-guide/primitive-functions/table)|[catenate first](../../../../language-reference-guide/primitive-functions/catenate-first)|
|`⌽⍟`|[reverse](../../../../language-reference-guide/primitive-functions/reverse)|[rotate](../../../../language-reference-guide/primitive-functions/rotate)|
|`⍉` |[transpose](../../../../language-reference-guide/primitive-functions/transpose)||
|`↑` |[mix](../../../../language-reference-guide/primitive-functions/mix)|[take](../../../../language-reference-guide/primitive-functions/take)|
|`↓` |[split](../../../../language-reference-guide/primitive-functions/split)|[drop](../../../../language-reference-guide/primitive-functions/drop)|
|`∊` |[enlist](../../../../language-reference-guide/primitive-functions/enlist)| |
|`⊂` |[enclose](../../../../language-reference-guide/primitive-functions/enclose)|[partitioned enclose](../../../../language-reference-guide/primitive-functions/partitioned-enclose)|
|`⊆` |[nest](../../../../language-reference-guide/primitive-functions/nest)|[partition](../../../../language-reference-guide/primitive-functions/partition)|


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

