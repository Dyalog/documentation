---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Quad Equal</span> <span class="command">⌸</span></h1>


Quad Equal is a monadic operator with an ambivalent operand

Operator Quad Equal means
[Key](../primitive-operators/key.md)
```apl
      'Banana' {⍺ ⍵}⌸ 3 1 4 1 5 9
┌─┬─────┐
│B│3    │
├─┼─────┤
│a│1 1 9│
├─┼─────┤
│n│4 5  │
└─┴─────┘
      'Banana' {⍺,+/⍵}⌸ 3 1 4 1 5 9
B  3
a 11
n  9     
      'Banana' {⍺ ⍵}⌸ 1 2 3 4 5 6
┌─┬─────┐
│B│1    │
├─┼─────┤
│a│2 4 6│
├─┼─────┤
│n│3 5  │
└─┴─────┘
      {⍺ ⍵}⌸ 'Banana'  ⍝ (same as above)
┌─┬─────┐
│B│1    │
├─┼─────┤
│a│2 4 6│
├─┼─────┤
│n│3 5  │
└─┴─────┘
```
[Language Elements](../glyphs.md)


