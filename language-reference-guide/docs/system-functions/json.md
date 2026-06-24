---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕JSON JSON
</div>

<h1 class="heading"><span class="name">JSON Convert</span> <span class="command">R←{X}⎕JSON Y</span></h1>

This function imports and exports data in [JavaScript Object Notation](https://www.json.org/json-en.html) (JSON) data interchange format.

## Syntax

If `X` is specified (that is, `⎕JSON` is called dyadically), it must be a numeric scalar with the value `0` for import or `1` for export.

<h3 class="example">Examples</h3>

Importing a JSON document to APL:
```apl
      0 ⎕JSON'[1,-2,3]'
1 ¯2 3
```
Exporting APL data to JSON:
```apl
      1 ⎕JSON 1 ¯2 3
[1,-2,3]
```

!!! Hint "Hints and Recommendations"
    As a mnemonic, think of `X` as specifying the desired "JSON-ness": `0` means "no JSON", that is, converting away from JSON; `1` means "yes JSON", that is, converting towards JSON.

If `X` is not specified (that is, `⎕JSON` is called monadically), its assumed value depends on `Y`:  If `Y` is a character array, `X` is assumed to be `0`; otherwise it is assumed to be `1`.

!!! Warning "Warning"
    Dyalog Ltd strongly recommends that `X` should always be specified to avoid code that seemingly works, only to fail on specific values.

`⎕JSON` has six [variant options](#variant-options): **Format**, **Compact**, **Null**, **HighRank**, **Charset**, and **Dialect**, specified using [`⍠`](../primitive-operators/variant.md). The principal option is **Format**.

## Limitations

JSON supports a limited number of data types, and there is no direct correspondence between JSON and APL data structures. In particular:

- JSON does not support arrays with rank &gt; 1.
- JSON does not support nested scalars.
- JSON includes Boolean values <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> which are distinct from numeric values <code class="language-nonAPL">1</code> and <code class="language-nonAPL">0</code>; these have no direct APL equivalent.
- JSON object members are named and these names might not be [valid names in APL](../../programming-reference-guide/introduction/names/).
- The [JSON5](https://json5.org/) dialect includes numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, which have no direct APL equivalent.

These differences are catered for in various ways as discussed below.

## JSON Import

If `X` is `0`, the JSON document `Y` is converted to the corresponding APL data `R`.

`Y` is a character scalar, vector, or matrix in JSON format. There is an implied newline character between each row of a matrix.

By default, `R` is APL data, possibly containing sub-arrays and/or sub-namespaces. If the variant option [**Format**](#variant-option-format) is set to `'M'`, `R` is instead a matrix that represents the JSON structure.

The [JSON standard](https://www.rfc-editor.org/info/rfc8259/#section-4) states that members of a JSON object should have unique names and that implementations vary in how they treat duplicates. Dyalog does not error on duplicates, but their handling depends on the **Format** variant option.

<h3 class="example">Example</h3>

```apl
      0 ⎕JSON'[1,-2,3]'
1 ¯2 3
```

For details and more examples, see [Import to Data](#import-to-data) and [Import to Matrix](#import-to-matrix).

## JSON Export

If `X` is `1`, the APL data `Y` is converted to a corresponding JSON document `R`.

`Y` is the data to be exported. By default, `Y` must be APL data that can be represented as JSON (subject to the [**HighRank**](#variant-option-highrank) variant option). If the [**Format**](#variant-option-format) variant option is set to `'M'`, `Y` must instead be a matrix representation such as would have been produced by importing JSON with **Format** being `'M'`. `⎕JSON` will signal `DOMAIN ERROR` if `Y` is incompatible with the specified (or implied) value of **Format**.

`R` is a character vector whose content depends upon the values of the [**Compact**](#variant-option-compact), [**Dialect**](#variant-option-dialect), and [**Charset**](#variant-option-charset) variant options.

Some JSON values lack a direct APL equivalent (<code class="language-nonAPL">true</code>, <code class="language-nonAPL">false</code>, <code class="language-nonAPL">null</code>, JavaScript fragments), and some APL representations of datasets do not correspond to common JSON practice. Such cases are handled by [wrappers](#wrappers).

<h3 class="example">Example</h3>

```apl
      1 ⎕JSON 1 ¯2 3
[1,-2,3]
```

For details and more examples, see [Export from Data](#export-from-data) and [Export from Matrix](#export-from-matrix).

## Name Mangling

When `⎕JSON` converts a JSON document to APL data and a member of a JSON object has a name that is not a valid APL name, the member is renamed using a name mangling algorithm. This results in a name that begins with `⍙`. Any characters that cannot be part of an APL name are replaced with their [decimal Unicode code point](ucs.md#monadic-ucs) surrounded by `⍙`s.

<h3 class="example">Example</h3>

In this example, the JSON document describes an object containing two numeric items, one named `a` (which is a valid APL name) and the other named `2a` (which is not a valid APL name):
```json
{"a": 1, "2a": 2}
```

When the object is imported (as a namespace), `⎕JSON` renames `2a` to a valid APL name:
```apl
      (0 ⎕JSON'{"a": 1, "2a": 2}').⎕NL 2
a  
⍙2a
```

When the namespace is exported, `⎕JSON` reverses the mangling:
```apl
      1 ⎕JSON (a:1 ⋄ ⍙2a:2)
{"a":1,"2a":2}
```

<h3 class="example">Example</h3>

This object has a member name with a character (`ý`; `⎕UCS 253`) that is not allowed in APL names:
```json
{"sýn":"vision"}
```
The `ý` is replaced with `⍙253⍙` ("253" is the Unicode decimal character code for this character):
```apl
      (0 ⎕JSON'{"sýn":"vision"}').⎕NL 2
⍙s⍙253⍙n
```

### Name Mangling Algorithm

[`7162⌶`](../primitive-operators/i-beam/json-translate-name.md) provides direct access to the name mangling algorithm.

<h3 class="example">Example</h3>

The above name translations are verified using `7162⌶`:
```apl
      0(7162⌶)'2a' 'sýn'
┌───┬────────┐
│⍙2a│⍙s⍙253⍙n│
└───┴────────┘
      1(7162⌶)'⍙2a' '⍙s⍙253⍙n'
┌──┬───┐
│2a│sýn│
└──┴───┘
```

## Variant Options

`⎕JSON` is controlled by six variant options. [](#variant-table) summarises each option's effect on import from JSON to APL (`X=0`) and export from APL to JSON (`X=1`). Each option is described in finer detail, with examples, below the table. Variant options specific to one direction are tolerated for the other direction even if they have no effect.

Table: Variant options overview { #variant-table }

| Variant Option                                                     | Value                                 | Effect on Import                                    | Effect on Export |
|--------------------------------------------------------------------|:-------------------------------------:|-----------------------------------------------------|------------------|
| [**Format**](#variant-option-format)<br><small>principal</small> | `'D'`<br><small>default</small>       | `R` is APL data corresponding to `Y`                | `Y` is APL data |
|_-                                                                -_| `'M'`                                 | `R` is an APL matrix encoding of `Y`                | `Y` is a 4-column APL matrix as from import with `'M'` |
| [**Dialect**](#variant-option-dialect)                           | `'JSON'`<br><small>default</small>    | Only strict JSON syntax is accepted                 | Only strict JSON syntax is produced |
|_-                                                                -_| `'JSON5'`                             | [JSON5](https://json5.org/) extensions are accepted | JSON5 features are used to improve readability and editability, and/or shorten output |
| [**Null**](#variant-option-null)                                 | `⊂'null'`<br><small>default</small>   | JSON <code class="language-nonAPL">null</code> becomes APL `⊂'null'`                   | APL `⊂'null'` becomes JSON <code class="language-nonAPL">null</code> |
|_-                                                                -_| `⎕NULL`                               | JSON <code class="language-nonAPL">null</code> becomes APL `⎕NULL`                     | APL `⎕NULL` becomes JSON <code class="language-nonAPL">null</code> |
| [**Compact**](#variant-option-compact)                           | `1`<br><small>default</small>         | None                                                | `R` has no whitespace outside quotes |
|_-                                                                -_| `0`                                   | None                                                | `R` has whitespace for readability and, if **Dialect** is `'JSON5'`, trailing commas after final elements and members |
| [**Charset**](#variant-option-charset)                           | `'Unicode'`<br><small>default</small> | None                                                | Unicode characters in `Y` are used when JSON standard allows |
|_-                                                                -_| `'ASCII'`                             | None                                                | Non-ASCII characters are converted to the hexadecimal form `\uNNNN`, and if **Dialect** is `'JSON5'`, also `\xNN` |
| [**HighRank**](#variant-option-highrank)                         | `'Error'`<br><small>default</small>   | None                                                | High-rank arrays are rejected |
|_-                                                                -_| `'Split'`                             | None                                                | High-rank arrays are split and [inverted table wrappers](#dataset-wrappers) accept text columns as matrices |

### Variant Option: Format

The **Format** variant option, the principal option, determines whether `⎕JSON` works with a direct APL representation of the data (`'D'` for "Data", the default) or with a four-column matrix that encodes the JSON structure (`'M'` for "Matrix") as nodes with depth, name, value, and type.

#### Import to Data

If **Format** is `'D'` (which stands for "Data", the default), the JSON document in `Y` is converted to the corresponding APL data `R`, possibly containing sub-arrays and/or sub-namespaces:

- JSON arrays are converted into APL vectors.
- JSON objects are converted into APL namespaces.
- JSON <code class="language-nonAPL">null</code> is converted into the specified (or implied) value of [**Null**](#variant-option-null) (`⊂'null'`, the default, or `⎕NULL`).
- JSON <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> and, if the [**Dialect**](#variant-option-dialect) variant option is `'JSON5'`, the JSON5 numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, are converted to enclosed character vectors `⊂'true'`, `⊂'false'`, and so on.
- If the JSON source contains object member names that are not valid APL names, they are converted to APL namespace members with [mangled names](#name-mangling). The original names can be obtained using [`7162⌶`](../primitive-operators/i-beam/json-translate-name.md).
- If duplicate names are found, the last member encountered is used and all previous members with the same name are discarded.

<h5 class="example">Examples</h5>

The following JSON document is stored as the character vector `json`:
```json
{
  "a": {
    "b": [
      "string 1",
      "string 2"
    ],
    "c": true,
    "d": {
      "e": false,
      "f⍺": [
        "string 3",
        123,
        1000.2,
        null
      ]
    }
  }
}
```
The JSON document is converted to APL data as a namespace:
```apl
      j←0 ⎕JSON json
      j
#.[JSON object]
```
Listing the sub-namespace and its members:
```apl
      j.⎕NL 9
a
      j.a.⎕NL 2
b
c
      j.a.b
┌────────┬────────┐
│string 1│string 2│
└────────┴────────┘
      j.a.c
┌────┐
│true│
└────┘
      j.a.⎕NL 9
d
```
Note that `f⍺` is an invalid APL name:
```apl
      j.a.d.⎕NL 2
e       
⍙f⍙9082⍙
      j.a.d.⍙f⍙9082⍙
┌────────┬───┬──────┬──────┐
│string 3│123│1000.2│┌────┐│
│        │   │      ││null││
│        │   │      │└────┘│
└────────┴───┴──────┴──────┘
```
The two ways to represent JSON <code class="language-nonAPL">null</code>s:
```apl
      0 ⎕JSON'[null,2,3]'
┌──────┬─┬─┐
│┌────┐│2│3│
││null││ │ │
│└────┘│ │ │
└──────┴─┴─┘
      0(⎕JSON⍠'Null'⎕NULL)'[null,2,3]'
 [Null]  2 3
```

#### Import to Matrix

If **Format** is `'M'` (which stands for "Matrix"), the JSON document `Y` is converted to a corresponding APL matrix `R` whose columns are as follows:

Table: Import matrix columns { #import-matrix-table }

| Column  | Contents                         |
|---------|----------------------------------|
| `R[;1]` | Depth                            |
| `R[;2]` | Name (for JSON object members)   |
| `R[;3]` | APL value                        |
| `R[;4]` | [JSON type](#import-types-table) |

The JSON types are as follows:

Table: JSON types { #import-types-table }

| `R[;4]` | `R[;3]` (APL value)                    | Corresponding JSON value |
|---------|----------------------------------------|--------------------------|
| `1`     | Empty (contents are in following rows) | Object                   |
| `2`     | Empty (contents are in following rows) | Array                    |
| `3`     | Number                                 | Number                   |
| `4`     | Character vector                       | String                   |
| `5`     | Specified by **Null** variant            | Null                     |
| `6`     | Enclosed character vector              | Lacking APL equivalent   |

Note that:

- JSON <code class="language-nonAPL">null</code> is converted into the specified (or implied) value of [**Null**](#variant-option-null); `⊂'null'` (the default) or `⎕NULL`.
- JSON values that lack an APL equivalent, <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code>, and, if **Dialect** is `'JSON5'`, the JSON5 numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, are converted to enclosed character vectors `⊂'true'`, `⊂'false'`, and so on.
- Object member names are reported as specified in the JSON text; they are not mangled as when **Format** is `'D'`.
- If duplicate names are found, all duplicate members are recorded in the result matrix.

<h5 class="example">Example</h5>
This example uses the character vector `json` from the previous example:

```apl
      json
{                  
  "a": {           
    "b": [         
      "string 1",  
      "string 2"   
    ],             
    "c": true,     
    "d": {         
      "e": false,  
      "f⍺": [      
        "string 3",
        123,       
        1000.2,    
        null       
      ]            
    }              
  }                
}                  
      0(⎕JSON⍠'M')json
┌─┬──┬────────┬─┐
│0│  │        │1│
├─┼──┼────────┼─┤
│1│a │        │1│
├─┼──┼────────┼─┤
│2│b │        │2│
├─┼──┼────────┼─┤
│3│  │string 1│4│
├─┼──┼────────┼─┤
│3│  │string 2│4│
├─┼──┼────────┼─┤
│2│c │┌────┐  │6│
│ │  ││true│  │ │
│ │  │└────┘  │ │
├─┼──┼────────┼─┤
│2│d │        │1│
├─┼──┼────────┼─┤
│3│e │┌─────┐ │6│
│ │  ││false│ │ │
│ │  │└─────┘ │ │
├─┼──┼────────┼─┤
│3│f⍺│        │2│
├─┼──┼────────┼─┤
│4│  │string 3│4│
├─┼──┼────────┼─┤
│4│  │123     │3│
├─┼──┼────────┼─┤
│4│  │1000.2  │3│
├─┼──┼────────┼─┤
│4│  │┌────┐  │5│
│ │  ││null│  │ │
│ │  │└────┘  │ │
└─┴──┴────────┴─┘
```

#### Export from Data

If **Format** is `'D'` (which stands for "Data"), the APL value `Y` is converted to a corresponding JSON document `R` as follows:

- APL vectors are converted to JSON arrays.
- APL arrays of higher rank are recursively split if [**HighRank**](#variant-option-highrank) is `'Split'`, otherwise `⎕JSON` will signal `DOMAIN ERROR`.
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

If **Format** is `'M'` (which stands for "Matrix"), the APL array `Y` is converted to a corresponding JSON document `R` and `Y` must be a matrix whose columns are as follows:

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

If there are any mismatches between the values in `Y[;3]` and the types in `Y[;4]`, `⎕JSON` will signal `DOMAIN ERROR` and report the first row where there is a mismatch (`⎕IO` sensitive) as illustrated in the following example.

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

### Variant Option: Dialect

If the **Dialect** variant option (default: `'JSON'`) is `'JSON5'`, [JSON5](https://json5.org/) extensions are enabled on import and export.

On import, all JSON5 extensions are accepted.

On export, the result is shortened by usage of identifiers without quotes, single quotes (`'`), and character escapes `\v` and of the form `\xNN` (for values less than hexadecimal 100, that is, `⎕UCS 256`). If [**Compact**](#variant-option-compact) is `0`, a trailing comma (`,`) is added after the last array element and object member.

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

      0(⎕JSON⍠'Dialect' 'JSON5')['["a\'
                                  'bc",'
                                  '//:)'
                                  '+.1,'
                                  '/**/'
                                  '0xf]']
┌───┬───┬──┐
│abc│0.1│15│
└───┴───┴──┘
```

### Variant Option: Null

The **Null** variant option selects how JSON <code class="language-nonAPL">null</code> is represented in APL, and must be either `⊂'null'` (the default) or `⎕NULL`:

- If **Null** is `⊂'null'`, `⎕NULL` causes `DOMAIN ERROR`.
- If **Null** is `⎕NULL`, `⊂'null'` is still exported as <code class="language-nonAPL">null</code> because it is interpreted as [raw text](#raw-text-wrapper).

<h4 class="example">Examples</h4>

```apl
      0 ⎕JSON'[null,null]'
┌──────┬──────┐
│┌────┐│┌────┐│
││null│││null││
│└────┘│└────┘│
└──────┴──────┘
      0(⎕JSON⍠'Null'⎕NULL)'[null,null]'
 [Null]  [Null] 

      1 ⎕JSON ⎕NULL ⎕NULL
DOMAIN ERROR: JSON export: item "[1]" of the right argument (⎕IO=1) cannot be converted
      1 ⎕JSON ⎕NULL ⎕NULL
        ∧
      1(⎕JSON⍠'Null'⎕NULL)⎕NULL ⎕NULL
[null,null]
```

### Variant Option: Compact

The **Compact** variant option can be used to generate JSON that is either dense (`1`, the default) or optimised for humans to read and edit (`0`).

If **Compact** is `0`:

- Line breaks are inserted after opening brackets `[` and `{` and before closing brackets `]` and `}`
- Each array element and object member is on its own line, indented with two spaces relative to its container array or object
- A space is inserted after `:` separating member name and value
- If [**Dialect**](#variant-option-dialect) is `'JSON5'`, a trailing comma (`,`) is added after the last array element and object member

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

### Variant Option: Charset

The **Charset** variant option can be used to either allow Unicode in the generated JSON (`'Unicode'`, the default) or restrict the output to ASCII characters (`'ASCII'`). When necessary, characters are converted to the hexadecimal form `\uNNNN`. If [**Dialect**](#variant-option-dialect) is `'JSON5'`, the form `\xNN` is used for values up to hexadecimal `FF` (`⎕UCS 255`).

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

### Variant Option: HighRank

If **HighRank** is `'Error'` (the default), `⎕JSON` will signal a `DOMAIN ERROR` upon encountering any arrays in `Y` of rank higher than 1. If **HighRank** is `'Split'`, `⎕JSON` will recursively split any such arrays as necessary; in addition, [datasets](#dataset-wrappers) as inverted tables can have text columns represented as matrices.

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
    It is common practice to initialise a list using a scalar rather than a one-element vector. However, this will be interpreted as raw text if no subsequent elements are added:
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

For wrapper code `4`, if [**HighRank**](#variant-option-highrank) is `'Split'`, character columns can also be stored as character matrices rather than vectors of character vectors, providing even better performance, but `⎕JSON` will preserve trailing spaces.

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
