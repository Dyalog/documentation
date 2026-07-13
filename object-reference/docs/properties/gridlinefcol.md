# <span>GridLineFCol</span> <span>Property</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

The GridLineFCol property specifies the colours of the grid lines in a [Grid](../objects/grid.md) object. GridLineFCol should be used if different coloured grid lines are required. If all the grid lines are the same colour, use [GridFCol](gridfcol.md).

GridLineFCol may be a scalar or a vector. Each item may be a 3-element vector of integer values in the range 0-255 which refer to the red, green and blue components of the colour respectively, or a scalar that defines a standard Windows colour element (see [BCol](bcol.md) for details). Note that a single RGB triplet must be enclosed.

The default value of GridLineFCol is an empty numeric vector (`⍬`). If so, all the grid lines are drawn using the single colour specified by [GridFCol](gridfcol.md).

Unlike [GridFCol](gridbcol.md), setting GridLineFCol overrides the colour which would be used if *Native Look and Feel* was enabled.

Elements of GridLineFCol are allocated to individual grid lines via the [RowLineTypes](rowlinetypes.md) and [ColLineTypes](collinetypes.md) properties.

See also: [GridLineWidth](gridlinewidth.md).
