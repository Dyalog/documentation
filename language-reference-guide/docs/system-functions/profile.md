---
search:
  boost: 2
---

# <span>Profiling Overview</span> `⎕PROFILE`

`⎕PROFILE` measures where an application spends its time, by recording how often each defined function and operator, and each of their lines, runs and how long it takes.

## Start Profiling

[`⎕PROFILE 'start'`](profile-start.md) makes the profiler active, using a chosen timer:

```apl
      ∇ Main
        Wait 0.2
        Wait 0.1
      ∇
      ∇ Wait s
        ⎕DL s
      ∇
      ⎕←⎕PROFILE 'start' 'elapsed'
 active  elapsed  0.000009997165762 0
      Main
```

## Stop Profiling

[`⎕PROFILE 'stop'`](profile-stop.md) makes the profiler inactive, and keeps the data that it has collected:

```apl
      ⎕←⎕PROFILE 'stop'
 inactive  elapsed  0.000009997165762 0
```

## Query Profiling State

[`⎕PROFILE 'state'`](profile-state.md) returns the state of the profiler:

```apl
      ⎕PROFILE 'state'
 inactive  elapsed  0.000009997165762 0
```

## Calibrate Profiling Timer

[`⎕PROFILE 'calibrate'`](profile-calibrate.md) measures the call time bias and granularity of the timer again:

```apl
      ⎕←⎕PROFILE 'calibrate'
 inactive  elapsed  0.000009997165762 0
```

## Get Flat Profiling Data

[`⎕PROFILE 'data'`](profile-data.md) returns the data with one row for each function and each of their lines:

```apl
      ⎕PROFILE 'data'
 #.Wait     2 301.002264         301.002264         10 10
 #.Wait  0  2   0.0001199805411    0.0001199805411   2  2
 #.Wait  1  2 300.999908         300.999908          2  2
 #.Main     1   0.008215996786   301.01048           9 19
 #.Main  0  1   0.00005000038072   0.00005000038072  1  1
 #.Main  1  1   0.002273998689   200.664644          2  7
 #.Main  2  1   0.005489986506   100.345384          2  7
```

## Get Profiling Data Tree

[`⎕PROFILE 'tree'`](profile-tree.md) returns the data as a tree, in which the rows for a called function follow the row for the line that called it:

```apl
      ⎕PROFILE 'tree'
0  #.Main     1   0.008215996786   301.01048          9 19
1  #.Main  0  1   0.00005000038072   0.00005000038072 1  1
1  #.Main  1  1   0.002273998689   200.664644         2  7
2  #.Wait     1 200.66237          200.66237          5  5
3  #.Wait  0  1   0.00004998582881   0.00004998582881 1  1
3  #.Wait  1  1 200.661167         200.661167         1  1
1  #.Main  2  1   0.005489986506   100.345384         2  7
2  #.Wait     1 100.339894         100.339894         5  5
3  #.Wait  0  1   0.00006999471225   0.00006999471225 1  1
3  #.Wait  1  1 100.338741         100.338741         1  1
```

## Clear Profiling Data

[`⎕PROFILE 'clear'`](profile-clear.md) discards the data, and makes the profiler inactive with no timer:

```apl
      ⎕←⎕PROFILE 'clear'
 inactive    0 0
```

## Profiling Data

There is one profiler for the whole session, whichever namespace uses `⎕PROFILE`. It holds its data outside the workspace. Therefore, profiling does not use workspace space. `)LOAD`, `)CLEAR`, `⎕PROFILE 'clear'`, and ending the session discard the data.

## Using `⎕PROFILE`

Profiling slows an application down significantly.

### Selecting a Timer

`⎕PROFILE` measures either CPU time or elapsed time. CPU time is generally of more interest when tuning the performance of an application. Elapsed time also includes time in which the interpreter does not use the CPU, such as the delays of [`⎕DL`](dl.md) in the examples above.

### Simple Profiling

These steps find the items that take more than 10% of the CPU time of an application:

1. Make sure that the application runs for long enough to overcome the timer granularity, which means at least `4000×4⊃⎕PROFILE 'state'` milliseconds
2. Start profiling with `⎕PROFILE 'start' 'CPU'`
3. Run the application
4. Stop profiling with `⎕PROFILE 'stop'`
5. Look in `⎕PROFILE 'data'` or `⎕PROFILE 'tree'` for the entries that take the most time

To find the items that take more than 1% of the run time, or to measure elapsed time rather than CPU time, take these steps before profiling:

1. Turn off as much hardware as possible, such as peripherals and network connections
2. Stop as many other tasks and processes as possible, such as anti-virus software, firewalls, internet services, and background tasks
3. Raise the priority of the Dyalog process above normal, but generally not to the highest priority

### Advanced Profiling

The times that `⎕PROFILE` reports include the time spent calling the timer. Therefore, a quick line that runs many times appears to take more time than it does. For more accurate measurements, or for an application that runs only briefly, subtract the call time bias multiplied by the number of timer calls:

```apl
      CallTimeBias←3⊃⎕PROFILE 'state'
      RawTimes←⎕PROFILE 'data'
      Adjusted←RawTimes[;4 5]-RawTimes[;6 7]×CallTimeBias
```

## The `]Profile` User Command

The `]Profile` user command is a high-level interface to `⎕PROFILE`, with tools that report on and analyse the profiling data. The [Application Tuning Guide](https://docs.dyalog.com/21.0/files/Application_Tuning_Guide.pdf) describes it.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>
