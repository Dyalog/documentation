---
search:
  exclude: true
---

# <span>Object Attributes</span> `⎕AT`

`⎕AT` reports attributes of the defined functions and operators named in `Y`, such as their valences and the time they were last fixed.

!!! Legacy "Legacy"
    `⎕AT` reports a fixed set of attributes, and only for defined functions and operators. [`⎕ATX`](atx.md) reports those and many more, selects exactly the ones wanted, and applies to other kinds of name as well.

## [Object Attributes for Dyalog](at-monadic.md)

Monadic `⎕AT` reports the valences, fix time, lock state, and author of each name at once:

```apl
      ∇ R←X plus Y
[1]     R←X+Y
[2]   ∇
      ⎕AT 'plus'
 1 2 0  2026 9 9 7 42 30 0  0  pete 

```

## [Object Attributes for APL2](at-dyadic.md)

Dyadic `⎕AT` reports one group of attributes, chosen by `X`, in the form that APL2 uses:

```apl
      ∇ R←X plus Y
[1]     R←X+Y
[2]   ∇
      1 ⎕AT 'plus'
1 2 0

```
