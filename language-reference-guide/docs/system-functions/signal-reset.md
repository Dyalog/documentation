---
search:
  boost: 2
---

# <span>Reset Event Constants</span> `{R}←⎕SIGNAL 0`{{key}}

[`⎕SIGNAL`](signal.md) `0` resets [`⎕DM`](dm.md), [`⎕DMX`](dmx.md), [`⎕EN`](en.md), and [`⎕EXCEPTION`](exception.md), which otherwise keep describing the most recent event indefinitely.

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
      ⎕SIGNAL 0
      ⎕DM ⎕EN ⎕DMX
┌┬─┬──┐
││0│  │
└┴─┴──┘
```

## Right Argument

`Y` is a scalar or vector whose first element is the integer `0`; any further elements are ignored. A `Y` of higher rank signals `RANK ERROR`.

## Result

The shy result `R` is `Y`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIGNAL SIGNAL reset clear
</div>
