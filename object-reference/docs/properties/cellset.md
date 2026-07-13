# <span>CellSet</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property identifies which cells in a [Grid](../objects/grid.md) are *set* (that is, have values) and which are empty. Its purpose is to allow large numeric matrices containing blank cells to be displayed and edited efficiently.


The CellSet property is a Boolean matrix with the same shape as the [Values](values.md) property. If an element of CellSet is 0, the cell is defined to be empty. Empty cells are displayed as blank and the cell contents by the [Values](values.md) property are ignored.


A more direct way to handle empty cells is to set  the corresponding elements of [Values](values.md) to empty vectors. However, if [Values](values.md) is otherwise entirely numeric, this makes the array nested when it would otherwise be simple. For large numeric matrices, this penalty can be severe. For example, a 100x100 array of 2-byte integer values occupies about 20Kb of workspace. Setting one or more elements of the array to an empty vector increases its size to 200Kb. However, because it is Boolean, the size of the CellSet property for a 100x100 array is only 1.27Kb and represents a significant space saving.


Note that if the [Values](values.md) property contains text and is therefore nested anyway, the CellSet property is not helpful in conserving workspace, although it may still be useful to separate empty cells from real data.


You can dynamically change a single element of CellSet using the [SetCellSet](../methodorevents/setcellset.md) method.



