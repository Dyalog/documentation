---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Left Shoe</span> <span class="command">⊂</span></h1>

Monadic Left Shoe means
[Enclose](../primitive-functions/enclose/index.md)
```apl
      1(2 3)
┌─┬───┐
│1│2 3│
└─┴───┘
      ⊂ 1(2 3)
┌───────┐
│┌─┬───┐│
││1│2 3││
│└─┴───┘│
└───────┘
      ⊂⊂ 1(2 3)
┌─────────┐
│┌───────┐│
││┌─┬───┐││
│││1│2 3│││
││└─┴───┘││
│└───────┘│
└─────────┘
```

Dyadic Left Shoe means

If `⎕ML<3`[ Partitioned Enclose](../primitive-functions/partitioned-enclose.md)
```apl
       0 1 0 1 ⊂ 1 2 3 4
┌───┬─┐
│2 3│4│
└───┴─┘
```

If `⎕ML≥3`[ Partition](../primitive-functions/partition.md)
```apl
      0 1 0 1 ⊂ 1 2 3 4
┌─┬─┐
│2│4│
└─┴─┘
```
[Language Elements](../glyphs.md)


