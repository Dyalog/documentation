---
search:
  exclude: true
---

# <span>Stop Vector</span> `⎕STOP`

`⎕STOP` deals with the stop controls of a defined function or operator: the lines before which execution is suspended.

## Query Stop Vector

[Monadic `⎕STOP`](stop-monadic.md) reports the lines on which stop controls are set:

```apl
      ⎕STOP 'FOO'
0 1
```

## Set Stop Vector

[Dyadic `⎕STOP`](stop-dyadic.md) sets the stop controls:

```apl
      ⊢0 1 ⎕STOP 'FOO'
0 1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>
