---
search:
  boost: 2
---

# <span>Evaluated Input</span> `⎕`{{key}}

Referencing `⎕` displays the prompt `⎕:` in the Session or terminal and requests input. The response is evaluated, and its result is returned.

<h2 class="example">Example</h2>

```apl
      10×⎕+2
⎕:
      ⍳3
30 40 50
```

In a terminal environment, the response is read from standard input, while the prompt `⎕:` and the response as echoed are written to standard error.

To take the response as characters rather than evaluating it, [reference `⍞`](quotequad-input.md) instead. To read a stream of 8-bit codes from a nominated device rather than from the Session or terminal, use [`⎕ARBIN`](arbin.md).

If evaluating the response signals an error, the error is reported as usual, unless [`⎕TRAP`](trap.md) intercepts it, and the prompt is displayed again. An EOF interrupt reports `EOF INTERRUPT` and the prompt is displayed again. A soft interrupt is ignored; a hard interrupt reports `INTERRUPT` and the prompt is displayed again.

<h2 class="example">Examples</h2>

```apl
      2+⎕
⎕:
      X
VALUE ERROR: Undefined name: X
      X
      ∧
⎕:
      2+⍳3
5 6 7
```

A [system command](../system-commands/index.md) can be entered. It takes effect and the prompt is displayed again, unless the command changes the environment:

```apl
      ⍴3,⎕
⎕:
      )SI
⎕
⎕:
      )CLEAR
clear ws
```

If the response is the [abort statement](../other-syntax/abort.md) `→`, execution is abandoned:

```apl
      1 2 3 = ⎕
⎕:
      →
```

## Interrupts and Time Limits

While `⎕` is awaiting input, a [`⎕TRAP`](trap.md) definition for an interrupt event in the range 1000–1008 does not fire: the interrupt is reported and the prompt is displayed again. A trap for any other event still applies to the expression entered at the prompt. A time limit set in [`⎕RTL`](rtl.md) has no effect either.

<h3 class="example">Example</h3>

The trap on `1000` does not fire when the interrupt arrives, so `INTERRUPT` is reported rather than `STOP`. The trap on `11` does fire, because the `DOMAIN ERROR` comes from the expression entered at the prompt:

```apl
      ⎕TRAP←(11 'C' '''ERROR''')(1000 'C' '''STOP''')
      2+⎕
⎕:
      (Interrupt)
INTERRUPT
⎕:
      'C'+2
ERROR
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ stdin stderr
</div>
