---
search:
  boost: 2
---

# <span>Query Profiling State</span> `R←⎕PROFILE'state'`{{key}}

This function returns the state of the [profiler](profile.md). There is one profiler for the whole session, whichever namespace uses `⎕PROFILE`.

<h2 class="example">Example</h2>

```apl
      ⎕PROFILE 'state'
 inactive    0 0
      ⎕PROFILE 'start' 'elapsed'
      ⎕PROFILE 'state'
 active  elapsed  0.000009997165762 0
```

## Right Argument

`Y` is `'state'`, which is not case-sensitive.

## Result

`R` is the state of the profiler, a 4-item vector:

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
