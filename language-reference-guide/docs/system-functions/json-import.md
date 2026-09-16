---
search:
  boost: 2
---

# <span>Import JSON</span> `R←{X} ⎕JSON Y`{{key}}

This function converts a JSON document to APL data. To convert APL data to JSON instead, see [Export JSON](json-export.md).

<h2 class="example">Example</h2>

```apl
      0 ⎕JSON'[1,-2,3]'
1 ¯2 3
```

## Right Argument

`Y` is a simple character scalar, vector, or matrix containing a JSON document. There is an implied newline character between each row of a matrix.

## Left Argument

`X` is `0`. It can be omitted when `Y` is a simple character array, which is what identifies the call as an import.

!!! Warning "Warning"
    Dyalog Ltd strongly recommends that `X` should always be specified to avoid code that seemingly works, only to fail on specific values.

## Result

`R` is the APL data corresponding to `Y`. Its form depends on the [`Format`](#variant-option-format) variant option: `'D'` gives a direct APL representation, `'M'` a four-column matrix encoding the JSON structure.

The [JSON standard](https://www.rfc-editor.org/info/rfc8259/#section-4) states that members of a JSON object should have unique names and that implementations vary in how they treat duplicates. Dyalog does not error on duplicates, but their handling depends on the `Format` variant option.

## Limitations

JSON supports a limited number of data types, and there is no direct correspondence between JSON and APL data structures. In particular:

- JSON does not support arrays with rank &gt; 1.
- JSON does not support nested scalars.
- JSON includes Boolean values <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> which are distinct from numeric values <code class="language-nonAPL">1</code> and <code class="language-nonAPL">0</code>; these have no direct APL equivalent.
- JSON object members are named and these names might not be [valid names in APL](../../programming-reference-guide/introduction/names.md).
- The [JSON5](https://json5.org/) dialect includes numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, which have no direct APL equivalent.

These differences are catered for in various ways as discussed below.

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

`⎕JSON` is controlled by six variant options, specified using [`⍠`](../primitive-operators/variant.md) and summarised in [](#variantoptionsforjsonimport). The principal option is `Format`. Options that affect only [export](json-export.md) are tolerated here, and have no effect.

Table: Variant options for importing with `⎕JSON` { #variantoptionsforjsonimport }

| Variant Option | Valid Values | Default | Effect |
|---|:---:|:---:|---|
| [`Format`](#variant-option-format)<br><small>principal</small> | `'D'` | `'D'` | `R` is APL data corresponding to `Y` |
|_-  -_| `'M'` |  | `R` is an APL matrix encoding of `Y` |
| [`Dialect`](#variant-option-dialect) | `'JSON'` | `'JSON'` | Only strict JSON syntax is accepted |
|_-  -_| `'JSON5'` |  | [JSON5](https://json5.org/) extensions are accepted |
| [`Null`](#variant-option-null) | `⊂'null'` | `⊂'null'` | JSON <code class="language-nonAPL">null</code> becomes APL `⊂'null'` |
|_-  -_| `⎕NULL` |  | JSON <code class="language-nonAPL">null</code> becomes APL `⎕NULL` |
| `Compact`, `Charset`, `HighRank` | | | No effect on import; see [Export JSON](json-export.md#variant-options) |

### Variant Option: `Format`

The `Format` variant option, the principal option, determines whether `⎕JSON` works with a direct APL representation of the data (`'D'` for "Data", the default) or with a four-column matrix that encodes the JSON structure (`'M'` for "Matrix") as nodes with depth, name, value, and type.

#### Import to Data

If `Format` is `'D'` (which stands for "Data", the default), the JSON document in `Y` is converted to the corresponding APL data `R`, possibly containing sub-arrays and/or sub-namespaces:

- JSON arrays are converted into APL vectors.
- JSON objects are converted into APL namespaces.
- JSON <code class="language-nonAPL">null</code> is converted into the specified (or implied) value of [`Null`](#variant-option-null) (`⊂'null'`, the default, or `⎕NULL`).
- JSON <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code> and, if the [`Dialect`](#variant-option-dialect) variant option is `'JSON5'`, the JSON5 numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, are converted to enclosed character vectors `⊂'true'`, `⊂'false'`, and so on.
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
`f⍺` is an invalid APL name:
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

If `Format` is `'M'` (which stands for "Matrix"), the JSON document `Y` is converted to a corresponding APL matrix `R` whose columns are as follows:

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
| `5`     | Specified by `Null` variant            | Null                     |
| `6`     | Enclosed character vector              | Lacking APL equivalent   |

In addition:

- JSON <code class="language-nonAPL">null</code> is converted into the specified (or implied) value of [`Null`](#variant-option-null); `⊂'null'` (the default) or `⎕NULL`.
- JSON values that lack an APL equivalent, <code class="language-nonAPL">true</code> and <code class="language-nonAPL">false</code>, and, if `Dialect` is `'JSON5'`, the JSON5 numeric constants <code class="language-nonAPL">Infinity</code>, <code class="language-nonAPL">-Infinity</code>, and <code class="language-nonAPL">NaN</code>, are converted to enclosed character vectors `⊂'true'`, `⊂'false'`, and so on.
- Object member names are reported as specified in the JSON text; they are not mangled as when `Format` is `'D'`.
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

### Variant Option: `Dialect`

If the `Dialect` variant option (default: `'JSON'`) is `'JSON5'`, all [JSON5](https://json5.org/) extensions are accepted. `Dialect` also affects [export](json-export.md#variant-option-dialect).

<h4 class="example">Example</h4>

```apl
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

### Variant Option: `Null`

The `Null` variant option selects how JSON <code class="language-nonAPL">null</code> is represented in APL, and must be either `⊂'null'` (the default) or `⎕NULL`.

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
```

The same representation is used when [exporting](json-export.md#variant-option-null).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕JSON JSON
</div>
