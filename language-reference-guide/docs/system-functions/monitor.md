---
search:
  exclude: true
---

# <span>Monitor Controls</span> `⎕MONITOR`

`⎕MONITOR` deals with the monitor controls of a tradfn or tradop: the lines for which timing statistics are collected.

## Query Monitor Controls

[Monadic `⎕MONITOR`](monitor-monadic.md) reports the statistics collected:

```apl
      ∇ FOO
[1]    A←?300 300⍴100
[2]    B←⌹A
[3]    C←⌹B
[4]    R1←⌊0.5+A+.×B
[5]    R2←A=C
      ∇
      (0,⍳5) ⎕MONITOR 'FOO'
      FOO
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
      ⊢1 ⎕MONITOR 'FOO'
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>
