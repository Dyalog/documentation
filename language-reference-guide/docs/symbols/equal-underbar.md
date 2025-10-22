---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Equal Underbar</span> <span class="command">≡</span></h1>

Monadic Equal Underbar means
[Depth](../primitive-functions/depth.md)
```apl

      ≡ 7
0
      ≡ 'abc'
1
      ≡ (1 2)(3 4)
2
      ≡ (1 2)(3 4)5
¯2
```

Note: Result is always positive if `⎕ML` is greater than or equal to 2

Dyadic Equal Underbar means
[Match](../primitive-functions/match.md)
```apl

      'b' 'e' 'x' ≡ 'bex'
1
      1 ≡ 1 1
0
```
[Language Elements](../glyphs.md)


