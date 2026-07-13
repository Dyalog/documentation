# <span>GridPaste</span> <span>Event 192</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user presses Shift+Insert and there is data in the clipboard that is in a suitable format for the [Grid](../objects/grid.md). The default action of the event is to copy the contents of the clipboard into the currently selected block of cells, or, if no cells are selected, into the block of cells starting at the current cell (CurCell). Note that if there is a selected range of cells and the shape of the data being pasted does not exactly match the size of the selected range, the system generates a [GridPasteError](./gridpasteerror.md) event in addition to the GridPaste event.


You may disable the paste facility entirely by setting the action code of the event to `¯1`. You may also disable an individual paste operation by returning 0 from a callback function.



The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :


|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GridPaste'` or 192|
|`[3]`|Values|New values (taken from the clipboard) which are to replace the existing values of the block of cells defined by Start and End.|
|`[4]`|CellSet flags|Boolean Matrix containing the new values of the [CellSet](../properties/cellset.md) property for the block of cells defined by Start and End.|
|`[5]`|Start|2-element integer vector containing the row, column address of the top left cell the selected block. If there is no selection, this is the address of the current cell(CurCell).|
|`[6]`|End|2-element integer vector containing  the row, column address of the bottom right cell in the selected block. If there is no selection, this is the address of the bottom right cell of the block starting at the current cell that will be overwritten|



You can replace the contents of a contiguous block of cells with the data in the clipboard, or with an arbitrary matrix of values, by calling GridPaste as a method.


If you call GridPaste with an argument of `⍬`, the data is taken from the clipboard; otherwise the data to be pasted is specified by the *Values* and *CellSet flags* parameters.. If you omit *Start*, data is pasted into the currently selected range of cells. If there are no cells selected, data is pasted starting at the current cell (CurCell). In either case, the block of replaced cells becomes selected.


