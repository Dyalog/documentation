---
search:
  boost: 2
---

# <span>Arbitrary Input</span> `R←X ⎕ARBIN Y`{{key}}

`⎕ARBIN` writes the bytes in `Y` to an output device, and then reads bytes from an input device until a condition in `X` ends the read.

<h2 class="example">Example</h2>

[`⎕NPUT`](nput.md) writes two lines to `data.txt`, each ending with a line feed (`10`), and the first of them is read, up to and including its line feed:

```apl
      (('ABC' 'DEF')'UTF-8' 10)⎕NPUT'data.txt'
      in←'data.txt'⎕NTIE 0
      (⍬ in)⎕ARBIN ⍬
65 66 67 10
```

## Left Argument

`X` is a 2-item vector:

|Item |Content|
|-----|-------|
|`1⊃X`|The [condition](#ending-the-read) that ends the read|
|`2⊃X`|The [input device](#devices), or a 2-item vector of the input device and the [output device](#devices)|

### Ending the Read

`1⊃X` is one of:

- an integer scalar, which is the number of bytes to read.
- an integer vector of bytes, any of which ends the read. The byte that ends it is the last item of `R`.
- an empty vector, which ends the read at a line feed (`10`).

The read also ends at the end of a file, and when the [time limit](#time-limit) is reached. `R` then holds the bytes read so far.

<h3 class="example">Example</h3>

Continuing with `in` from the example above, each read starts where the previous one ended. The last read asks for 5 bytes, but only the final line feed is left:

```apl
      (2 in)⎕ARBIN ⍬
68 69
      ((70 90) in)⎕ARBIN ⍬
70
      (5 in)⎕ARBIN ⍬
10
```

### Devices

The input device and the output device are each one of:

- the tie number of a native file, from [`⎕NTIE`](ntie.md) or [`⎕NCREATE`](ncreate.md). Reading and writing start at the current position in the file, and move it past the bytes read or written.
- under Unix, a file descriptor that the command that started the interpreter opened, for example, `9` when the interpreter was started with `9<data.txt`. The descriptors `0`, `1`, and `2` (standard input, output, and error) signal `DOMAIN ERROR`. The interpreter does not check that any other descriptor was opened by that command, and it has descriptors of its own open.

The output device is optional. If it is omitted, `Y` is written to standard output, which can only be reached in this way. Under Microsoft Windows, what is written to standard output does not appear in the Session.

A negative number that is not a tie number signals `DOMAIN ERROR`. The output device is only checked when `Y` is not empty. A device that is not open for reading or writing, as the read or write needs, signals `FILE ERROR`, for example, an output device tied for reading only.

!!! Warning "Warning"
    Do not read or write the same tie with both `⎕ARBIN` or [`⎕ARBOUT`](arbout.md) and native file functions such as [`⎕NREAD`](nread.md) and [`⎕NREPLACE`](nreplace.md). The interpreter keeps track of the position in a native file, but `⎕ARBIN` and `⎕ARBOUT` move the position without updating its record, so a native file function can then read or write at the wrong place.

<h3 class="example">Example</h3>

Under Unix, a FIFO (named pipe) can be both the input device and the output device. The digits are written to it, and 10 bytes are then read back:

```apl
      ⎕SH'mkfifo fifo'
      in←'fifo'⎕NTIE 0
      out←'fifo'⎕NTIE 0
      (10 (in out))⎕ARBIN ⎕UCS ⎕D
48 49 50 51 52 53 54 55 56 57
```

A device that sets the high bit of each byte for parity sends a line feed as `138`, so a read from it ends at either byte:

```apl
      ((10 138) (in out))⎕ARBIN 138
138
```

## Right Argument

`Y` is an integer scalar or a simple integer vector of the bytes to write to the output device before the read. Each item is from `¯128` to `255`, and a negative item `b` is written as the byte `256+b`. If `Y` is empty, nothing is written.

An item outside that range, or that is not an integer, signals `DOMAIN ERROR`. An array of rank 2 or more signals `RANK ERROR`.

## Result

`R` is a simple integer vector of the bytes read, each from `0` to `255`. Their meaning depends on the input device.

## Time Limit

Under Unix, [`⎕RTL`](rtl.md) is an implicit argument of `⎕ARBIN`. If it is not `0`, a read that has not ended after that many seconds ends then, and `R` holds the bytes read so far. Under Microsoft Windows, `⎕RTL` has no effect on `⎕ARBIN`.

<h3 class="example">Example</h3>

Continuing with the FIFO under [Devices](#devices), `AB` is written to it, but no line feed follows. After 2 seconds, the read ends with the 2 bytes:

```apl
      ⎕RTL←2
      (⍬ (in out))⎕ARBIN 65 66
65 66
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ARBIN ARBIN
</div>
