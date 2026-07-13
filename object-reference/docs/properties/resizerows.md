# <span>ResizeRows</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property determines whether or not the user may resize rows in the [Grid](../objects/grid.md). It is a Boolean scalar or vector with one element per column. A value of 1 indicates that the corresponding row is resizable by the user. A value of  0 means that the corresponding row may not be resized by the user.


If a row is resizable, the cursor changes to a double headed arrow when the mouse pointer is placed over the lower border of the row title. The user may change the height of the row by dragging this border up and down. The user may also resize a row by double-clicking over its bottom border. This causes the row to be resized to fit the data and the height of the row is automatically adjusted to display the tallest value in any of its cells. Either operation generates a [SetRowSize](../methodorevents/setrowsize.md) event.


Note that the user may cause the row to disappear altogether by dragging it to a zero height. Once this has been done, this row may only be restored if the row above it is itself not resizable.



