# <span>AlignChar</span> <span>Property</span>

**Description**

The AlignChar property specifies a character on which the data displayed in a column of a Grid is to be aligned vertically. It is useful to align columns of numbers that are formatted by the [FormatString](formatstring.md) property. AlignChar may be a scalar or singleton that applies to all columns of the Grid, or a vector with one element per column.

If the data in the column is left-justified, it is aligned using the first occurrence of the alignment character in each cell counting from the left. If the data is right-justified, it is aligned using the first occurrence of the alignment character from the right-hand end of the text.

If the text in a cell does not contain an alignment character, it is aligned as if the alignment character were placed following the last digit.

**Application**

Objects: [Grid](../objects/grid.md)
