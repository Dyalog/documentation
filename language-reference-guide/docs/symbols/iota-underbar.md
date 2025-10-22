---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Iota Underbar</span> <span class="command">⍸</span></h1>

Monadic Iota Underbar means
[Where](../primitive-functions/where.md)
```apl
      ⍸ 1 0 0 1 1
1 4 5
      bmat
0 1 0
1 0 1
      ⍸ bmat
┌───┬───┬───┐
│1 2│2 1│2 3│
└───┴───┴───┘
```

Dyadic Iota Underbar means
[Interval Index](../primitive-functions/interval-index.md)
```apl
      'AEIOU' ⍸ 'DYALOG'
1 5 1 3 4 2

      2 4 6 ⍸ 1 2 3 4 5 6 7
0 1 1 2 2 3 3

      mat
1 2
3 4
5 6
      mat ⍸ 3 3
1
      mat ⍸ 3 5
2
```
[Language Elements](../glyphs.md)
