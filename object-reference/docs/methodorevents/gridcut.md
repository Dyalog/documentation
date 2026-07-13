# <span>GridCut</span> <span>Event 190</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user presses Shift+Delete and there are selected cells in the [Grid](../objects/grid.md). The default action of the event is to copy the contents of the selected block(s) of cells to the clipboard and then to empty the selected cells. You may disable this effect entirely by setting the action code of the event to `¯1`. You may also disable the cut operation by returning 0 from a callback function.


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows:


|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GridCut'` or 190|
|`[3]`|Start|2-element integer vector or matrix containing the row, column address(es) of the top left cell(s) in the selected block(s)|
|`[4]`|End|2-element integer vector or matrix containing the row, column address(es) of the bottom right cell in the selected block|
|`[5]`|Data|2-element nested vector. The first element is a matrix containing the values of the selected block(s) of cells. This is the data that will be copied to the clipboard. The second element is a Boolean matrix containing the values of the [CellSet](../properties/cellset.md) property for the selected block(s) of cells.|


Note that the values of Start and End are sensitive to the index origin, `⎕IO`.


If more than one block of cells is selected, Start and End are matrices whose rows identify the start and end cells of each of the selected blocks, and Data is the contents of the selected blocks catenated along the appropriate dimension according to their relative positions in the Grid.


The data copied to the clipboard is registered in Dyalog (APL internal), Wk3 (Lotus), XlTable (Excel) and tab/new-line delimited text formats.



