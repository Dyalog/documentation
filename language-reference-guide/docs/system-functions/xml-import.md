---
search:
  boost: 2
---

# <span>Import XML</span> `R←{X} ⎕XML Y`{{key}}

This function converts XML text to an APL array. To convert an APL array to XML instead, see [Export XML](xml-export.md). For XML terminology and the extent to which `⎕XML` handles the standard, see [XML Convert](xml.md).

<h2 class="example">Example</h2>

```apl
      x←'<xml><document id="001">An introduction to XML'
      x,←'</document></xml>'

      ]Display v←⎕XML x
┌→───────────────────────────────────────────────────────┐
↓   ┌→──┐      ┌⊖┐                      ┌→────────┐      │
│ 0 │xml│      │ │                      ⌽ ┌⊖┐ ┌⊖┐ │    3 │
│   └───┘      └─┘                      │ │ │ │ │ │      │
│                                       │ └─┘ └─┘ │      │
│                                       └∊────────┘      │
│   ┌→───────┐ ┌→─────────────────────┐ ┌→───────────┐   │
│ 1 │document│ │An introduction to XML│ ↓ ┌→─┐ ┌→──┐ │ 5 │
│   └────────┘ └──────────────────────┘ │ │id│ │001│ │   │
│                                       │ └──┘ └───┘ │   │
│                                       └∊───────────┘   │
└∊───────────────────────────────────────────────────────┘
```

## Right Argument

`Y` is a character vector containing an XML string.

## Left Argument

