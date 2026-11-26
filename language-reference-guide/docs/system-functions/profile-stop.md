---
search:
  boost: 2
---

# <span>Stop Profiling</span> `{R}←⎕PROFILE'stop'`{{key}}

This function makes the [profiler](profile.md) inactive, and keeps the data that it has collected. [`⎕PROFILE 'start'`](profile-start.md) with the same timer resumes collection.

<h2 class="example">Example</h2>

The run of `Wait` after profiling stops is not counted in the data that [`⎕PROFILE 'data'`](profile-data.md) reports:

```apl
      ∇ Wait s
        ⎕DL s
      ∇
      ⎕PROFILE 'start' 'elapsed'
      Wait 0.1
      ⎕←⎕PROFILE 'stop'
 inactive  elapsed  0.000009997165762 0
      Wait 0.1
      1⊃(,3)⎕PROFILE 'data'
1 1 1
```

## Right Argument

`Y` is `'stop'`, which is not case-sensitive.

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
