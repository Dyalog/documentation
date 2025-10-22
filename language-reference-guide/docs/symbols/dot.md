---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Dot</span> <span class="command">.</span></h1>
Dot can be used as a dyadic operator with dyadic operands

Operator Dot means
[Inner Product](../primitive-operators/inner-product.md)

```apl
      1 2 3 +.× 4 5 6
32
      3 ∧.= 3 3 3 3
1
      mat
1 2
3 4
      mat +.× mat   ⍝ matrix product
 7 10
15 22
```

Used with Jot in place of the left operand Jot Dot means
[Outer Product](../primitive-operators/outer-product.md)
```apl
      1 2 3 ∘.× 4 5 6 7
 4  5  6  7
 8 10 12 14
12 15 18 21

```

!!!note
    Dot is also used as a decimal point and as a name separator in namespace reference syntax.

[Language Elements](../glyphs.md)


