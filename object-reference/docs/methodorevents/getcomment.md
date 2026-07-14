# <span>GetComment</span> <span>Method 222</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This method is used to retrieve the comment associated with a cell in a [Grid](../objects/grid.md).

The argument to GetComment is a 2-element array as follows:

|-----|------|-------|
|`[1]`|Row   |integer|
|`[2]`|Column|integer|

For example, the following expression retrieves the comment associated with the cell at row 3, column 1.
```apl
      F.C.GetComment 3 1
 1 3  Hello  175 100
```

Note that to retrieve a comment associated with a row or column *title*, the appropriate element in the argument should be `¯1`.

If there is no comment associated with the specified cell, the result is a scalar 1.
