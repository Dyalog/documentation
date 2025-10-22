---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Grade Up</span> <span class="command">⍋</span></h1>

Monadic Grade Up means
[Grade Up](../primitive-functions/grade-up.md)
```apl
      ⍋ 33 11 44 66 22
2 5 1 3 4

      names←'Joe' 'Sue' 'Sam'
      ages←34 22 25

      names[⍋ages]
┌───┬───┬───┐
│Sue│Sam│Joe│
└───┴───┴───┘

      ⍋ 'ABC' ⎕NULL ⍬ ¯3j4 'A'
3 2 4 5 1
```

Dyadic Grade Up means
[Dyadic Grade Up](../primitive-functions/dyadic-grade-up.md)
```apl
      ⍋ 'Banana'
1 2 4 6 3 5

      'an' ⍋ 'Banana'
2 4 6 3 5 1
```
[Language Elements](../glyphs.md)


