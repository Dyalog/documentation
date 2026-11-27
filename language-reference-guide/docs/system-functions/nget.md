---
search:
  boost: 2
---

# <span>Read Text File</span> `R←{X} ⎕NGET Y`{{key}}

This function reads the contents of the specified text file. See also [Write Text File](nput.md).

`Y` is either a character vector/scalar containing the name of the file to be read, or a 2-item vector whose first item is the file name and whose second is an integer scalar specifying `flags` for the operation.

- if `flags` is `0` then `R[1]` is a character vector. This is the default.
- if `flags` is `1` then `R[1]` is a nested array of character vectors.
- if `flags` is `2` then `R[1]` is a matrix, with each row corresponding to a line in the text file specified within `X`.

The optional left argument `X` is the [file encoding](#file-encodings) of the file. If the file starts with a byte order mark (BOM), the BOM determines the encoding, whatever `X` is. Otherwise, `X` determines it, or, if `X` is omitted, `⎕NGET` examines the file to decide its encoding.

The result `R` is a 3-element vector comprising `(content) (encoding) (newline)`  where:

|---|---|
|`content`|A simple character vector, or a vector of character vectors, according to the value of `flags` .|
|`encoding`|The encoding that was actually used to read the file. If this is a UTF format, it will always include the appropriate endianness (except for UTF-8 to which endianness doesn't apply) and a -BOM or -NOBOM suffix to indicate whether or not a BOM is actually present in the file. For example, UTF-16LE-BOM. If `X` is a [byte map](#file-encodings), `encoding` is that same byte map.|
|`newline`|Determined by the first occurrence in the file of one of the newline characters identified in the line separator table, or `⍬` if no such line separator is found.|

If `content` is simple then all its line separators (listed in the table below) are replaced by (normalised to) `⎕UCS 10`, which in the Classic Edition must be in `⎕AVU` (else `TRANSLATION ERROR`). If the file is not empty and does not end with a line separator, `⎕UCS 10` is added at the end, so that a simple `content` always ends with a line separator, as each line of a POSIX text file does.

If `content` is nested, it is formed by splitting the contents of the file on the occurrence of any of the line separators  shown in the table below. These line separators are  removed.

The 3rd element of the result `newline` is a numeric vector from the *Value* column of the table below corresponding to the first occurrence of any of the **newline characters** in the file. If none of these characters are present, the value is `⍬`.

Table: Line Separators { #Line_Separators }

|Value                          |Code  |Description                          |
|-------------------------------|------|-------------------------------------|
|newline characters                                                        |||
|13                             |`CR`  |Carriage Return (U+000D)             |
|10                             |`LF`  |Line Feed (U+000A)                   |
|13 10                          |`CRLF`|Carriage Return followed by Line Feed|
|133                            |`NEL` |New Line (U+0085)                    |
|other line separator characters                                           |||
|11                             |`VT`  |Vertical Tab (U+000B)                |
|12                             |`FF`  |Form Feed (U+000C)                   |
|8232                           |`LS`  |Line Separator (U+2028)              |
|8233                           |`PS`  |Paragraph Separator (U+2029)         |

## File Encodings

<!-- This section is also on csv.md, nput.md, r.md, and shell.md, adapted to each page. A change here might be needed there too. -->

A file encoding is either the name of an encoding or a byte map.

The name of an encoding is one of these character vectors, which are case-sensitive:

|Name|Encoding|
|----|--------|
|`'UTF-8'`|UTF-8|
|`'UTF-16LE'`|UTF-16, little-endian|
|`'UTF-16BE'`|UTF-16, big-endian|
|`'UTF-16'`|UTF-16, with the endianness of the platform, which is big-endian under AIX, and little-endian on all other platforms|
|`'UTF-32LE'`|UTF-32, little-endian|
|`'UTF-32BE'`|UTF-32, big-endian|
|`'UTF-32'`|UTF-32, with the endianness of the platform, which is big-endian under AIX, and little-endian on all other platforms|
|`'ASCII'`|7-bit ASCII|
|`'Windows-1252'`|8-bit Windows-1252|
|`'ANSI'`|8-bit Windows-1252, the same as `'Windows-1252'`|

A UTF name can end in `-BOM` or `-NOBOM`, as in `'UTF-8-BOM'`. When reading, this makes no difference.

A byte map is a numeric vector of 256 items, one for each byte value from `0` to `255` in order. Each item is the code point of the character that the byte represents, or `¯1` if the byte represents no character. Apart from `¯1`, no code point can appear more than once.

Bytes that are not valid in the file encoding signal `TRANSLATION ERROR`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NGET NGET
</div>
