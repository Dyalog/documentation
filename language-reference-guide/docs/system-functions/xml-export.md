---
search:
  boost: 2
---

# <span>Export XML</span> `R←{X} ⎕XML Y`{{key}}

This function converts an APL array to XML text. To convert XML to an APL array instead, see [Import XML](xml-import.md). For XML terminology and the extent to which `⎕XML` handles the standard, see [XML Convert](xml.md).

<h2 class="example">Example</h2>

```apl
      v←[0 'xml' ''  ⍬
         1 't'   'c' (,¨'as')]
      ⎕XML v
<xml>
  <t a="s">c</t>
</xml>
```

## Right Argument

`Y` is a 3, 4, or 5 column matrix, one row per node, whose columns are:

|Column|Description                                                          |
|------|---------------------------------------------------------------------|
|1     |Numeric value which indicates the level of nesting                   |
|2     |Element name, other markup text, or empty character vector when empty|
|3     |Character data or empty character vector when empty                  |
|4     |Attribute name and value pairs, ( `0 2⍴⊂''` ) when empty             |
|5     |A numeric value which indicates what the row contains                |

This is the form that [importing](xml-import.md#result) produces, so XML can be imported, edited as an array, and exported again. Some simplifications to the array are accepted:

- The fifth column is not needed for XML generation and is effectively ignored. Any numeric values are accepted, or the column can be omitted altogether. If the fifth column is omitted, then the fourth column can also be omitted.
- For the fourth column, if there are no attributes in a particular row, then the `(0 2⍴⊂'')` can be abbreviated as `⍬` (zilde). If there is only one attribute, then a 2-element vector can be specified.
- Data in the third column and attribute values in the fourth column (if present) can be provided as either character vectors or numeric values. Numeric values are implicitly formatted as if [`⎕PP`](pp.md) was set to 17.

The following validations are performed on the data in the array:

- All elements within the array are checked for type.
- Values in column 1 must be non-negative and start from level 0, and the increment from one row to the next must be `≤` +1.
- Tag names in column 2 and attribute names in column 4 (if present) must conform to the XML name definition.

## Left Argument

`X` is optional, and specifies [variant options](#variant-options) as a set of option/value pairs, each a character vector. `X` can be a 2-element vector, or a vector of 2-element character vectors. The [`⍠`](../primitive-operators/variant.md) operator is the recommended way to set these options; `X` is retained for backwards compatibility.

An option name or value is spelled differently here than for `⍠`: lower case throughout, with a dash inserted before a capital that is not the first letter. `UnknownEntity` is therefore `unknown-entity`, and `Preserve` is `preserve`. The names and values are case-sensitive either way.

## Result

`R` is a character vector containing the generated XML. Character references and entity references are emitted in place of characters where necessary, to ensure that valid XML is generated. However, markup, if present, is *not* validated, and it is possible to generate invalid XML if care is not taken with markup constructs.

## Variant Options

`⎕XML` supports three variant options, specified using the [`⍠`](../primitive-operators/variant.md) operator and summarised in [](#variant-table). There is no principal option. `Markup`, which affects only import, is tolerated here, but has no effect.

Table: Variant options { #variant-table }

|Variant Option|Value|Effect|
|---|:---:|---|
|[`Whitespace`](#variant-option-whitespace)|`'Strip'`<br><small>(default)</small>|Leading and trailing whitespace sequences are removed; remaining whitespace sequences within the data are replaced by a single space. `R` is formatted and indented to show the data structure|
||`'Trim'`|Synonymous with `'Strip'`|
|_-  -_|`'Preserve'`|Whitespace in the data is preserved as given, except that line endings are represented by Linefeed (`⎕UCS 10`). `R` has no formatting or indentation other than that contained within the data|
|[`UnknownEntity`](#variant-option-unknownentity)|`'Replace'`<br><small>(default)</small>|Esc (`⎕UCS 27`) in data is rejected|
|_-  -_|`'Preserve'`|Esc (`⎕UCS 27`) in data is replaced by `&`|
|`Markup`|&nbsp;|Only affects [import](xml-import.md#variant-options)|

### Variant Option: `Whitespace`

`Whitespace` specifies the default formatting of the generated XML, which the `xml:space` attribute can override. Attribute values are not character data, so whitespace in attribute values is always preserved.

<h4 class="example">Examples</h4>

```apl
      (⎕XML⍠'Whitespace' 'Strip')v
<xml>
  <t a="s">c</t>
</xml>

      (⎕XML⍠'Whitespace' 'Preserve')v
<xml><t a="s">c</t></xml>
```

### Variant Option: `UnknownEntity`

`UnknownEntity` determines what happens to Esc characters (`⎕UCS 27`) in data, which [import](xml-import.md#variant-option-unknownentity) puts there in place of the leading `&` of an unknown entity reference.

<h4 class="example">Examples</h4>

`'Preserve'` restores the `&`, so that an unknown entity reference survives a round trip:

```apl
      u←(⎕XML⍠'UnknownEntity' 'Preserve')'<a>&unknown;</a>'
      (⎕XML⍠'UnknownEntity' 'Preserve')u
<a>&unknown;</a>
```

`'Replace'`, the default, rejects the Esc rather than emitting it:

```apl
      ⎕XML u
DOMAIN ERROR: Invalid character in data in row 1
      ⎕XML u
      ∧
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XML XML
</div>
