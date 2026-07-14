# <span>ComboEx</span> <span>Object</span>

[Parents](../parentlists/comboex.md), [Children](../childlists/comboex.md), [Properties](../proplists/comboex.md), [Methods](../methodlists/comboex.md), [Events](../eventlists/comboex.md)

**Purpose:** The ComboEx object is an extended version of the Combo object that provides additional features including item images

**Description**

The ComboEx object is a ComboBox that supports item images and indenting. It is a superset of the [Combo](combo.md) object and supports all its functionality. For further details, see ["Combo"](combo.md).

For most purposes, you can use the ComboEx object in place of the [Combo](combo.md) object whether or not you make use of the extended features of the ComboEx.

Like the basic [Combo](combo.md), the list of text items in the ComboEx is specified by the [Items](../properties/items.md) property. You may associate images with each of the text items using the [ImageListObj](../properties/imagelistobj.md), [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) properties.

To do so, [ImageListObj](../properties/imagelistobj.md) specifies the name of an ImageList object that contains a set of images. [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) map individual images from the ImageList to each of the text items specified by Items. [ImageIndex](../properties/imageindex.md) specifies the image to be displayed when the item is not selected; [SelImageIndex](../properties/selimageindex.md) specifies the image to be displayed when the item is selected.

The [Indents](../properties/indents.md) property specifies the amount by which each of the items are indented in units of 10 pixels

The appearance of the items is additionally controlled by the [EditImage](../properties/editimage.md) and [EditImageIndent](../properties/editimageindent.md) properties. These are Boolean and their effect is summarised in the table below. Notice that Images are displayed only if both these properties are set to 1 (which is the default).

There are certain restrictions that apply to a ComboEx object with Style `'Simple'`, namely:

- images and indents do not apply to the edit control portion of the object.
- the object may not redraw properly if [EditImage](../properties/editimage.md) and/or [EditImageIndent](../properties/editimageindent.md) are set to 0 or if [CaseSensitive](../properties/casesensitive.md) or [PathWordBreak](../properties/pathwordbreak.md) are set to 1.
- [PathWordBreak](../properties/pathwordbreak.md) does not work.

|&nbsp;|EditImageIndent||
|---|---|---|
|EditImage|0|1|
|0|No images displayed, item text is indented as specified by [Indents](../properties/indents.md)|No images displayed, item text is indented as specified by [Indents](../properties/indents.md) plus the width of the images in ImageList|
|1|No images displayed, item text is indented as specified by [Indents](../properties/indents.md)|Images are displayed, items are indented as specified by [Indents](../properties/indents.md)|
