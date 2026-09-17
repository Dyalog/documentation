---
search:
  boost: 2
---

# <span>Import XML</span> `R←{X} ⎕XML Y`{{key}}

This function converts XML text to an APL array. To convert an APL array to XML instead, see [Export XML](xml-export.md). For XML terminology and the extent to which `⎕XML` handles the standard, see [XML Convert](xml.md).

<h2 class="example">Example</h2>

```apl
      v←⎕XML'<xml><t a="s">c</t></xml>'
      v
┌─┬───┬─┬─────┬─┐
│0│xml│ │     │3│
├─┼───┼─┼─────┼─┤
│1│t  │c│┌─┬─┐│5│
│ │   │ ││a│s││ │
│ │   │ │└─┴─┘│ │
└─┴───┴─┴─────┴─┘
```

## Right Argument

`Y` is a character vector containing an XML string.

## Left Argument

`X` is optional, and specifies [variant options](#variant-options) as a set of option/value pairs, each a character vector. `X` can be a 2-element vector, or a vector of 2-element character vectors. The [`⍠`](../primitive-operators/variant.md) operator is the recommended way to set these options; `X` is retained for backwards compatibility.

An option name or value is spelled differently from its `⍠` form: lower case throughout, with a dash before a capital that is not the first letter. `UnknownEntity` is therefore `unknown-entity`, and `Preserve` is `preserve`. The names and values are case-sensitive either way.

## Result

`R` is a 5-column matrix, one row per node, whose columns are:

|Column|Description                                                          |
|------|---------------------------------------------------------------------|
|1     |Numeric value that indicates the level of nesting                    |
|2     |Element name, other markup text, or empty character vector when empty|
|3     |Character data or empty character vector when empty                  |
|4     |Attribute name and value pairs, ( `0 2⍴⊂''` ) when empty             |
|5     |A numeric value that indicates what the row contains                 |

The values in column 5 have the following meanings:

|Value|Description                  |
|-----|-----------------------------|
|1    |Element                      |
|2    |Child element                |
|4    |Character data               |
|8    |Markup not otherwise defined |
|16   |Comment markup               |
|32   |Processing instruction markup|

These values are additive. For example, a value of 5 in column 5 means that the row contains both an element (value 1) and character data (value 4).

### How the Result is Built

The level number in column 1 is `0` for the outermost level, and each subsequent level is one greater. Thus, for `<xml><document id="001">An introduction to XML</document></xml>` the _xml_ element is at level `0`, the _document id_ element at level `1`, and the text within the _document id_ element at level `2`.

Each tag contains an element name and zero or more attribute name and value pairs, delimited by `<` and `>` characters. The delimiters are not included in the result. The element name is stored in column 2, and the attributes in column 4 as an *n*×2 matrix of character values for the *n* (including zero) pairs.

All XML markup other than tags is delimited by either `<!` and `>`, or `<?` and `>` characters. By default these are not stored in the result, but the [`Markup`](#variant-option-markup) variant option can be used to specify that they are. Such markup is stored in column 2 in its entirety, except for the leading and trailing `<` and `>` characters, and nested constructs are treated as a single block. Because those characters are stripped, such entries always have either `!` or `?` as the first character.

Character data itself has no tag name or attributes. As an optimisation, when character data is the sole content of an element it is included with its parent rather than as a separate row. The level number stored is then that of the parent; the data itself implicitly has a level number one greater.

Column 5 describes each row as a convenience to simplify processing of the array, although this information could be deduced. A row can contain an entry for an element, character data, markup not otherwise defined, a comment, or a processing instruction, and an element has zero or more of these as children. For all types except elements the value is as shown above; for an element it is the value of the row itself (`1`) added to those of its children, so an element containing one or more sub-elements and character data is `7`, that is `1` (element) + `2` (child element) + `4` (character data). In addition:

- Odd values always represent elements. Odd values other than `1` indicate that there are children.
- Elements that contain just character data (`5`) are combined into a single row, as noted above.
- Only immediate children are considered when computing the value. For example, an element that contains a sub-element that in turn contains character data does not itself contain the character data.
- The computed value is derived from what is actually preserved in the array. For example, if the source XML contains an element that contains a comment, but comments are being discarded, there is no entry for the comment in the array, and column 5 for the element does not indicate that it has a child comment.

## Limitations

`⎕XML` does not process the contents of markup other than tags, so no validation takes place. This has varying effects, including but not limited to the following:

- Constraints specified in markup such as element type declarations are ignored, so syntactically correct elements that fall outside their constraint are not rejected.
- Default attributes in attribute-list declarations are not automatically added to elements.
- Conditional sections are always ignored.
- Only standard, predefined entity references are recognised; entity declarations that define other entity references have no effect, so `⎕XML` converts only the predefined types.
- External entities are not processed.

Because markup that describes the format of allowable data is not processed, no error is reported if element contents and attributes do not conform to their restricted declarations.

A [CDATA section](xml.md#cdata-sections) is never recorded as markup: its content appears as character data instead. XML imported to an APL array and exported again therefore has no CDATA sections, although [Export XML](xml-export.md#result) can generate them from markup.

## Variant Options

`⎕XML` supports three variant options, `Whitespace`, `Markup`, and `UnknownEntity`, specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md), summarised in [](#variantoptionsforxml), and described in detail beneath it. There is no principal option.

Table: Variant options for `⎕XML` { #variantoptionsforxml }

|Variant Option|Value|Effect|
|---|:---:|---|
|[`Whitespace`](#variant-option-whitespace)|`'Strip'`<br><small>(default)</small>|Leading and trailing whitespace sequences are removed; remaining whitespace sequences are replaced by a single space|
||`'Trim'`|Leading and trailing whitespace sequences are removed; all remaining whitespace sequences are handled as for `'Preserve'`|
|_-  -_|`'Preserve'`|Whitespace is preserved as given, except that line endings are represented by Linefeed (`⎕UCS 10`)|
|[`Markup`](#variant-option-markup)|`'Strip'`<br><small>(default)</small>|Markup data is not included in `R`|
|_-  -_|`'Preserve'`|Markup text appears in `R`, without the leading `<` and trailing `>` of the tag, in the second column|
|[`UnknownEntity`](#variant-option-unknownentity)|`'Replace'`<br><small>(default)</small>|The reference is replaced by a single `?` character|
|_-  -_|`'Preserve'`|The reference is included in the data as given, but with the leading `&` replaced by Esc (`⎕UCS 27`)|

The examples below all use this XML:

```apl
      eg←∊(
          '<xml>'
          '  <a>'
          '    Data1'
          '    <!-- Comment -->'
          '    Data2'
          '    <b> Data3 </b>'
          '    Data4'
          '    <c att="val"/>'
          '  </a>'
          '</xml>'
      ),¨⎕UCS 10
```

### Variant Option: `Whitespace`

The `Whitespace` variant option specifies the default handling of whitespace surrounding and within character data, which the `xml:space` attribute can override. Attribute values are not character data, so whitespace in attribute values is always preserved. The default is `'Strip'`.

Line endings are normalised to `0x0A` before the XML is parsed, whatever `Whitespace` is set to.

<h4 class="example">Examples</h4>

```apl
      (⎕XML⍠'Whitespace' 'Strip')eg
┌─┬───┬───────────┬─────────┬─┐
│0│xml│           │         │3│
├─┼───┼───────────┼─────────┼─┤
│1│a  │           │         │7│
├─┼───┼───────────┼─────────┼─┤
│2│   │Data1 Data2│         │4│
├─┼───┼───────────┼─────────┼─┤
│2│b  │Data3      │         │5│
├─┼───┼───────────┼─────────┼─┤
│2│   │Data4      │         │4│
├─┼───┼───────────┼─────────┼─┤
│2│c  │           │┌───┬───┐│1│
│ │   │           ││att│val││ │
│ │   │           │└───┴───┘│ │
└─┴───┴───────────┴─────────┴─┘
```

```apl
      (⎕XML⍠'Whitespace' 'Preserve')eg
┌─┬───┬─────────┬─────────┬─┐
│0│xml│         │         │7│
├─┼───┼─────────┼─────────┼─┤
│1│   │         │         │4│
│ │   │         │         │ │
├─┼───┼─────────┼─────────┼─┤
│1│a  │         │         │7│
├─┼───┼─────────┼─────────┼─┤
│2│   │         │         │4│
│ │   │    Data1│         │ │
│ │   │         │         │ │
│ │   │    Data2│         │ │
│ │   │         │         │ │
├─┼───┼─────────┼─────────┼─┤
│2│b  │ Data3   │         │5│
├─┼───┼─────────┼─────────┼─┤
│2│   │         │         │4│
│ │   │    Data4│         │ │
│ │   │         │         │ │
├─┼───┼─────────┼─────────┼─┤
│2│c  │         │┌───┬───┐│1│
│ │   │         ││att│val││ │
│ │   │         │└───┴───┘│ │
├─┼───┼─────────┼─────────┼─┤
│2│   │         │         │4│
│ │   │         │         │ │
├─┼───┼─────────┼─────────┼─┤
│1│   │         │         │4│
│ │   │         │         │ │
└─┴───┴─────────┴─────────┴─┘
```

### Variant Option: `Markup`

The `Markup` variant option determines whether markup, other than entity tags, appears in `R`. The text of a [comment](xml.md#comments) is therefore kept when `Markup` is `'Preserve'`, and discarded otherwise. The default is `'Strip'`.

<h4 class="example">Examples</h4>

```apl
      (⎕XML⍠'Markup' 'Strip')eg
┌─┬───┬───────────┬─────────┬─┐
│0│xml│           │         │3│
├─┼───┼───────────┼─────────┼─┤
│1│a  │           │         │7│
├─┼───┼───────────┼─────────┼─┤
│2│   │Data1 Data2│         │4│
├─┼───┼───────────┼─────────┼─┤
│2│b  │Data3      │         │5│
├─┼───┼───────────┼─────────┼─┤
│2│   │Data4      │         │4│
├─┼───┼───────────┼─────────┼─┤
│2│c  │           │┌───┬───┐│1│
│ │   │           ││att│val││ │
│ │   │           │└───┴───┘│ │
└─┴───┴───────────┴─────────┴─┘
```

```apl
      (⎕XML⍠'Markup' 'Preserve')eg
┌─┬──────────────┬─────┬─────────┬──┐
│0│xml           │     │         │3 │
├─┼──────────────┼─────┼─────────┼──┤
│1│a             │     │         │23│
├─┼──────────────┼─────┼─────────┼──┤
│2│              │Data1│         │4 │
├─┼──────────────┼─────┼─────────┼──┤
│2│!-- Comment --│     │         │16│
├─┼──────────────┼─────┼─────────┼──┤
│2│              │Data2│         │4 │
├─┼──────────────┼─────┼─────────┼──┤
│2│b             │Data3│         │5 │
├─┼──────────────┼─────┼─────────┼──┤
│2│              │Data4│         │4 │
├─┼──────────────┼─────┼─────────┼──┤
│2│c             │     │┌───┬───┐│1 │
│ │              │     ││att│val││  │
│ │              │     │└───┴───┘│  │
└─┴──────────────┴─────┴─────────┴──┘
```

### Variant Option: `UnknownEntity`

The `UnknownEntity` variant option determines what happens when an unknown entity reference, or a character reference for a Unicode character that cannot be represented as an APL character, is encountered. In Classic versions of Dyalog APL this is any Unicode character that does not appear in [`⎕AVU`](avu.md). The default is `'Replace'`.

<h4 class="example">Examples</h4>

```apl
      (⎕XML⍠'UnknownEntity' 'Replace')'<a>&unknown;</a>'
┌─┬─┬─┬───┬─┐
│0│a│?│   │5│
└─┴─┴─┴───┴─┘
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
