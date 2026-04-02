---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>

<h1 class="heading"><span class="name">Profile Application</span> <span class="command">{R}←{X}⎕PROFILE Y</span></h1>

`⎕PROFILE` facilitates the profiling of either CPU consumption or elapsed time for a workspace. It does so by retaining time measurements collected for APL functions/operators and function/operator lines. `⎕PROFILE` is used to both control the state of profiling and retrieve the collected profiling data.

`Y` specifies the action to perform and any options for that action, if applicable. `Y` is case-insensitive. The result `R` is, in some cases, shy.

|Syntax                              |Description                                                                    |
|----------------------------------|-------------------------------------------------------------------------------|
|`{state}←⎕PROFILE 'start' {timer}`|Turn profiling on using the specified timer, or resume if profiling was stopped|
|`{state}←⎕PROFILE 'stop'`         |Suspend the collection of profiling data                                       |
|`{state}←⎕PROFILE 'clear'`        |Turn profiling off, if active, and discard any collected profiling data        |
|`{state}←⎕PROFILE 'calibrate'`    |Calibrate the profiling timer                                                  |
|`state←⎕PROFILE 'state'`          |Query profiling state                                                          |
|`data←⎕PROFILE 'data'`            |Retrieve profiling data in flat form                                           |
|`data←⎕PROFILE 'tree'`            |Retrieve profiling data in tree form                                           |

## Actions

`⎕PROFILE` has two states:

- active – the profiler is running and profiling data is being collected. 
- inactive – the profiler is not running.

For most actions, the result of `⎕PROFILE` is its current state, and comprises:

- `[1]` – Character vector indicating the `⎕PROFILE` state.
- `[2]` – Character vector indicating the timer being used.
- `[3]` – Call time bias (in milliseconds), that is, the time that is consumed for the system to take a time measurement.
- `[4]` – Timer granularity (in milliseconds), that is, the resolution of the timer being used.

### Turn Profiling On

Syntax: `{state} ← ⎕PROFILE 'start' {timer}`

Turns profiling on using the specified timer, or resumes profiling if it was stopped.

`timer` is an optional, case-independent, character vector. Possible values are:

- `'CPU'` (the default)
- `'elapsed'`
- `'none'` – `⎕PROFILE` records the number of times each line of code is executed without incurring the timing overhead.
- `'coverage'` – `⎕PROFILE` identifies which lines of code are executed without incurring the timing or counting overhead.

The first time a particular timer is chosen, `⎕PROFILE` will spend 1,000 milliseconds (1 second) to approximate the call time bias and granularity for that timer.

<h3 class="example">Example</h3>
```apl
      ⊢⎕PROFILE 'start' 'CPU'
 active  CPU  0.000489407284 0
```

### Suspend Data Collection

Suspends the collection of profiling data

Syntax: `{state}←⎕PROFILE 'stop'`

<h3 class="example">Example</h3>
```apl
      ⊢⎕PROFILE 'stop'
 inactive  CPU  0.000489407284 0
```

### Turn Profiling Off

Syntax: `{state}←⎕PROFILE 'clear'`

Clears any collected profiling data and, if profiling is active, places profiling into an inactive state.

<h3 class="example">Example</h3>
```apl
      ⊢⎕PROFILE 'clear'
 inactive    0 0
```

### Calibrate Profiling Timer

Syntax: `{state}←⎕PROFILE 'calibrate'`

Causes `⎕PROFILE` to perform a 1,000 millisecond calibration to approximate the call time bias and granularity for the current timer.

!!! Info "Information"
    A timer must have been previously selected by using `⎕PROFILE 'start'`, otherwise a `DOMIAN ERROR` is generated.

`⎕PROFILE` will retain the lesser of the current timer values compared to the new values computed by the calibration. This ensures that the smallest possible values of which we can be certain is used.

<h3 class="example">Example</h3>
```apl
      ⊢⎕PROFILE'calibrate'
 active  CPU  0.000489407284 0
```

