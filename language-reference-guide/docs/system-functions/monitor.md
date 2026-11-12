---
search:
  exclude: true
---

# <span>Monitor Controls</span> `⎕MONITOR`

`⎕MONITOR` deals with the monitor controls of a tradfn or tradop: the lines for which timing statistics are collected.

## Query Monitor Controls

[Monadic `⎕MONITOR`](monitor-monadic.md) reports the statistics collected:

```apl
      ⎕MONITOR 'FOO'
0 1 35 35 0
1 1  1  1 0
2 1 14 14 0
3 1 14 14 0
4 1  6  6 0
5 1  0  0 0
```

## Set Monitor Controls

[Dyadic `⎕MONITOR`](monitor-dyadic.md) sets the monitor controls:

```apl
      ⊢(0,⍳10) ⎕MONITOR 'FOO'
0 1 2 3 4 5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>
