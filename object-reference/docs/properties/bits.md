# <span>Bits</span> <span>Property</span>

**Description**

This property defines the pattern in a [Bitmap](../objects/bitmap.md), [Cursor](../objects/cursor.md), or [Icon](../objects/icon.md) object, or the pattern of a bitmap stored in the Windows clipboard.

For a [Bitmap](../objects/bitmap.md), [Clipboard](../objects/clipboard.md) or [Icon](../objects/icon.md), Bits is an integer matrix each of whose elements represents the colour of the corresponding pixel in the bitmap. The colours are specified as 0-origin indices into the [CMap](cmap.md) property, which itself defines the complete set of different colours (the colour map) used by the object.

Please note that Bits and [CMap](cmap.md) may **only** be used to represent an image with a colour palette of **256 colours or less**. If the colour palette is larger, the values of Bits and [CMap](cmap.md) reported by `⎕WG` will be (0 0). For a high-colour image, use [CBits](cbits.md) instead.

For a [Cursor](../objects/cursor.md), Bits is a Boolean matrix which specifies the shape of the cursor. For a [Cursor](../objects/cursor.md) and [Icon](../objects/icon.md), Bits is used in conjunction with the [Mask](mask.md) property.

See [CMap](cmap.md) for further details.

**Application**

Objects: [Bitmap](../objects/bitmap.md), [Clipboard](../objects/clipboard.md), [Cursor](../objects/cursor.md), [Icon](../objects/icon.md)
