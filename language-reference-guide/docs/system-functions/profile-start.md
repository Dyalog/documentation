---
search:
  boost: 2
---

# <span>Start Profiling</span> `{R}←⎕PROFILE'start'{T}`{{key}}

This function makes the [profiler](profile.md) active, so that it collects data about each defined function and operator that runs, and about each of their lines. [`⎕PROFILE 'stop'`](profile-stop.md) makes it inactive again.

<h2 class="example">Example</h2>

Collecting the elapsed time of a function that waits:

```apl
      ∇ Wait s
[1]    ⎕DL s
      ∇
      ⎕←⎕PROFILE 'start' 'elapsed'
 active  elapsed  0.000009997165762 0
      Wait 0.1
      ⎕PROFILE 'stop'
```

## Right Argument

The right argument is `'start'`, optionally followed by `T`, the name of a timer. Neither is case-sensitive.

|`T`|Data collected for each function, operator, and line|
|---|----------------------------------------------------|
|`'CPU'`|the number of times that it runs, and the CPU time that it takes|
|`'elapsed'`|the number of times that it runs, and the elapsed time that it takes|
|`'none'`|the number of times that it runs|
|`'coverage'`|whether it runs|

If `T` is omitted, the timer is `'CPU'`.

## Result

`R` is the [state](#state) of the profiler, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## Collected Data

Starting with the timer that collected the existing data resumes collection, and adds to the data. Here, the numbers of runs that [`⎕PROFILE 'data'`](profile-data.md) reports for `Wait` and its lines count both runs:

```apl
      ⎕PROFILE 'start' 'elapsed'
      Wait 0.1
      ⎕PROFILE 'stop'
      1⊃(,3)⎕PROFILE 'data'
2 2 2
```

Starting with a different timer signals `DOMAIN ERROR`. Therefore, `⎕PROFILE 'start'` on its own cannot resume data that the `'elapsed'` timer collected:

```apl
      ⎕PROFILE 'start'
DOMAIN ERROR: Cannot change timer without first clearing collected data
      ⎕PROFILE'start'
      ∧
```

[`⎕PROFILE 'clear'`](profile-clear.md) discards the data, after which any timer can be chosen.

## Calibration

The first time in a session that the `'CPU'` or `'elapsed'` timer is chosen, `⎕PROFILE` spends one second measuring its call time bias and granularity. [`⎕PROFILE 'calibrate'`](profile-calibrate.md) measures them again.

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
