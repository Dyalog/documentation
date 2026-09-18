---
search:
  boost: 2
---

# <span>Standard Output</span> `⎕←X`{{key}}

Assigning an array to `⎕` displays it in the Session or terminal, in the same form as [implicit output](../../programming-reference-guide/introduction/output.md); see [Display of Arrays](../../programming-reference-guide/introduction/arrays/display-of-arrays.md). To read a value from there instead, [reference `⎕`](quad-input.md).

<h2 class="example">Example</h2>

```apl
      ⎕←2+⍳5
3 4 5 6 7
      ⎕←2 4⍴'WINEMART'
WINE
MART
```

To display characters without a trailing new-line, [assign to `⍞`](quotequad-output.md) instead. Error messages, the output of [system commands](../system-commands/index.md), and the messages reported by the editor are all directed in the same way as output through `⍞`. To write a stream of 8-bit codes to a nominated device rather than to the Session or terminal, use [`⎕ARBOUT`](arbout.md).

In a terminal environment, output through `⎕` is written to standard output, and output through `⍞` to standard error, so the two can be redirected separately.

Assigning to `⎕` generates the [SessionPrint](../../object-reference/methodorevents/sessionprint.md) event on the [Session](../../windows-ui-guide/the-session-object/session-object.md) object, which a callback can use to alter or suppress what is displayed.

## Print Width

Output through `⎕` is folded at the width given by [`⎕PW`](pw.md), with the continuation indented. Output through `⍞` is not.

<h3 class="example">Example</h3>

```apl
      ⎕←⍳25
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
      ⎕PW←42
      ⎕←⍳25
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
      18 19 20 21 22 23 24 25
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ stdout
</div>
