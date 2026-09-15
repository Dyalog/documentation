---
search:
  boost: 2
---

# <span>Character Input</span> `⍞`{{key}}

Referencing `⍞` requests input from the Session or terminal and returns the response as a character vector.

<h2 class="example">Example</h2>

```apl
      R←⍞
INPUT
      R
INPUT
```

In a terminal environment, the response is read from standard input.

To have the response evaluated rather than taken as characters, [reference `⎕`](quad-input.md) instead. To read a stream of 8-bit codes from a nominated device rather than from the Session or terminal, use [`⎕ARBIN`](arbin.md).

If the reference was preceded by [assignments to `⍞`](quotequad-output.md) with no intervening input or output, the last line of that output forms part of the response. Input through `⍞` therefore includes any output through `⍞` since the last new-line character.

<h2 class="example">Examples</h2>

The prompt written with `⍞` is returned as part of the response, so `R` is 14 characters rather than the 5 typed:

```apl
      ⍞←'OPTION : ' ⋄ R←⍞
OPTION : INPUT
      R
OPTION : INPUT
      ⍴R
14
```

## Interrupts and Time Limits

A soft interrupt entered while `⍞` is awaiting input reports `INPUT INTERRUPT` and suspends execution, unless it is trapped:

```apl
      R←⍞
      (Interrupt)
INPUT INTERRUPT
```

A non-zero [`⎕RTL`](rtl.md) imposes a time limit on input through `⍞`. Exceeding it reports `TIMEOUT`, which is a trappable event:

```apl
      ⎕RTL←5 ⋄ ⍞←'PASSWORD : ' ⋄ R←⍞
PASSWORD :
TIMEOUT
      ⎕RTL←5 ⋄ ⍞←'PASSWORD : ' ⋄ R←⍞
                                   ∧
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍞ stdin
</div>
