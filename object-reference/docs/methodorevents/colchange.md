# <span>ColChange</span> <span>Method 159</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This method is used to change the data in a column of a [Grid](../objects/grid.md).

The argument to ColChange is a 2-element array as follows:

|-----|-------------|-------|
|`[1]`|Column number|integer|
|`[2]`|Column data  |array  |

Note that the *Column data* must be a scalar or a vector whose length is equal to the number of rows in the [Grid](../objects/grid.md). Its elements may be scalar numbers, character vectors or matrices.
