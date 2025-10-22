---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Jot</span> <span class="command">∘</span></h1>

Jot is a dyadic operator

Operator Jot means Beside or Bind

[Beside](../primitive-operators/beside.md) (function composition)
```apl
      ⌽∘⍳¨ 3 4 5
┌─────┬───────┬─────────┐
│3 2 1│4 3 2 1│5 4 3 2 1│
└─────┴───────┴─────────┘

      ¯1 ⌽∘⍳¨ 3 4 5
┌─────┬───────┬─────────┐
│3 1 2│4 1 2 3│5 1 2 3 4│
└─────┴───────┴─────────┘

      +∘÷/ 40⍴1    ⍝ continued fraction
1.61803
```

[Bind](../primitive-operators/bind.md) (left and right argument currying)
```apl
      next ← 1∘+
      next 23
24
      prev ← -∘1
      prev 23
22
```
N.B. Jot is also used in conjunction with Dot to mean
      [Outer Product](../primitive-operators/outer-product.md).

[Language Elements](../glyphs.md)


