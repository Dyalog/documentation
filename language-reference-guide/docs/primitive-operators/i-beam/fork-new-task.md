
<!-- Hidden search keywords -->
<div style="display: none;">
  4000⌶
</div>






<h1 class="heading"><span class="name">Fork New Task</span> <span class="command">R←4000⌶Y</span></h1>



!!! note
    **AIX only**


`Y` must be is a simple empty vector but is ignored.


This function *forks* the current APL task. This means that it initiates a new separate copy of the APL program, with exactly the same APL state indicator.


Following the execution of this function, there will be two identical APL processes running on the machine, each with the same state indicator and set of APL objects and values. However, none of the external interfaces and resources in the parent process will exist in the newly forked child process.


The function will return a result in both processes.

- In the parent process, `R` is the process id of the child (forked) process.
- In the child process, `R` is a scalar zero.




The following external interfaces and resources that may be present in the parent process are not replicated in the child process:

- Component file ties
- Native file ties
- Mapped file associations
- Auxiliary Processors
- .NET objects
- Edit windows
- Clipboard entries
- GUI objects (all children of `'.'`)
- I/O to the current terminal



Note that External Functions established using `⎕NA` are replicated in the child process.


The function will fail with a `DOMAIN ERROR` if there is more than one APL thread running.


The function will fail with a `FILE ERROR 11 Resource temporarily unavailable` if an attempt is made to exceed the maximum number of processes allowed per user.


