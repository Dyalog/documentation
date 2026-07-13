# Threads

Dyalog APL supports multithreading - the ability to run more than one APL expression at the same time.

This unique capability allows you to perform background processing, such as printing, database retrieval, database update, calculations, and so forth while at the same time perform other interactive tasks.

Multithreading may be used to improve throughput and system responsiveness.

**A thread is a strand of execution in the APL workspace.**

A thread is created by calling a function *asynchronously*, using the primitive operator `Spawn`: *&* or by the asynchronous invocation of a callback function.

With a traditional APL *synchronous* function call, execution of the calling environment is paused, *pendent* on the return of the called function. With an *asynchronous* call, both calling environment and called function proceed to execute concurrently.

An asynchronous function call is said to start a new *thread* of execution. Each thread has a unique *thread number*, with which, for example, its presence can be monitored or its execution terminated.

Any thread can spawn any number of sub-threads, subject only to workspace availability. This implies a hierarchy in which a thread is said to be a *child thread* of its *parent thread*. The *base thread* at the root of this hierarchy has thread number 0.

With multithreading, APL’s stack or state indicator can be viewed as a branching tree in which the path from the base to each leaf is a thread.

At any point in time, only one thread is actually running; the others are paused. Each APL thread has its own state indicator, or SI stack. When APL switches from one thread to another, it saves the current stack (with all its local variables and function calls), restores the new one, and then continues processing.

When a parent thread terminates, any of its children which are still running, become the children of (are ‘adopted’ by) the parent’s parent.

Thread numbers are allocated sequentially from 0 to 2147483647. At this point, the sequence ‘wraps around’ and numbers are allocated from 0 again avoiding any still in use. The sequence is reinitialised when a `)RESET` command is issued, or the active workspace is cleared, or a new workspace is loaded. A workspace may not be saved with threads other than the base thread: 0, running.
