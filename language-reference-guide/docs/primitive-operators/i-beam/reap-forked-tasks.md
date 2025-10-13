
<!-- Hidden search keywords -->
<div style="display: none;">
  4002⌶
</div>






<h1 class="heading"><span class="name">Reap Forked Tasks</span> <span class="command">R←4002⌶Y</span></h1>



!!! note
    **AIX only**


Under UNIX, when a child process terminates, it signals to its parent that it has terminated and waits for the parent to acknowledge that signal. `4002⌶` is the mechanism to allow the APL programmer to issue such acknowledgements.


`Y` must be a simple empty vector but is ignored.



The result `R` is a matrix containing the list of the newly-terminated processes which have been terminated as a result of receiving the acknowledgement, along with information about each of those processes as described below.


`R[;1]` is the process ID (PID) of the terminated child


`R[;2]` is `¯1` if the child process terminated normally, otherwise it is the signal number which caused the child process to terminate.


`R[;3]` is `¯1` if the child process terminated as the result of a signal, otherwise it is the exit code of the child process


The remaining 15 columns are the contents of the `rusage` structure returned by the underlying `wait3()` system call. Note that the two timevalstructs are each returned as a floating point number.


The current `rusage` structure contains:
```c
struct rusage {
    struct timeval ru_utime; /* user time used */
    struct timeval ru_stime; /* system time used */
    long   ru_maxrss;        /* maximum resident set size */
    long   ru_ixrss;         /* integral shared memory size */
    long   ru_idrss;         /* integral unshared data size */
    long   ru_isrss;         /* integral unshared stack size */
    long   ru_minflt;        /* page reclaims */
    long   ru_majflt;        /* page faults */
    long   ru_nswap;         /* swaps */
    long   ru_inblock;       /* block input operations */
    long   ru_oublock;       /* block output operations */
    long   ru_msgsnd;        /* messages sent */
    long   ru_msgrcv;        /* messages received */
    long   ru_nsignals;      /* signals received */
    long   ru_nvcsw;         /* voluntary context switches */
    long   ru_nivcsw;        /* involuntary context switches */
};
```


`4002⌶` may return the PID of an abnormally terminated Auxiliary Processor; APL code should check that the list of processes that have been reaped is a superset of the list of processes that have been started.

<h2 class="example">Example</h2>
```apl
     ∇ tryforks;pid;fpid;rpid
[1]    rpids←fpids←⍬
[2]    :For i :In ⍳5
[3]        fpid←4000⌶'' ⍝ fork() a process
[4]   ⍝ if the child, hang around for a while
[5]        :If fpid=0
[6]            ⎕DL 2×i
[7]            ⎕OFF
[8]        :Else
[9]   ⍝ if the parent, save child's pid
[10]           +fpids,←fpid
[11]       :EndIf
[12]   :EndFor
[13]
[14]   :For i :In ⍳20
[15]       ⎕DL 3
[16]  ⍝ get list of newly terminated child processes
[17]       rpid←4002⌶''
[18]  ⍝ and if not empty, make note of their pids
[19]       :If 0≠⊃⍴rpid
[20]           +rpids,←rpid[;1]
[21]       :EndIf
[22]  ⍝ if all fork()'d child processes accounted for
[23]       :If fpids≡fpids∩rpids
[24]           :Leave  ⍝ quit
[25]       :EndIf
[26]   :EndFor
     ∇
```


