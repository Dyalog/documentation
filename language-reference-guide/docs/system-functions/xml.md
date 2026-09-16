# <span>XML Convert</span> `⎕XML`

`⎕XML` converts between XML text and APL arrays. It imports when the right argument is a simple character vector, and exports otherwise.

## [Import XML](xml-import.md)

A character vector holding XML is converted to a five-column matrix describing it:

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

## [Export XML](xml-export.md)

Such a matrix is converted back to XML text:

```apl
      ⎕XML v
<xml>
  <t a="s">c</t>
</xml>
```

## Introduction to XML and Glossary of Terms

XML is an open standard, designed to allow exchange of data between applications. The [full specification](http://www.w3.org/TR/2008/REC-xml-20081126/) describes functionality, including processing directives and other directives, which can transform XML data as it is read, and which a full XML processor would be expected to handle.

The `⎕XML` function is designed to handle XML to the extent required to import and export APL data. It favours speed over complexity - some markup is tolerated but largely ignored, and there are no XML query or validation features. APL applications which require processing, querying or validation will need to call external tools for this, and finally call `⎕XML` on the resulting XML to perform the transformation into APL arrays.

XML grammar such as processing instructions and document type declarations can optionally be stored in the APL array, but will not be processed or validated. This is principally to allow regeneration of XML from XML input which contains such structures, but an APL application could process the data if it chose to do so.

The XML definition uses specific terminology to describe its component parts. The following is a summary of the terms used in this section:

### Character Data

Character data consists of free-form text. The free-form text should not include the characters `>`, `<` or `&`, so these must be represented by their entity references (`&gt;`, `&lt;`, and `&amp;` respectively), or numeric character references.

### Entity References and Character References

Entity references are named representations of single characters that cannot normally be used in character data because they are used to delimit markup, such as `&gt;` for `>`. Character references are numeric representations of any character, such as `&#32;` for a space. Character references always take values in the Unicode code space, regardless of the encoding of the XML text itself.

`⎕XML` converts entity references and all character references which the APL character set is able to represent into their character equivalent when generating APL array data; when generating XML it converts any or all characters to entity references as needed.

There is a predefined set of entity references, and the XML specification allows others to be defined within the XML using the `<!ENTITY >` markup. `⎕XML` does not process these additional declarations and therefore will only convert the predefined types.

### Whitespace

Whitespace sequences consist of one or more spaces, tabs or line-endings. Within character data, sequences of one or more whitespace characters are replaced with a single space when this is enabled by the whitespace option. Line endings are represented differently on different systems (0x0D 0x0A, 0x0A and 0x0D are all used) but are normalized by converting them all to 0x0A before the XML is parsed, regardless of the setting of the whitespace option.

### Elements

An element consists of a balanced pair of tags or a single empty element tag. Tags are given names, and start and end tag names must match.

An example pair of tags, named TagName is

`<TagName></TagName>`

This pair is shown with no content between the tags; this can be abbreviated as an empty element tag as

`<TagName/>`

Tags can be given zero or more attributes, which are specified as name/value pairs; for example

`<TagName AttName="AttValue">`

Attribute values can be delimited by either double quotes as shown or single quotes (apostrophes); they cannot contain certain characters (the delimiting quote, `&` or `<`) and these must be represented by entity or character references.

The content of elements can be zero or more mixed occurrences of character data and nested elements. Tags and attribute names *describe* data, attribute values and the content within tags contain the data itself. Nesting of elements allows structure to be defined.

Because certain markup which describes the format of allowable data (such as element type declarations and attribute-list declarations) is not processed, no error will be reported if element contents and attributes do not conform to their restricted declarations, nor are attributes automatically added to tags if not explicitly given.

Attributes with names beginning **xml:** are reserved. Only **xml:space** is treated specially by `⎕XML`. When converting both from and to XML, the value for this attribute has the following effects on space normalization for the character data within this element and child elements within it (unless subsequently overridden):

- **default** – space normalisation is as determined by the `Whitespace` variant option. 
- **preserve** - space normalization is disabled – all whitespace is preserved as given.
- **any other value** – rejected.

Regardless of whether the attribute name and value have a recognised meaning, the attribute will be included in the APL array / generated XML. When the names and values of attributes are examined, the comparisons are case-sensitive and take place after entity references and character references have been expanded.

### Comments

Comments are fully supported markup. They are delimited by `<!--` and `-->` and all text between these delimiters is ignored. This text is included in the APL array if markup is being preserved, or discarded otherwise.

### CDATA Sections

CDATA Sections are fully supported markup. They are used to delimit text within character data which has, or might have, markup text in it which is not to be processed as such. They and are delimited by `<![CDATA[` and `]]>`. CDATA sections are never recorded in the APL array as markup when XML is processed – instead, that data appears as character data. This means that if you convert XML to an APL array and then convert this back to XML, CDATA sections are not regenerated. It is, however, possible to generate CDATA sections in XML by presenting them as markup.

### Processing Instructions

Processing Instructions are delimited by `<&` and `&>` but are otherwise treated as other markup, below.

### Other Markup

The remainder of XML markup, including document type declarations,  XML declarations and text declarations are all delimited by `<!` and `>`, and can contain nested markup. If markup is being preserved the text, including nested markup, will appear as a single row in the APL array.  `⎕XML` does not process the contents of such markup. This has varying effects, including but not limited to the following:

- No validation is performed.
- Constraints specified in markup such element type declarations will be ignored and therefore syntactically correct elements which fall outside their constraint will not be rejected.
- Default attributes in attribute-list declarations will not be automatically added to elements.
- Conditional sections will always be ignored.
- Only standard, predefined, entity references will be recognized; entity declarations which define others entity references will have no effect.
- External entities are not processed.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XML XML
</div>
