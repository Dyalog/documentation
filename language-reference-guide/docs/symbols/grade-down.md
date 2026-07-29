---
search:
  exclude: true
---
# <span>Grade Down</span> `⍒`

Monadic Grade Down means
[Grade Down](../primitive-functions/grade-down.md)
```apl
      ⍒ 33 11 44 66 22
4 3 1 5 2

      names←'Joe' 'Sue' 'Sam'
      ages←34 22 25

      names[⍒ages]
┌───┬───┬───┐
│Joe│Sam│Sue│
└───┴───┴───┘ 

      ⍒ 'ABC' ⎕NULL ⍬ ¯3j4 'A'
1 5 4 2 3
```

Dyadic Grade Down means
[Dyadic Grade Down](../primitive-functions/dyadic-grade-down.md)
```apl
Provide collating sequence for character data.

      ⍒ 'Banana'
3 5 2 4 6 1

      'an' ⍒ 'Banana'
1 3 5 2 4 6
```
[Language Elements](../glyphs.md)
