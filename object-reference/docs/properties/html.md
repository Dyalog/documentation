# <span>HTML</span> <span>Property</span>

**Description**

The HTML property is a character vector that specifies the content to be rendered by the [HTMLRenderer](../objects/htmlrenderer.md) object. Dyalog does not perform any pre-processing of the text nor does it verify that it is properly formed HTML using single-byte  character data, including any necessary escaping and encoding.

See also: [URL](url.md).

!!! note
    Typically, you will need to UTF-8 encode any text outside the Unicode range 0-127.

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
