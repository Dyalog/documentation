---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕JSON JSON
</div>

<h1 class="heading"><span class="name">JSON Convert</span> <span class="command">R←{X}⎕JSON Y</span></h1>

!!! Warning "Warning"
    The default for `X` depends on the type of `Y`, and Dyalog Ltd strongly recommends not relying on that.

This function imports and exports data in [JavaScript Object Notation](https://www.json.org/json-en.html) (JSON) Data Interchange Format.

JSON supports a limited number of data types and there is not a direct correspondence between JSON and APL data structures. In particular:

- JSON does not support arrays with rank &gt;1.
- JSON does not support nested scalars.
- JSON includes Boolean values `true` and `false` which are distinct from numeric values `1` and `0` and have no direct APL equivalent.
- The [JSON5](https://json5.org/) standard includes numeric constants `Infinity`, `-Infinity`, `NaN` and `-NaN` which have no direct APL equivalent.
- JSON object members are named and these names might not be valid names in APL.

These differences are catered for in various ways as discussed below.

If specified, `X` must be a numeric scalar with the value `0` (import JSON) or `1` (export JSON). Dyalog Ltd strongly recommends that `X` should always be used, however, if `X` is not specified and `Y` is a character array, `X` is assumed to be `0` (import); otherwise it is assumed to be `1` (export).

JSON Import (`X=0`) converts a JSON (in the form of an APL character array) to a corresponding APL array. JSON Export (`X=1`) converts an APL array to the corresponding JSON (in the form of an APL character array).

Other options for `⎕JSON` are `Format`, `Compact`, `Null`, `HighRank`, `Charset` and `Dialect` which are specified using `⍠` (see [Variant operator](../primitive-operators/variant.md)). The Principal Option is `Format`.

## Variant Options Common to both Import and Export

The following variant options pertain equally to both import and export. Variant options specific to import or export are tolerated for the other operation even if they have no effect.

### Format Option

The `Format` variant option determines if the imported or exported APL array is the closest APL equivalent to the corresponding JSON data or if it is a matrix that encodes the JSON data.

### Dialect Option

The `Dialect` variant option can be used to enable [JSON5](https://json5.org/) extensions on import and export.

| Dialect | Effect on import     | Effect on export |
|------------|-----------------|-----------------|
| `'JSON'` { .shaded } | JSON5 extensions are allowed. | Object member names that are valid ECMAScript 5.1 identifiers are exported without quotes, single quotes (`'`) are used if it makes the result shorter, trailing comma (`,`) is added after the last array element and object member if `Compact` is `0`, character escape values less than hexadecimal 100 (`⎕UCS 256`) are converted to the form `\xNN`. |
| `'JSON5'` | JSON5 extensions are rejected (`DOMAIN ERROR`). | Object member names are always quoted, only double quotes (`"`) are used, no trailing comma is added to arrays or objects, character escapes only use the form `\uNNNN`. |

**Examples**
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

### Null Option

The `Null` variant option can be used to select how JSON `null` is represented in APL.

| Null  | Exporting `⎕NULL` |
|------------|-----------------|
| `⊂'null'` { .shaded } | Rejected (`DOMAIN ERROR`). |
| `⎕NULL` | Allowed. |

Note that `Null` being `⎕NULL` will still let `⊂'null'` be exported, as it will be interpreter as wrapper (mechanism for special handling) of raw text. See [Wrapper code 1](#wrapper-code-1-raw-text).

**Examples**

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

## JSON Import (`X` is `0`)
`Y` is a character vector or matrix in JSON format. There is an implied newline character between each row of a matrix.

The content of the result `R` depends upon the `Format` variant, which can be `'D'` (the default) or`'M'`.

The JSON standard says that members of a JSON object should have unique names and that different implementations behave differently when there are duplicates. Dyalog does not error on duplicate names, but the behaviour depends on the `Format` variant.

### Import as Data (`Format` is `'D'`)

If `Format` is`'D'` (which stands for "Data") the JSON in `Y` is converted to APL data and `R` is an array or a namespace containing arrays and sub-namespaces.

- JSON objects are converted into APL namespaces.
- JSON `true` and `false` and, if the `Dialect` variant option is `'JSON5'`, the JSON5 numeric constants `Infinity`, `-Infinity`, `NaN`, and `-NaN` are converted to enclosed character vectors `⊂'true'`,`⊂'false'`, and so forth.
- If the JSON source contains object member names which are not valid APL names they are converted to APL namespace members with mangled names using a translation mechanism. See [JSON Name Mangling](#json-name-mangling). `7162⌶` can be used to obtain the original name. See [JSON Translate Name](../primitive-operators/i-beam/json-translate-name.md).
- If duplicate names are found, the last member encountered is used and all previous members with the same name are discarded.

**Examples**

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
      j←0 ⎕JSON json
      j
#.[JSON object]
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
      j.a.d.⎕NL 2 ⍝ Note that f⍺ is an invalid APL name
e       
⍙f⍙9082⍙
      j.a.d.e
┌─────┐
│false│
└─────┘
      j.a.d.⍙f⍙9082⍙
┌────────┬───┬──────┬──────┐
│string 3│123│1000.2│┌────┐│
│        │   │      ││null││
│        │   │      │└────┘│
└────────┴───┴──────┴──────┘

      0 ⎕JSON'[null,2,3]'
┌──────┬─┬─┐
│┌────┐│2│3│
││null││ │ │
│└────┘│ │ │
└──────┴─┴─┘
      0(⎕JSON⍠'Null'⎕NULL)'[null,2,3]'
 [Null]  2 3
```
### Import as Matrix (`Format` is `'M'`)

If `Format` is `'M'` (which stands for "Matrix") the result `R` is a matrix whose columns contain the following:

|------------|--------------------------------|
| `[;1]`     | Depth                          |
| `[;2]`     | Name (for JSON object members) |
| `[;3]`     | APL value                      |
| `[;4]`     | JSON type (integer: see below) |

- JSON values that lack an APL equivalent, `true` and `false`, and, if `Dialect` is `'JSON5'`, the JSON5 numeric constants `Infinity`, `-Infinity`, `NaN`, and `-NaN` are converted to enclosed character vectors `⊂'true'`,`⊂'false'`, and so forth.
- Object member names are reported as specified in the JSON text (they are not mangled as when `Format` is `'D'`).
- If duplicate names are found, all duplicate members are recorded in the result matrix.

| `R[;4]` (JSON type) | `R[;3]` (APL value) | Corresponding JSON value |
|------|-----------------------------|---------------------------|
| `1`  | Namespace                   | Object                    |
| `2`  | Vector                      | Array                     |
| `3`  | Number                      | Number                    |
| `4`  | Character vector            | String                    |
| `5`  | Specified by `Null` variant | Null                      |
| `6`  | Enclosed character vector   | Lacking APL equivalent    |

**Example**

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

## JSON Export (`X` is `1`)

`Y` is the data to be exported as JSON. What constitutes a valid value of `Y` depends upon the `Format` variant, which can be`'D'` (the default) or `'M'`. If `Format` is `'M'`, `Y` must be a matrix representation of JSON such as would have been produced by JSON Import with `Format` being `'M'`; otherwise it must be an array or namespace that can be represented as JSON (subject to the `HighRank` variant option).

`⎕JSON` will signal `DOMAIN ERROR` if `Y` is incompatible with the specified (or implied) value of `Format`.

`R` is a character vector whose content depends upon the value of the `Compact` variant, see below.

### Export Data (`Format` is `'D'`)

If `Format` is `'D'` (which stands for "Data") the APL value in `Y` is converted to JSON.

- APL namespaces are converted to JSON objects.
- Enclosed vectors are wrappers (mechanisms for special handling). See [Wrappers](#wrappers).
- If a namespace member name is mangled (made into a valid APL) such as would have been produced by JSON name mangling (a translation mechanism), it is demangled. See [JSON Name Mangling](#json-name-mangling). `7162⌶` can be used to obtain the original name. See [JSON Translate Name](../primitive-operators/i-beam/json-translate-name.md).

**Example**

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

### Export Matrix (`Format` is `'M'`)

If `Format` is `'M'` (which stands for "Matrix"), `Y` must be a matrix whose columns contain the following:

|------------|---------------------------------------|
| `[;1]`     | Depth                                 |
| `[;2]`     | Name (for JSON object members)        |
| `[;3]`     | APL value                             |
| `[;4]`     | JSON type (integer: see below)        |

| `Y[;4]` (JSON type) | `Y[;3]` (APL value)       | Corresponding JSON value |
|----------------|---------------------------|--------------------------|
| `1`            | Empty array               | Object                   |
| `2`            | Empty array               | Array                    |
| `3`            | Numeric scalar            | Number                   |
| `4`            | Character vector          | String                   |
| `5`            | Null                      | Null                     |
| `6`            | Enclosed character vector | Lacking APL equivalent   |
| `7`            | Enclosed character vector | Raw text (see [Wrapper code 1](#wrapper-code-1-raw-text) |

The difference between JSON types `6` and `7` is that `6` only allows the special values that can be imported, while `7` allows any text whatsoever.

If there are any mismatches between the values in `Y[;3]` and the types in `Y[;4]`, `⎕JSON` will signal `DOMAIN ERROR` and report the first row where there is a mismatch (`⎕IO` sensitive) as illustrated in the following example.

**Example**

```apl
      M←0(⎕JSON⍠'Format' 'M')'{"values": [ 75, 300 ]}'
      M
┌─┬──────┬───┬─┐
│0│      │   │1│
├─┼──────┼───┼─┤
│1│values│   │2│
├─┼──────┼───┼─┤
│2│      │75 │3│
├─┼──────┼───┼─┤
│2│      │300│3│
└─┴──────┴───┴─┘

      M[3;3]←⊂'75' ⍝ character not numeric

      M            ⍝ but looks the same as before

┌─┬──────┬───┬─┐
│0│      │   │1│
├─┼──────┼───┼─┤
│1│values│   │2│
├─┼──────┼───┼─┤
│2│      │75 │3│
├─┼──────┼───┼─┤
│2│      │300│3│
└─┴──────┴───┴─┘

      1(⎕JSON⍠'Format' 'M')M
DOMAIN ERROR: JSON export: value does not match the specified type in row 3 (⎕IO=1)
      1(⎕JSON⍠'Format' 'M')M
      ∧
```

### Compact Option

The `Compact` variant option can be used to make it easier for humans to read and edit the generated JSON.

| Compact | Description                                                        |
|---------|--------------------------------------------------------------------|
| `0`     | The JSON text is padded with spaces and line breaks for readability. |
| `1` { .shaded } | The JSON text is compacted into its minimal form.                  |

**Example**

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
      ⍴json←1 ⎕JSON ns
97
      json
{"a":{"b":["charvec 1","charvec 2"],"c":true,"d":{"e":false,"f⍺":["charvec 3",123,1000.2,null]}}}

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

### Charset Option

The `Charset` variant option can be used to restrict the output to ASCII characters. 

| Charset    | Description     |
|------------|-----------------|
| `'Unicode'` { .shaded } | All Unicode characters in `Y` are passed unchanged in the result `R`. |
| `'ASCII'` | Non-ASCII characters are converted to an encoded string of the form `\uNNNN` where `NNNN` is the upper-case hexadecimal value of the character in the Unicode system. For example, `é` (e-acute) is converted to `\u00E9`. Furthermore, if `Dialect` is `'JSON5'`, values less than hexadecimal 100 (`⎕UCS 256`) are converted to the form `\xNN`. |

**Example**

```apl
      ns←(dé:'DÉ')
      ns.dé
DÉ
      1 ⎕JSON ns
{"dé":"DÉ"}
      1(⎕JSON⍠'Charset' 'ASCII')ns
{"d\u00E9":"D\u00C9"}
```

### HighRank Option

The `HighRank` variant option can be used to instruct `⎕JSON` to pre-process higher-rank arrays into a form that can be represented by JSON. Note that if necessary, the transformation is applied recursively throughout the high-rank array(s) specified by `Y`.

| HighRank | Description                                        |
|----------|----------------------------------------------------|
| `'Split'` | High-rank data is split into nested vectors.       |
| `'Error'` { .shaded } | High-rank data is rejected (`DOMAIN ERROR`) |

**Example**

```apl
      d
┌─────┬─────────────────────────┐
│1 2  │ABC                      │
│A B  │DEF                      │
├─────┼─────────────────────────┤
│1 2 3│1            0.5         │
│4 5 6│0.3333333333 0.25        │
│     │                         │
│     │0.2          0.1666666667│
│     │0.1428571429 0.125       │
└─────┴─────────────────────────┘
      1 ⎕JSON d
DOMAIN ERROR: JSON export: the right argument cannot be converted (⎕IO=1)
      1 ⎕JSON d
      ∧
      1 (⎕JSON⍠'HighRank' 'Split') d
[[[1,2,3],[4,5,6]],[[[1,0.5],[0.3333333333333333,0.25]],[[0.2,0.1666666666666667],[0.1428571428571428,0.125]]]]
```

### Wrappers

A wrapper is an enclosed vector of the form:

```apl
      ⊂code special
```

This structure has been chosen to identify special treatment because a nested scalar cannot be represented in JSON or JavaScript. A wrapper can be specified directly in the right argument to `⎕JSON` and/or as part of the array structure specified by the right argument, as a sub-array or in a namespace. This allows a special array to be processed appropriately as part of a general data structure that is to be rendered as JSON.

The structure of the `special` array is specified within the wrapper by a leading numeric code. Code `1` (the default) allows insertion of raw text, including JSON values such as `null` and `true`. Codes `2`, `3` and `4` identify various representations of a *dataset*.

The term *dataset* is used here to mean a collection of data, usually presented in tabular form. Each named column (also called a *field*) represents a particular variable. Each row (also called a *record*) corresponds to a given member of the dataset in question, listing its value for each of the variables, such as price and quantity of an item.

In APL, a dataset is traditionally represented as a collection of variables:

```apl
      fields←'item' 'price' 'qty'
      items←'Knife' 'Fork' 'Spoon'
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

Note that the JSON structure can be represented in APL:

```apl
      ⎕←Fields{()⎕VSET(↑⍺)⍵}⍤1⍉↑items price qty
 #.[Namespace]  #.[Namespace]  #.[Namespace] 
```

If such a representation is already used in an APL application, then no special handling is necessary to generate the corresponding JSON. However, transforming a dataset into a vector of namespaces, just for export to JSON, can be expensive and cumbersome. `⎕JSON`'s wrapper codes `2`, `3`, and `4`, provide a quick and efficient way to transform the common APL representations of a dataset directly into a JSON array of objects.

#### Wrapper code `1`: Raw Text

Special JSON values such as `null`, `true` and `false` do not directly correspond to specific APL values and therefore require special handling. This is provided by wrapper code `1`:

```apl
      1 ⎕JSON 42 'text'(⊂1 'null')(⊂1 'true')(⊂1 'false')
[42,"text",null,true,false]
```
The code number can be omitted:
```apl
      1 ⎕JSON 42 'text'(⊂'null')(⊂'true')(⊂'false')
[42,"text",null,true,false]
```

This feature can be used to inject any raw text, although unless it is valid JSON it cannot then be re-imported.

!!! Warning "Warning"
    Out of convenience, it is common to initialise a list using a scalar rather than a one-element vector. Doing so for an eventual vector of character vectors will fail if the value is exported before a subsequent element is added:
    ```apl
          list←⊂'foo'
          1 ⎕JSON list
    foo
          1 ⎕JSON list,'bar' 'baz'
    ["foo","bar","baz"]
    ```
    It is therefore important to initialise as a proper vector:
    ```apl
          list←,⊂'foo'
          1 ⎕JSON list
    ["foo"]
    ```

The following example illustrates how JavaScript objects can be exported. In the example, the object contains a JavaScript function which is specified by the contents of an enclosed character vector.

**Example**

```apl
      slider←(
          range:⊂'true'
          min:0
          max:500
          values:75 300
          slide:⊂' function( event, ui ) {$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );}'
      )
      1 ⎕JSON slider
{"max":500,"min":0,"range":true,"slide":function(event,ui){$("#amount").val("$"+ui.values[0] + " - $" + ui.values[1]);},"values":[75,300]}
```

#### Wrapper code `2`: Single Mixed-Type Matrix

A dataset can be represented as a single mixed-type matrix:

```apl
      ⎕←singleMatrix←fields⍪⍉↑items price qty
┌─────┬─────┬───┐
│item │price│qty│
├─────┼─────┼───┤
│Knife│3    │23 │
├─────┼─────┼───┤
│Fork │4    │45 │
├─────┼─────┼───┤
│Spoon│5    │67 │
└─────┴─────┴───┘
```

The advantage of this structure is that it preserves visual fidelity with a printed table.

`⎕JSON` will produce an array of objects when given an enclosed vector where the first element is a `2` and the second element is a single matrix:

```apl
      1 ⎕JSON⊂2 singleMatrix
[{"item":"Knife","price":3,"qty":23},{"item":"Fork","price":4,"qty":45},{"item":"Spoon","Price":5,"qty":67}]
```

Note that the APL structure *can* be represented in JSON, though this is not a common way to represent a dataset:

```apl
      1(⎕JSON⍠'HighRank' 'Split')singleMatrix
[["item","Price","qty"],["Knife",3,23],["Fork",4,45],["Spoon",5,67]]
```

#### Wrapper code `3`: Value matrix with separate header vector

A dataset can be represented as a value matrix with a separate header vector:

```apl
      ⎕←valueMatrix_header←(⍉↑items price qty)fields
┌────────────┬────────────────┐
│┌─────┬─┬──┐│┌────┬─────┬───┐│
││Knife│3│23│││item│Price│qty││
│├─────┼─┼──┤│└────┴─────┴───┘│
││Fork │4│45││                │
│├─────┼─┼──┤│                │
││Spoon│5│67││                │
│└─────┴─┴──┘│                │
└────────────┴────────────────┘
```

The advantage of this structure is that it allows indexing into the rows and columns of the data.

`⎕JSON` will produce an array of objects when given an enclosed vector where the first element is a `3` and the second element is a two-element vector consisting of a value matrix and a header:

```apl
      1 ⎕JSON⊂3 valueMatrix_header
[{"item":"Knife","Price":3,"qty":23},{"item":"Fork","Price":4,"qty":45},{"item":"Spoon","Price":5,"qty":67}]
```

Note that the APL structure *can* be represented in JSON, though this is not a common way to represent a dataset:

```apl
      1(⎕JSON⍠'HighRank' 'Split')valueMatrix_header
[[["Knife",3,23],["Fork",4,45],["Spoon",5,67]],["item","Price","qty"]]
```

#### Wrapper code `4`: Inverted table with a separate header vector

A dataset can be represented as an inverted table (vector of column vectors) together with a separate header vector:

```apl
      ⎕←invertedTable_header←(items price qty)fields
┌───────────────────────────────────┬────────────────┐
│┌──────────────────┬─────┬────────┐│┌────┬─────┬───┐│
││┌─────┬────┬─────┐│3 4 5│23 45 67│││item│Price│qty││
│││Knife│Fork│Spoon││     │        ││└────┴─────┴───┘│
││└─────┴────┴─────┘│     │        ││                │
│└──────────────────┴─────┴────────┘│                │
└───────────────────────────────────┴────────────────┘
```

The advantage of this structure is that it can consume significantly less memory compared to the matrix forms and that it can make certain types of look-ups faster. This is because numeric columns are stored as simple numeric vectors and character columns can be stored as simple character matrices.

`⎕JSON` will produce an array of objects when given an enclosed vector where the first element is a `4` and the second element is a two-element vector consisting of an inverted table and a header:

```apl
      1 ⎕JSON⊂4 invertedTable_header
[{"item":"Knife","Price":3,"qty":23},{"item":"Fork","Price":4,"qty":45},{"item":"Spoon","Price":5,"qty":67}]
```

Note that the APL structure *can* be represented in JSON, though this is not a common way to represent a dataset:

```apl
      1 ⎕JSON invertedTable_header
[[["Knife","Fork","Spoon"],[3,4,5],[23,45,67]],["item","Price","qty"]]
```

If `HighRank` is `1`, character columns can also be stored as character matrices:

```apl
      ⎕←invertedTable2_header←(↑¨items price qty)fields
┌──────────────────────┬────────────────┐
│┌─────┬─────┬────────┐│┌────┬─────┬───┐│
││Knife│3 4 5│23 45 67│││item│price│qty││
││Fork │     │        ││└────┴─────┴───┘│
││Spoon│     │        ││                │
│└─────┴─────┴────────┘│                │
└──────────────────────┴────────────────┘
      1 ⎕JSON⍠'HighRank' 'Split'⊂4 invertedTable2_header
[{"item":"Knife","price":3,"qty":23},{"item":"Fork ","price":4,"qty":45},{"item":"Spoon","price":5,"qty":67}]
```

Note that the APL structure *can* be represented in JSON, though this is not a common way to represent a dataset:

```apl
      1(⎕JSON⍠'HighRank' 'Split')invertedTable2_header
[[["Knife","Fork ","Spoon"],[3,4,5],[23,45,67]],["item","price","qty"]]
```

#### Selection

A subset of a dataset's records (rows) and fields (columns) can be selected, with each subset being specified as a vector of indices.

To select a subset of the records, the wrapper takes the form:

```apl
      ⊂code dataset records
```

To select a subset of the fields, the wrapper takes the form:

```apl
      ⊂code dataset(⊂⍬)fields
```

To select a subset of the records and the fields , the wrapper takes the form:

```apl
      ⊂code dataset records fields
```

**Examples**

The following example selects the second record (Fork):

```apl
      1 ⎕JSON⊂4 invertedTable_header 2
[{"item":"Fork","Price":4,"qty":45}]
```

The following example selects the first and third fields (`item` and `qty`):

```apl
      1 ⎕JSON⊂4 invertedTable_header(⊂⍬)(1 3)
[{"item":"Knife","qty":23},{"item":"Fork","qty":45},{"item":"Spoon","qty":67}]
```

The following example selects the second record (Fork) and the first and third fields (item and qty):

```apl
      1 ⎕JSON⊂4 invertedTable_header 2(1 3)
[{"item":"Fork","qty":45}]
```

#### Namespaces and Sub-Arrays

Wrappers in namespaces and sub-arrays are recognised for special treatment.

**Example**

```apl
      1 ⎕JSON(test:⊂2 matrix)(⊂2 matrix)
[{"test":[{"item":"Knife","Price":3,"qty":23},{"item":"Fork","Price":4,"qty":45},{"item":"Spoon","Price":5,"qty":67}]},[{"item":"Knife","Price":3,"qty":23},{"item":"Fork","Price":4,"qty":45},{"item":"Spoon","Price":5,"qty":67}]]
```

## JSON Name Mangling

When Dyalog converts from JSON to APL data, and a member of a JSON object has a name which is not a valid APL name, it is renamed.

**Example**

In this example, the JSON describes an object containing two numeric items, one named `a` (which is a valid APL name) and the other named `2a` (which is not):
```apl
{"a": 1, "2a": 2}
```

When this JSON is imported as an APL namespace using `⎕JSON`, Dyalog converts the name `2a` to a valid APL name. The *name mangling* algorithm creates a name beginning with `⍙`.
```apl
      (0 ⎕JSON'{"a": 1, "2a": 2}').⎕NL 2
a  
⍙2a
```

When Dyalog exports JSON it performs the reverse *name mangling*, so:
```apl
      1 ⎕JSON 0 ⎕JSON'{"a": 1, "2a": 2}'
{"a":1,"2a":2}

```

Should you need to create and decode these names directly,`7162⌶` provides the same name mangling and un-mangling operations. See [JSON Translate Name](../primitive-operators/i-beam/json-translate-name.md).
```apl
      0(7162⌶)'2a'
⍙2a
      1(7162⌶)'⍙2a'
2a
```
