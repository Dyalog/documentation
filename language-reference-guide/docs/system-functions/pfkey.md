---
search:
  exclude: true
---

# <span>Programmable Function Key</span> `⎕PFKEY`

`⎕PFKEY` deals with the definitions of programmable function keys, which type a sequence of keystrokes when they are pressed.

## Query Programmable Function Key

[Monadic `⎕PFKEY`](pfkey-monadic.md) returns the definition of a function key:

```apl
      x←(')FNS',⊂'ER')⎕PFKEY 1
      ⎕PFKEY 1
┌─┬─┬─┬─┬──┐
│)│F│N│S│ER│
└─┴─┴─┴─┴──┘
```

## Set Programmable Function Key

[Dyadic `⎕PFKEY`](pfkey-dyadic.md) sets the definition of a function key:

```apl
      (')VARS',⊂'ER')⎕PFKEY 2
┌─┬─┬─┬─┬─┬──┐
│)│V│A│R│S│ER│
└─┴─┴─┴─┴─┴──┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PFKEY PFKEY
</div>
