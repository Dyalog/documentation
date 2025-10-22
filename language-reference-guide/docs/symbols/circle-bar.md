---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Circle Bar</span> <span class="command">⊖</span></h1>

Monadic Circle Bar means
[Reverse First](../primitive-functions/reverse-first.md)
```apl
      mat
1  2  3  4
5  6  7  8
9 10 11 12

      ⊖ mat
9 10 11 12
5  6  7  8
1  2  3  4
```

Dyadic Circle Bar means
[Rotate First](../primitive-functions/rotate-first.md)
```apl
      0 1 2 ¯1 ⊖ mat
1  6 11 12
5 10  3  4
9  2  7  8
```
[Language Elements](../glyphs.md)


