<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>






<h1 class="heading"><span class="name">Profile Application</span> <span class="command">{R}←{X}⎕PROFILE Y</span></h1>



`⎕PROFILE` facilitates the profiling of either CPU consumption or elapsed time for a workspace. It does so by retaining time measurements collected for APL functions/operators and function/operator lines. `⎕PROFILE` is used to both control the state of profiling and retrieve the collected profiling data.


See also: [Application Tuning Guide](https://docs.dyalog.com/18.0/Application%20Tuning%20Guide.pdf).


`Y` specifies the action to perform and any options for that action, if applicable. `Y` is case-insensitive. Note that the result `R` is in some cases shy.


|Use                               |Description                                                                   |
|----------------------------------|------------------------------------------------------------------------------|
|`{state}←⎕PROFILE 'start' {timer}`|Turn profiling on using the specified timer or resume if profiling was stopped|
|`{state}←⎕PROFILE 'stop'`         |Suspend the collection of profiling data                                      |
|`{state}←⎕PROFILE 'clear'`        |Turn profiling off, if active, and discard any collected profiling data       |
|`{state}←⎕PROFILE 'calibrate'`    |Calibrate the profiling timer                                                 |
|`state←⎕PROFILE 'state'`          |Query profiling state                                                         |
|`data←⎕PROFILE 'data'`            |Retrieve profiling data in flat form                                          |
|`data←⎕PROFILE 'tree'`            |Retrieve profiling data in tree form                                          |




`⎕PROFILE` has 2 states:

- active – the profiler is running and profiling data is being collected. 
- inactive – the profiler is not running.




For most actions, the result of `⎕PROFILE` is its current state and contains:


|-----|---------------------------------------------------------------------------------------------------------------------------------------|
|`[1]`|character vector indicating the `⎕PROFILE` state having one of the values `'active'` or `'inactive'`                                   |
|`[2]`|character vector indicating the timer being used having one of the values `'CPU'` or `'elapsed'`                                       |
|`[3]`|call time bias in milliseconds. This is the amount of time, in milliseconds, that is consumed for the system to take a time measurement|
|`[4]`|timer granularity in milliseconds. This is the resolution of the timer being used                                                      |


## {state}←⎕PROFILE 'start' {timer}


Turn profiling on; `timer` is an optional case-independent character vector containing  `'CPU'` or `'elapsed'` or `'none'` or `'coverage'`. If omitted, it defaults to `'CPU'`. If `timer` is `'none'`, `⎕PROFILE`  records  just the number of times each line of code is executed without incurring the timing overhead. If `timer` is `'coverage'`, `⎕PROFILE`   only identifies which  lines of code are executed without incurring the timing or counting overhead.


The first time a particular timer is chosen, `⎕PROFILE` will spend 1000 milliseconds (1 second) to approximate the call time bias and granularity for that timer.
```apl
      ⊢⎕PROFILE 'start' 'CPU'
 active  CPU  0.0001037499999 0.0001037499999
```

## {state}←⎕PROFILE 'stop'


Suspends the collection of profiling data.
```apl
      ⊢⎕PROFILE 'stop'
 inactive  CPU  0.0001037499999 0.0001037499999
```

## {state}←⎕PROFILE 'clear'


Clears any collected profiling data and, if profiling is active, places profiling in an inactive state.
```apl
      ⊢⎕PROFILE 'clear'
 inactive    0 0
```

## {state}←⎕PROFILE 'calibrate'


Causes `⎕PROFILE` to perform a 1000 millisecond calibration to approximate the call time bias and granularity for the current timer. Note, a timer must have been previously selected by using `⎕PROFILE 'start'`.


`⎕PROFILE` will retain the lesser of the current timer values compared to the new values computed by the calibration. The rationale for this is to use the smallest possible values of which we can be certain.
```apl
      ⊢⎕PROFILE'calibrate'
 active  CPU  0.0001037499997 0.0001037499997
```

## state←⎕PROFILE 'state'


Returns the current profiling state.
```apl
      )CLEAR
clear ws
      ⎕PROFILE 'state'
 inactive    0 0
 
      ⎕PROFILE 'start' 'CPU'
 active  CPU  0.0001037499997 0.0001037499997
      ⎕PROFILE 'state'
 active  CPU  0.0001037499997 0.0001037499997
```

## data←{X} ⎕PROFILE 'data'


Retrieves the collected profiling data. If the optional left argument `X` is omitted, the result is a matrix with the following columns:


|------|----------------------------------------------------------------------------|
|`[;1]`|function name                                                               |
|`[;2]`|function line number or `⍬` for a whole function entry                      |
|`[;3]`|number of times the line or function was executed                           |
|`[;4]`|accumulated time (ms) for this entry exclusive of items called by this entry|
|`[;5]`|accumulated time (ms) for this entry inclusive of items called by this entry|
|`[;6]`|number of times the timer function was called for the exclusive time        |
|`[;7]`|number of times the timer function was called for the inclusive time        |

## Example: (numbers have been truncated for formatting)
```apl
      ⎕PROFILE 'data'
#.foo             1  1.04406  39347.64945   503 4080803 #.foo      1      1  0.12488     0.124887     1       1 #.foo      2    100  0.58851 39347.193900   200 4080500 #.foo      3    100  0.21340     0.213406   100     100 #.NS1.goo       100 99.44404   39346.6053 50300 4080300 #.NS1.goo  1    100  0.61679     0.616793   100     100 #.NS1.goo  2  10000 67.80292   39314.9642 20000 4050000 #.NS1.goo  3  10000 19.60274      19.6027 10000   10000
 
```


If `X` is specified it must be a simple vector of column indices. In this case, the result has the same shape as `X` and is a vector of the specified column vectors:
```apl
X ⎕PROFILE 'data' ←→ ↓[⎕IO](⎕PROFILE 'data')[;X]
```


If column 2 is included in the result, the value `¯1` is used instead of `⍬` to indicate a whole-function entry.

## data←{X} ⎕PROFILE 'tree'


Retrieve the collected profiling data in tree format:


|------|----------------------------------------------------------------------------|
|`[;1]`|depth level                                                                 |
|`[;2]`|function name                                                               |
|`[;3]`|function line number or `⍬` for a whole function entry                      |
|`[;4]`|number of times the line or function was executed                           |
|`[;5]`|accumulated time (ms) for this entry exclusive of items called by this entry|
|`[;6]`|accumulated time (ms) for this entry inclusive of items called by this entry|
|`[;7]`|number of times the timer function was called for the exclusive time        |
|`[;8]`|number of times the timer function was called for the inclusive time        |


The optional left argument is treated in exactly the same way as for `X ⎕PROFILE 'data'`.

<h2 class="example">Example</h2>
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


Note that rows with an even depth level in column `[;1]` represent function summary entries and odd depth level rows are function line entries. Recursive functions will generate separate rows for each level of recursion.

## Notes

### Profile Data Entry Types


The results of `⎕PROFILE 'data'` and `⎕PROFILE 'tree'` have two types of entries; function summary entries and function line entries. Function summary entries contain `⍬` in the line number column, whereas function line entries contain the line number. Dfns line entries begin with 0 as they do not have a header line like traditional functions. The timer data and timer call counts in function summary entries represent the aggregate of the function line entries plus any time spent that cannot be directly attributed to a function line entry. This could include time spent during function initialisation, etc.

<h2 class="example">Example</h2>
```apl
 #.foo         1  1.04406 39347.649450   503 4080803
 #.foo    1    1  0.12488     0.124887     1       1
 #.foo    2  100  0.58851 39347.193900   200 4080500
 #.foo    3  100  0.21340     0.213406   100     100
```

#### Timer Data Persistence


The profiling data collected is stored outside the workspace and will not impact workspace availability. The data is cleared upon workspace load, clear workspace, `⎕PROFILE 'clear'`, or interpreter sign off.

## The PROFILE User Command


`]PROFILE` is a utility which implements a high-level interface to `⎕PROFILE` and provides reporting and analysis tools that act upon the profiling data. For further information, see Tuning Applications using the Profile User Command.

#### Using `⎕PROFILE` Directly


If you choose to use `⎕PROFILE` directly, the following guidelines and information may be of use to you.


Note: Running your application with `⎕PROFILE` turned on incurs a significant processing overhead and will slow your application down.

##### Decide which timer to use


`⎕PROFILE` supports profiling of either CPU or elapsed time. CPU time is generally of more interest in profiling application performance.


#### Simple Profiling


To get a quick handle on the top CPU time consumers in an application, use the following procedure:

- Make sure the application runs long enough to collect enough data to overcome the timer granularity – a reasonable rule of thumb is to make sure the application runs for at least `(4000×4⊃⎕PROFILE 'state')` milliseconds.
- Turn profiling on with `⎕PROFILE 'start' 'CPU'`
- Run your application.
- Pause the profiler with `⎕PROFILE 'stop'`
- Examine the profiling data from `⎕PROFILE 'data'` or `⎕PROFILE 'tree'` for entries that consume large amounts of resource.



This should identify any items that take more than 10% of the run time.


To find finer time consumers, or to focus on elapsed time rather than CPU time, take the following additional steps prior to running the profiler:


Turn off as much hardware as possible. This would include peripherals, network connections, etc.

- Turn off as many other tasks and processes as possible. These include anti-virus software, firewalls, internet services, background tasks.
- Raise the priority on the Dyalog APL task to higher than normal, but in general avoid giving it the highest priority.
- Run the profiler as described above.


Doing this should help identify items that take more than 1% of the run time.

##### Advanced Profiling


The timing data collected by `⎕PROFILE` is not adjusted for the timer's call time bias; in other words, the times reported by `⎕PROFILE` include the time spent calling the timer function. One effect of this can be to make "cheap" lines that are called many times seem to consume more resource. If you desire more accurate profiling measurements, or if your application takes a short amount of time to run, you will probably want to adjust for the timer call time bias. To do so, subtract from the timing data the timer's' 'call time bias multiplied by the number of times the timer was called.

<h5 class="example">Example</h5>
```apl
      CallTimeBias←3⊃⎕PROFILE 'state'
      RawTimes←⎕PROFILE 'data'
      Adjusted←RawTimes[;4 5]-RawTimes[;6 7]×CallTimeBias
```


