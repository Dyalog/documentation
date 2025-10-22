---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Backslash Bar</span> <span class="command">⍀</span></h1>


# Used as a Function

Monadic Backslash Bar is not defined

Dyadic Backslash Bar means
[Expand First](../primitive-functions/expand.md)
```apl

      mat
1  2  3  4
5  6  7  8
9 10 11 12

      1 0 2 1 ⍀ mat
1  2  3  4
0  0  0  0
5  6  7  8
5  6  7  8
9 10 11 12
```

# Used as an Operator

Backslash Bar is a monadic operator with a dyadic operand

Operator Backslash Bar means
[Scan First](../primitive-operators/scan-first.md)
```apl
      +⍀ mat
 1  2  3  4
 6  8 10 12
15 18 21 24 
```
[Language Elements](../glyphs.md)


