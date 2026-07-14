# <span>ResizeCols</span> <span>Property</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This property determines whether or not the user may resize columns in the [Grid](../objects/grid.md). It is a Boolean scalar or vector with one element per column. A value of 1 indicates that the corresponding column is resizable by the user. A value of  0 means that the corresponding column may not be resized by the user.

If a column is resizable, the cursor changes to a double headed arrow when the mouse pointer is placed over the right-hand border of the column title. The user may resize the column by dragging this border. The user may also resize a column by double-clicking over its right-hand border. This causes the column to be resized to fit the data and the width of the column is automatically adjusted to display the widest value in any of its cells. Either operation generates a [SetColSize](../methodorevents/setcolsize.md) event.

Note that the user may cause the column to disappear altogether by dragging it to a zero width. Once this has been done, this column may only be restored if the column to its left is itself not resizable.
