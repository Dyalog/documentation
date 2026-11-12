---
search:
  exclude: true
---

# <span>Trace Vector</span> `⎕TRACE`

`⎕TRACE` deals with the trace controls of a tradfn or tradop: the lines whose results are displayed as they are executed.

## Query Trace Vector

[Monadic `⎕TRACE`](trace-monadic.md) reports the lines on which trace controls are set:

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      0 1 ⎕TRACE 'FOO'
      ⎕TRACE 'FOO'
0 1
```

## Set Trace Vector

[Dyadic `⎕TRACE`](trace-dyadic.md) sets the trace controls:

```apl
      ⎕←1 ⎕TRACE 'FOO'
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>
