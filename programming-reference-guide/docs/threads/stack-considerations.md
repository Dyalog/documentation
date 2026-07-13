# Stack Considerations

When you start a thread, it begins with the SI stack of the calling function and sees all of the local variables defined in all the functions down the stack. However, unless the calling function specifically waits for the new thread to terminate (see [Language Reference: Wait for Threads to Terminate](../../../language-reference-guide/system-functions/tsync)), the calling functions will (bit by bit, in their turn) continue to execute. The new thread's view of its calling environment may then change. Consider the following example:

Suppose that you had the following functions: `RUN[3]` calls `INIT` which in turn calls `GETDATA` but as 3 separate threads with 3 different arguments:
```apl
     ∇ RUN;A;B
[1]    A←1
[2]    B←'Hello World'
[3]    INIT
[4]    CALC
[5]    REPORT
     ∇
```
```apl
     ∇ INIT;C;D
[1]    C←D←0
[2]    GETDATA&'Sales'
[3]    GETDATA&'Costs'
[4]    GETDATA&'Expenses'
     ∇
```

When each `GETDATA` thread starts, it immediately *sees* (via `⎕SI`) that it was called by `INIT` which was in turn called by `RUN`, and it *sees* local variables `A`, `B`, `C` and `D`. However, once `INIT[4]` has been executed, `INIT` terminates, and execution of the root thread continues by calling `CALC`. From then on, each `GETDATA` thread no longer sees `INIT` (it thinks that it was called directly from `RUN`) nor can it see the local variables `C` and `D` that `INIT` had defined. However, it *does* continue to see the locals `A` and `B` defined by `RUN`, until `RUN` itself terminates.

Note that if `CALC` were also to define locals `A` and `B`, the `GETDATA` threads would still see the values defined by `RUN` and not those defined by `CALC`. However, if `CALC` were to modify `A` and `B` (as globals) without localising them, the `GETDATA` threads would see the modified values of these variables, whatever they happened to be at the time.
