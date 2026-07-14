# <span>Size</span> <span>Property</span>

[**Applies To**](../propertyapplies/size.md)

**Description**

This is a 2-element numeric vector specifying the height and width of the object.

For the [Bitmap](../objects/bitmap.md) object, Size is set and reported in pixels. Setting the Size of a [Bitmap](../objects/bitmap.md) causes it to be scaled (up or down).

For all other objects, Size is reported and set in units defined by the [Coord](coord.md) property and, if [Coord](coord.md) is `'User'`, the [XRange](xrange.md) and [YRange](yrange.md) properties of the object's parent.

For the [Root](../objects/root.md) object, if [Coord](coord.md) is `'Prop'` the value of Size is (100,100). If [Coord](coord.md) is `'Pixel'` the value of Size reports the number of pixels on the screen.

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), the Size property defines the area within the object, and excludes its title bar, menu bar and border if these are present.

For a [Combo](../objects/combo.md) object with a "drop-down" list, the first element of Size (height) is ignored. The height of the edit field is determined by the height of the font, while the size of the list box is determined by the [Rows](rows.md) property.

Otherwise the Size property defines the total size of the object, including borders, edges etc.

When specifying Size, you can set the height or width to a default value (`⎕WC`) or leave it unchanged (`⎕WS`) by giving the corresponding element a value of `⍬`.
