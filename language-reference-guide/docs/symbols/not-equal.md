---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Not Equal</span> <span class="command">≠</span></h1>

Monadic Not Equal means
[Unique Mask](../primitive-functions/unique-mask.md)
```apl
      ≠ 'Banana'
1 1 1 0 0 0

      ≠ 'Mississippi'
1 1 1 0 0 0 0 0 1 0 0
```

Dyadic Not Equal means
[Not Equal To](../primitive-functions/not-equal-to.md)
```apl
      1 2 3 ≠ 4 2 ¯1
1 0 1

      0 1 0 1 ≠ 0 0 1 1
0 1 1 0

      'Banana' ≠ 'a'
1 0 1 0 1 0

      7 ≠ '7'
1
```
[Language Elements](../glyphs.md)


