# <span>RowChange</span> <span>Method 158</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This method is used to change the data in a row of a [Grid](../objects/grid.md) object.

The argument to RowChange is a 2-element array as follows.

|-----|----------|-------|
|`[1]`|Row number|integer|
|`[2]`|Row data  |array  |

*Row data* must be a scalar or a vector whose length is equal to the number of columns in the Grid. Its elements may be scalar numbers, character vectors or matrices.
