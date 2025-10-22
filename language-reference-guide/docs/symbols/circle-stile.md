---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Circle Stile</span> <span class="command">⌽</span></h1>

Monadic Circle Stile means
[Reverse](../primitive-functions/reverse.md)
```apl
      ⌽ 'trams'
smart

      mat
1  2  3  4
5  6  7  8
9 10 11 12

      ⌽ mat
 4  3  2 1
 8  7  6 5
12 11 10 9

      ⌽[1] mat
9 10 11 12
5  6  7  8
1  2  3  4
```

Dyadic Circle Stile means
[Rotate](../primitive-functions/rotate.md)
```apl
      3 ⌽ 'HatStand'
StandHat

      ¯2 ⌽ 1 2 3 4 5 6
5 6 1 2 3 4

      ¯1 ⌽ mat
 4 1  2  3
 8 5  6  7
12 9 10 11

      1 ¯1 2 ⌽ mat
 2  3 4  1
 8  5 6  7
11 12 9 10

      0 1 2 ¯1 ⌽[1] mat
1  6 11 12
5 10  3  4
9  2  7  8
```
[Language Elements](../glyphs.md)


