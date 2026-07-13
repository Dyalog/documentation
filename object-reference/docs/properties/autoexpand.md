# <span>AutoExpand</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property is a 2-element Boolean value that specifies whether or not rows and columns may be added to a [Grid](../objects/grid.md) object by the user.


If the first element of AutoExpand is 1, a row is added when the current cell is within the last row of the [Grid](../objects/grid.md) and the user presses Cursor Down


Similarly, if the second element is 1, a column is added when the current cell is within the last column of the [Grid](../objects/grid.md) and the user presses Cursor Right.


Note that when a row or column is added, the appropriate properties (including [Values](values.md) and [CellTypes](celltypes.md)) are expanded accordingly.


The default value for AutoExpand is (0 0).


If AutoExpand is enabled, the [Grid](../objects/grid.md) generates [AddRow](../methodorevents/addrow.md) and [AddCol](../methodorevents/addcol.md) events. You can return a zero from a callback function to selectively prevent the addition of rows and columns if appropriate.


