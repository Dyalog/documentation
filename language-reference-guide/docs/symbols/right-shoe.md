---
search:
  exclude: true
---
# <span>Right Shoe</span> `⊃`

Monadic Right Shoe means

If `⎕ML<2`[First](../primitive-functions/first.md)
```apl
      ⊃ 'Word'
W
      ⊃ (1 2)(3 4 5)
1 2
```

If `⎕ML≥2`[Mix](../primitive-functions/mix.md)
```apl
      ⊃ (2 2)(3 3 3)
2 2 0
3 3 3
```

Dyadic Right Shoe means
[Pick](../primitive-functions/pick.md)
```apl
      3 ⊃ 'Word'
r
      2 ⊃ (1 2)(3 4 5)
3 4 5

      2 1 ⊃ (1 2)(3 4 5)
3
```
[Language Elements](../glyphs.md)
