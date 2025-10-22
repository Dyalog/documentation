---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Down Arrow</span> <span class="command">↓</span></h1>

Monadic Down Arrow means
[Split](../primitive-functions/split.md)
```apl
      mat
1  2  3  4
5  6  7  8
9 10 11 12

      ↓ mat
┌───────┬───────┬──────────┐
│1 2 3 4│5 6 7 8│9 10 11 12│
└───────┴───────┴──────────┘

      ↓[1] mat
┌─────┬──────┬──────┬──────┐
│1 5 9│2 6 10│3 7 11│4 8 12│
└─────┴──────┴──────┴──────┘
```

Dyadic Down Arrow means
[Drop](../primitive-functions/drop/index.md)
```apl
      4 ↓ 'Pineapple'
apple
      ¯5 ↓ 'Pineapple'
Pine
      1 ¯2 ↓ mat
5  6
9 10
      1 ↓ mat
5  6  7  8
9 10 11 12
```
[Language Elements](../glyphs.md)


