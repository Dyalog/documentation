# <span>XML Convert</span> `⎕XML`

`⎕XML` converts between XML text and APL arrays. It imports when the right argument is a simple character vector, and exports when it is a matrix.

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

## Introduction to XML

XML is an open standard, designed to allow exchange of data between applications. The [full specification](http://www.w3.org/TR/2008/REC-xml-20081126/) describes functionality, including processing directives and other directives, which can transform XML data as it is read, and which a full XML processor would be expected to handle.

The `⎕XML` function is designed to handle XML to the extent required to import and export APL data. It favours speed over complexity – some markup is tolerated but largely ignored, and there are no XML query or validation features. An APL application that requires processing, querying, or validation calls an external tool for that, and then calls `⎕XML` on the resulting XML to transform it into APL arrays.

XML grammar such as processing instructions and document type declarations can optionally be stored in the APL array, but is not processed or validated. This is principally to allow regeneration of XML from XML input that contains such structures, although an APL application can process the data itself.

## Glossary of Terms

The XML definition uses specific terminology to describe its component parts. The following is a summary of the terms used in this section:

### Character Data

Character data consists of free-form text. The free-form text should not include the characters `>`, `<` or `&`, so these must be represented by their entity references (`&gt;`, `&lt;`, and `&amp;` respectively), or numeric character references.

### Entity References and Character References

Entity references are named representations of single characters that cannot normally be used in character data because they are used to delimit markup, such as `&gt;` for `>`. Character references are numeric representations of any character, such as `&#32;` for a space. Character references always take values in the Unicode code space, regardless of the encoding of the XML text itself.

There is a predefined set of entity references, and the XML specification allows others to be defined within the XML using the `<!ENTITY >` markup.

### Whitespace

Whitespace sequences consist of one or more spaces, tabs, or line endings. Line endings are represented differently on different systems: `0x0D 0x0A`, `0x0A`, and `0x0D` are all used.

### Elements

An element consists of a balanced pair of tags or a single empty element tag. Tags are given names, and start and end tag names must match.

An example pair of tags, named TagName, is `<TagName></TagName>`. This pair is shown with no content between the tags; this can be abbreviated as an empty element tag, `<TagName/>`.

Tags can be given zero or more attributes, which are specified as name/value pairs, for example `<TagName AttName="AttValue">`.

Attribute values can be delimited by either double quotes as shown or single quotes (apostrophes); they cannot contain certain characters (the delimiting quote, `&` or `<`) and these must be represented by entity or character references.

The content of elements can be zero or more mixed occurrences of character data and nested elements. Tags and attribute names *describe* data, attribute values and the content within tags contain the data itself. Nesting of elements allows structure to be defined.

Attributes with names beginning `xml:` are reserved. Only `xml:space` is treated specially by `⎕XML`. When converting both from and to XML, the value of this attribute has the following effects on space normalisation for the character data within this element and child elements within it, unless subsequently overridden:

- `default` – space normalisation is as determined by the `Whitespace` variant option.
- `preserve` – space normalisation is disabled; all whitespace is preserved as given.
- any other value – rejected.

Regardless of whether the attribute name and value have a recognised meaning, the attribute is included in the APL array or generated XML. When the names and values of attributes are examined, the comparisons are case-sensitive and take place after entity references and character references have been expanded.

### Comments

Comments are fully supported markup. They are delimited by `<!--` and `-->`, and all text between these delimiters is ignored.

### CDATA Sections

CDATA Sections are fully supported markup. They are used to delimit text within character data that has, or might have, markup text in it that is not to be processed as such. They are delimited by `<![CDATA[` and `]]>`.

### Processing Instructions

Processing Instructions are delimited by `<?` and `?>` but are otherwise treated as [other markup](#other-markup).

### Other Markup

The remainder of XML markup, including document type declarations, XML declarations, and text declarations, is delimited by `<!` and `>`, and can contain nested markup.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XML XML
</div>
