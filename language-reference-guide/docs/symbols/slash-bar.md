---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Slash Bar</span> <span class="command">⌿</span></h1>

# Used as a Function

Monadic Slash Bar is not defined

Dyadic Slash Bar means
[Replicate First (Compress First)](../primitive-functions/replicate-first.md)
```apl
      mat
1  2  3  4
5  6  7  8
9 10 11 12

      1 0 2 ⌿ mat
1  2  3  4
9 10 11 12
9 10 11 12
```

# Used as an Operator

Slash Bar is a monadic operator with a dyadic operand

Operator Slash Bar means
[Reduce First,  Reduce First N-Wise ](../primitive-operators/reduce-first/index.md)
```apl
      +⌿ mat
15 18 21 24

      2 +⌿ mat     ⍝ pair-wise
 6  8 10 12
14 16 18 20
```
[Language Elements](../glyphs.md)


