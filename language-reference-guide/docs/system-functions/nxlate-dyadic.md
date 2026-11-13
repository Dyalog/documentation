---
search:
  boost: 2
---

# <span>Set Native File Translation Vector</span> `{R}←X ⎕NXLATE Y`{{key}}

This function sets the [translate vector](#translate-vector) of a [native file](../../programming-reference-guide/native-files.md), which maps characters onto bytes when the file is read or written with conversion code 82. [Monadic `⎕NXLATE`](nxlate-monadic.md) returns it without changing it.

!!! Legacy "Legacy"
    In the Unicode Edition, `⎕NXLATE` is retained for backwards compatibility purposes. It is relevant only to native files that are read or written with conversion code 82, such as files written by the Classic Edition.

<h2 class="example">Example</h2>

The same characters are written with the default translate vector, and then with one that represents each character by its position in `⎕AV`:

```apl
      t←'data.txt'⎕NCREATE 0
      'Grüße'⎕NAPPEND t 82
      old←((⍳256)-⎕IO)⎕NXLATE t
      'Grüße'⎕NAPPEND t 82
      256|⎕NREAD t 83 10 0
71 114 252 223 101 71 34 236 139 21
```

With the default translate vector restored, the first five bytes read back as the characters that were written:

```apl
      old ⎕NXLATE t
      ⎕NREAD t 82 5 0
Grüße
```

## Left Argument

`X` is the new [translate vector](#translate-vector), a simple integer vector of 256 items, each in the range `0` to `255`.

## Right Argument

`Y` is a simple integer scalar, either the tie number of a native file or `0`. `0` identifies the translate vector that [`⎕DR`](dr.md) uses in the Classic Edition to convert to and from character data (data type 82). Any other number signals `FILE TIE ERROR`.

## Result

`R` is the previous translate vector, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## Translate Vector

A translate vector is a simple integer vector of 256 items, each in the range `0` to `255`. Each item is the byte that represents the character in the same position of the [atomic vector](av.md), `⎕AV`.

Conversion code 82 of [`⎕NREAD`](nread.md), [`⎕NAPPEND`](nappend.md), and [`⎕NREPLACE`](nreplace.md) uses the translate vector of the file. When characters are written, each one is replaced with its byte. When bytes are read, each one becomes the first character of `⎕AV` that the translate vector maps onto it, or `⎕AV[⎕IO]` if there is none.

In the Unicode Edition, [`⎕AVU`](avu.md) defines the characters of `⎕AV`. Writing a character that is not in `⎕AV` signals `TRANSLATION ERROR`.

A native file gets the default translate vector each time it is tied or created. The default maps most of the characters of `⎕AV` that are in the ANSI (Windows-1252) character set onto their codes in it, and maps the APL symbols onto other codes. In the Classic Edition, the default is derived from the output translate table (normally `WIN.DOT`).

The translate vector `(⍳256)-⎕IO` represents each character by its position in `⎕AV`, counting from 0. This is the internal representation of characters in the Classic Edition, which therefore writes and reads them without translation.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NXLATE NXLATE
</div>
