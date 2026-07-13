---
search:
  exclude: true
---
# <span>Rho</span> `⍴`

Monadic Rho means
[Shape](../primitive-functions/shape.md)
```apl
      mat
1  2  3  4
5  6  7  8
9 10 11 12

      ⍴ mat
3 4
      ⍴⍴ mat
2
      ⍴ 'your boat'
9
      ⍴ 7

      ⍴⍴ 7
0
```

Dyadic Rho means
[Reshape](../primitive-functions/reshape.md)
```apl
      2 3 4 ⍴ 1 2 3 4 5 6 7
1 2 3 4
5 6 7 1
2 3 4 5
       
6 7 1 2
3 4 5 6
7 1 2 3
```
[Language Elements](../glyphs.md)


