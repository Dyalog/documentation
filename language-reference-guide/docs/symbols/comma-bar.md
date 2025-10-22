---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Comma Bar</span> <span class="command">⍪</span></h1>

Monadic Comma Bar means
[Table](../primitive-functions/table.md)
```apl
      ⍪ 2 3 4
2
3
4
      cube    ⍝ 3D array
1 2
3 4
   
5 6
7 8
      ⍪ cube
1 2 3 4
5 6 7 8
```
Dyadic Comma Bar means
[Catenate First](../primitive-functions/catenate-first.md)
```apl
      mat
1 2 3
4 5 6

      mat ⍪ 0
1 2 3
4 5 6
0 0 0

      mat ⍪ 7 8 9
1 2 3
4 5 6
7 8 9
```
[Language Elements](../glyphs.md)


