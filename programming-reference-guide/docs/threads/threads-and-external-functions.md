# Threads & External Functions

External functions in dynamic link libraries (DLLs) defined using the `⎕NA` interface may be run in separate C threads. Such threads:

- **take advantage of multiple processors** if the operating system permits.
- allow APL to **continue processing in parallel** during the execution of a `⎕NA` function. 

When you define an external function using `⎕NA`, you may specify that the function be run in a separate C thread by appending an ampersand (&) to the function name, for example:
```apl
      'beep'⎕NA'user32|MessageBeep& i'    
      ⍝ MessageBeep will run in a separate C thread
```

When APL first comes to execute a multi-threaded `⎕NA` function, it starts a new C-thread, executes the function within it, and waits for the result. Other APL threads may then run in parallel.

Note that when the `⎕NA` call finishes and returns its result, its new C-thread is retained to be re-used by any subsequent multithreaded `⎕NA` calls made within the same APL thread. Thus any APL thread that makes any multi-threaded `⎕NA` calls maintains a separate C-thread for their execution. This C-thread is discarded when its APL thread finishes.

Note that there is no point in specifying a `⎕NA` call to be multi-threaded, unless you wish to execute other APL threads at the same time.

In addition, if your `⎕NA` call needs to access an APL GUI object (strictly, a window or other handle) it should normally run within the same C-thread as APL itself, and not in a separate C-thread. This is because Windows associates objects with the C-thread that created them. Although you *can* use a multi-threaded `⎕NA` call to access (say) a Dyalog APL Form via its window handle, the effects may be different than if the `⎕NA` call was not multi-threaded. In general, `⎕NA` calls that access APL (GUI) objects should not be multi-threaded.

If you wish to run the same `⎕NA` call in separate APL threads at the same time, you must ensure that the DLL is *thread-safe*. Functions in DLLs which are not *thread-safe*, must be prevented from running concurrently by using the `:Hold` control structure. Note that all the standard Windows API DLLs **are** *thread safe*.

Notice that you may define two separate functions (with different names), one single-threaded and one multi-threaded, associated with the same function in the DLL. This allows you to call it in either way.
