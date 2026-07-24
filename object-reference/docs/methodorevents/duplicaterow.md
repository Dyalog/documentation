# <span>DuplicateRow</span> <span>Method 177</span>

**Description**

This method is used to duplicate a row in a [Grid](../objects/grid.md) object.

The argument to DuplicateRow is a 2, 3, 4 or 5-element vector as follows:

|-----|-----------------|--------------------------------------------|
|`[1]`|Source Row number|number of the row (integer) to be duplicated|
|`[2]`|Target Row number|new row number (integer)                    |
|`[3]`|Comment flag     |0 or 1 (optional, default 1)                |
|`[4]`|Lock flag        |0 or 1 (optional, default 1)                |
|`[5]`|Undo flag        |0 or 1 (optional; default 0)                |

If the *Comment flag* is 1 (the default), any Comments associated with cells in the source row are duplicated in the target row.

If the *Lock flag* is 1 (the default), the lock state of the row is duplicated; otherwise, the new row is not locked.

If the *Undo flag* is 1, the row may subsequently be restored by invoking the Undo method. If this element is omitted or is 0, the operation may not be undone.

**Application**

Objects: [Grid](../objects/grid.md)
