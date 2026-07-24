# <span>CharFormat</span> <span>Property</span>

**Description**

The CharFormat property describes or applies formatting to the currently selected text in a [RichEdit](../objects/richedit.md) object. If the selection is empty, it reports or specifies the default character formatting for the object. It is a 5-element nested array structured as follows:

|---|---|
|`[1]`|A vector of character vectors which describes the text attributes and is comprised of the following keywords:<br/>`'Autocolour'` default colour (Windows text colour)<br/>`'Bold'` bold text<br/>`'Italic'` bold text<br/>`'Underline'` underlined<br/>`'StrikeOut'` line through text<br/>`'Protected'` protected (read-only) text|
|`[2]`|A character vector that specifies the face name of the font used to draw the text|
|`[3]`|Character height in [Twips](../miscellaneous/twips.md) .|
|`[4]`|Text colour. A single integer or an enclosed vector of 3 RGB values. The default is 0 which implies the standard Windows text colour.|
|`[5]`|Integer specifying the vertical offset of the character from the base line in [Twips](../miscellaneous/twips.md) . This is used to specify superscript (positive offset) and subscript (negative offset) symbols. The default value is 0.|

When you set the character format using `⎕WC` or `⎕WS` the following rules apply:

If you just want to set a single text attribute (element 1) you may specify a simple vector, for example `(⎕WS 'CharFormat' 'Protected')` is valid and will add the protected text attribute to the current set of text attributes.

To unset a text attribute (element 1) you must insert the tilde (~) character before the name of the attribute. For example, the expression `(⎕WS 'CharFormat' '~Bold')` will turn the bold text attribute off.

You need only specify the number of elements required, but you must insert proper values for the elements you wish to remain unaltered. However, you may use `''` in the first element to leave the text attributes unchanged.

If there is no text selected, CharFormat specifies the *default* character format, that is, the format that will be used to draw the next (and subsequent) characters that the user enters. If there *is* text selected it specifies the format of the selected block of text. If the format is not strictly homogeneous, `⎕WG` may report the format of the first character in the selected block, or, if the block contains characters which use completely different fonts, the result of `(⎕WG 'CharFormat')` will be empty.

`(⎕WS 'CharFormat' ...)` will set the format of the currently selected block of text. To set the format of an arbitrary block of text you must select it first using `(⎕WS 'SelText' ...)`.

**Application**

Objects: [RichEdit](../objects/richedit.md)
