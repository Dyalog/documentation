---
search:
  boost: 2
---

# <span>Query Stop Vector</span> `R←⎕STOP Y`{{key}}

This function reports the lines of a defined function or operator on which stop controls are set. [Dyadic `⎕STOP`](stop-dyadic.md) sets them.

<h2 class="example">Example</h2>

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      0 1 ⎕STOP 'FOO'
      ⎕STOP 'FOO'
0 1
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible defined function or operator: a tradfn, tradop, dfn, or dop. Any other name signals `DOMAIN ERROR`.

## Result

`R` is a simple integer vector of the line numbers on which stop controls are set, in ascending order. `0` means that a stop control is set immediately before exit from the function or operator.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>
