## Timer Overhead

As with all system timers, a cost is associated with the collection of timing data using the `⎕PROFILE` system function. In optimised applications the overhead can be significant; although it is unlikely to impact the identification of hot spots, it can distort results.

By default, reports produced with the `]Profile` user command automatically adjust for timer bias, using the recorded bias – this can be disabled for a report by including the `&#8209;bias=0` modifier and modifier value.

The cost of querying a timer can vary significantly with system load, and repeatable timings are only possible if there is very little activity on the system; the variability is due to the timer calling the operating system kernel, which is servicing all processes on the machine. Dyalog Ltd. recommends increasing the priority of the application being profiled as this can reduce the variability (but will not eliminate it completely).

The timer cost and granularity are estimated the first time that `⎕PROFILE` is run in an APL session. A new calibration can be requested by calling `⎕PROFILE 'calibrate'`.
