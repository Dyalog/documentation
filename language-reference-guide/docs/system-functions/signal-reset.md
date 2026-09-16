---
search:
  boost: 2
---

# <span>Reset Event Constants</span> `{R}←⎕SIGNAL 0`{{key}}

This form of `⎕SIGNAL` does not generate an event. Instead it resets [`⎕DM`](dm.md), [`⎕DMX`](dmx.md), [`⎕EN`](en.md), and [`⎕EXCEPTION`](exception.md), which otherwise keep describing the most recent event indefinitely. To generate an event instead, see [Signal Default Event](signal-default.md) and [Signal Extended Event](signal-extended.md).

<h2 class="example">Example</h2>

```apl
      ÷0
DOMAIN ERROR: Divide by zero
      ÷0
      ∧
      ⎕DM ⎕EN ⎕DMX
┌───────────────────────────────┬──┬───────────────────────────┐
│┌────────────┬────────┬───────┐│11│  EM       DOMAIN ERROR    │
││DOMAIN ERROR│      ÷0│      ∧││  │  Message  Divide by zero  │
│└────────────┴────────┴───────┘│  │                           │
└───────────────────────────────┴──┴───────────────────────────┘
      ⎕←⎕SIGNAL 0
0
      ⎕DM ⎕EN ⎕DMX
┌┬─┬──┐
││0│  │
└┴─┴──┘
```

## Right Argument

`Y` is a scalar or vector whose first element is the integer `0`.

## Left Argument

There is no left argument:

```apl
      'msg'⎕SIGNAL 0
DOMAIN ERROR: Cannot provide a left argument with the given right argument
      'msg'⎕SIGNAL 0
           ∧
```

`⎕SIGNAL 0` is the only form that resets these system constants. Naming `EN` as `0` in an [extended event](signal-extended.md) does not reset them either:

```apl
      ⎕SIGNAL⊂⊂('EN' 0)
DOMAIN ERROR: Invalid error number for signal
      ⎕SIGNAL⊂⊂('EN' 0)
      ∧
```

## Result

`R` is `Y`. It is shy, so it is only displayed if the expression forces it:

```apl
      ⎕SIGNAL 0
      ⎕←⎕SIGNAL 0
0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL reset clear
</div>
