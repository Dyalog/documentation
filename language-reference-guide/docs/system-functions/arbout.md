---
search:
  boost: 2
---

# <span>Arbitrary Output</span> `{R}←X ⎕ARBOUT Y`{{key}}

`⎕ARBOUT` writes the bytes in `Y` to the output device `X`.

<h2 class="example">Example</h2>

```apl
      out←'abc.txt'⎕NCREATE 0
      out ⎕ARBOUT 65 66 67
      ⎕NSIZE out
3
```

## Left Argument

`X` is one of:

- the tie number of a native file, from [`⎕NTIE`](ntie.md) or [`⎕NCREATE`](ncreate.md). Writing starts at the current position in the file, replaces any bytes there, and moves the position past the bytes written.
- under Unix, a file descriptor that the command that started the interpreter opened, for example, `9` when the interpreter was started with `9>out.txt`. The descriptors `0`, `1`, and `2` (standard input, output, and error) signal `DOMAIN ERROR`. The interpreter does not check that any other descriptor was opened by that command, and it has descriptors of its own open.

A negative number that is not a tie number signals `DOMAIN ERROR`, and a tie that is not open for writing signals `FILE ERROR`.

!!! Warning "Warning"
    Do not read or write the same tie with both [`⎕ARBIN`](arbin.md) or `⎕ARBOUT` and native file functions such as [`⎕NREAD`](nread.md) and [`⎕NREPLACE`](nreplace.md). The interpreter keeps track of the position in a native file, but `⎕ARBIN` and `⎕ARBOUT` move the position without updating its record, so a native file function can then read or write at the wrong place.

<h3 class="example">Examples</h3>

Continuing with `abc.txt` from the example above, a new tie starts at the beginning of the file, so `XY` replaces `AB`. `⎕ARBIN` reads the file back:

```apl
      ⎕NUNTIE out
      out←'abc.txt'⎕NTIE 0
      out ⎕ARBOUT 88 89
      ⎕NUNTIE out
      in←'abc.txt'⎕NTIE 0
      ⎕UCS(3 in)⎕ARBIN ⍬
XYC
```

Under Unix, if the interpreter was started with `9>out.txt`, this writes `123` and a line feed to **out.txt**:

```apl
      9 ⎕ARBOUT 49 50 51 10
```

## Right Argument

`Y` is an integer scalar or a simple integer vector of the bytes to write. Each item is from `¯128` to `255`, and a negative item `b` is written as the byte `256+b`. If `Y` is empty, nothing is written.

An item outside that range, or that is not an integer, signals `DOMAIN ERROR`. An array of rank 2 or more signals `RANK ERROR`.

<h3 class="example">Example</h3>

Text is written in a particular encoding by converting it to bytes first. In UTF-8, each Greek letter takes 2 bytes, so the 10 characters take 19 bytes:

```apl
      out←'greeting.txt'⎕NCREATE 0
      out ⎕ARBOUT 'UTF-8'⎕UCS'Καλό Πάσχα'
      ⎕NSIZE out
19
```

## Result

The [shy](../../programming-reference-guide/introduction/results.md#shy-results) result `R` is an empty numeric vector.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ARBOUT ARBOUT
</div>
