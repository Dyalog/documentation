# Globals and the Order of Execution

It is important to recognise that any reference or assignment to a global or semi-global object (including GUI objects) is **inherently dangerous** (that is, a source of programming error) if more than one thread is running. Worse still, programming errors of this sort may not become apparent during testing because they are dependent upon random timing differences. Consider the following example:

```apl
     ∇ BUG;SEMI_GLOBAL
[1]    SEMI_GLOBAL←0
[2]    FOO& 1
[3]    GOO& 1
     ∇
 
     ∇ FOO
[1]    :If SEMI_GLOBAL=0
[2]        DO_SOMETHING SEMI_GLOBAL
[3]    :Else
[4]        DO_SOMETHING_ELSE SEMI_GLOBAL
[5]    :EndIf
     ∇
 
     ∇ GOO
[1]    SEMI_GLOBAL←1
     ∇
```

In this example, it is formally impossible to predict in which order APL will execute statements in `BUG`, `FOO` or `GOO` from `BUG[2]` onwards. For example, the actual sequence of execution may be:
```apl
      BUG[1] → BUG[2] → FOO[1] → FOO[2] →
               DO_SOMETHING[1]
```

or
```apl
      BUG[1] → BUG[2] → BUG[3] → GOO[1] →
               FOO[1] → FOO[2] → FOO[3] →
               FOO[4] → DO_SOMETHING_ELSE[1]
```

This is because APL may switch from one thread to another between any two lines in a defined function. In practice, because APL gives each thread a significant time-slice, it is likely to execute many lines, maybe even hundreds of lines, in one thread before switching to another. However, you must not rely on this; **thread-switching may occur at any time between lines in a defined function**.

Secondly, consider the possibility that APL switches from the `FOO` thread to the `GOO` thread after `FOO[1]`. If this happens, the value of `SEMI_GLOBAL` passed to `DO_SOMETHING` will be 1 and not 0. Here is another source of error.

In  this case, there are two ways to resolve the problem. To ensure that the value of `SEMI_GLOBAL` remains the same from `FOO[1]` to `FOO[2]`, you can use diamonds instead of separate statements. For example:
```apl
      :If SEMI_GLOBAL=0 ⋄ DO_SOMETHING SEMI_GLOBAL
```

Even better, although less efficient, you can use `:Hold` to synchronise access to the variable. For example:
```apl
      ∇ FOO
[1]    :Hold 'SEMI_GLOBAL'
[2]        :If SEMI_GLOBAL=0
[3]            DO_SOMETHING SEMI_GLOBAL
[4]        :Else
[5]            DO_SOMETHING_ELSE SEMI_GLOBAL
[6]        :EndIf
[7]    :EndHold
     ∇
 
     ∇ GOO
[1]    :Hold 'SEMI_GLOBAL'
[2]        SEMI_GLOBAL←1
[3]    :EndHold
     ∇
```

Now, although you still cannot be sure which of `FOO` and `GOO` will run first, you can be sure that `SEMI_GLOBAL` will not change (because `GOO` cuts in) within `FOO`.

Note that the string used as the argument to `:Hold` is completely arbitrary, so long as threads competing for the same resource use the same string.

!!! warning
     These types of problems are inherent in all multithreading programming languages, and not just with Dyalog APL. *If you want to take advantage of the additional power provided by multithreading, it is advisable to think carefully about the potential interaction between different threads.*
