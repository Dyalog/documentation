# Thread Switching

!!! warning
    Programming with threads requires care!

The interpreter may switch between running threads at the following points:

- Between any two lines of a defined function or operator.
- On entry to a dfn or dop.
- While waiting for a `⎕DL` to complete.
- While awaiting input from:
    * `⎕DQ`
    * `⎕SR`
    * `⎕ED`
- The session prompt or `⎕:` or `⍞.`
- While awaiting the completion of an external operation:
    * A call on an external (AP) function.
    * A call on a `⎕NA` (DLL) function.
    * A call on an OLE function.
    * A call on a .NET function.

At any of these points, the interpreter might execute code in other threads. If such threads change the global environment; for example by changing the value of, or expunging a name; then the changes will appear to have happened while the thread in question passes through the switch point. It is the task of the application programmer to organise and contain such behaviour.

You can prevent threads from interacting in critical sections of code by using the `:Hold` control structure.

## High Priority Callback Functions

Note that the interpreter cannot perform thread-switching during the execution of a *high-priority callback*. This is a callback function that is invoked by a *high-priority* event which demands that the interpreter must return a result to Windows before it may process any other event. Such high-priority events include Configure, ExitWindows, DateTimeChange, DockStart, DockCancel, DropDown. It is therefore not permitted to use a `:Hold` control structure in a high-priority callback function.
