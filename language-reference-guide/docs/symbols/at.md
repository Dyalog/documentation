---
search:
  exclude: true
---
<h1 class="heading"><span class="name">At</span> <span class="command">@</span></h1>

At is a dyadic operator

Operator At means
[At](../primitive-operators/at.md)
```apl
      (0@2 4) 1 2 3 4 5
1 0 3 0 5

      10 (×@2 4) 1 2 3 4 5
1 20 3 40 5

      (÷@2 4) 1 2 3 4 5
1 0.5 3 0.25 5

      '*'@(2∘|) 1 2 3 4 5   ⍝ Boolean selection 1 0 1 0 1
* 2 * 4 *

      ⌽@(2∘|) 1 2 3 4 5     ⍝ Reversal of sub-array 1 3 5
5 2 3 4 1
```
[Language Elements](../glyphs.md)
