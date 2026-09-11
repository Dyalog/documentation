# Multi-Threading Language Elements

The following language elements are provided to support threads.

- Primitive operator, _spawn_: [`&`](../../language-reference-guide/primitive-operators/spawn.md).
- System functions: [`⎕DL`](../../language-reference-guide/system-functions/dl.md), [`⎕TALLOC`](../../language-reference-guide/system-functions/talloc.md), [`⎕TCNUMS`](../../language-reference-guide/system-functions/tcnums.md), [`⎕TGET`](../../language-reference-guide/system-functions/tget.md), [`⎕TID`](../../language-reference-guide/system-functions/tid.md), [`⎕TKILL`](../../language-reference-guide/system-functions/tkill.md), [`⎕TNAME`](../../language-reference-guide/system-functions/tname.md), [`⎕TNUMS`](../../language-reference-guide/system-functions/tnums.md), [`⎕TPOOL`](../../language-reference-guide/system-functions/tpool.md), [`⎕TPUT`](../../language-reference-guide/system-functions/tput.md), [`⎕TREQ`](../../language-reference-guide/system-functions/treq.md), [`⎕TSYNC`](../../language-reference-guide/system-functions/tsync.md).
- An extension to the GUI [Event](../../object-reference/properties/event.md#asynchronous-callback-function-name-followed-by) syntax to allow asynchronous callbacks.
- An extension to [`⎕NA`](../../language-reference-guide/system-functions/na.md#multi-threading) syntax (appending `&` to the function name) to run an external function in its own system thread.
- A control structure: [`:Hold`](../defined-functions-and-operators/traditional-functions-and-operators/control-structures/hold.md).
- System commands: [`)HOLDS`](../../language-reference-guide/system-commands/holds.md), [`)TID`](../../language-reference-guide/system-commands/tid.md).
- Extended [`)SI`](../../language-reference-guide/system-commands/si.md) and [`)SINL`](../../language-reference-guide/system-commands/sinl.md) display.

## Running Callback Functions as Threads

A callback function is associated with a particular event via the Event property of the object concerned. A callback function is executed by [`⎕DQ`](../../language-reference-guide/system-functions/dq.md) when the event occurs, or by [`⎕NQ`](../../language-reference-guide/system-functions/nq.md).

If you append the character `&` to the name of the callback function in the `Event` specification, the callback function will be executed asynchronously as a thread when the event occurs. If not, it is executed synchronously as before.

For example, the event specification:
```apl
      ⎕WS'Event' 'Select' 'DoIt&'
```

tells `⎕DQ` to execute the callback function `DoIt` *asynchronously as a thread* when a Select event occurs on the object.
