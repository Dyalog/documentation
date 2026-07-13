# <span>ResizeRowTitles</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property determines whether or not the user may alter the width of the row titles in the [Grid](../objects/grid.md). It is either 1, which indicates that the width of the row titles is adjustable by the user, or 0 which means that it is not.


If the width of the row titles is adjustable, the cursor changes to a double headed arrow when the mouse pointer is placed over the left-hand border of the first column title. The user may resize the row titles by dragging this border. The user may also resize the row titles by double-clicking over this border. This causes the row titles to be resized to fit the data and the width of the row titles is automatically adjusted to display the longest string in any of its rows. Either operation generates a [SetColSize](../methodorevents/setcolsize.md) event. The value of the column number reported by the event is `¯1`.


Note that the user may cause the row titles to disappear altogether by dragging them to a zero width. Once this has been done, the row titles cannot be restored.



