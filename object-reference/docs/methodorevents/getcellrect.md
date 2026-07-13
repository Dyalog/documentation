# <span>GetCellRect</span> <span>Method 201</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This method returns the rectangle associated with a particular cell in a Grid.


The argument to GetCellRect is a 2-element vector as follows:


|-----|------|-------|
|`[1]`|Row   |integer|
|`[2]`|Column|integer|


The result is a 2-element nested vector. The first element contains the y and x-coordinate of the top-left corner of the cell. The second element contains the height and width of the cell.


The result is reported in terms of the coordinate system of the Grid object.



