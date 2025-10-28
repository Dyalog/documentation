<h1 class="heading"><span class="name">Threading</span></h1>

The .NET Framework is inherently a multi-threaded environment. For example, ASP.NET runs its own thread pool from which it allocates system threads to its clients. Calls from ASP.NET into APL Web Pages and Web Services will typically be made from different system threads. This means that APL will receive calls from .NET while it is processing a previous call. The situation is further complicated when you write an APL Web Page that calls an APL Web Service, both of which may be hosted by a single Dyalog DLL inside ASP.NET. In these circumstances, ASP.NET may well allocate different system threads to the .NET calls, which are made into the two separate APL objects. Although in the first example (multiple clients) APL could theoretically impose its own queuing mechanism for incoming calls, it cannot do so in the second case without causing a deadlock situation.

It is important to remember that whether running as DYALOG.EXE, or as the Dyalog DLL, the Dyalog interpreter executes in a *single system thread*. However, APL does provide the ability to run several APL threads at the same time. If you are unfamiliar with APL threads, see *Language Reference, Chapter 1* for an introduction to this topic.

To resolve this situation, Dyalog automatically allocates APL threads to .NET system threads and maintains a thread synchronisation table so that calls on the same system thread are routed to the same APL thread, and vice versa. This is important because a GUI object (cf. `System.Winforms`) is owned by the system thread that created it and can only be accessed by that thread.

The way that system threads are allocated to APL threads differs between the case where APL is running as the primary executable (DYALOG.EXE) or as a DLL hosted by another program. The latter is actually the simpler of the two and will be considered first.

## DYALOG DLL Threading

In this case, all calls into the Dyalog DLL are initiated by Microsoft .NET.

When a .NET system thread first needs to run an APL function, APL starts a new APL thread for it, and executes the function in that APL thread. For example, if the first call is a request to create a new instance of an APL .NET object, its constructor function will be run in APL thread 1. An entry is made in the internal thread table that associates the originating system thread with APL thread 1. When the constructor function terminates, the APL thread is retained so that it is available for a subsequent call on its associated system thread. In this respect, the automatically created APL thread differs from an APL thread that was created using the spawn operator `&` (See Language Reference).

When a subsequent call comes in, APL locates the originating system thread in its internal thread table, and runs the appropriate APL function in the corresponding APL thread. Once again, when the function terminates, the APL thread is retained for future use. If a call comes in on a new system thread, a new APL thread is created.

Notice that under normal circumstances, APL thread 0 is never used in the Dyalog DLL. It is only ever used if, during debugging, the APL programmer explicitly changes to thread 0 by executing `)TID 0` and then runs an expression.

Periodically, APL checks the existence of all of the system threads in the internal thread table, and removes those entries that are no longer running. This prevents the situation arising that all APL threads are in use.

## DYALOG.EXE Threading

In these cases, all calls to Microsoft .NET are initiated by Dyalog. However, these calls may well result in calls being made back from .NET into APL.

When you make a .NET call from APL thread 0, the .NET call is run on **the same system thread** that is running APL itself.

When you make a .NET call from any other APL thread, the .NET call is run on a different system thread. Once again, the correspondence between the APL thread number and the associated system thread is maintained (for the duration of the APL thread) so that there are no thread/GUI ownership problems. Furthermore, APL callbacks invoked by .NET calls back into APL will automatically be routed to the appropriate APL thread. Notice that, unlike a call to a DLL via `⎕NA`, there is no way to control whether or not the system uses a different system thread for a .NET call. It will always do so if called from an APL thread other than APL thread 0.

## Thread Switching

Dyalog will potentially *thread switch*, that is, switch execution from one APL thread to another, at the start of any line of APL code. In addition, Dyalog will potentially thread switch when a .NET method is called or when a .NET property is referenced or assigned a value. If the .NET call accesses a relatively slow device, such as a disk or the internet,  this feature can improve overall throughput by allowing other APL code while a .NET call is waiting. On a multi-processor computer, APL may truly execute in parallel with the .NET code.

Note that when running DYALOG.EXE, .NET calls made from APL thread 0 will prevent any switching between APL threads. This is because the .NET code is being executed in the same system thread as APL itself. If you want to use APL multi-threading in conjunction with .NET calls, it is therefore advisable to perform all of the .NET calls from threads other than APL thread 0.
