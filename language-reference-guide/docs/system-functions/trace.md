---
search:
  exclude: true
---

# <span>Trace Vector</span> `⎕TRACE`

`⎕TRACE` deals with the trace controls of a tradfn or tradop: the lines whose results are displayed as they are executed.

## Query Trace Vector

[Monadic `⎕TRACE`](trace-monadic.md) reports the lines on which trace controls are set:

```apl
      ⎕TRACE 'DSL'
0 1 2 3 4 5 6
```

## Set Trace Vector

[Dyadic `⎕TRACE`](trace-dyadic.md) sets the trace controls:

```apl
      ⊢(0,⍳6) ⎕TRACE 'DSL'
0 1 2 3 4 5 6
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>