### Query Profiling State

Syntax: `state←⎕PROFILE 'state'`

Queries and returns the current profiling state.

<h3 class="example">Example</h3>
```apl
      )CLEAR
clear ws
      ⎕PROFILE 'state'
 inactive    0 0
 
      ⊢⎕PROFILE 'start' 'CPU'
 active  CPU  0.000489407284 0
      ⎕PROFILE 'state'
 active  CPU  0.000489407284 0
```

### Retrieve Data (Flat Form)

Syntax: `data←{X} ⎕PROFILE 'data'`


Retrieves the collected profiling data and returns it in flat form. If the `X` is omitted, the result is a matrix with the following columns:

- `[;1]` – function name
- `[;2]` – function line number or `⍬` for a whole function entry
- `[;3]` – number of times the line or function was executed
- `[;4]` – accumulated time (ms) for this entry exclusive of items called by this entry
- `[;5]` – accumulated time (ms) for this entry inclusive of items called by this entry
- `[;6]` – number of times the timer function was called for the exclusive time
- `[;7]` – number of times the timer function was called for the inclusive time

<h3 class="example">Example</h3>
Numbers in this example have been truncated for formatting purposes.
```apl
      ⎕PROFILE 'data'
#.foo             1  1.04406  39347.64945   503 4080803
#.foo      1      1  0.12488     0.124887     1       1
#.foo      2    100  0.58851 39347.193900   200 4080500
#.foo      3    100  0.21340     0.213406   100     100
#.NS1.goo       100 99.44404   39346.6053 50300 4080300
#.NS1.goo  1    100  0.61679     0.616793   100     100
#.NS1.goo  2  10000 67.80292   39314.9642 20000 4050000
#.NS1.goo  3  10000 19.60274      19.6027 10000   10000
```

If `X` is specified, it must be a simple vector of column indices. The result `R` has the same shape as `X`, and is a vector of the specified column vectors.

```apl
X ⎕PROFILE 'data' ←→ ↓[⎕IO](⎕PROFILE 'data')[;X]
```

If `[;2]` is included in the result, then the value `¯1` is used instead of `⍬` to indicate a whole-function entry.

### Retrieve Data (Tree Form)

Syntax: `data←{X} ⎕PROFILE 'tree'`

Retrieves the collected profiling data and returns it in tree form. If the `X` is omitted, the result is a matrix with the following columns: 

- `[;1]` – depth level
- `[;2]` – function name
- `[;3]` – function line number or `⍬` for a whole function entry
- `[;4]` – number of times the line or function was executed
- `[;5]` – accumulated time (ms) for this entry exclusive of items called by this entry
- `[;6]` – accumulated time (ms) for this entry inclusive of items called by this entry
- `[;7]` – number of times the timer function was called for the exclusive time
- `[;8]` – number of times the timer function was called for the inclusive time

<h2 class="example">Example</h2>
Numbers in this example have been truncated for formatting purposes.
```apl
      ⎕PROFILE 'tree'
0  #.foo               1     1.04406 39347.64945     503 4080803
1  #.foo      1        1     0.12488     0.12488       1       1
1  #.foo      2      100     0.58851 39347.19390     200 4080500
2  #.NS1.goo         100    99.44404 39346.60538   50300 4080300
3  #.NS1.goo  1      100     0.61679     0.61679     100     100
3  #.NS1.goo  2    10000    67.80292 39314.96426   20000 4050000
4  #.NS2.moo       10000 39247.16133 39247.16133 4030000 4030000
5  #.NS2.moo  1    10000    39.28315    39.28315   10000   10000
5  #.NS2.moo  2  1000000 36430.65236 36430.65236 1000000 1000000
5  #.NS2.moo  3  1000000  1645.36214  1645.36214 1000000 1000000
3  #.NS1.goo  3    10000    19.60274    19.60274   10000   10000
1  #.foo      3      100     0.21340     0.21340     100     100
```

