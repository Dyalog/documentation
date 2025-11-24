---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XML XML
</div>






<h1 class="heading"><span class="name">XML Convert</span> <span class="command">R←{X} ⎕XML Y</span></h1>



`⎕XML` converts an XML string into an APL array or converts an APL array into an XML string.


Options for `⎕XML` are specified using the Variant operator `⍠` or by the optional left argument `X`. The former is recommended but the older mechanism using the left argument is still supported.



For conversion *from* XML, `Y` is a character vector containing an XML string. The result `R` is a 5 column matrix whose columns are made up as follows:


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

<h2 class="example">Example</h2>
```apl
      x←'<xml><document id="001">An introduction to XML'
      x,←'</document></xml>'
```
```apl
      ]display v←⎕XML x
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


For conversion *to* XML, `Y` is a 3, 4 or 5 column matrix and the result `R` is a character vector. The columns of `Y` have the same meaning as those described above for the result of converting *from* XML.

<h2 class="example">Example</h2>
```apl
      ⎕XML v
<xml> 
  <document id="001">An introduction to XML</document>
</xml>
```

## Introduction to XML and Glossary of Terms


XML is an open standard, designed to allow exchange of data between applications. The full specification [^1] describes functionality, including processing directives and other directives, which can transform XML data as it is read, and which a full XML processor would be expected to handle.


The `⎕XML` function is designed to handle XML to the extent required to import and export APL data. It favours speed over complexity - some markup is tolerated but largely ignored, and there are no XML query or validation features. APL applications which require processing, querying or validation will need to call external tools for this, and finally call `⎕XML` on the resulting XML to perform the transformation into APL arrays.


XML grammar such as processing instructions, document type declarations etc. may optionally be stored in the APL array, but will not be processed or validated. This is principally to allow regeneration of XML from XML input which contains such structures, but an APL application could process the data if it chose to do so.


The XML definition uses specific terminology to describe its component parts. The following is a summary of the terms used in this section:

### Character Data


Character data consists of free-form text. The free-form text should not include the characters '>', '<' or '&', so these must be represented by their entity references ('&gt;', '&lt;' and '&amp;' respectively), or numeric character references.

### Entity References and Character References


Entity references are named representations of single characters which cannot normally be used in character data because they are used to delimit markup, such as &gt; for '>'. Character references are numeric representations of any character, such as &#20; for space. Note that character references always take values in the Unicode code space, regardless of the encoding of the XML text itself.


`⎕XML` converts entity references and all character references which the APL character set is able to represent into their character equivalent when generating APL array data; when generating XML it converts any or all characters to entity references as needed.


There is a predefined set of entity references, and the XML specification allows others to be defined within the XML using the `<!ENTITY >` markup. `⎕XML` does not process these additional declarations and therefore will only convert the predefined types.

### Whitespace


Whitespace sequences consist of one or more spaces, tabs or line-endings. Within character data, sequences of one or more whitespace characters are replaced with a single space when this is enabled by the whitespace option. Line endings are represented differently on different systems (0x0D 0x0A, 0x0A and 0x0D are all used) but are normalized by converting them all to 0x0A before the XML is parsed, regardless of the setting of the whitespace option.

### Elements


An element consists of a balanced pair of tags or a single empty element tag. Tags are given names, and start and end tag names must match.


An example pair of tags, named TagName is


`<TagName></TagName>`


This pair is shown with no content between the tags; this may be abbreviated as an empty element tag as


`<TagName/>`


Tags may be given zero or more attributes, which are specified as name/value pairs; for example


`<TagName AttName="AttValue">`


Attribute values may be delimited by either double quotes as shown or single quotes (apostrophes); they may not contain certain characters (the delimiting quote, '&' or '<') and these must be represented by entity or character references.


The content of elements may be zero or more mixed occurrences of character data and nested elements. Tags and attribute names *describe* data, attribute values and the content within tags contain the data itself. Nesting of elements allows structure to be defined.


Because certain markup which describes the format of allowable data (such as element type declarations and attribute-list declarations) is not processed, no error will be reported if element contents and attributes do not conform to their restricted declarations, nor are attributes automatically added to tags if not explicitly given.


Attributes with names beginning **xml:** are reserved. Only **xml:space** is treated specially by `⎕XML`. When converting both from and to XML, the value for this attribute has the following effects on space normalization for the character data within this element and child elements within it (unless subsequently overridden):

- **default** – space normalization is as determined by the **whitespace** option. 
- **preserve** - space normalization is disabled – all whitespace is preserved as given.
- **any other value** – rejected.


Regardless of whether the attribute name and value have a recognised meaning, the attribute will be included in the APL array / generated XML. Note that when the names and values of attributes are examined, the comparisons are case-sensitive and take place after entity references and character references have been expanded.

### Comments


Comments are fully supported markup. They are delimited by '<!--' and '-->' and all text between these delimiters is ignored. This text is included in the APL array if markup is being preserved, or discarded otherwise.

### CDATA Sections


CDATA Sections are fully supported markup. They are used to delimit text within character data which has, or may have, markup text in it which is not to be processed as such. They and are delimited by '<![CDATA[' and ']]>'. CDATA sections are never recorded in the APL array as markup when XML is processed – instead, that data appears as character data. Note that this means that if you convert XML to an APL array and then convert this back to XML, CDATA sections will not be regenerated. It is, however, *possible* to generate CDATA sections in XML by presenting them as markup.

### Processing Instructions


Processing Instructions are delimited by '<&' and '&>' but are otherwise treated as other markup, below.

### Other markup


The remainder of XML markup, including document type declarations,  XML declarations and text declarations are all delimited by '<!' and '>', and may contain nested markup. If markup is being preserved the text, including nested markup, will appear as a single row in the APL array.  `⎕XML` does not process the contents of such markup. This has varying effects, including but not limited to the following:

- No validation is performed.
- Constraints specified in markup such element type declarations will be ignored and therefore syntactically correct elements which fall outside their constraint will not be rejected.
- Default attributes in attribute-list declarations will not be automatically added to elements.
- Conditional sections will always be ignored.
- Only standard, predefined, entity references will be recognized; entity declarations which define others entity references will have no effect.
- External entities are not processed.

## Conversion from XML

- The level number in the first column of the result `R` is 0 for the outermost level and subsequent levels are represented by an increase of 1 for each level. Thus, for
- <xml><document id="001">An introduction to XML </document></xml>
- The *xml* element is at level 0 and the *document id* element is at level 1. The text within the *document id* element is at level 2.
- Each tag in the XML contains an element name and zero or more attribute name and value pairs, delimited by '<' and '>' characters. The delimiters are not included in the result matrix. The element name of a tag is stored in column 2 and the attribute(s) in column 4.
- All XML markup other than tags are delimited by either '<!' and '>', or '<?' and '>' characters. By default these are not stored in the result matrix but the **markup** option may be used to specify that they are. The elements are stored in their entirety, except for the leading and trailing '<' and '>' characters, in column 2. Nested constructs are treated as a single block. Because the leading and trailing '<' and '>' characters are stripped, such entries will always have either '!' or '&' as the first character.
- Character data itself has no tag name or attributes. As an optimisation, when character data is the sole content of an element, it is included with its parent rather than as a separate row in the result. Note that when this happens, the level number stored is that of the parent; the data itself implicitly has a level number one greater.
- Attribute name and value pairs associated with the element name are stored in the fourth column, in an (*n x 2*) matrix of character values, for the *n* (including zero) pairs.
- Each row is further described in the fifth column as a convenience to simplify processing of the array (although this information could be deduced). Any given row may contain an entry for an element, character data, markup not otherwise defined, a comment or a processing instruction. Furthermore, an element will have zero or more of these as children. For all types except elements, the value in the fifth column is as shown above. For elements, the value is computed by adding together the value of the row itself (1) and those of its children. For example, the value for a row for an element which contains one or more sub-elements and character data is 7 – that is 1 (element) + 2 (child element) + 4 (character data). It should be noted that:
- Odd values always represent elements. Odd values other than 1 indicate that there are children.
- Elements which contain just character data (5) are combined into a single row as noted previously.
- Only immediate children are considered when computing the value. For example, an element which contains a sub-element which in turn contains character data does not itself contain the character data.
- The computed value is derived from what is actually preserved in the array. For example, if the source XML contains an element which contains a comment, but comments are being discarded, there will be no entry for the comment in the array and the fifth column for the element will not indicate that it has a child comment.


### Conversion to XML


Conversion to XML takes an array with the format described above and generates XML text from it. There are some simplifications to the array which are accepted:

- The fifth column is not needed for XML generation and is effectively ignored. Any numeric values are accepted, or the column may be omitted altogether. If the fifth column is omitted then the fourth column may also be omitted.
- For the fourth column, if there are no attributes in a particular row then the `(0 2⍴⊂'')` may be abbreviated as `⍬` (zilde). If there is only one attribute then a 2-element vector can be specified.
- Data in the third column and attribute values in the fourth column (if present) may be provided as either character vectors or numeric values. Numeric values are implicitly formatted as if `⎕PP` was set to 17.




The following validations are performed on the data in the array:

- All elements within the array are checked for type.
- Values in column 1 must be non-negative and start from level 0, and the increment from one row to the next must be `≤` +1. 
- Tag names in column 2 and attribute names in column 4 (if present) must conform to the XML name definition.



Then, character references and entity references are emitted in place of characters where necessary, to ensure that valid XML is generated. However, markup, if present, is *not* validated and it is possible to generate invalid XML if care in not taken with markup constructs.

### Options


There are 3 options which may be specified using the Variant operator `⍠` (recommended) or by the optional left argument `X` (retained for backwards compatibility). The names are different and are case-sensitive; they must be spelled exactly as shown below.


|Option names for Variant|Option names for left argument|
|------------------------|------------------------------|
|Whitespace              |whitespace                    |
|Markup                  |markup                        |
|UnknownEntity           |unknown-entity                |


The values of each option are tabulated below. In each case the value of the option for Variant is given first, followed by its equivalent for the optional left argument in brackets; for example, **UnknownEntity (unknown-entity)**.


Note that the default value is shown first, and that the option names and values are case-sensitive.


If options are specified using the optional left argument,  `X` specifies a set of option/value pairs, each of which is a character vector. `X` can be a 2-element vector, or a vector of 2-element character vectors. In the examples below, this method is illustrated by the equivalent expression written as a comment, following the recommended approach using the Variant operator `⍠`:
```apl

      ]display (⎕XML⍠'Whitespace' 'Strip')eg
      ⍝      'whitespace' 'strip' ⎕XML eg
