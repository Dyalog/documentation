---
search:
  boost: 2
---

# <span>Export CSV</span> `{R}←X ⎕CSV Y`{{key}}

Dyadic `⎕CSV` exports Comma Separated Value (CSV) data to a CSV file, or converts data from an internal format to CSV format.

`⎕CSV` output is not affected by [`⎕PP`](pp); numeric values are always represented with full precision.

The left argument `X` is either:

- a matrix or a vector of vectors/matrices containing the data to be converted to CSV format.
- or a 2-element vector containing a matrix or vector of vectors/matrices containing the data to be converted to CSV format, and a vector of character vectors containing the header record.

`Y` is a 1 or 2-element vector containing:

|-----|---------------------------------------|
|`[1]`|Destination of CSV Data (see below)    |
|`[2]`|Description of the CSV data (see below)|

*Destination* - may be one of:

- a character vector or scalar containing a file name
- a native tie number
- an empty character vector, indicating that the CSV data is to be returned in the result `R`

*Description*

If `Y[1]` is a file name or tie number, *Description* may be:

- a character vector specifying the file encoding such as `'UTF-8'` (see [File Encodings](nget-dyadic.md)).
- a 256-element numeric vector that maps each possible byte value (0-255) to a Unicode code point (1st element = Unicode code point corresponding to byte value 0, and so on). ¯1 indicates that the corresponding byte value is not mapped to any character. Apart from ¯1, no value may appear in the table more than once.

If `Y[1]` is empty, *Description* may be a character scalar `'S'` (simple) or `'N'` (nested). If omitted, the default is `'S'`

## MetaCharacters

Some characters in a CSV file are metacharacters that define the structure of the data; for example, the field separator character between fields. Characters that are not metacharacters are literal characters. The variant options QuoteChar, EscapeChar, and DoubleQuote make it possible to interpret metacharacters as literal characters, and thus permit fields to contain field separator characters, leading and trailing spaces, and line-endings.

Fixed-width fields do not require these options and they are ignored if fixed-width fields are being processed.

## Variant Options

Dyadic `⎕CSV` may be applied using the _variant_ operator with the following options.

|Name|Meaning|Default|
|---|---|---|
|Decimal|the decimal mark in numeric fields - one of `'.'` or `','`|`'.'`|
|DoubleQuote|A Boolean which indicates whether (`1`) or not (`0`) a quote character within a quoted field is represented by two consecutive quote characters|`1`|
|EscapeChar|The escape character, which may be specified as an empty character vector (meaning none is defined) or a character scalar|`0`|
|ForceQuotes|A number specifying the degree to which quotes are applied around fields even if not strictly required. Possible values are:<ul><li>`0` – add only if required</li><li>`1` – add to all fields containing character data and to fields containing numeric data if required</li><li>`2` – add to all fields even if not required</li></ul>If ForceQuotes is a scalar, the value applies to all columns; if it is a vector of values then each value applies to the corresponding column.|`0`|
|IfExists|a character vector `'Error'` or `'Replace'` which specifies, when creating a named file which already exists, whether to overwrite it ( `'Replace'` ) or signal an error ( `'Error'` )|`'Error'`|
|LineEnding|the line ending sequence - see [Line separators:](nget-monadic.md)|(13 10) on Windows; 10 on other platforms|
|QuoteChar|The field quote character (delimiter), which may be specified as an empty character vector (meaning none is defined) or a character scalar|`"`|
|Separator|the field separator, any single character. If Widths is other than `⍬` , Separator is ignored.|`','`|
|Thousands|the thousands separator in numeric fields, which can be specified as an empty character vector (meaning no separator is defined) or a character scalar|`''`|
|Trim|a Boolean specifying whether whitespace is trimmed at the beginning and end of character fields|`1`|
|Widths|a vector of numeric values describing the width (in characters) of the corresponding columns in the CSV source, or `⍬` for variable width delimited fields|`⍬`|

The Separator, QuoteChar, and EscapeChar characters, when defined, must be different. Other options defined for import are also accepted but ignored.

The Overwrite variant option (Boolean) from Version 16.0 remains supported but is deprecated in favour of IfExists.

### QuoteChar, EscapeChar, and DoubleQuote options

- The CSV text will be generated such that it can be read back according to the corresponding rules for import.
- If these options do not permit this (for example, a field contains the quote character and neither DoubleQuote or EscapeChar are set) an error is signalled.
- Quoting and Escaping is used as conservatively as possible.
- If both QuoteChar and EscapeChar are set, quoting is favoured.

If `Y` specifies that the CSV data is written to a file then `R` is the number of bytes (not characters) written, and is shy.

Otherwise, `R` is the CSV data in the format specified in Y, and is not shy.

## Internal Format

Arrays that are suitable for exporting as CSV data are represented by 3 possible structures:

- A table (a matrix whose elements are character vectors or scalars, or numbers).
- A vector, each of whose items contain field (column) values. Character field values are character matrices; numeric field values are numeric vectors.
- A vector, each of whose items contain field (column) values. Character field values are vectors of character vectors; numeric field values are numeric vectors.

<h3 class="example">Examples</h3>
```apl
      CSVFile←'c:\Dyalog16.0\sales.csv'
      DATA⍪←'Gizmos' 23
      DATA HDR ⎕CSV''
┌→────────────┐
│Product,Sales│
│             │
│Widgets,1912 │
│             │
│Gimlets,205  │
│             │
│Dingbats,189 │
│             │
│Gizmos,23    │
│             │
│             │
└─────────────┘

       CSVFile1←'c:\Dyalog16.0\sales1.csv'
       ⎕←DATA HDR ⎕CSV CSVFile1
  
67
       DATA⍪←'Gimbals' 123
       ⎕←DATA HDR ⎕CSV CSVFile1
FILE NAME ERROR: Unable to create file ("The file exists.")
       ⎕←DATA HDR ⎕CSV CSVFile1
      ∧
```

![csv_excel1](../img/csv-excel1.png)

## Notes

- When `Y` contains only the destination of the CSV data (that is, omits the description in its second element) it does not have to be enclosed to form a single element vector.
- Native files are written from the current file position. On successful completion, the file position will be at the end of the written data. If an error is signalled the amount of data written is undefined.
- If the file encoding specifies that a BOM is required and output is to a native file, it will only be written if the file position is initially at 0 - that is, the start of the file is being written.
- When fixed width fields are written, character data shorter than the specified width is padded with spaces to the right and character data longer than the specified width signals an error. Numeric data is converted to character data as far as possible so that it fits into the specified width. If this is not possible, an error is signalled.
- Tab-separated fields may be exported by specifying `'Separator' (⎕UCS 9)`.
- Fields containing a single embedded new line are supported. On export, line feed characters are mapped back to the defined line ending sequence.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CSV CSV
</div>
