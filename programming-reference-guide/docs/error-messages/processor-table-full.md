

# <span>PROCESSOR TABLE FULL</span> `76`

This report can only occur in a UNIX environment.

This report is given when the limit on the number of processes (tasks) that the computer system can support would be exceeded.  The limit is installation dependent.  The report is given when an attempt is made to initiate a further process, occurring when an APL session is started.

It is necessary to wait until active processes are completed before the required task may proceed.  If the condition should occur frequently, the solution is to increase the limit on the number of processes for the computer system.

<h2 class="example">Example</h2>
```apl
      'prefect' ⎕SH 'prefect'
PROCESSOR TABLE FULL
      'prefect' ⎕SH 'prefect'
      ^
```
