---
search:
  boost: 2
---

# <span>Import CSV</span> `R←⎕CSV Y`{{key}}

This function converts comma-separated values (CSV) to an APL array, reading them from a named file, a native file, or an array of text. [Dyadic `⎕CSV`](csv-dyadic.md) converts in the other direction. The [internal format](csv.md#internal-format) of the result and the role of [metacharacters](csv.md#metacharacters) are common to both.

<h2 class="example">Example</h2>

```apl
      ⎕CSV⊂'Product,Sales' 'Widgets,1912'
┌───────┬─────┐
│Product│Sales│
├───────┼─────┤
│Widgets│1912 │
└───────┴─────┘
```

## Right Argument

`Y` is either the source of the CSV data on its own, or a vector of up to four items:

|Item |Content                                        |
|-----|-----------------------------------------------|
|`1⊃Y`|[Source](#source)                              |
|`2⊃Y`|[Description](#description) of the source      |
|`3⊃Y`|[Column types](#column-types)                  |
|`4⊃Y`|[Header row indicator](#header-row-indicator)  |

A file name or a tie number does not need to be enclosed when it is the whole of `Y`. A vector of character vectors does, because otherwise its items are taken as the items of `Y`.

### Source

The source is one of:

- a character vector or scalar containing a file name
- a native tie number
- a character vector or scalar containing CSV data with embedded line endings, in which case the description must be `'S'` so that the data is not taken as a file name
- a vector of character vectors or scalars containing CSV data, each of which is a record

<h4 class="example">Example</h4>

[`⎕NPUT`](nput.md) writes a file, which `⎕CSV` then reads by name:

```apl
      (⊂'Product,Sales' 'Widgets,1912' 'Gimlets,205' 'Dingbats,189')⎕NPUT'sales.csv'
      ⎕CSV'sales.csv'
┌────────┬─────┐
│Product │Sales│
├────────┼─────┤
│Widgets │1912 │
├────────┼─────┤
│Gimlets │205  │
├────────┼─────┤
│Dingbats│189  │
└────────┴─────┘
```

### Description

If the source is a file name or a tie number, the description is one of:

- a character vector that names the [file encoding](nget.md#Encodings), for example, `'UTF-8'`
- a 256-item numeric vector that maps each byte value, from `0` to `255` in order, to a Unicode code point, with `¯1` for a byte value that is not mapped to any character; apart from `¯1`, no value can appear more than once

If the description is omitted or empty, the file encoding is deduced as described in [File Handling](#file-handling).

If the source is CSV data, the description is `'S'` (simple) or `'N'` (nested). The default is `'N'`.

### Column Types

The column types are a numeric scalar or vector of the codes in the table below, one per field. A scalar applies to every field. If the column types are omitted or `⍬`, every field contains character data: a field that contains only numbers is converted to numbers only if its column type says so.

|Code|The field                                                                                                                                      |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------|
|`0` |is ignored                                                                                                                                     |
|`1` |contains character data                                                                                                                        |
|`2` |contains numbers; a field that is empty or cannot be converted to a number signals an error                                                    |
|`3` |contains numbers; a field that is empty or cannot be converted to a number is replaced with the value of the `Fill` variant option             |
|`4` |contains numbers; a field that is empty or cannot be converted to a number is returned as character data, so this code is not permitted when the `Invert` variant option is `1`|
|`5` |contains numbers; an empty field is replaced with the value of the `Fill` variant option, and a field that cannot be converted to a number signals an error|

<h4 class="example">Example</h4>

The sales figures in `sales.csv`, written under [Source](#source), are numbers only when their column type says so, and can then be summed:

```apl
      data hdr←⎕CSV'sales.csv' '' (1 2) 1
      +/data[;2]
2306
```

### Header Row Indicator

The header row indicator is a Boolean that says whether the first record is a header row of column labels. The default is `0`. If it is `1`, the header row is read as character data, regardless of the column types, and is returned separately in the result.

<h4 class="example">Example</h4>

`sales.csv`, written under [Source](#source), starts with a header row:

```apl
      ⎕CSV'sales.csv' '' ⍬ 1
┌───────────────┬───────────────┐
│┌────────┬────┐│┌───────┬─────┐│
││Widgets │1912│││Product│Sales││
│├────────┼────┤│└───────┴─────┘│
││Gimlets │205 ││               │
│├────────┼────┤│               │
││Dingbats│189 ││               │
│└────────┴────┘│               │
└───────────────┴───────────────┘
```

## Result

`R` is the imported data, in the [internal format](csv.md#internal-format) chosen by the [`Invert`](#variant-option-invert) variant option.

If the [header row indicator](#header-row-indicator) is `1`, `R` is instead a 2-item vector:

|Item |Content                                                |
|-----|-------------------------------------------------------|
|`1⊃R`|The imported data, without the header row              |
|`2⊃R`|A vector of character vectors containing the header row|

## Variant Options

Import is controlled by the variant options summarised in [](#variantoptionsforcsv), specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md). The principal option is `Invert`.

Table: Variant options for importing with `⎕CSV` { #variantoptionsforcsv }

|Name       |Meaning                                     |Default|
|-----------|--------------------------------------------|-------|
|`Decimal`    |The decimal mark in numeric fields, either `'.'` or `','` |`'.'`|
|`DoubleQuote`|A Boolean that says whether (`1`) or not (`0`) [two consecutive quote characters](#variant-option-doublequote) within a quoted field represent a quote character|`1`    |
|`EscapeChar` |The [escape character](#variant-option-escapechar): a character scalar, or an empty character vector, meaning that none is defined|`''`   |
|`Fill`       |The number that replaces an empty field of [column type](#column-types) `3` or `5`, or a non-numeric field of column type `3`|`0`    |
|`Invert`<br><small>principal</small>|The [internal format](#variant-option-invert) of the result: `0`, `1`, or `2`|`0`    |
|`QuoteChar`  |The [field quote character](#variant-option-quotechar): a character scalar, or an empty character vector, meaning that none is defined|`"`    |
|`Ragged`     |A Boolean that says whether records can have [varying numbers of fields](#variant-option-ragged)|`0`    |
|`Records`    |The maximum number of records to process, or `0` for no limit|`0`    |
|`Separator`  |The field separator, any single character; ignored if `Widths` is not `⍬`|`','`  |
|`Thousands`  |The thousands separator in numeric fields: a character scalar, or an empty character vector, meaning that none is defined|`''`   |
|`Trim`       |A Boolean that says whether whitespace that is neither quoted nor escaped is trimmed at the beginning and end of fields|`1`    |
|`Widths`     |The width, in characters, of each field for fixed-width fields, or `⍬` for fields that are delimited by the separator|`⍬`    |

The `Separator`, `QuoteChar`, and `EscapeChar` characters, when defined, must be different. Tab-separated fields can be imported by setting `Separator` to `⎕UCS 9`.

The [variant options for export](csv-dyadic.md#variantoptionsforcsv) are also accepted, but ignored.

### Variant Option: `Invert`

`Invert` chooses which [internal format](csv.md#internal-format) the result has:

- `0`: a table
- `1`: a vector of fields, with character fields as character matrices
- `2`: a vector of fields, with character fields as vectors of character vectors

<h4 class="example">Examples</h4>

The sales figures in `sales.csv`, written under [Source](#source), become a single numeric vector:

```apl
      (⎕CSV⍠'Invert' 1)'sales.csv' '' (1 2) 1
┌───────────────────────┬───────────────┐
│┌────────┬────────────┐│┌───────┬─────┐│
││Widgets │1912 205 189│││Product│Sales││
││Gimlets │            ││└───────┴─────┘│
││Dingbats│            ││               │
│└────────┴────────────┘│               │
└───────────────────────┴───────────────┘
      (⎕CSV⍠'Invert' 2)'sales.csv' '' (1 2) 1
┌─────────────────────────────────────────┬───────────────┐
│┌──────────────────────────┬────────────┐│┌───────┬─────┐│
││┌───────┬───────┬────────┐│1912 205 189│││Product│Sales││
│││Widgets│Gimlets│Dingbats││            ││└───────┴─────┘│
││└───────┴───────┴────────┘│            ││               │
│└──────────────────────────┴────────────┘│               │
└─────────────────────────────────────────┴───────────────┘
```

### Variant Option: `QuoteChar`

If `QuoteChar` is set, then fields can be delimited by the quote character. Within a quoted field, all characters except the quote character, and the [escape character](#variant-option-escapechar) if it is defined, are literal characters. A quoted field can therefore contain separators and line endings. Import converts each line ending in a field to a single line feed character.

<h4 class="example">Example</h4>

```apl
      ⎕CSV⊂'"a,b",c' 'd,e'
┌───┬─┐
│a,b│c│
├───┼─┤
│d  │e│
└───┴─┘
```

### Variant Option: `EscapeChar`

If `EscapeChar` is set, then any character can be prefixed by the escape character, which is typically `'\'`. The escape character followed by a character `c` is the literal character `c`, even if `c` on its own is a metacharacter.

<h4 class="example">Example</h4>

```apl
      (⎕CSV⍠'EscapeChar' '\')⊂'a\,b,c' 'd,e'
┌───┬─┐
│a,b│c│
├───┼─┤
│d  │e│
└───┴─┘
```

### Variant Option: `DoubleQuote`

If `DoubleQuote` is `1`, then two consecutive [quote characters](#variant-option-quotechar) within a quoted field are the literal quote character.

<h4 class="example">Example</h4>

```apl
      ⎕CSV⊂'"e""f",g' 'h,i'
┌───┬─┐
│e"f│g│
├───┼─┤
│h  │i│
└───┴─┘
```

### Variant Option: `Ragged`

If `Ragged` is `0`, every record must have the same number of fields, or, for fixed-width fields, the same number of characters.

If `Ragged` is `1`, the expected number of fields is given by the `Widths` variant option, by the column types, or by both, and each record is made to fit:

- a record of delimited fields is extended with empty fields, or truncated, to the expected number of fields
- a record of fixed-width fields is extended with spaces, or truncated, to the total width that `Widths` specifies

<h4 class="example">Example</h4>

The second record is extended and the third is truncated:

```apl
      (⎕CSV⍠'Ragged' 1)('a,b,c' '1' '2,3,4,5')'N'(1 1 1)
┌─┬─┬─┐
│a│b│c│
├─┼─┼─┤
│1│ │ │
├─┼─┼─┤
│2│3│4│
└─┴─┴─┘
```

## File Handling

Data can be read from a named file or a tied native file. A tied native file can be read in sections by calling `⎕CSV` repeatedly, with the `Records` variant option limiting the number of records that each call reads, until no more data is read.

The file must contain text in one of the supported [file encodings](nget.md#Encodings). The file encoding is determined as follows:

1. If the file starts with a byte order mark (BOM), the BOM determines the encoding, regardless of the description. A BOM is found only when the file is read from its start, so when a native file is read in sections, only the first section can find it.
2. Otherwise, if the description specifies a file encoding, that encoding is used.
3. Otherwise, a native file is decoded as UTF-8, and a named file is examined to deduce its likely encoding, using the same method as [`⎕NGET`](nget.md).

A native file is read from its current file position. When `⎕CSV` completes, the file position is at the first character that was not processed, which is the end of the file unless the `Records` variant option limited the number of records read. If an error is signalled, the file position is undefined.

Unlike `⎕NGET`, `⎕CSV` does not report the file encoding or the line-ending type of the file.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CSV CSV
</div>
