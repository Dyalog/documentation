<h1 class="heading"><span class="name">High-Priority Callback Functions</span></h1>

A high-priority callback function is one that is  invoked by a high-priority
event which demands that Dyalog must return a result to the operating system before it
may process any other event. Such high-priority events include Configure, ExitWindows, DateTimeChange, DockStart, DockCancel, DropDown, GetTipText, GesturePan, GestureZoom, GestureRotate, GestureTwoFingerTap, GesturePressAndTap.

If a high-priority callback function  is traced or stops for any reason, the system is *in limbo* until the windows notification has been actioned. This will occur only when the callback exits. During this time, it is not possible to reset the state indicator or save the workspace.

In the following example, there is a deliberate error on `GenCB[2]` which is assigned as the callback function for the GesturePan event on object `f.s1`.
```apl
      f.s1.onGesturePan←'GenCB'
```
```apl
     ∇ GenCB m
[1]    m
[2]    ∘
     ∇

```

[user drags finger in object]
```apl

 #.f.s1  GesturePan  1  84 103  0 0 
SYNTAX ERROR
GenCB[2] ∘
        ∧
      )SI
#.GenCB[2]*
⎕DQ
      →
DOMAIN ERROR: Operation cannot be completed with an "external" call on the stack
      →
     ∧
      )RESET
Can't )RESET with external call on the stack.
      )CLEAR
Can't )CLEAR with external call on the stack.
      )SAVE
Cannot perform operation with calls to or from external functions or certain callbacks.
```

The only way to restore the situation to normal is to force the callback function to exit. For example:
```apl
      →0
      )SI

```

## Thread-Switching and :Hold

Dyalog cannot perform thread-switching during the execution of a
high-priority callback.

`:Hold`
 with a non-zero number of tokens is not permitted in a high-priority callback and an attempt to use it  will cause the error:
```apl
 DOMAIN ERROR: Cannot :Hold within high priority callback
```
