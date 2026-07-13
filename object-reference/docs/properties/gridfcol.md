# <span>GridFCol</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


The GridFCol property specifies the colour of the grid lines in a [Grid](../objects/grid.md) object.


GridFCol may be a 3-element vector of integer values  in the range 0-255 which refer to the red, green and blue components of the colour respectively, or it may be a scalar that defines a standard Windows colour element (see [BCol](bcol.md) for details). Its default value is 0 which obtains the colour defined for Window text.


The grid lines may be removed by setting GridFCol to the same colour as the background colour of the cells, which is defined by [BCol](bcol.md).


Finer control of the colour of the grid lines can be achieved by using [GridLineFCol](gridlinefcol.md) instead.


Unlike [GridLineFCol](gridlinefcol.md), the value of GridFCol is ignored when *Native Look and Feel* is enabled; the colour is taken from the current theme.



