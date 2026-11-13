---
search:
  boost: 2
---

# <span>Query Native File Translation Vector</span> `R←⎕NXLATE Y`{{key}}

This function returns the [translate vector](#translate-vector) of a [native file](../../programming-reference-guide/native-files.md), which maps characters onto bytes when the file is read or written with conversion code 82. [Dyadic `⎕NXLATE`](nxlate-dyadic.md) sets it.

!!! Legacy "Legacy"
    In the Unicode Edition, `⎕NXLATE` is retained for backwards compatibility purposes. It is relevant only to native files that are read or written with conversion code 82, such as files written by the Classic Edition.

<h2 class="example">Example</h2>

The translate vector gives the bytes that represent characters in the file:

```apl
      t←'data.txt'⎕NCREATE 0
      (⎕NXLATE t)[⎕AV⍳'Grüße']
71 114 252 223 101
      'Grüße'⎕NAPPEND t 82
      256|⎕NREAD t 83 5 0
71 114 252 223 101
```

## Right Argument

`Y` is a simple integer scalar, either the tie number of a native file or `0`. `0` identifies the translate vector that [`⎕DR`](dr.md) uses in the Classic Edition to convert to and from character data (data type 82). Any other number signals `FILE TIE ERROR`.

## Result

`R` is the translate vector, a simple integer vector of 256 items.

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
