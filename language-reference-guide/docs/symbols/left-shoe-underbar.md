---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Left Shoe Underbar</span> <span class="command">⊆</span></h1>


Monadic Left Shoe Underbar means
[Nest](../primitive-functions/nest.md)
```apl
      ⊆ 'this'
┌────┐
│this│
└────┘
      ⊆ 'this' 'that'
┌────┬────┐
│this│that│
└────┴────┘
```

Dyadic Left Shoe Underbar means
[Partition](../primitive-functions/partition.md)
```apl
      1 0 0 1 1 ⊆ 1 2 3 4 5
┌─┬───┐
│1│4 5│
└─┴───┘
       1 1 2 2 2⊆⍳5
┌───┬─────┐
│1 2│3 4 5│
└───┴─────┘
    ' ' (≠⊆⊢) ' many a  time'
┌────┬─┬────┐
│many│a│time│
└────┴─┴────┘
```
[Language Elements](../glyphs.md)