`X` is optional, and specifies [variant options](#variant-options) as a set of option/value pairs, each a character vector. `X` can be a 2-element vector, or a vector of 2-element character vectors. The [`⍠`](../primitive-operators/variant.md) operator is the recommended way to set these options; `X` is retained for backwards compatibility.

## Result

`R` is a 5 column matrix whose columns are made up as follows:

|Column|Description                                                          |
|------|---------------------------------------------------------------------|
|1     |Numeric value which indicates the level of nesting                   |
|2     |Element name, other markup text, or empty character vector when empty|
|3     |Character data or empty character vector when empty                  |
|4     |Attribute name and value pairs, ( `0 2⍴⊂''` ) when empty             |
|5     |A numeric value which indicates what the row contains                |

The values in column 5  have the following meanings:

|Value|Description                  |
|-----|-----------------------------|
|1    |Element                      |
|2    |Child element                |
|4    |Character data               |
|8    |Markup not otherwise defined |
|16   |Comment markup               |
|32   |Processing instruction markup|

These values are additive. For example, a value of 5 in column 5 means that the row contains both an element (value 1) and character data (value 4).

## How the Result is Built

- The level number in the first column of the result `R` is 0 for the outermost level and subsequent levels are represented by an increase of 1 for each level. Thus, for "&lt;xml>&lt;document id="001">An introduction to XML &lt;/document>&lt;/xml>&lt;/code>" the _xml_ element is at level 0 and the _document id_ element is at level 1. The text within the _document id_ element is at level 2.
- Each tag in the XML contains an element name and zero or more attribute name and value pairs, delimited by `<` and `>` characters. The delimiters are not included in the result matrix. The element name of a tag is stored in column 2 and the attribute(s) in column 4.
- All XML markup other than tags are delimited by either `<!` and `>`, or `<?` and `>` characters. By default these are not stored in the result matrix but the `Markup` option can be used to specify that they are. The elements are stored in their entirety, except for the leading and trailing `<` and `>` characters, in column 2. Nested constructs are treated as a single block. Because the leading and trailing `<` and `>` characters are stripped, such entries will always have either `!` or `&` as the first character.
- Character data itself has no tag name or attributes. As an optimisation, when character data is the sole content of an element it is included with its parent rather than as a separate row in the result. When this happens, the level number stored is that of the parent; the data itself implicitly has a level one number greater.
- Attribute name and value pairs associated with the element name are stored in the fourth column, in an (*n x 2*) matrix of character values, for the *n* (including zero) pairs.
- Each row is further described in the fifth column as a convenience to simplify processing of the array (although this information could be deduced). Any given row can contain an entry for an element, character data, markup not otherwise defined, a comment or a processing instruction. Furthermore, an element will have zero or more of these as children. For all types except elements, the value in the fifth column is as shown above. For elements, the value is computed by adding together the value of the row itself (1) and those of its children. For example, the value for a row for an element which contains one or more sub-elements and character data is 7 – that is 1 (element) + 2 (child element) + 4 (character data). In addition:
- Odd values always represent elements. Odd values other than 1 indicate that there are children.
- Elements which contain just character data (5) are combined into a single row as noted previously.
- Only immediate children are considered when computing the value. For example, an element which contains a sub-element which in turn contains character data does not itself contain the character data.
- The computed value is derived from what is actually preserved in the array. For example, if the source XML contains an element which contains a comment, but comments are being discarded, there will be no entry for the comment in the array and the fifth column for the element will not indicate that it has a child comment.

## Variant Options

`⎕XML` supports three variant options, specified using the [`⍠`](../primitive-operators/variant.md) operator and summarised in [](#variant-table), or through the optional [left argument](#left-argument) using the alternative name shown in the table. There is no principal option. The names and values are case-sensitive and must be written exactly as shown.

Table: Variant options { #variant-table }

|Variant Option|Left-argument name|Value|Effect|
|---|---|:---:|---|
|[`Whitespace`](#variant-option-whitespace)|`whitespace`|`'Strip'`<br><small>(default)</small>|Leading and trailing whitespace sequences are removed; remaining whitespace sequences are replaced by a single space|
|_-  -_||`'Trim'`|Leading and trailing whitespace sequences are removed; all remaining whitespace sequences are handled as for `'Preserve'`|
|_-  -_||`'Preserve'`|Whitespace is preserved as given, except that line endings are represented by Linefeed (`⎕UCS 10`)|
|[`Markup`](#variant-option-markup)|`markup`|`'Strip'`<br><small>(default)</small>|Markup data is not included in `R`|
|_-  -_||`'Preserve'`|Markup text appears in `R`, without the leading `<` and trailing `>` of the tag, in the second column|
|[`UnknownEntity`](#variant-option-unknownentity)|`unknown-entity`|`'Replace'`<br><small>(default)</small>|The reference is replaced by a single `?` character|
|_-  -_||`'Preserve'`|The reference is included in the data as given, but with the leading `&` replaced by Esc (`⎕UCS 27`)|

Errors detected in the input array or options all cause `DOMAIN ERROR`.

The examples below all use this XML:

```apl
      eg←¯1↓∊{⍵,⎕UCS 10}¨'<xml>' '  <a>' '    Data1' '    <!-- Comment -->' '    Data2' '    <b> Data3 </b>' '    Data4' '    <c att="val"/>' '  </a>' '</xml>'
      ]Display eg
┌→───────────────────┐
│<xml>               │
│  <a>               │
│    Data1           │
│    <!-- Comment -->│
│    Data2           │
│    <b> Data3 </b>  │
│    Data4           │
│    <c att="val"/>  │
│  </a>              │
│</xml>              │
└────────────────────┘
```

### Variant Option: `Whitespace`

`Whitespace` specifies the default handling of whitespace surrounding and within character data, which the `xml:space` attribute can override. Attribute values are not character data, so whitespace in attribute values is always preserved.

<h4 class="example">Examples</h4>

```apl
      ]Display (⎕XML⍠'Whitespace' 'Strip')eg
┌→────────────────────────────────────────┐
↓   ┌→──┐ ┌⊖┐           ┌→────────┐       │
│ 0 │xml│ │ │           ⌽ ┌⊖┐ ┌⊖┐ │     3 │
│   └───┘ └─┘           │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌⊖┐           ┌→────────┐       │
│ 1 │a│   │ │           ⌽ ┌⊖┐ ┌⊖┐ │     7 │
│   └─┘   └─┘           │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌⊖┐   ┌→──────────┐ ┌→────────┐       │
│ 2 │ │   │Data1 Data2│ ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   └───────────┘ │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌→────┐       ┌→────────┐       │
│ 2 │b│   │Data3│       ⌽ ┌⊖┐ ┌⊖┐ │     5 │
│   └─┘   └─────┘       │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌⊖┐   ┌→────┐       ┌→────────┐       │
│ 2 │ │   │Data4│       ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   └─────┘       │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌⊖┐           ┌→────────────┐   │
│ 2 │c│   │ │           ↓ ┌→──┐ ┌→──┐ │ 1 │
│   └─┘   └─┘           │ │att│ │val│ │   │
│                       │ └───┘ └───┘ │   │
│                       └∊────────────┘   │
└∊────────────────────────────────────────┘
```

```apl
      ]Display (⎕XML⍠'Whitespace' 'Preserve')eg
┌→──────────────────────────────────────┐
↓   ┌→──┐ ┌⊖┐         ┌→────────┐       │
│ 0 │xml│ │ │         ⌽ ┌⊖┐ ┌⊖┐ │     7 │
│   └───┘ └─┘         │ │ │ │ │ │       │
│                     │ └─┘ └─┘ │       │
│                     └∊────────┘       │
│   ┌⊖┐   ┌→─┐        ┌→────────┐       │
│ 1 │ │   │  │        ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   │  │        │ │ │ │ │ │       │
│         └──┘        │ └─┘ └─┘ │       │
│                     └∊────────┘       │
│   ┌→┐   ┌⊖┐         ┌→────────┐       │
│ 1 │a│   │ │         ⌽ ┌⊖┐ ┌⊖┐ │     7 │
│   └─┘   └─┘         │ │ │ │ │ │       │
│                     │ └─┘ └─┘ │       │
│                     └∊────────┘       │
│   ┌⊖┐   ┌→────────┐ ┌→────────┐       │
│ 2 │ │   │         │ ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   │    Data1│ │ │ │ │ │ │       │
│         │         │ │ └─┘ └─┘ │       │
│         │    Data2│ └∊────────┘       │
│         │         │                   │
│         └─────────┘                   │
│   ┌→┐   ┌→──────┐   ┌→────────┐       │
│ 2 │b│   │ Data3 │   ⌽ ┌⊖┐ ┌⊖┐ │     5 │
│   └─┘   └───────┘   │ │ │ │ │ │       │
│                     │ └─┘ └─┘ │       │
│                     └∊────────┘       │
│   ┌⊖┐   ┌→────────┐ ┌→────────┐       │
│ 2 │ │   │         │ ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   │    Data4│ │ │ │ │ │ │       │
│         │         │ │ └─┘ └─┘ │       │
│         └─────────┘ └∊────────┘       │
│   ┌→┐   ┌⊖┐         ┌→────────────┐   │
│ 2 │c│   │ │         ↓ ┌→──┐ ┌→──┐ │ 1 │
│   └─┘   └─┘         │ │att│ │val│ │   │
│                     │ └───┘ └───┘ │   │
│                     └∊────────────┘   │
│   ┌⊖┐   ┌→─┐        ┌→────────┐       │
│ 2 │ │   │  │        ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   │  │        │ │ │ │ │ │       │
│         └──┘        │ └─┘ └─┘ │       │
│                     └∊────────┘       │
│   ┌⊖┐   ┌→┐         ┌→────────┐       │
│ 1 │ │   │ │         ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   │ │         │ │ │ │ │ │       │
│         └─┘         │ └─┘ └─┘ │       │
│                     └∊────────┘       │
└∊──────────────────────────────────────┘
```

### Variant Option: `Markup`

`Markup` determines whether markup, other than entity tags, appears in `R`. It has no effect on [export](xml-export.md#variant-options).

<h4 class="example">Examples</h4>

```apl

      ]Display (⎕XML⍠'Markup' 'Strip')eg
┌→────────────────────────────────────────┐
↓   ┌→──┐ ┌⊖┐           ┌→────────┐       │
│ 0 │xml│ │ │           ⌽ ┌⊖┐ ┌⊖┐ │     3 │
│   └───┘ └─┘           │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌⊖┐           ┌→────────┐       │
│ 1 │a│   │ │           ⌽ ┌⊖┐ ┌⊖┐ │     7 │
│   └─┘   └─┘           │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌⊖┐   ┌→──────────┐ ┌→────────┐       │
│ 2 │ │   │Data1 Data2│ ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   └───────────┘ │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌→────┐       ┌→────────┐       │
│ 2 │b│   │Data3│       ⌽ ┌⊖┐ ┌⊖┐ │     5 │
│   └─┘   └─────┘       │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌⊖┐   ┌→────┐       ┌→────────┐       │
│ 2 │ │   │Data4│       ⌽ ┌⊖┐ ┌⊖┐ │     4 │
│   └─┘   └─────┘       │ │ │ │ │ │       │
│                       │ └─┘ └─┘ │       │
│                       └∊────────┘       │
│   ┌→┐   ┌⊖┐           ┌→────────────┐   │
│ 2 │c│   │ │           ↓ ┌→──┐ ┌→──┐ │ 1 │
│   └─┘   └─┘           │ │att│ │val│ │   │
│                       │ └───┘ └───┘ │   │
│                       └∊────────────┘   │
└∊────────────────────────────────────────┘
```

```apl
      ]Display (⎕XML⍠'Markup' 'Preserve')eg
┌→──────────────────────────────────────────────┐
↓   ┌→──┐            ┌⊖┐     ┌→────────┐        │
│ 0 │xml│            │ │     ⌽ ┌⊖┐ ┌⊖┐ │     3  │
│   └───┘            └─┘     │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌→┐              ┌⊖┐     ┌→────────┐        │
│ 1 │a│              │ │     ⌽ ┌⊖┐ ┌⊖┐ │     23 │
│   └─┘              └─┘     │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌⊖┐              ┌→────┐ ┌→────────┐        │
│ 2 │ │              │Data1│ ⌽ ┌⊖┐ ┌⊖┐ │     4  │
│   └─┘              └─────┘ │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌→─────────────┐ ┌⊖┐     ┌→────────┐        │
│ 2 │!-- Comment --│ │ │     ⌽ ┌⊖┐ ┌⊖┐ │     16 │
│   └──────────────┘ └─┘     │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌⊖┐              ┌→────┐ ┌→────────┐        │
│ 2 │ │              │Data2│ ⌽ ┌⊖┐ ┌⊖┐ │     4  │
│   └─┘              └─────┘ │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌→┐              ┌→────┐ ┌→────────┐        │
│ 2 │b│              │Data3│ ⌽ ┌⊖┐ ┌⊖┐ │     5  │
│   └─┘              └─────┘ │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌⊖┐              ┌→────┐ ┌→────────┐        │
│ 2 │ │              │Data4│ ⌽ ┌⊖┐ ┌⊖┐ │     4  │
│   └─┘              └─────┘ │ │ │ │ │ │        │
│                            │ └─┘ └─┘ │        │
│                            └∊────────┘        │
│   ┌→┐              ┌⊖┐     ┌→────────────┐    │
│ 2 │c│              │ │     ↓ ┌→──┐ ┌→──┐ │ 1  │
│   └─┘              └─┘     │ │att│ │val│ │    │
│                            │ └───┘ └───┘ │    │
│                            └∊────────────┘    │
└∊──────────────────────────────────────────────┘
```

### Variant Option: `UnknownEntity`

`UnknownEntity` determines what happens when an unknown entity reference, or a character reference for a Unicode character that cannot be represented as an APL character, is encountered. In Classic versions of Dyalog APL this is any Unicode character that does not appear in [`⎕AVU`](avu.md).

<h4 class="example">Examples</h4>

```apl
      ]Display (⎕XML⍠'UnknownEntity' 'Replace')'<a>&unknown;</a>'
┌→────────────────────────┐
↓   ┌→┐ ┌→┐ ┌→────────┐   │
│ 0 │a│ │?│ ⌽ ┌⊖┐ ┌⊖┐ │ 5 │
│   └─┘ └─┘ │ │ │ │ │ │   │
│           │ └─┘ └─┘ │   │
│           └∊────────┘   │
└∊────────────────────────┘
```

With `'Preserve'`, the reference survives as given, with Esc in place of the leading `&`:

```apl
      u←(⎕XML⍠'UnknownEntity' 'Preserve')'<a>&unknown;</a>'
      ⎕UCS⊃u[1;3]
27 117 110 107 110 111 119 110 59
```

Such data cannot be [exported](xml-export.md#variant-option-unknownentity) unless `UnknownEntity` is `'Preserve'` there too, which turns the Esc back into `&`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XML XML
</div>
