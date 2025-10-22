---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Equal Underbar Slash</span> <span class="command">≢</span></h1>

Monadic Not Equal Underbar means
[Tally](../primitive-functions/tally.md)
```apl
      ≢ 'a'
1
      ≢ 7 4 2
3
      ≢ 5 4 3⍴0 
5
      ≢ (1 2)(3 4)
2
     mat
1 2 3
4 5 6
      ≢ mat   ⍝ note how "tally"
2
      ⍴ mat   ⍝ differs from "shape"
2 3
```

Dyadic Not Equal Underbar means
[Not Match](../primitive-functions/not-match.md)
```apl
      'bex' ≢ 'b','e','x' 
0
      1 ≢ 1 1
1
```
[Language Elements](../glyphs.md)


