<h1 class="heading"><span class="name">Multi-Threading Language Elements</span></h1>

The following language elements are provided to support threads.

- Primitive operator, spawn: [`&`](../../../language-reference-guide/primitive-operators/spawn/).
- System functions: [`⎕TID`](../../../language-reference-guide/system-functions/tid/), [`⎕TCNUMS`](../../../language-reference-guide/system-functions/tcnums/),  [`⎕TNUMS`](../../../language-reference-guide/system-functions/tnums/), [`⎕TKILL`](../../../language-reference-guide/system-functions/tkill/), [`⎕TSYNC`](../../../language-reference-guide/system-functions/tsync/).
- An extension to the GUI [Event](../../..//object-reference/properties/event/#asynchronous-callback-function-name-followed-by) syntax to allow asynchronous callbacks.
- A control structure: [`:Hold`](../defined-functions-and-operators/traditional-functions-and-operators/control-structures/hold.md).
- System commands: [`)HOLDS`](../../../language-reference-guide/system-commands/holds/), [`)TID`](../../../language-reference-guide/system-commands/tid/).
- Extended [`)SI`](../../../language-reference-guide/system-commands/si/) and [`)SINL`](../../../language-reference-guide/system-commands/sinl/) display.

## Running Callback Functions as Threads

A callback function is associated with a particular event via the Event property of the object concerned. A callback function is executed by [`⎕DQ`](../../../language-reference-guide/system-functions/dq/) when the event occurs, or by [`⎕NQ`](../../../language-reference-guide/system-functions/nq/).

If you append the character `&` to the name of the callback function in the `Event` specification, the callback function will be executed asynchronously as a thread when the event occurs. If not, it is executed synchronously as before.

For example, the event specification:
```apl
      ⎕WS'Event' 'Select' 'DoIt&'
```

tells `⎕DQ` to execute the callback function `DoIt` *asynchronously as a thread* when a Select event occurs on the object.
