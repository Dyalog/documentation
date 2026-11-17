---
search:
  boost: 2
---

# <span>Calibrate Profiling Timer</span> `{R}←⎕PROFILE'calibrate'`{{key}}

This function spends one second measuring the call time bias and granularity of the timer that the [profiler](profile.md) uses. For each, it keeps the lower of the previous and the new value, so that it uses the smallest value that it can be certain of. The first time in a session that the `'CPU'` or `'elapsed'` timer is chosen, [`⎕PROFILE 'start'`](profile-start.md) calibrates it in the same way.

<h2 class="example">Example</h2>

A timer must be in use:

```apl
      ⎕PROFILE 'calibrate'
DOMAIN ERROR: No timer in use
      ⎕PROFILE'calibrate'
      ∧
      ⎕PROFILE 'start' 'elapsed'
      ⎕←⎕PROFILE 'calibrate'
 active  elapsed  0.000009997165762 0
```

## Right Argument

`Y` is `'calibrate'`, which is not case-sensitive.

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
