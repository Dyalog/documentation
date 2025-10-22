---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Diaeresis</span> <span class="command">¨</span></h1>

Diaeresis is a monadic operator with an ambivalent operand

Operator Diaeresis means
[Each (with monadic operand)](../primitive-operators/each/each-with-monadic-operand.md) or [Each (with dyadic operand)](../primitive-operators/each/each-with-dyadic-operand.md)
```apl
      ⊃¨ 1 2 3 'ABC' (9 8 7)
1 2 3 A 9

      +/¨ (1 2 3 4)(5 6 7)
10 18

      3 ↑¨ 1 2 (3 4) 'V'
┌─────┬─────┬─────┬───┐
│1 0 0│2 0 0│3 4 0│V  │
└─────┴─────┴─────┴───┘

      1 2 3 ,¨ 99
┌────┬────┬────┐
│1 99│2 99│3 99│
└────┴────┴────┘
```
[Language Elements](../glyphs.md)