Rows with an even depth level in `[;1]` represent function summary entries; odd depth level rows are function line entries. Recursive functions generate separate rows for each level of recursion.

If `X` is specified, it must be a simple vector of column indices. The result `R` has the same shape as `X`, and is a vector of the specified column vectors.

```apl
X ⎕PROFILE 'tree' ←→ ↓[⎕IO](⎕PROFILE 'tree')[;X]
```

## Profile Data Entry Types

The results of `⎕PROFILE 'data'` and `⎕PROFILE 'tree'` have two types of entries; function summary entries and function line entries. Function summary entries contain `⍬` in the line number column, whereas function line entries contain the line number. Line entries for dfns start with 0 as, unlike tradfns, they do not have a header line. The timer data and timer call counts in function summary entries represent the aggregate of the function line entries plus any time spent that cannot be directly attributed to a function line entry. This could include time spent during function initialisation, and so on.

<h3 class="example">Example</h3>
```apl
 #.foo         1  1.04406 39347.649450   503 4080803
 #.foo    1    1  0.12488     0.124887     1       1
 #.foo    2  100  0.58851 39347.193900   200 4080500
 #.foo    3  100  0.21340     0.213406   100     100
```

## Timer Data Persistence

The profiling data collected is stored outside the workspace and will not impact workspace availability. The data is cleared upon workspace load, clear workspace, `⎕PROFILE 'clear'`, or interpreter sign off.

## Using `⎕PROFILE`

!!! Info "Information"
    Running your application with `⎕PROFILE` turned on incurs a significant processing overhead and will slow dwon your application.
	
If you choose to use `⎕PROFILE`, the following guidelines and information may be of use to you.

### Selecting a Timer

`⎕PROFILE` supports profiling of either CPU or elapsed time. CPU time is generally of more interest in profiling application performance.

### Simple Profiling

The following procedure should help you to identify any items that take more than 10% of the run time on the top CPU time consumers in an application:

1. Ensure the application runs for a long enough period to collect enough data to overcome the timer granularity. As a guide, the application should run for at least `(4000×4⊃⎕PROFILE 'state')` milliseconds.
2. Turn profiling on with `⎕PROFILE 'start' 'CPU'`
3. Run your application.
4. Pause the profiler with `⎕PROFILE 'stop'`
5. Examine the profiling data from `⎕PROFILE 'data'` or `⎕PROFILE 'tree'` for entries that consume large amounts of resource.

To identify items that take more than 1% of the run time, or to focus on elapsed time rather than CPU time, take the following additional steps prior to running the profiler:

1. Turn off as much hardware as possible. This would include peripherals, network connections, and so on.
2. Turn off as many other tasks and processes as possible. These include anti-virus software, firewalls, internet services, and background tasks.
3. Raise the priority on the Dyalog task to higher than normal (in general, avoid giving it the highest priority).
4. Run the profiler as described above.

### Advanced Profiling

The timing data collected by `⎕PROFILE` is not adjusted for the timer's call time bias; this means that the times reported by `⎕PROFILE` include the time spent calling the timer function. One effect of this is that "cheap" lines that are called many times appear to consume more resource. If you require more accurate profiling measurements, or if your application takes a short amount of time to run, you might want to adjust for the timer call time bias. To do so, subtract from the timing data the timer's' call time bias multiplied by the number of times the timer was called.

<h4 class="example">Example</h4>
```apl
      CallTimeBias←3⊃⎕PROFILE 'state'
      RawTimes←⎕PROFILE 'data'
      Adjusted←RawTimes[;4 5]-RawTimes[;6 7]×CallTimeBias
```

## The PROFILE User Command

`]Profile` implements a high-level interface to `⎕PROFILE`, and provides reporting and analysis tools that act on the profiling data. For more information, see the [_Application Tuning Guide_](https://docs.dyalog.com/20.0/files/Application_Tuning_Guide.pdf).
