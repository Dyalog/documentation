---
search:
  boost: 2
---

# <span>Export CSV</span> `{R}←X ⎕CSV Y`{{key}}

This function converts an APL array to comma-separated values (CSV), writing them to a named file or a native file, or returning them as an array of text. [Monadic `⎕CSV`](csv-monadic.md) converts in the other direction. The [internal format](csv.md#internal-format) of the data and the role of [metacharacters](csv.md#metacharacters) are common to both.

<h2 class="example">Example</h2>

```apl
      ['Product' 'Sales'
       'Widgets' 1912   ]⎕CSV''
Product,Sales
Widgets,1912

```

## Left Argument

`X` is one of:

- the data, in one of the [internal formats](csv.md#internal-format)
- a 2-item vector: the data, and a vector of character vectors containing the header row

<h3 class="example">Example</h3>

`data` is a table of sales figures, and `hdr` holds its column labels:

```apl
      data←['Widgets'  1912
            'Gimlets'   205
            'Dingbats'  189]
      hdr←'Product' 'Sales'
      data hdr ⎕CSV''
Product,Sales
Widgets,1912
Gimlets,205
Dingbats,189

```

## Right Argument

`Y` is either the destination of the CSV data on its own, or a vector of up to two items:

|Item |Content                                        |
|-----|-----------------------------------------------|
|`1⊃Y`|[Destination](#destination)                    |
|`2⊃Y`|[Description](#description) of the destination |

The destination does not need to be enclosed when it is the whole of `Y`.

### Destination

The destination is one of:

- a character vector or scalar containing a file name
- a native tie number
- an empty character vector, which returns the CSV data in `R`

<h4 class="example">Example</h4>

`data` and `hdr`, defined under [Left Argument](#left-argument), are written to a new file, which [`⎕NGET`](nget.md) reads back:

```apl
      data hdr ⎕CSV'sales.csv'
      ⊃⎕NGET'sales.csv' 1
┌─────────────┬────────────┬───────────┬────────────┐
│Product,Sales│Widgets,1912│Gimlets,205│Dingbats,189│
└─────────────┴────────────┴───────────┴────────────┘
```

### Description

If the destination is a file name or a tie number, the description is one of:

- a character vector that names the [file encoding](nget.md#Encodings), for example, `'UTF-8'`
- a 256-item numeric vector that maps each byte value, from `0` to `255` in order, to a Unicode code point, with `¯1` for a byte value that is not mapped to any character; apart from `¯1`, no value can appear more than once

If the destination is empty, the description is `'S'` (simple) or `'N'` (nested). The default is `'S'`.

<h4 class="example">Example</h4>

The nested description returns one character vector per record of `data` and `hdr`, defined under [Left Argument](#left-argument):

```apl
      data hdr ⎕CSV'' 'N'
┌─────────────┬────────────┬───────────┬────────────┐
│Product,Sales│Widgets,1912│Gimlets,205│Dingbats,189│
└─────────────┴────────────┴───────────┴────────────┘
```

## Result

If the CSV data is written to a file, `R` is the number of bytes (not characters) written, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

Otherwise, `R` is the CSV data, as a simple character vector or as a vector of character vectors according to the [description](#description), and is not shy.

`⎕CSV` writes numbers with full precision, as if [`⎕PP`](pp.md) were 17, whatever its value. The text differs from APL's own formatting in that a negative number or exponent has `-` rather than `¯`, for example, `-1.5` and `1E-7`.

## Variant Options

Export is controlled by the variant options summarised in [](#variantoptionsforcsv), specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md).

Table: Variant options for exporting with `⎕CSV` { #variantoptionsforcsv }

|Name|Meaning|Default|
|---|---|---|
|`Decimal`|The decimal mark in numeric fields, either `'.'` or `','`|`'.'`|
|`DoubleQuote`|A Boolean that says whether (`1`) or not (`0`) a quote character within a quoted field is written as [two consecutive quote characters](#variant-option-doublequote)|`1`|
|`EscapeChar`|The [escape character](#variant-option-escapechar): a character scalar, or an empty character vector, meaning that none is defined|`''`|
|`ForceQuotes`|The degree to which fields are quoted when quotes are not required:<ul><li>`0`: only when required</li><li>`1`: all fields that contain character data, and fields that contain numeric data when required</li><li>`2`: all fields</li></ul>A scalar applies to all fields; a vector gives a value for each field.|`0`|
|`IfExists`|What happens when the named file [already exists](#variant-option-ifexists): `'Error'` signals an error and `'Replace'` overwrites the file|`'Error'`|
|`LineEnding`|The [line-ending sequence](nget.md#Line_Separators)|`13 10` on Microsoft Windows, `10` on other platforms|
|`QuoteChar`|The [field quote character](#variant-option-quotechar): a character scalar, or an empty character vector, meaning that none is defined|`"`|
|`Separator`|The field separator, any single character; ignored if `Widths` is not `⍬`|`','`|
|`Thousands`|The thousands separator in numeric fields: a character scalar, or an empty character vector, meaning that none is defined|`''`|
|`Trim`|A Boolean that says whether whitespace is trimmed at the beginning and end of character fields|`1`|
|`Widths`|The width, in characters, of each field for [fixed-width fields](#variant-option-widths), or `⍬` for fields that are delimited by the separator|`⍬`|

The `Separator`, `QuoteChar`, and `EscapeChar` characters, when defined, must be different. Tab-separated fields can be exported by setting `Separator` to `⎕UCS 9`.

The [variant options for import](csv-monadic.md#variantoptionsforcsv) are also accepted, but ignored.

!!! Legacy "Legacy"
    The Boolean `Overwrite` variant option is retained for backwards compatibility purposes. `IfExists` supersedes it.

Export generates CSV data that import can read back with the same variant options. If the options cannot achieve that, an error is signalled.

### Variant Option: `QuoteChar`

If `QuoteChar` is set, then a field that contains a metacharacter is delimited by the quote character. Fields are quoted only when required, unless `ForceQuotes` says otherwise. A field can contain a line feed character, which is written as the line-ending sequence that `LineEnding` specifies.

<h4 class="example">Example</h4>

```apl
      ['a,b' 1 ⋄]⎕CSV''
"a,b",1

```

### Variant Option: `EscapeChar`

If `EscapeChar` is set, then a metacharacter in a field can be written with the escape character before it. If `QuoteChar` is also set, quoting is preferred to escaping.

<h4 class="example">Example</h4>

With no quote character, the separator in the first field is escaped:

```apl
      ['a,b' 1 ⋄](⎕CSV⍠('QuoteChar' '')('EscapeChar' '\'))''
a\,b,1

```

### Variant Option: `DoubleQuote`

If `DoubleQuote` is `1`, then a [quote character](#variant-option-quotechar) within a quoted field is written as two consecutive quote characters. If `DoubleQuote` is `0`, a quote character in a field must be [escaped](#variant-option-escapechar) instead, and if no escape character is defined, an error is signalled.

<h4 class="example">Examples</h4>

```apl
      ['a"b' 1 ⋄]⎕CSV''
"a""b",1

      ['a"b' 1 ⋄](⎕CSV⍠('DoubleQuote' 0)('EscapeChar' '\'))''
"a\"b",1

```

### Variant Option: `IfExists`

If the named file already exists, `IfExists` chooses whether `⎕CSV` signals `FILE NAME ERROR` (`'Error'`) or replaces the file (`'Replace'`).

<h4 class="example">Example</h4>

`data` gains a further record, and replaces `sales.csv`, which was created under [Destination](#destination) from `data` and `hdr`:

```apl
      data⍪←'Gizmos' 23
      data hdr(⎕CSV⍠'IfExists' 'Replace')'sales.csv'
      ⊃⎕NGET'sales.csv' 1
┌─────────────┬────────────┬───────────┬────────────┬─────────┐
│Product,Sales│Widgets,1912│Gimlets,205│Dingbats,189│Gizmos,23│
└─────────────┴────────────┴───────────┴────────────┴─────────┘
```

### Variant Option: `Widths`

With fixed-width fields, a character field that is shorter than its width is padded with spaces on the right, and one that is longer signals an error. A number is converted to as many characters as fit in its width, and if it cannot be made to fit, an error is signalled.

<h4 class="example">Example</h4>

`1234` is shortened to fit in three characters:

```apl
      ['ab' 1234 ⋄](⎕CSV⍠'Widths'(4 3))''
ab  1E3

```

## File Handling

A native file is written from its current file position. When `⎕CSV` completes, the file position is at the end of the data written. If an error is signalled, the amount of data written is undefined.

If the file encoding calls for a byte order mark (BOM), it is written to a native file only if the file position is initially `0`, that is, when writing starts at the beginning of the file.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CSV CSV
</div>
