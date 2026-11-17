---
search:
  boost: 2
---

# <span>Clear Profiling Data</span> `{R}←⎕PROFILE'clear'`{{key}}

This function discards the data that the [profiler](profile.md) has collected, and makes it inactive with no timer in use. [`⎕PROFILE 'start'`](profile-start.md) can then choose any timer. `)LOAD`, `)CLEAR`, and ending the session also discard the data.

<h2 class="example">Example</h2>

```apl
      ∇ Wait s
[1]    ⎕DL s
      ∇
      ⎕PROFILE 'start' 'elapsed'
      Wait 0.1
      ⎕←⎕PROFILE 'clear'
 inactive    0 0
      ⍴⎕PROFILE 'data'
0 7
      ⎕←⎕PROFILE 'start' 'CPU'
 active  CPU  0.000601 0
```

## Right Argument

`Y` is `'clear'`, which is not case-sensitive.

## Result

`R` is the [state](#state) of the profiler, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## State

The state of the profiler is a 4-item vector:

|Item|Content|
|----|-------|
|`1⊃R`|`'active'` while the profiler collects data, otherwise `'inactive'`|
|`2⊃R`|the timer (`'CPU'`, `'elapsed'`, `'none'`, or `'coverage'`), or `''` when no timer is in use|
|`3⊃R`|the call time bias, which is the time in milliseconds that one measurement with the timer takes|
|`4⊃R`|the granularity, which is the resolution of the timer in milliseconds|

When no timer is in use, `3⊃R` and `4⊃R` are `0`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>
