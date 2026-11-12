---
search:
  boost: 2
---

# <span>Query Monitor Controls</span> `R←⎕MONITOR Y`{{key}}

This function reports the timing statistics collected for the lines of a tradfn or tradop on which monitor controls are set. [Dyadic `⎕MONITOR`](monitor-dyadic.md) sets them.

<h2 class="example">Example</h2>

`FOO` is defined, and its monitor controls are set, in the [example for dyadic `⎕MONITOR`](monitor-dyadic.md). After it has run once:

```apl
      ⎕MONITOR 'FOO'
0 1 35 35 0
1 1  1  1 0
2 1 14 14 0
3 1 14 14 0
4 1  6  6 0
5 1  0  0 0
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible defined function or operator. Any other name signals `DOMAIN ERROR`.

## Result

`R` is a simple integer matrix with one row for each line on which a monitor control is set, and 5 columns:

|Column|Content|
|------|-------|
|`R[;1]`|The line number, or `0` for the function or operator as a whole|
|`R[;2]`|The number of times the line was executed|
|`R[;3]`|The CPU time, in milliseconds|
|`R[;4]`|The elapsed time, in milliseconds|
|`R[;5]`|Reserved|

Monitor controls do not apply to dfns and dops: for a dfn or dop, `R` is empty.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>
