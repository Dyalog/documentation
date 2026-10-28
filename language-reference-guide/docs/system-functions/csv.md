---
search:
  exclude: true
---

# <span>Comma Separated Values</span> `⎕CSV`

`⎕CSV` converts between comma-separated values (CSV) and APL arrays, reading from or writing to a named file, a native file, or an array of text. It imports when called monadically, and exports when called dyadically.

## Import CSV

[Monadic `⎕CSV`](csv-monadic.md) converts CSV data to an APL array:

```apl
      ⎕CSV⊂'Product,Sales' 'Widgets,1912'
┌───────┬─────┐
│Product│Sales│
├───────┼─────┤
│Widgets│1912 │
└───────┴─────┘
```

## Export CSV

[Dyadic `⎕CSV`](csv-dyadic.md) converts an APL array to CSV data:

```apl
      ['Product' 'Sales'
       'Widgets' 1912   ]⎕CSV''
Product,Sales
Widgets,1912

```

## Internal Format

An APL array that holds CSV data, whether returned by import or given to export, has one of three structures:

- a table: a matrix whose items are character vectors or scalars, or numbers
- a vector with one item per field (column), in which a character field is a character matrix and a numeric field is a numeric vector
- a vector with one item per field, in which a character field is a vector of character vectors and a numeric field is a numeric vector

The [`Invert`](csv-monadic.md#variant-option-invert) variant option chooses the structure that import returns.

## Metacharacters

Some characters in CSV data are _metacharacters_, which define its structure, for example, the field separator between fields. All other characters are literal characters. The [`QuoteChar`](csv-monadic.md#variant-option-quotechar), [`EscapeChar`](csv-monadic.md#variant-option-escapechar), and [`DoubleQuote`](csv-monadic.md#variant-option-doublequote) variant options make it possible to interpret metacharacters as literal characters, so that fields can contain field separators, leading and trailing spaces, and line endings. Export applies the [same options](csv-dyadic.md#variant-option-quotechar) when it writes such fields.

Fixed-width fields do not need these options, which are ignored when fixed-width fields are processed.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CSV CSV
</div>
