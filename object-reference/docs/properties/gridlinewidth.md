# <span>GridLineWidth</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


The GridLineWidth property specifies the widths in pixels of the grid lines in a [Grid](../objects/grid.md) object.



GridLineWidth may be an integer scalar or a vector. Its default value is an empty numeric vector (`⍬`). If so, grid lines are drawn 1-pixel wide.


Grid lines are always displayed so that 1 pixel is drawn *within* the cell. If the width is greater than 1 pixel, the additional pixels are drawn *between* the cells.


If an element of GridLineWidth is 0, the corresponding grid lines are not drawn.


Elements of GridLineWidth are allocated to individual grid lines via the [RowLineTypes](rowlinetypes.md) and [ColLineTypes](collinetypes.md) properties.


See also: [GridLineFCol](gridlinefcol.md).


