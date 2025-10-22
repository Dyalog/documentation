---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Iota</span> <span class="command">⍳</span></h1>

Monadic Iota means
[Index Generator
      ](../primitive-functions/index-generator.md)
```apl

      ⍳ 10
1 2 3 4 5 6 7 8 9 10

      ⍳ 2 3
┌───┬───┬───┐
│1 1│1 2│1 3│
├───┼───┼───┤
│2 1│2 2│2 3│
└───┴───┴───┘
```

Dyadic Iota means


[Index Of
      ](../primitive-functions/index-of.md)
```apl

      'ABCDABCDEF' ⍳ 'ACF'
1 3 10

      mat
1 2
3 4
5 6
      mat ⍳ 5 6
3

```
[Language Elements](../glyphs.md)
