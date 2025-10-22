---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Squad</span> <span class="command">⌷</span></h1>

Squad means
[Materialise](../primitive-functions/materialise.md)
```apl
      ⌷ ⍵
If ⍵ is an array, returns ⍵.
If ⍵ is ref to an instance of a Dyalog Class with a 
Default Numbered property, all items of that property
are returned.
If ⍵ is a COM or .NET collection, returns all elements
in the collection as an array.
```

Index with Axes means
[Index](../primitive-functions/index-function/index-with-axes.md)
```apl
      mat
1  2  3  4
5  6  7  8
9 10 11 12
      
      2 3 ⌷ mat
7
      2 ⌷ mat
5 6 7 8

      2 ⌷[2] mat
2 6 10
```
[Language Elements](../glyphs.md)


