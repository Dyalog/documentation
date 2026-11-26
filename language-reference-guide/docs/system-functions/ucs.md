---
search:
  exclude: true
---

# <span>Convert Unicode</span> `⎕UCS`

`⎕UCS` converts between characters and the integers that represent them in Unicode.

## Convert Unicode Code Point

[Monadic `⎕UCS`](ucs-monadic.md) converts between characters and their code points:

```apl
      ⎕UCS 'Hello'
72 101 108 108 111
```

## Convert Unicode Representation

[Dyadic `⎕UCS`](ucs-dyadic.md) converts between characters and their UTF-8, UTF-16, or UTF-32 encodings:

```apl
      'UTF-8' ⎕UCS 'ABCÆØÅ'
65 66 67 195 134 195 152 195 133
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕UCS UCS
</div>
