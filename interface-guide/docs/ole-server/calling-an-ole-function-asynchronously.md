# Calling an OLE Function Asynchronously

## Introduction

Functions exported by an OLEServer are executed (by the underlying OLE technology) in a *synchronous* manner. This means that the OLE client must wait for the function to complete before it can continue processing.

In certain cases the client may not be interested in a result from a function and it may be desirable for client not to have to wait. For example, if a function updates files or performs a printing task, it would be nice for the client application to continue while the server performs this task in background, or indeed (using DCOM) on another computer.

For an *out-of-process* OLE Server, this can be achieved by having the function that is called directly by the client *post* an event (using `⎕NQ`) onto the event queue and then return. When the function terminates, APL will take the next event from the queue and take the appropriate action. If the event has an associated callback function, APL will invoke it. Note that this happens immediately *after* the original function has terminated and a result (if any) has been returned to the client. This means that the APL OLEServer continues processing at the same time as the client application.

Note however that while the OLEServer is processing, further OLE requests will be queued. For example, if the client were to call the same function again immediately, the function would not be invoked until the original processing has finished and the client would therefore wait (note that OLE itself will actually time-out after a certain period). Nevertheless, this technique is an effective way to offload batch processing tasks to a second (background) APL process or to one running on a different computer.

## The OLEASYNC Workspace

The OLEASYNC workspace illustrates this technique. It contains a single namespace called `Async` which exports 2 functions (methods), `PRINT` and `ASYNC` and two variables (properties) `ERRCODE` and `COPIES`.

The first function, `PRINT`, prints a specified number of test pages *in the background*. `PRINT` does not actually do any printing. All it does is to associate a second function `PRINT_CB` as a callback on a user-defined event 3001 (the choice of 3001 is purely arbitrary). It then posts an event 3001 onto the queue and returns 0 as its result.

The function also illustrates the use of `:Trap`. Should either of the statements on lines `[3]` and `[4]` fail, the function terminates cleanly and returns `⎕DM` instead.
```apl
      ∇ R←PRINT N
[1]    ⍝ Prints N test pages "in background"
[2]    :Trap 0
[3]        '.'⎕WS'Event' 3001 'PRINT_CB'N
[4]        ⎕NQ'.' 3001
[5]        (R ERRCODE)←0
[6]    :Else
[7]        (R ERRCODE)←⎕DM ⎕EN
[8]    :EndTrap
     ∇
```

The actual printing is performed by `PRINT_CB` *after* `PRINT` has returned to the client and *while* the client itself continues processing. It too uses `:Trap` to terminate cleanly should an error occur.
```apl
      ∇ N PRINT_CB MSG;PR;I;M
[1]    ⍝ Callback function : prints N test pages
[2]    :Trap 0
[3]        'PR'⎕WC'Printer'
[4]        :For I :In ⍳N
[5]            'PR.'⎕WC'Text'(20 60⍴'Testing')(0 0)
[6]            1 ⎕NQ'PR' 'NewPage'
[7]        :EndFor
[8]        ERRCODE←0
[9]    :Else
[10]       ERRCODE←⎕EN
[11]   :EndTrap
     ∇
```

Note that the client can (later) query `ERRCODE` to find out whether or not the operation succeeded. Indeed, referencing `ERRCODE` will synchronise the client and server because the server will have to wait until `PRINT_CB` completes before it can service the request for the value of `ERRCODE`.

The `ASYNC` function illustrates a slightly different approach and may be used to execute any expression asynchronously. It simply associates its argument (a character vector) as an expression to be executed when (user-defined) event 3001 occurs. It then *posts* this event onto the queue as before.
```apl
      ∇ R←ASYNC CMD
[1]    ⍝ Executes expression CMD "asynchronously"
[2]    :Trap 0
[3]        '#.Async'⎕WS'Event' 3001 'DO'CMD
[4]        ⎕NQ'#.Async' 3001
[5]        (R ERRCODE)←0
[6]    :Else
[7]        (R ERRCODE)←⎕DM ⎕EN
[8]    :EndTrap
     ∇
```

The callback function `DO` is invoked (later) when the event 3001 is processed from the event queue. This happens immediately after the function `ASYNC` has returned its result to the client workspace. `DO` simply executes its left argument, which is the string that was supplied as the right argument to `ASYNC`.
```apl
      ∇ CMD DO MSG
[1]    :Trap 0
[2]        ⍎CMD
[3]        ERRCODE←0
[4]    :Else
[5]        ERRCODE←⎕EN
[6]    :EndTrap
     ∇
```

You may wonder why it is necessary to use a callback function as opposed to an execute expression. In particular, why not have `ASYNC[3]` as follows?
```apl
[3]        '#.Async'⎕WS'Event' 3001 '⍎CMD'
```

The reason is that whilst a callback will execute in the *instance* of the OLEServer namespace connected to this client (which is what we want), an execute expression will be executed in the master OLEServer namespace itself.

The namespace contains a fourth function called `LPR` which is designed to be called via `ASYNC` using an expression such as `ASYNC 'LPR'`.
```apl
      ∇ LPR;PR;I
[1]    :Trap 0
[2]        'PR'⎕WC'Printer'
[3]        :For I :In ⍳COPIES
[4]            'PR.'⎕WC'Text'(20 60⍴'Testing')(0 0)
[5]            1 ⎕NQ'PR' 'NewPage'
[6]        :EndFor
[7]        ERRCODE←0
[8]    :Else
[9]        ERRCODE←⎕EN
[10]   :EndTrap
     ∇
```

Note that the number of copies to be printed is defined by the (global) variable `COPIES` whose default value is 1. This is done only to illustrate that `LPR` called via `DO` runs in the correct instance of the OLEServer (using *your* value of `COPIES`) as opposed to in the master OLEServer namespace itself.

## Testing dyalog.Async

Load OLEASYNC and then register dyalog.Async as an OLE object by doing the following:
```apl
      Async.⎕WC 'OLEServer'
      'Async'⎕WS'ExportedFns' ('PRINT' 'ASYNC')
      'Async'⎕WS'ExportedVars' ('ERRCODE' 'COPIES')
 
```

Rename the workspace to avoid overwriting the original and `)SAVE` it.
```apl
      )WSID c:\MyWS\MYASYNC
was C:\Program Files\Dyalog\Dyalog APL-64 15.0 Unicode\Samples\ole\oleasync.dws
      )SAVE
c:\MyWS\MYASYNC.dws saved Wed Jun  1 14:11:01 2016

```

Finally, register the OLE Server using *File/Export*. **Note that dyalog.Async will only work as an out-of-process OLE Server.**

Now clear the workspace and test dyalog.Async using Dyalog APL as an OLE client application. You could also try calling it from Excel. Note that the results from the functions `PRINT` and `ASYNC` are returned immediately.
```apl
      )CLEAR
clear ws
      'TEST' ⎕WC 'OLEClient' 'dyalog.Async'
 
      TEST.PRINT 3
0
      TEST.ERRCODE
0
      TEST.COPIES←2
      TEST.COPIES
2
      TEST.ASYNC 'LPR'
0
      TEST.ASYNC 99 ⍝ Wrong !
0
      TEST.ERRCODE
11
```
