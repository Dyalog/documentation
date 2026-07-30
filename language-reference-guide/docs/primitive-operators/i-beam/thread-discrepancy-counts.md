---
search:
  boost: 2
---


# <span>Thread Discrepancy Counts</span> `R←4061⌶Y`{{key}}

`Y` must be `0` but is ignored.

As it runs, the interpreter checks that its own record of each thread's scheduling status is consistent. These checks are always enabled.

The result `R` is an integer vector of the number of times each discrepancy has been detected since the interpreter started:

|Element|Discrepancy                   |
|-------|------------------------------|
|`R[1]` |Inconsistent thread status    |
|`R[2]` |Possible missed thread wakeup |

A non-zero count reports that the interpreter detected an inconsistency in its own scheduling, not that the application is at fault.

Details of each occurrence are written to the log file enabled by [`109⌶`](log-file-for-deprecations.md). This function reports the counts when no such log file is enabled, so that you can see whether anything was detected, then enable logging and run the application again to capture the details. The first time a discrepancy is detected, if no log file is enabled, a message is written to the Status window.

!!! note
    These checks verify assumptions made by the current thread scheduler and are expected to be withdrawn in a later release.

<h2 class="example">Example</h2>
```apl
      4061⌶0
5 1
```
Five inconsistent thread statuses and one possible missed thread wakeup have been detected.

<!-- Hidden search keywords -->
<div style="display: none;">
  4061⌶
</div>
