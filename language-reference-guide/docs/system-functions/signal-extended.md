---
search:
  boost: 2
---

# <span>Signal Extended Event</span> `{R}←⎕SIGNAL Y`{{key}}

[`⎕SIGNAL`](signal.md) with a set of name/value pairs generates an event with additional information added to the [default event](signal-default.md).

<h2 class="example">Example</h2>

```apl
      ⎕SIGNAL⊂('EN' 200)('Vendor' 'Andy')('Message' 'My error')
ERROR 200: My error
      ⎕SIGNAL⊂('EN' 200)('Vendor' 'Andy')('Message' 'My error')
      ∧
      ⍪⎕DMX.(EN EM Vendor)
┌─────────┐
│200      │
├─────────┤
│ERROR 200│
├─────────┤
│Andy     │
└─────────┘
```

## Right Argument

`Y` is a scalar or vector whose first element is a set of name/value pairs, given either as a vector of two-element vectors or as a two-column matrix; any further elements of `Y` are ignored. A `Y` of higher rank signals `RANK ERROR`.

```apl
      ⎕SIGNAL⊂2 2⍴'EN' 200 'Message' 'My error'
ERROR 200: My error
      ⎕SIGNAL⊂2 2⍴'EN' 200 'Message' 'My error'
      ∧
```

Each pair names a member of [`⎕DMX`](dmx.md) and the value to report for it; members not named keep their default value. `EN` must be among the names, and its value must be a permitted [event number](signal-default.md#right-argument), otherwise `⎕SIGNAL` signals `DOMAIN ERROR`.

The names that can be given are `Category`, `EM`, `EN`, `ENX`, `HelpURL`, `Message`, `OSError`, and `Vendor`. The remaining members of `⎕DMX`, `DM` and `InternalLocation`, are always derived by the interpreter and cannot be set:

```apl
      ⎕SIGNAL⊂('EN' 200)('InternalLocation' 'here')
DOMAIN ERROR: Unexpected name in signalled ⎕DMX specification
      ⎕SIGNAL⊂('EN' 200)('InternalLocation' 'here')
      ∧
```

Each value must suit its name: `ENX` takes an integer, and `OSError` a three-element vector of an integer, an integer, and a character vector.

!!! Info "Information"
    Dyalog might extend `⎕DMX` in a future release, which would change the names that can be given here.

!!! Warning "Warning"
    Only the first element of `Y` is used, so a single pair needs enclosing twice: once as the set of pairs, and once as the first element of `Y`. Under-enclosing it leaves `⎕SIGNAL` reading the name `EN` as a set of two one-character pairs:

    ```apl
          ⎕SIGNAL⊂('EN' 200)
    DOMAIN ERROR: Unexpected name in signalled ⎕DMX specification
          ⎕SIGNAL⊂('EN' 200)
          ∧
          ⎕SIGNAL⊂⊂('EN' 200)
    ERROR 200
          ⎕SIGNAL⊂⊂('EN' 200)
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
    [1]    :Trap 0 ⋄ {⎕SIGNAL⊂⊂('EN' 200)}0 ⋄ r←'not signalled'
    [2]    :Else ⋄ r←'caught here'
    [3]    :EndTrap
         ∇

          Trapped
    caught here
    ```

## .NET Exceptions

`EN` `90` throws a .NET exception. There is no left argument to carry an exception object, so the exception thrown is always a plain `System.Exception`:

```apl
      ⎕SIGNAL⊂⊂('EN' 90)
EXCEPTION: Exception of type 'System.Exception' was thrown.
      ⎕SIGNAL⊂⊂('EN' 90)
      ∧
      ⎕EXCEPTION
System.Exception: Exception of type 'System.Exception' was thrown.
```

To throw an exception object of your own, use a [default event](signal-default.md#net-exceptions).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL ⎕DMX DMX error event
</div>
