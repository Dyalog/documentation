---
search:
  boost: 2
---

# <span>Signal Default Event</span> `{R}←{X} ⎕SIGNAL Y`{{key}}

[`⎕SIGNAL`](signal.md) with an event number generates that event, without [adding further information](signal-extended.md) about it.

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

`Y` is a scalar or vector whose first element is a simple integer event number; any further elements are ignored. A `Y` of higher rank signals `RANK ERROR`.

Permitted event numbers are `0` to `999` and `1006`. `0` [resets the event constants](signal-reset.md) rather than generating an event, and any other value signals `DOMAIN ERROR`.

The numbers Dyalog uses are listed under [`⎕TRAP`](trap.md#TrapEvents); `500` to `999` are reserved for events of your own. An event number with no standard message gets one of the form `ERROR n`:

```apl
      ⎕SIGNAL 500
ERROR 500
      ⎕SIGNAL 500
      ∧
```

## Left Argument

`X` is the event message, replacing the standard one. It is optional: omitting it, or supplying an empty vector, uses the standard [event message](em.md) for the event number in `Y`. See [APL Error Messages](../../programming-reference-guide/error-messages/apl-errors.md) for the standard messages.

`X` must be a simple character scalar or vector, or a [reference to an exception object](#net-exceptions).

<h2 class="example">Example</h2>

`Divide` traps `DOMAIN ERROR` itself, then re-signals event `11` with a message of its own:

```apl
      Divide←{
          11::'DIVISION ERROR'⎕SIGNAL 11
          ⍺÷⍵
      }
      2 4 6 Divide 0
DIVISION ERROR
      2 4 6 Divide 0
            ∧
```

## Result

`R` is `Y`, and is shy. An event is generated, so `R` is only of interest when nothing is signalled, which happens when `Y` is empty.

## Effect on Execution

Generating an event interrupts execution. The state indicator is cut back to exit the function, operator, or dfn capsule containing the line that invoked `⎕SIGNAL`, or to exit the [`⍎`](../primitive-functions/execute.md) expression that invoked it. The event is then generated in the environment that is left.

Because the state indicator is cut back past the function that invoked `⎕SIGNAL`, a [`:Trap`](../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/trap.md) or [`⎕TRAP`](trap.md) in that same function does not intercept the event; one in a calling function does.

!!! Hint "Hints and Recommendations"
    To let a function trap an event that it signals itself, invoke `⎕SIGNAL` from a dfn, which is then the capsule that the state indicator is cut back to:

    ```apl
          ⎕VR'Trapped'
         ∇ r←Trapped
    [1]    :Trap 0 ⋄ {⎕SIGNAL ⍵}200 ⋄ r←'not signalled'
    [2]    :Else ⋄ r←'caught here'
    [3]    :EndTrap
         ∇

          Trapped
    caught here
    ```

## .NET Exceptions

Event `90` throws a .NET exception. `X` is then a reference to an object that is, or derives from, the .NET class `System.Exception`:

```apl
      ⎕USING←'System'
      Ctor←{
          ⍵∊0 1:⎕IO⊢←⍵
          ex←⎕NEW ArgumentException(⊂'IO must be 0 or 1')
          ex ⎕SIGNAL 90
      }
      Ctor 2
EXCEPTION: IO must be 0 or 1
      Ctor 2
      ∧
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL error event
</div>
