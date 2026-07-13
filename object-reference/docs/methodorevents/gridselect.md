# <span>GridSelect</span> <span>Event 165</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user performs or cancels the selection of a block of cells in a [Grid](../objects/grid.md) object. This event is reported after the selection has changed. Setting its action code to `¯1` has no effect and the result of a callback function cannot be used to alter the selection that has been made. You may however control the user's ability to make selections using the [CellSelect](../properties/cellselect.md) property.


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------|---------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Object|ref or character vector                                                                                                    |
|`[2]`|Event |`'GridSelect'` or 165                                                                                                      |
|`[3]`|Start |2-element integer vector or matrix containing the row, column address(es) of the top left cell(s) in the selected block(s) |
|`[4]`|End   |2-element integer vector or matrix containing the row, column address(es) of the bottom right cell(s) in the selected block|


Note that the values of Start and End are sensitive to the index origin, `⎕IO`.


If the selection is made with the mouse, the GridSelect event is reported when the left mouse button is released. If the selection is made using the cursor keys, the GridSelect event is reported when the Shift key is released.


The GridSelect event is also generated when the current selection is cancelled by clicking on a cell with the mouse or by pressing a cursor key.



