---
search:
  exclude: true
---

# <span>Map File</span> `⎕MAP`

`⎕MAP` associates a file with an array in the workspace, so that the array's data is read from the file, and changes to the array can be written back to it.

## Map Array File

[Monadic `⎕MAP`](map-monadic.md) maps a file that holds an APL array, whose data type and shape are recorded in the file:

```apl
      var←⎕MAP 'var.dat' 'W'
```

## Map Raw Data File

[Dyadic `⎕MAP`](map-dyadic.md) maps a file of raw data, with the data type and shape given by the left argument:

```apl
      vec←645 ¯1 ⎕MAP 'data.bin'
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
