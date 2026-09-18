---
search:
  exclude: true
---

# <span>Object Attributes</span> `⎕AT`

`⎕AT` reports attributes of the defined functions and operators named in the right argument, such as their valences and the time they were last fixed.

A newer system function, [`⎕ATX`](atx.md), can be used instead: it is a superset of `⎕AT`, reporting many more attributes, on more kinds of name, and only the ones asked for.

## Object Attributes for Dyalog

[Monadic `⎕AT`](at-monadic.md) reports the valences, fix time, lock state, and author of each name at once:

```apl
      ∇ R←X plus Y
[1]     R←X+Y
[2]   ∇
      ⎕AT 'plus'
 1 2 0  2026 9 9 7 42 30 0  0  pete 

```

## Object Attributes for APL2

[Dyadic `⎕AT`](at-dyadic.md) reports one group of attributes, chosen by the left argument, in the form that APL2 uses:

```apl
      ∇ R←X plus Y
[1]     R←X+Y
[2]   ∇
      1 ⎕AT 'plus'
1 2 0

```
