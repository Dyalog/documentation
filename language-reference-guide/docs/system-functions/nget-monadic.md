---
search:
  boost: 2
---

# <span>Get Text File Content</span> `R←⎕NGET Y`{{key}}

This function reads the contents of the specified text file. See also [Write Text File](nput.md).

`Y` is either a character vector/scalar containing the name of the file to be read, or a 2-item vector whose first item is the file name and whose second is an integer scalar specifying `flags` for the operation.

- if `flags` is `0` then `R[1]` is a character vector. This is the default.
- if `flags` is `1` then `R[1]` is a nested array of character vectors.
- if `flags` is `2` then `R[1]` is a matrix, with each row corresponding to a line in the text file specified within `Y`.

If the start of the file contains a recognised Byte Order Mark (BOM), the file is decoded according to the BOM. Otherwise, the file is examined to try to decide its encoding and is decoded accordingly. Use [dyadic `⎕NGET`](nget-dyadic.md) to specify the encoding manually.

The result `R` is a 3-element vector comprising `(content) (encoding) (newline)`  where:

|---|---|
|`content`|A simple character vector, or a vector of character vectors, according to the value of `flags` .|
|`encoding`|The encoding that was actually used to read the file. If this is a UTF format, it will always include the appropriate endianness (except for UTF-8 to which endianness doesn't apply) and a -BOM or -NOBOM suffix to indicate whether or not a BOM is actually present in the file. For example, UTF-16LE-BOM.|
|`newline`|Determined by the first occurrence in the file of one of the newline characters identified in the line separator table, or `⍬` if no such line separator is found.|

If `content` is simple then all its line separators (listed in the table below) are replaced by (normalised to) `⎕UCS 10`, which in the Classic Edition must be in `⎕AVU` (else `TRANSLATION ERROR`).

If `content` is nested, it is formed by splitting the contents of the file on the occurrence of any of the line separators  shown in the table below. These line separators are  removed.

The 3rd element of the result `newline` is a numeric vector from the *Value* column of the table below corresponding to the first occurrence of any of the **newline characters** in the file. If none of these characters are present, the value is `⍬`.

Table: Line separators: {: #Line_Separators }

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

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NGET NGET
</div>
