# Using APLMON

APLMON is enabled and disabled using the APLMON method of Root. It takes a single argument, the name of the file to which the results are to be written. If the file name is empty, APLMON is disabled.

Accumulated data is only actually written to the file when the method is called or when Dyalog terminates. The name of the file to which the results are written is returned as a shy result. This mechanism allows you to log application results in separate files.

<h2 class="example">Example</h2>

Run APLMON and output the data to `myapplication.csv`:
```apl
      a←2 ⎕NQ'.' 'APLMON' 'C:\aplmon\myapplication.csv'
      a

      ⍴a
0
```

The empty result indicates that APLMON was disabled prior to this call.

<h2 class="example">Example</h2>

Output the data and disable APLMON:
```apl
      +2 ⎕NQ '.' 'APLMON' ''
C:\aplmon\myapplication.csv
```

The file name in the result indicates that data has been output to that file and APLMON has been disabled.

# Time measurement

The overhead of using APLMON reduces the overall speed of execution significantly. However, this does not affect the relative accuracy of the measurements.

For optimal  accuracy,   time  measurement should be done with as few other processes running as possible, and in a process that has a higher priority than others.

To change process priority on Microsoft Windows: Start Dyalog, then launch the *Task Manager.* In the *Processes* tab, right-click on *Dyalog* and select *Go to details* from the pop-up menu that appears. Right-click on `dyalog.exe` in the *Details* tab; move the cursor to *Set priority* in the pop-up menu that appears, then select *Above normal* from the additional pop-up menu. A higher priority is not needed (everything else is *Normal* by default) and if set higher, the Dyalog process could cause the operating system to hang and make user control difficult.
