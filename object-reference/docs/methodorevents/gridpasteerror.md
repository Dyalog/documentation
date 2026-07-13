# <span>GridPasteError</span> <span>Event 194</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user presses Shift+Insert and
there is data in the clipboard, but the system is unable to paste the data into
the [Grid](../objects/grid.md). This occurs if there is a currently
selected block of cells whose shape does not match the shape of the data in the
clipboard. It also occurs if there is no selected block of cells, and pasting
the data in starting at the current cell (CurCell) would overflow the [Grid](../objects/grid.md).
Setting the action code of this event to `¯1`, or returning a 0 from a callback function attached to it, has no effect.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq),
or supplied as the right argument to your callback function, is a 6-element
vector as follows:

|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GridPasteError'` or 194|
|`[3]`|Values|Contents of the clipboard.|
|`[4]`|CellSet flags|Boolean array indicating which elements of the clipboard data are         empty.|
|`[5]`|Start|2-element integer vector containing the row, column address of the top         left cell in the selected block. If there is no selection, this is the         address of the current cell (CurCell).|
|`[6]`|End|2-element integer vector containing the row, column address of the         bottom right cell in the selected block. If there is no selection, this         is the address of the bottom right cell of the block starting at the         current cell that will be overwritten|
|`[7]`|Error Number|`4 (RANK ERROR)` or `5         (LENGTH ERROR)`|
