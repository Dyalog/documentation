---
search:
  exclude: true
---
# <span>Up Arrow</span> `↑`

Monadic Up Arrow means

If `⎕ML<2` [Mix](../primitive-functions/mix.md)
```apl
      ↑ 'Hip' 'Hop'
Hip
Hop
      ↑ (6 4) 5 3
6 4
5 0
3 0
      ↑[0.5] 'Hip' 'Hop'
HH
io
pp
```

If `⎕ML≥2` [First](../primitive-functions/first.md)
```apl
      ↑ (6 4) 5 3
6 4
```

Dyadic Up Arrow means
[Take](../primitive-functions/take/index.md)
```apl
      4 ↑ 'Pineapple'
Pine
      ¯5 ↑ 'Pineapple'
apple

      mat
1  2  3  4
5  6  7  8
9 10 11 12
      
      2 ¯3 ↑ mat
2 3 4
6 7 8

      ¯2 ↑ mat
5  6  7  8
9 10 11 12

      ¯2 3 ↑ 7
0 0 0
7 0 0
```
[Language Elements](../glyphs.md)