```


Errors detected in the input arrays or options will all cause `DOMAIN ERROR`.

### Whitespace (whitespace)


When converting from XML `Whitespace` specifies the default handling of white space surrounding and within character data. When converting to XML `Whitespace` specifies the default formatting of the XML. Note that attribute values are not comprised of character data so white space in attribute values is always preserved.


|Converting from XML||
|---|---|
|Strip (strip)|All leading and trailing whitespace sequences are removed; remaining whitespace sequences are replaced by a single space character|
|`Trim(trim)`|All leading and trailing whitespace sequences are removed; all remaining white space sequences are handled as preserve|
|`Preserve(preserve)`|Whitespace is preserved as given except that line endings are represented by Linefeed 				( `⎕UCS 10` )|
|Converting to XML||
|Strip (strip)|All leading and trailing whitespace sequences are removed; remaining whitespace sequences within the data are replaced by a single space character. XML is generated with formatting and indentation to show the data structure|
|`Trim(trim)`|Synonymous with `strip`|
|`Preserve(preserve)`|White space in the data is preserved as given, except that line endings are represented by Linefeed 				( `⎕UCS 10` ). XML is generated with no formatting and indentation other than that which is contained within the data|
```apl

      ]display eg
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
```apl
 
      ]display (⎕XML⍠'Whitespace' 'Strip')eg
      ⍝      'whitespace' 'strip' ⎕XML eg
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
      ]display (⎕XML⍠'Whitespace' 'Preserve')eg
      ⍝         'whitespace' 'preserve' ⎕XML eg
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

### Markup (markup)


When converting from XML, `Markup` determines whether markup (other than entity tags) appears in the output array or not. When converting to XML `Markup` has no effect.


|Converting from XML                                                                                                                       ||
|--------------------|----------------------------------------------------------------------------------------------------------------------|
|Strip (strip)       |Markup data is not included in the output array                                                                       |
|`Preserve(preserve)`|Markup text appears in the output array, without the leading '<' and trailing '>' in the tag (2 <sup>nd</sup> ) column|
```apl
  
      ]display eg
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
```apl

      ]display (⎕XML⍠'Markup' 'Strip')eg
      ⍝      'markup' 'strip' ⎕XML eg
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
      ]display (⎕XML⍠'Markup' 'Preserve')eg
      ⍝         'markup' 'preserve' ⎕XML eg
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

### UnknownEntity (unknown-entity)


When converting from XML, this option determines what happens when an unknown entity reference, or a character reference for a Unicode character which cannot be represented as an APL character, is encountered. In Classic versions of Dyalog APL that is any Unicode character which does not appear in `⎕AVU`. When converting to XML, this option determines what happens to Esc characters (`⎕UCS 27`) in data.


|Converting from XML                                                                                                              ||
|--------------------|-------------------------------------------------------------------------------------------------------------|
|Replace (replace)   |The reference is replaced by a single '?' character                                                          |
|`Preserve(preserve)`|The reference is included in the output data as given, but with the leading '&' replaced by Esc ( `⎕UCS 27` )|
|Converting to XML                                                                                                                ||
|Replace (replace)   |Esc ( `⎕UCS 27` ) is preserved                                                                               |
|`Preserve(preserve)`|Esc ( `⎕UCS 27` ) is replaced by '&'                                                                         |




[^1]: http://www.w3.org/TR/2008/REC-xml-20081126/