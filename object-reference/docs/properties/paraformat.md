# <span>ParaFormat</span> <span>Property</span>

**Description**

The ParaFormat property describes the current paragraph format or the paragraph format of the currently selected text in a [RichEdit](../objects/richedit.md) object. It is a 6-element nested array structured as follows:

|---|---|
|`[1]`|A character vector that specifies the text alignment. This may be `'Left'` (the default), `'Right'` or `'Centre'`|
|`[2]`|The size of the indentation of the first line in the paragraph measured from the left margin in [Twips](../miscellaneous/twips.md) .|
|`[3]`|The size of the horizontal offset of the start of the second and subsequent lines. This is measured in [Twips](../miscellaneous/twips.md) relative to the first line indentation specified in element [2].|
|`[4]`|The size of the right indentation measured in [Twips](../miscellaneous/twips.md) from the right margin.|
|`[5]`|An integer value specifying the bullet/numbering option. 0 mean no numbering, 1 means bullets.|
|`[6]`|An integer vector specifying the size of any tab stops measured in [Twips](../miscellaneous/twips.md) from the left margin and specified in ascending order.|

If there is no text selected, ParaFormat specifies the *current* paragraph formatting format, that is, that which will be used to format the current (and subsequent) lines of characters that the user enters. If there *is* text selected ParaFormat specifies the paragraph formatting of the selected block of text. If the format is not strictly homogeneous, `⎕WG` will report the format of the first paragraph in the selected block

`(⎕WS 'ParaFormat' ...)` will set the format of the currently selected block of text. To set the format of an arbitrary block of text you must select it first using `(⎕WS 'SelText' ...)`.

**Application**

Objects: [RichEdit](../objects/richedit.md)
