<h1 class="heading"><span class="name">Data Collection</span></h1>

!!! Warning "Warning"
	The `⎕PROFILE` system function can collect very large quantities of data. This means that, to profile a large application or to save a dataset as an XML file, the workspace size might need to be increased significantly.

For complete documentation of the `⎕PROFILE` system function, see the [Language Reference Guide](../../language-reference-guide ).

## Before Initiating the Collection of Data

To improve the accuracy of the data and minimise the impact of timer overhead (see [Timer Overhead](#timer-overhead)):

* Switch off as much hardware as possible, including peripherals and network connections.
* Switch off as many other tasks and processes as possible, including anti-virus software, firewalls, internet services and background tasks.
* Raise the priority on the Dyalog APL task to higher than normal.
!!! windows "Dyalog on Microsoft Windows"
    On Microsoft Windows, avoid giving it the highest priority.

Data collected by the `⎕PROFILE` system function is cumulative whenever the `⎕PROFILE` system function is in an active state (but does not persist between Sessions); to discard any previously-collected data, enter `⎕PROFILE 'clear'`.

## Initiating the Collection of Data

Data collection is initiated by entering:
```apl
⎕PROFILE'start'
```

This puts ⎕PROFILE into an active state.

⎕PROFILE supports profiling using either CPU or elapsed time. CPU
time is usually of more interest in profiling application performance
and, by default, ⎕PROFILE will register CPU usage data using the
best available counter.

## Collecting Data

Whether data is being collected or not can be verified by entering:
```apl
⎕PROFILE 'state'
```

This returns a 4 element vector, in which:

|-----|---------------------------|
|`[1]`|is a character vector indicating the state of `⎕PROFILE`.<br />Can be either `active` or `inactive` (must be `active` for data collection).|
|`[2]`|is a character vector indicating the timer being used.<br />Can be `CPU`, `elapsed`, `coverage` or `none`.|
|`[3]`| is the call time bias in milliseconds, that is the amount of time that is consumed when the system takes a time measurement.|
|`[4]`| is the timer granularity in milliseconds, that is, the resolution of the timer being used. On most platforms this will be zero, indicating that the granularity is smaller than the cost and cannot be estimated.|

During data collection, the following data is recorded for each function and for each individual line in a function:
 * Calls – the number of times the function or line was executed.
 * Exclusive Time – milliseconds spent executing the function or line, excluding time spent in functions that were called by the function or line.
 * Inclusive Time – milliseconds spent executing the function or line, including time spent in functions that were called by the function or line.

The times collected by the `⎕PROFILE` system function include the time spent calling the timer function. This means that lines that are called a large number of times can appear to consume more resource than they actually do. For more accurate profiling measurements, adjustments should be made for the timer call time bias. To do this, the application should be run for a sufficiently long period to collect enough data to overcome the timer granularity – a reasonable rule of thumb is to make sure the application runs for at least `4000×4⊃⎕PROFILE 'state'` milliseconds.

The profiling data that is collected is stored outside the workspace and does not impact workspace availability.

`⎕PROFILE` can collect data for functions that are dynamically paged in and out of the workspace.

!!! Info "Information"
	Results can be confusing if several different functions with the same name are used at different times during execution – these are treated as the same function by `⎕PROFILE`.

## Stopping the Collection of Data
Data collection is stopped by entering: 
```apl
⎕PROFILE 'stop'
```
This puts `⎕PROFILE` into an inactive state.

## Timer Overhead

As with all system timers, a cost is associated with the collection of timing data using the `⎕PROFILE` system function. In optimised applications the overhead can be significant; although it is unlikely to impact the identification of hot spots, it can distort results.

By default, reports produced with the `]Profile` user command automatically adjust for timer bias, using the recorded bias – this can be disabled for a report by including the `&#8209;bias=0` modifier and modifier value.

The cost of querying a timer can vary significantly with system load, and repeatable timings are only possible if there is very little activity on the system; the variability is due to the timer calling the operating system kernel, which is servicing all processes on the machine. Dyalog Ltd. recommends increasing the priority of the application being profiled as this can reduce the variability (but will not eliminate it completely).

The timer cost and granularity are estimated the first time that `⎕PROFILE` is run in an APL session. A new calibration can be requested by calling `⎕PROFILE 'calibrate'`.
