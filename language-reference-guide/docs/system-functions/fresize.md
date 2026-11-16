---
search:
  exclude: true
---

# <span>Compact/Resize Component File</span> `⎕FRESIZE`

`⎕FRESIZE` compacts a component file.

## Compact Component File

[Monadic `⎕FRESIZE`](fresize-monadic.md) compacts the file, leaving its maximum size unchanged:

```apl
      ⎕FRESIZE 1
```

## Resize Component File

[Dyadic `⎕FRESIZE`](fresize-dyadic.md) also sets the maximum size of the file:

```apl
      100000 ⎕FRESIZE 1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRESIZE FRESIZE
</div>
