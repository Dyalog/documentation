---
search:
  exclude: true
---

# <span>Format</span> `⎕FMT`

`⎕FMT` formats an array as a character matrix.

## Resolve Display Format

[Monadic `⎕FMT`](fmt-monadic.md) returns the display of an array as a character matrix:

```apl
      ⎕FMT 2 4⍴⍳8
1 2 3 4
5 6 7 8
```

## Format Array

[Dyadic `⎕FMT`](fmt-dyadic.md) formats the columns of an array as the format specification says:

```apl
      'I3,F5.2' ⎕FMT 2 4⍴⍳8
  1 2.00  3 4.00
  5 6.00  7 8.00
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>
