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
