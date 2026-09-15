---
search:
  boost: 2
---

# <span>Message Output</span> `⍞←X`{{key}}

Assigning an array to `⍞` displays it in the Session or terminal without the new-line that normally ends the last line of output. Successive assignments with no intervening input or output therefore continue on the same line.

<h2 class="example">Example</h2>

```apl
      ⍞←'Hello'
Hello
```

To display an array with a trailing new-line, [assign to `⎕`](quad-output.md) instead. To write a stream of 8-bit codes to a nominated device rather than to the Session or terminal, use [`⎕ARBOUT`](arbout.md).

Error messages, the output of [system commands](../system-commands/index.md), and the messages reported by the editor are all directed in the same way as output through `⍞`. In a terminal environment, output through `⍞` is written to standard error, and output through `⎕` to standard output, so the two can be redirected separately.

Numeric output is formatted as it is for [implicit output](../../programming-reference-guide/introduction/output.md); see [Display of Arrays](../../programming-reference-guide/introduction/arrays/display-of-arrays.md). Output through `⍞` ignores [`⎕PW`](pw.md); how a line longer than the width of the Session or terminal is treated depends on the Session or terminal itself.

<h2 class="example">Examples</h2>

An array of rank greater than 1 is displayed as implicit output displays it, except that the last line does not end with a new-line, so the next assignment continues it:

```apl
      ⍞←2 3⍴'a' ⋄ ⍞←'x'
aaa
aaax
```

Successive assignments build one line:

```apl
      ⍞←'2+2' ⋄ ⍞←'=' ⋄ ⍞←4
2+2=4
```

## Overstrikes

A backspace moves the cursor back one character, so the character that follows overstrikes the one already there. Where the two form a composite character, that character is displayed; where they do not, the second character replaces the first.

<h3 class="example">Example</h3>

`S` overstruck with `|` forms `$`, while `S` overstruck with `O` forms nothing, so the `O` replaces the `S`. The backspace need not be a separate assignment:

```apl
      ⍞←'S' ⋄ ⍞←⎕UCS 8 ⋄ ⍞←'|'
$
      ⍞←'S'(⎕UCS 8)'O'
O
```

[`⎕FMT`](format-dyadic.md) resolves overstrikes the same way, which is a convenient way to discover what a pair produces:

```apl
      ⎕FMT'S'(⎕UCS 8)'|'
$
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍞ stderr
</div>
