---
search:
  boost: 2
---

# <span>Signal Extended Event</span> `{R}←⎕SIGNAL Y`{{key}}

This form of `⎕SIGNAL` generates an event whose reported details are chosen rather than taken from the event number. To generate one of Dyalog's own events instead, see [Signal Default Event](signal-default.md).

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

The first element of `Y` is a set of name/value pairs, given either as a vector of two-element vectors or as a two-column matrix. Each pair names a member of [`⎕DMX`](dmx.md) and the value to report for it; members not named keep the value they would have had.

```apl
      ⎕SIGNAL⊂2 2⍴'EN' 200 'Message' 'My error'
ERROR 200: My error
      ⎕SIGNAL⊂2 2⍴'EN' 200 'Message' 'My error'
      ∧
```

`EN` must be among the names, and its value must be a permitted [event number](signal-default.md#right-argument):

```apl
      ⎕SIGNAL⊂⊂('Message' 'My error')
DOMAIN ERROR: Invalid error number for signal
      ⎕SIGNAL⊂⊂('Message' 'My error')
      ∧
```

The names that can be given are `Category`, `EM`, `EN`, `ENX`, `HelpURL`, `Message`, `OSError`, and `Vendor`. The remaining members of `⎕DMX`, `DM` and `InternalLocation`, are always derived by the interpreter and cannot be set:

```apl
      ⎕SIGNAL⊂('EN' 200)('InternalLocation' 'here')
DOMAIN ERROR: Unexpected name in signalled ⎕DMX specification
      ⎕SIGNAL⊂('EN' 200)('InternalLocation' 'here')
      ∧
```

Each value must suit its name, so `ENX` and `OSError` take numbers rather than text.

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

## Left Argument

There is no left argument:

```apl
      'msg'⎕SIGNAL⊂⊂('EN' 200)
DOMAIN ERROR: Cannot provide a left argument with the given right argument
      'msg'⎕SIGNAL⊂⊂('EN' 200)
           ∧
```

The event message that a [default event](signal-default.md) takes as its left argument is given as the `EM` pair here:

```apl
      ⎕SIGNAL⊂('EN' 200)('EM' 'My message')
My message
      ⎕SIGNAL⊂('EN' 200)('EM' 'My message')
      ∧
```

## Result

`R` is `Y`, and is shy. An event is generated, so `R` is only of interest when nothing is signalled, which happens when `Y` is empty.

## Effect on Execution

The effect on the state indicator and on error trapping is the same as for a [default event](signal-default.md#effect-on-execution).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL ⎕DMX DMX error event
</div>
