# <span>ResizeColTitles</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property determines whether or not the user may alter the height of the column titles in the [Grid](../objects/grid.md). It is either 1, which indicates that the height of the column titles is adjustable by the user, or 0 which means that it is not.


If the height of the column titles is adjustable, the cursor changes to a double headed arrow when the mouse pointer is placed over the top border of the first row title  The user may resize the column titles by dragging this border. The user may also resize the column titles by double-clicking over this border. This causes the column titles to be resized to fit the data and the height of the column titles is automatically adjusted to display the tallest heading in any of its columns. Either operation generates a [SetRowSize](../methodorevents/setrowsize.md) event. The value of the row number reported by the event is `¯1`.


Note that the user may cause the column titles to disappear altogether by dragging them to a zero height. Once this has been done, the row titles cannot be restored.



