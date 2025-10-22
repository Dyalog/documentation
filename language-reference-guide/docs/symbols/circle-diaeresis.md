---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Circle Diaeresis</span> <span class="command">⍥</span></h1>

Circle Diaeresis is a dyadic operator with an ambivalent left operand

Operator Circle Diaeresis means
[Over](../primitive-operators/over.md)
```apl
      -⍥⌊ 3.6                 ⍝ Same as ∘ or ⍤ monadically
¯3
      5.1 -⍥⌊ 3.6             ⍝ Applies ⌊ to both arguments
2
      'Dyalog' ≡⍥⎕C 'DYALOG'  ⍝ Case-insensitive match
1
      'Dyalog' ≡⍥⎕C 'IBM'
0
```
[Language Elements](../glyphs.md)


