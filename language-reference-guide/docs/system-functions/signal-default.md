---
search:
  boost: 2
---

# <span>Signal Default Event</span> `{R}←{X} ⎕SIGNAL Y`{{key}}

This form of `⎕SIGNAL` generates one of the events that Dyalog itself generates, identified by its event number. To choose the values reported in [`⎕DMX`](dmx.md) instead, see [Signal Extended Event](signal-extended.md).

<h2 class="example">Example</h2>

```apl
      'Hello'⎕SIGNAL 200
Hello
      'Hello'⎕SIGNAL 200
             ∧
      ⎕DMX
 EM       Hello
 Message
```

## Right Argument

The first element of `Y` is a simple integer event number. Permitted values are `0`, `1` to `999`, and `1006`; `0` [resets the event constants](signal-reset.md) rather than generating an event. Any other value signals `DOMAIN ERROR`:

```apl
      ⎕SIGNAL 1007
DOMAIN ERROR: Invalid error number for signal
      ⎕SIGNAL 1007
      ∧
```

The numbers Dyalog uses are listed under [`⎕TRAP`](trap.md#TrapEvents); `500` to `999` are reserved for events of your own. An event number with no standard message gets one of the form `ERROR n`:

```apl
      ⎕SIGNAL 500
ERROR 500
      ⎕SIGNAL 500
      ∧
```

## Left Argument

`X` is the event message, replacing the standard one. It is optional: omitting it, or supplying an empty vector, uses the standard message for the event number in `Y`. See [APL Error Messages](../../programming-reference-guide/error-messages/apl-errors.md) for the standard messages.

`X` must be a simple character scalar or vector, or an object reference.

<h2 class="example">Example</h2>

`DIVIDE` traps `DOMAIN ERROR` itself, then re-signals event `11` with a message of its own:

```apl
      ⎕VR'DIVIDE'
     ∇ R←A DIVIDE B;⎕TRAP
[1]    ⎕TRAP←11 'E' '→ERR'
[2]    R←A÷B ⋄ →0
[3]   ERR:'DIVISION ERROR'⎕SIGNAL 11
     ∇

      2 4 6 DIVIDE 0
DIVISION ERROR
      2 4 6 DIVIDE 0
            ∧
```

## Result

`R` is `Y`, and is shy. An event is generated, so `R` is only of interest when nothing is signalled, which happens when `Y` is empty.

## Effect on Execution

Generating an event interrupts execution. The state indicator is cut back to exit the function or operator containing the line that invoked `⎕SIGNAL`, or to exit the [`⍎`](../primitive-functions/execute.md) expression that invoked it. Within a dfn, it is cut back to exit the containing [capsule](../../programming-reference-guide/defined-functions-and-operators/dfns-and-dops/capsules.md). The event is then generated in the environment that is left.

Because the state indicator is cut back past the function that invoked `⎕SIGNAL`, a [`:Trap`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/trap.md) or [`⎕TRAP`](trap.md) in that same function does not intercept the event; one in a calling function does.

If [`⎕TRAP`](trap.md) is set to intercept the event, the trap is taken. Otherwise the standard system action follows, which can cut the state indicator back further if it holds locked functions or operators.

## .NET Exceptions

Event `90` throws a .NET exception. `X` is then a reference to an object that is, or derives from, the .NET class `System.Exception`. This constructor `CTOR` expects a value for [`⎕IO`](io.md):

```apl
     ∇ CTOR IO;EX
[1]    :If IO∊0 1
[2]        ⎕IO←IO
[3]    :Else
[4]        EX←ArgumentException.New'IO must be 0 or 1'
[5]        EX ⎕SIGNAL 90
[6]    :EndIf
     ∇
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL error event
</div>
