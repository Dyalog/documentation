---
search:
  exclude: true
---

# <span>Data Representation</span> `⎕DR`

`⎕DR` deals with the internal data type of an array.

## Query Data Representation

[Monadic `⎕DR`](dr-monadic.md) returns the data type of its argument:

```apl
      ⎕DR 10
83
```

## Transform Data Representation

[Dyadic `⎕DR`](dr-dyadic.md) converts its argument to the data type given by its left argument:

```apl
      11 ⎕DR 10
0 0 0 0 1 0 1 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DR DR
</div>
