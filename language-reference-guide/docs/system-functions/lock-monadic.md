---
search:
  boost: 2
---

# <span>Lock Function</span> `{R}←⎕LOCK Y`{{key}}

`Y` must be a simple character scalar, or vector which is taken to be the name of a defined function or operator in the active workspace. `⎕LOCK` does not apply to dfns or derived functions.

The active referent to the name in the workspace is locked.  Stop, trace and monitor settings, established by the `⎕STOP`, `⎕TRACE` and `⎕MONITOR` functions, are cancelled.

The function code is hidden and suspension within it is prevented.

The shy result `R` is the [lock state](lock-dyadic.md) (`1`, `2`, or `3`) of `Y`.

A `DOMAIN ERROR` is reported if `Y` is ill-formed.

<h2 class="example">Examples</h2>
```apl
      ⎕FX'r←foo' 'r←10'
      62 ⎕ATX'foo'  
  r←foo   r←10 
      ≢62 ⎕ATX'foo'
2
      ⎕LOCK'foo'
      ≢62 ⎕ATX'foo'
0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕LOCK LOCK
</div>
