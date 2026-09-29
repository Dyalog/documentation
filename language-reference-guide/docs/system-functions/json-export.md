---
search:
  boost: 2
---

# <span>Export JSON</span> `R←{1} ⎕JSON Y`{{key}}

This function converts APL data to a JSON document. To convert a JSON document to APL data instead, see [Import JSON](json-import.md).

<h2 class="example">Example</h2>

```apl
      1 ⎕JSON 1 ¯2 3
[1,-2,3]
```

## Right Argument

`Y` is the data to be exported. By default, `Y` must be APL data that can be represented as JSON (subject to the [`HighRank`](#variant-option-highrank) variant option). If the [`Format`](#variant-option-format) variant option is set to `'M'`, `Y` must instead be a matrix representation such as would have been produced by importing JSON with `Format` being `'M'`. `⎕JSON` signals `DOMAIN ERROR` if `Y` is incompatible with the specified (or implied) value of `Format`.

`Y` can contain [wrappers](#wrappers) that give special handling to arrays JSON cannot represent directly.

## Left Argument

The left argument `1` can be omitted when `Y` is not a simple character array, which is what identifies the call as an export, but Dyalog Ltd recommends specifying the left argument to avoid code that seemingly works, only to fail on specific values.

## Result

`R` is a simple character vector containing the JSON document corresponding to `Y`. Its content depends on the [`Compact`](#variant-option-compact), [`Dialect`](#variant-option-dialect), and [`Charset`](#variant-option-charset) variant options.

`⎕JSON` output is not affected by [`⎕PP`](pp.md); numbers are always represented with full precision.

Some JSON values lack a direct APL equivalent (<code class="language-nonAPL">true</code>, <code class="language-nonAPL">false</code>, <code class="language-nonAPL">null</code>, JavaScript fragments), and some APL representations of datasets do not correspond to common JSON practice. Such cases are handled by [wrappers](#wrappers).

## Limitations

JSON supports a limited number of data types, and there is no direct correspondence between JSON and APL data structures. In particular:

- JSON does not support arrays with rank &gt; 1.
- JSON does not support nested scalars.
- JSON includes Boolean values <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> which are distinct from numeric values <code class="language-nonAPL">1</code> and <code class="language-nonAPL">0</code>; these have no direct APL equivalent.
- JSON object members are named and these names might not be [valid names in APL](../../programming-reference-guide/introduction/names.md).
- The [JSON5](https://json5.org/) dialect includes numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, which have no direct APL equivalent.

These differences are catered for in various ways as discussed below.

## Name Mangling

When `⎕JSON` converts APL data to a JSON document, a namespace member whose name begins with `⍙` is assumed to carry a name that [import](json-import.md#name-mangling) mangled, and the mangling is reversed: the leading `⍙` is dropped and each `⍙NNN⍙` group is replaced by the character with [decimal Unicode code point](ucs.md#monadic-ucs) `NNN`.

<h3 class="example">Example</h3>

The member named `⍙2a` is exported under its original name `2a`, which is not a valid APL name:

```apl
      1 ⎕JSON (a:1 ⋄ ⍙2a:2)
{"a":1,"2a":2}
```

<h3 class="example">Example</h3>

`⍙253⍙` is restored to `ý` (`⎕UCS 253`):

```apl
      1 ⎕JSON (⍙s⍙253⍙n:'vision')
{"sýn":"vision"}
```

A name is only un-mangled when doing so yields a name that is not valid in APL, because only such names are mangled in the first place. Any other name is exported as it stands, so a member name that genuinely begins with `⍙` survives:

```apl
      1 ⎕JSON (⍙abc:1)
{"⍙abc":1}
```

### Name Mangling Algorithm

[`7162⌶`](../primitive-operators/i-beam/json-translate-name.md) provides direct access to the name mangling algorithm.

<h3 class="example">Example</h3>

The above name translations are verified using `7162⌶`:

```apl
      1(7162⌶)'⍙2a' '⍙s⍙253⍙n' '⍙abc'
┌──┬───┬────┐
│2a│sýn│⍙abc│
└──┴───┴────┘
      0(7162⌶)'2a' 'sýn' '⍙abc'
┌───┬────────┬──────────┐
│⍙2a│⍙s⍙253⍙n│⍙⍙9049⍙abc│
└───┴────────┴──────────┘
```

## Variant Options

`⎕JSON` supports six variant options, `Format`, `Dialect`, `Null`, `Compact`, `Charset`, and `HighRank`, specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md), summarised in [](#variantoptionsforjson), and described in detail beneath it. The principal option is `Format`.

Table: Variant options for `⎕JSON` { #variantoptionsforjson }

| Variant Option | Value | Effect |
|---|:---:|---|
| [`Format`](#variant-option-format)<br><small>principal</small> | `'D'`<br><small>(default)</small> | `Y` is APL data |
|_-  -_| `'M'` | `Y` is a 4-column APL matrix as from import with `'M'` |
| [`Dialect`](#variant-option-dialect) | `'JSON'`<br><small>(default)</small> | Only strict JSON syntax is produced |
|_-  -_| `'JSON5'` | JSON5 features are used to improve readability and editability, and/or shorten output |
| [`Null`](#variant-option-null) | `⊂'null'`<br><small>(default)</small> | APL `⊂'null'` becomes JSON <code class="language-nonAPL">null</code> |
|_-  -_| `⎕NULL` | APL `⎕NULL` becomes JSON <code class="language-nonAPL">null</code> |
| [`Compact`](#variant-option-compact) | `1`<br><small>(default)</small> | `R` has no whitespace outside quotes |
|_-  -_| `0` | `R` has whitespace for readability and, if `Dialect` is `'JSON5'`, trailing commas after final elements and members |
| [`Charset`](#variant-option-charset) | `'Unicode'`<br><small>(default)</small> | Unicode characters in `Y` are used when JSON standard allows |
|_-  -_| `'ASCII'` | Non-ASCII characters are converted to the hexadecimal form `\uNNNN`, and if `Dialect` is `'JSON5'`, also `\xNN` |
| [`HighRank`](#variant-option-highrank) | `'Error'`<br><small>(default)</small> | High-rank arrays are rejected |
|_-  -_| `'Split'` | High-rank arrays are split and [inverted table wrappers](#dataset-wrappers) accept text columns as matrices |

### Variant Option: `Format`

The `Format` variant option, the principal option, determines whether `⎕JSON` works with a direct APL representation of the data (`'D'` for "Data", the default) or with a four-column matrix that encodes the JSON structure (`'M'` for "Matrix") as nodes with depth, name, value, and type.

#### Export from Data

If `Format` is `'D'` (which stands for "Data"), the APL value `Y` is converted to a corresponding JSON document `R` as follows:

- APL vectors are converted to JSON arrays.
- APL arrays of higher rank are recursively split if [`HighRank`](#variant-option-highrank) is `'Split'`, otherwise `⎕JSON` signals `DOMAIN ERROR`.
- APL namespaces are converted to JSON objects.
- Enclosed vectors whose leading element is a wrapper code are interpreted as [wrappers](#wrappers) (mechanisms for special handling).
- If a namespace member name appears to be mangled (has a form that would have been produced by [name mangling](#name-mangling)), it is demangled.

<h5 class="example">Example</h5>

```apl
      ns←(
          a:(
              b:(
                  'charvec 1'
                  'charvec 2'
              )
              c:⊂'true'
              d:(
                  e:⊂'false'
                  ⍙f⍙9082⍙:(
                      'charvec 3'
                      123
                      1000.2
                      ⊂'null'
                  )
              )
          )
      )
      1 ⎕JSON ns
{"a":{"b":["charvec 1","charvec 2"],"c":true,"d":{"e":false,"f⍺":["charvec 3",123,1000.2,null]}}}
```

#### Export from Matrix

If `Format` is `'M'` (which stands for "Matrix"), the APL array `Y` is converted to a corresponding JSON document `R` and `Y` must be a matrix whose columns are as follows:

Table: Export matrix columns { #export-matrix-table }

| Column  | Contents                        |
|---------|---------------------------------|
| `Y[;1]` | Depth                           |
| `Y[;2]` | Name (for JSON object members)  |
| `Y[;3]` | APL value                       |
| `Y[;4]` | [JSON type](#export-types-table) |

The JSON types are as follows:

Table: JSON types { #export-types-table }

| `Y[;4]` | `Y[;3]` (APL value)       | Corresponding JSON value |
|---------|---------------------------|--------------------------|
| `1`     | Empty array               | Object                   |
| `2`     | Empty array               | Array                    |
| `3`     | Numeric scalar            | Number                   |
| `4`     | Character vector          | String                   |
| `5`     | Null                      | Null                     |
| `6`     | Enclosed character vector | Lacking APL equivalent   |
| `7`     | Enclosed character vector | [Raw text](#raw-text-wrapper) |

The difference between JSON types `6` and `7` is that `7` allows any text but `6` only allows the special values that can be imported.

If there are any mismatches between the values in `Y[;3]` and the types in `Y[;4]`, `⎕JSON` signals `DOMAIN ERROR` and reports the first row where there is a mismatch (`⎕IO` sensitive) as illustrated in the following example.

<h5 class="example">Example</h5>

```apl
      m←0(⎕JSON⍠'M')'{"values": [ 75, 300 ]}'
      m
┌─┬──────┬───┬─┐
│0│      │   │1│
├─┼──────┼───┼─┤
│1│values│   │2│
├─┼──────┼───┼─┤
│2│      │75 │3│
├─┼──────┼───┼─┤
│2│      │300│3│
└─┴──────┴───┴─┘
```

To illustrate type mismatches, the above matrix is modified by replacing one number with a character vector that looks the same:

```apl
      m[3;3]←⊂'75'
      m
┌─┬──────┬───┬─┐
│0│      │   │1│
├─┼──────┼───┼─┤
│1│values│   │2│
├─┼──────┼───┼─┤
│2│      │75 │3│
├─┼──────┼───┼─┤
│2│      │300│3│
└─┴──────┴───┴─┘
      1(⎕JSON⍠'M')m
DOMAIN ERROR: JSON export: value does not match the specified type in row 3 (⎕IO=1)
      1(⎕JSON⍠'M')m
      ∧
```

### Variant Option: `Dialect`

The `Dialect` variant option selects which syntax is produced, and must be either `'JSON'` or `'JSON5'`. With `'JSON5'`, the result is shortened by usage of identifiers without quotes, single quotes (`'`), and character escapes `\v` and of the form `\xNN` (for values less than hexadecimal 100, that is, `⎕UCS 256`). If [`Compact`](#variant-option-compact) is `0`, a trailing comma (`,`) is added after the last array element and object member. The default is `'JSON'`.

<h4 class="example">Examples</h4>

```apl
      1 ⎕JSON(a:'é"')
{"a":"é\""}
      1(⎕JSON⍠'Dialect' 'JSON5')(a:'é"')
{a:'é"'}

      1(⎕JSON⍠'Charset' 'ASCII'⍠'Compact' 0)(a:'é"')
{
  "a": "\u00E9\""
}
      1(⎕JSON⍠'Charset' 'ASCII'⍠'Compact' 0⍠'Dialect' 'JSON5')(a:'é"')
{
  a: '\xE9"',
}
```

### Variant Option: `Null`

The `Null` variant option selects which APL representation of JSON <code class="language-nonAPL">null</code> is exported as <code class="language-nonAPL">null</code>, and must be either `⊂'null'` (the default) or `⎕NULL`:

- If `Null` is `⊂'null'`, `⎕NULL` causes `DOMAIN ERROR`.
- If `Null` is `⎕NULL`, `⊂'null'` is still exported as <code class="language-nonAPL">null</code> because it is interpreted as [raw text](#raw-text-wrapper).

<h4 class="example">Examples</h4>

```apl
      1 ⎕JSON ⎕NULL ⎕NULL
DOMAIN ERROR: JSON export: item "[1]" of the right argument (⎕IO=1) cannot be converted
      1 ⎕JSON ⎕NULL ⎕NULL
        ∧
      1(⎕JSON⍠'Null'⎕NULL)⎕NULL ⎕NULL
[null,null]
```

### Variant Option: `Compact`

The `Compact` variant option can be used to generate JSON that is either dense (`1`, the default) or optimised for humans to read and edit (`0`).

If `Compact` is `0`:

- Line breaks are inserted after opening brackets `[` and `{` and before closing brackets `]` and `}`
- Each array element and object member is on its own line, indented with two spaces relative to its container array or object
- A space is inserted after `:` separating member name and value
- If [`Dialect`](#variant-option-dialect) is `'JSON5'`, a trailing comma (`,`) is added after the last array element and object member

<h4 class="example">Example</h4>

The following examples use this namespace as APL data:

```apl
      ns←(
          a:(
              b:(
                  'charvec 1'
                  'charvec 2'
              )
              c:⊂'true'
              d:(
                  e:⊂'false'
                  ⍙f⍙9082⍙:(
                      'charvec 3'
                      123
                      1000.2
                      ⊂'null'
                  )
              )
          )
      )
```

Conversion to compact JSON:

```apl
      ⍴json←1 ⎕JSON ns
97
      json
{"a":{"b":["charvec 1","charvec 2"],"c":true,"d":{"e":false,"f⍺":["charvec 3",123,1000.2,null]}}}
```

Non-compact JSON takes more than twice as much space, but is more readable, and easier for humans to edit:

```apl
      ⍴json←1(⎕JSON⍠'Compact' 0)ns
208
      1(⎕JSON⍠'Compact' 0)ns
{
  "a": {
    "b": [
      "charvec 1",
      "charvec 2"
    ],
    "c": true,
    "d": {
      "e": false,
      "f⍺": [
        "charvec 3",
        123,
        1000.2,
        null
      ]
    }
  }
}
```

### Variant Option: `Charset`

The `Charset` variant option can be used to either allow Unicode in the generated JSON (`'Unicode'`, the default) or restrict the output to ASCII characters (`'ASCII'`). When necessary, characters are converted to the hexadecimal form `\uNNNN`. If [`Dialect`](#variant-option-dialect) is `'JSON5'`, the form `\xNN` is used for values up to hexadecimal `FF` (`⎕UCS 255`).

<h4 class="example">Example</h4>

```apl
      ns←(dé:'DÉ')
      ns.dé
DÉ
      1 ⎕JSON ns
{"dé":"DÉ"}
      1(⎕JSON⍠'Charset' 'ASCII')ns
{"d\u00E9":"D\u00C9"}
```

### Variant Option: `HighRank`

The `HighRank` variant option selects how arrays in `Y` of rank higher than 1 are treated, and must be either `'Error'` or `'Split'`. With `'Error'`, `⎕JSON` signals a `DOMAIN ERROR` upon encountering one. With `'Split'`, `⎕JSON` recursively splits any such arrays as necessary; in addition, [datasets](#dataset-wrappers) as inverted tables can have text columns represented as matrices. The default is `'Error'`.

<h4 class="example">Example</h4>

```apl
      d←[[1 2 ⋄ 'AB']['ABC' ⋄ 'DEF']
         (2 3⍴⍳6)    (2 2 2⍴×⍨⍳8)   ]
      d
┌─────┬─────┐
│1 2  │ABC  │
│A B  │DEF  │
├─────┼─────┤
│1 2 3│ 1  4│
│4 5 6│ 9 16│
│     │     │
│     │25 36│
│     │49 64│
└─────┴─────┘

      1 ⎕JSON d
DOMAIN ERROR: JSON export: the right argument cannot be converted (⎕IO=1)
      1 ⎕JSON d
      ∧
      1(⎕JSON⍠'HighRank' 'Split')d
[[[[1,2],"AB"],["ABC","DEF"]],[[[1,2,3],[4,5,6]],[[[1,4],[9,16]],[[25,36],[49,64]]]]]
```

## Wrappers

A wrapper is an enclosed vector with the basic form `⊂wrapperCode wrapperData`. The `wrapperCode` can be omitted, and index vectors can be appended for data subsetting.

Some APL representations of datasets do not correspond to common JSON practice for datasets. A wrapper provides special handling if such an APL representation is encountered inside a nested scalar; nested were selected for this purpose because they cannot be represented in JSON or JavaScript.

A wrapper can be given directly as the right argument to `⎕JSON` or as part of the right argument's data structure (as a sub-array or in a sub-namespace). This allows a special array to be processed appropriately as part of a general data structure that is to be rendered as JSON.

The structure of the special array is specified within the wrapper by a leading numeric code. Code `1` (the default) allows insertion of raw text, including JSON values such as <code class="language-nonAPL">null</code> and <code class="language-nonAPL">true</code>. Codes `2`, `3`, and `4` identify various representations of a *dataset*. The term *dataset* is used here to mean a collection of data, usually presented in tabular form. Each named column (also called a *field*) represents a particular variable. Each row (also called a *record*) corresponds to a given member of the dataset in question, listing its value for each of the variables, such as price and quantity of an item.

In APL, a dataset is traditionally represented as a collection of variables:

```apl
      fields←'item' 'price' 'qty'
      item←'Knife' 'Fork' 'Spoon'
      price←3 4 5
      qty←23 45 67
```

However, when a single array is needed, it is commonly represented as either a single mixed-type matrix that includes headers, a mixed-type matrix of values with a separate header vector, or an inverted table of values with a separate header vector.

In JSON, a dataset is almost universally represented as an *array of objects* (JavaScript nomenclature for APL's *vector of namespaces*):

```json
[
  {
    "item": "Knife",
    "price": 3,
    "qty": 23
  },
  {
    "item": "Fork",
    "price": 4,
    "qty": 45
  },
  {
    "item": "Spoon",
    "price": 5,
    "qty": 67
  }
]
```

The JSON structure can be represented in APL as:

```apl
      ⎕←fields{()⎕VSET(↑⍺)⍵}⍤1⍉↑item price qty
 #.[Namespace]  #.[Namespace]  #.[Namespace] 
```

If such a representation is already used in an APL application, then no special handling is necessary to generate the corresponding JSON. However, transforming a dataset into a vector of namespaces, just for export to JSON, is cumbersome and can be expensive. `⎕JSON`'s wrapper codes `2`, `3`, and `4`, provide a quick and efficient way to transform the common APL representations of a dataset directly into a JSON array of objects.

### Raw Text Wrapper

Special JSON values such as <code class="language-nonAPL">null</code>, <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> do not directly correspond to specific APL values and, therefore, require special handling. This is provided by wrapper code `1`:

```apl
      1 ⎕JSON 42 'text'(⊂1 'null')(⊂1 'true')(⊂1 'false')
[42,"text",null,true,false]
```

As `1` is the default code number, it can be omitted:

```apl
      1 ⎕JSON 42 'text'(⊂'null')(⊂'true')(⊂'false')
[42,"text",null,true,false]
```

This feature can be used to inject any raw text, although unless it is valid JSON it cannot then be re-imported.

!!! Warning "Warning"
    It is common practice to initialise a list using a scalar rather than a one-element vector. However, this is interpreted as raw text if no subsequent elements are added:
    ```apl
          list←⊂'foo'
          1 ⎕JSON list
    foo
          1 ⎕JSON list,'bar' 'baz'
    ["foo","bar","baz"]
    ```

    It is, therefore, important to convert to a vector before initialising:

    ```apl
          list←,⊂'foo'
          1 ⎕JSON list
    ["foo"]
    ```

<h4 class="example">Example</h4>

This example illustrates how JavaScript objects can be exported; the object contains a JavaScript function that is specified by the contents of an enclosed character vector:

```apl
      slider←(
          range:⊂'true'
          min:0
          max:500
          values:75 300
          slide:⊂'function(event,ui){$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);}'
      )
      1 ⎕JSON slider
{"max":500,"min":0,"range":true,"slide":function(event,ui){$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);},"values":[75,300]}
```

### Dataset Wrappers

Wrapper codes `2`, `3`, and `4` produce identical JSON output (an array of objects; the canonical JSON representation of a dataset), but each allows different APL representation of the dataset:

Table: Wrapper codes { #wrapper-codes-table }

| Code | Data                                                                          | Advantage |
|--------------|----------------------------------------------------------------------------------------|-----------|
| `2`          | Single mixed-type matrix (first row is header vector)                                  | Preserves visual fidelity with a printed table |
| `3`          | Two-element nested vector: value matrix and header vector                              | Allows indexing into the rows and columns of the data |
| `4`          | Two-element nested vector: inverted table (vector of column vectors) and header vector | Less memory and faster lookups |

For wrapper code `4`, if [`HighRank`](#variant-option-highrank) is `'Split'`, character columns can also be stored as character matrices rather than vectors of character vectors, providing even better performance, but `⎕JSON` preserves trailing spaces.

<h4 class="example">Examples</h4>

The data arrays are defined as follows:

```apl
      ⎕←singleMatrix←fields⍪⍉↑item price qty
┌─────┬─────┬───┐
│item │price│qty│
├─────┼─────┼───┤
│Knife│3    │23 │
├─────┼─────┼───┤
│Fork │4    │45 │
├─────┼─────┼───┤
│Spoon│5    │67 │
└─────┴─────┴───┘
      ⎕←valueMatrix←⍉↑item price qty
┌─────┬─┬──┐
│Knife│3│23│
├─────┼─┼──┤
│Fork │4│45│
├─────┼─┼──┤
│Spoon│5│67│
└─────┴─┴──┘
      ⎕←invertedTable←item price qty
┌──────────────────┬─────┬────────┐
│┌─────┬────┬─────┐│3 4 5│23 45 67│
││Knife│Fork│Spoon││     │        │
│└─────┴────┴─────┘│     │        │
└──────────────────┴─────┴────────┘
      ⎕←invertedTable2←↑¨item price qty
┌─────┬─────┬────────┐
│Knife│3 4 5│23 45 67│
│Fork │     │        │
│Spoon│     │        │
└─────┴─────┴────────┘
      ⎕←header←fields
┌────┬─────┬───┐
│item│price│qty│
└────┴─────┴───┘
```

All wrapper invocations produce the same array of objects (except for trailing spaces when using a character matrix to represent a text field):

```apl
      1 ⎕JSON⊂2 singleMatrix
[{"item":"Knife","price":3,"qty":23},{"item":"Fork","price":4,"qty":45},{"item":"Spoon","price":5,"qty":67}]
      1 ⎕JSON⊂3(valueMatrix header)
[{"item":"Knife","price":3,"qty":23},{"item":"Fork","price":4,"qty":45},{"item":"Spoon","price":5,"qty":67}]
      1 ⎕JSON⊂4(invertedTable header)
[{"item":"Knife","price":3,"qty":23},{"item":"Fork","price":4,"qty":45},{"item":"Spoon","price":5,"qty":67}]
      1(⎕JSON⍠'HighRank' 'Split')⊂4(invertedTable2 header)
[{"item":"Knife","price":3,"qty":23},{"item":"Fork ","price":4,"qty":45},{"item":"Spoon","price":5,"qty":67}]
```

Without their wrappers, each APL structure *can* be represented in JSON, though this is not a common way to represent a dataset:

```apl
      1(⎕JSON⍠'HighRank' 'Split')singleMatrix
[["item","price","qty"],["Knife",3,23],["Fork",4,45],["Spoon",5,67]]
      1(⎕JSON⍠'HighRank' 'Split')valueMatrix header
[[["Knife",3,23],["Fork",4,45],["Spoon",5,67]],["item","price","qty"]]
      1 ⎕JSON invertedTable header
[[["Knife","Fork","Spoon"],[3,4,5],[23,45,67]],["item","price","qty"]]
      1(⎕JSON⍠'HighRank' 'Split')invertedTable2 header
[[["Knife","Fork ","Spoon"],[3,4,5],[23,45,67]],["item","price","qty"]]
```

### Selection of a Subset

A subset of a dataset's records (rows) and fields (columns) can be selected, with each subset being specified as a vector of strictly ascending indices and `⊂⍬` meaning "all" records (and/or fields):

Table: Wrappers forms for selecting dataset subsets { #subset-table }

| Subset             | Wrapper form                               |
|--------------------|--------------------------------------------|
| records            | `⊂wrapperCode wrapperData recordIndices`              |
| fields             | `⊂wrapperCode wrapperData(⊂⍬)fieldIndices`            |
| records and fields | `⊂wrapperCode wrapperData recordIndices fieldIndices` |

<h4 class="example">Examples</h4>

To select the second record (Fork):

```apl
      1 ⎕JSON⊂4(invertedTable header)2
[{"item":"Fork","price":4,"qty":45}]
```

To select the first and third fields (`item` and `qty`):

```apl
      1 ⎕JSON⊂4(invertedTable header)(⊂⍬)(1 3)
[{"item":"Knife","qty":23},{"item":"Fork","qty":45},{"item":"Spoon","qty":67}]
```

To select the second record (Fork) and the first and third fields (`item` and `qty`):

```apl
      1 ⎕JSON⊂4(invertedTable header)2(1 3)
[{"item":"Fork","qty":45}]
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕JSON JSON
</div>
