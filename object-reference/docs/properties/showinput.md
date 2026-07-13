# <span>ShowInput</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property specifies whether or not the cells in a [Grid](../objects/grid.md) are displayed using their associated input objects.



The ShowInput property is either a single Boolean value that applies to all the cells in a [Grid](../objects/grid.md), or it is a vector whose elements are mapped to individual cells via the [CellTypes](celltypes.md) property. A value of 0 means that the corresponding cell is displayed normally. A value of 1 indicates that the cell is displayed using its associated input object, as it is when it is the current cell. ShowInput is relevant to cells displayed using [Combo](../objects/combo.md) and [Button](../objects/button.md) objects.



The example below illustrates the appearance of a [Grid](../objects/grid.md) in which ShowInput is set to 0 for the Job Title column and 1 for the Region and Permanent columns.


![](../img/show1.gif)




The appearance of the same [Grid](../objects/grid.md) but with ShowInput set to 0 throughout is illustrated below:


![](../img/show2.gif)



