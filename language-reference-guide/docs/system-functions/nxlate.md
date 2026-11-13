---
search:
  exclude: true
---

# <span>Native File Translation Vector</span> `⎕NXLATE`

`⎕NXLATE` deals with translate vectors, which map the characters of the [atomic vector](av.md) onto single bytes.

## Query Native File Translation Vector

[Monadic `⎕NXLATE`](nxlate-monadic.md) returns the translate vector of a native file:

```apl
      t←'data.txt'⎕NCREATE 0
      (⎕NXLATE t)[⎕AV⍳'Grüße']
71 114 252 223 101
```

## Set Native File Translation Vector

[Dyadic `⎕NXLATE`](nxlate-dyadic.md) sets the translate vector of a native file, here the file tied under [Query Native File Translation Vector](#query-native-file-translation-vector):

```apl
      ((⍳256)-⎕IO)⎕NXLATE t
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NXLATE NXLATE
</div>
