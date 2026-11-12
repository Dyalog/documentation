---
search:
  boost: 2
---

# <span>Query Monitor Controls</span> `R←⎕MONITOR Y`{{key}}

This function reports the timing statistics collected for the lines of a tradfn or tradop on which monitor controls are set. [Dyadic `⎕MONITOR`](monitor-dyadic.md) sets them.

<h2 class="example">Example</h2>

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

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible function or operator. A name that is not the name of a function or operator signals `DOMAIN ERROR`.

## Result

`R` is a simple integer matrix with one row for each line on which a monitor control is set, and 5 columns:

|Column|Content|
|------|-------|
|`R[;1]`|The line number, or `0` for the function or operator as a whole|
|`R[;2]`|The number of times the line was executed|
|`R[;3]`|The CPU time, in milliseconds|
|`R[;4]`|The elapsed time, in milliseconds|
|`R[;5]`|Reserved|

Monitor controls apply only to tradfns and tradops. For any other function or operator, such as a dfn, a dop, or a derived function, `R` is empty.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>
