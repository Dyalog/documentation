---
search:
  exclude: true
---

# <span>Stop Vector</span> `⎕STOP`

`⎕STOP` deals with the stop controls of a defined function or operator, which mark the lines before which execution is suspended.

## Query Stop Vector

[Monadic `⎕STOP`](stop-monadic.md) reports the lines on which stop controls are set:

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      0 1 ⎕STOP 'FOO'
      ⎕STOP 'FOO'
0 1
```

## Set Stop Vector

[Dyadic `⎕STOP`](stop-dyadic.md) sets the stop controls:

```apl
      ⎕←1 ⎕STOP 'FOO'
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>
