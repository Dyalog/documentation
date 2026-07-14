# <span>GridCopy</span> <span>Event 191</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user presses Ctrl+Insert and there are selected cells in the [Grid](../objects/grid.md). The default action of the event is to copy the contents of the selected block of cells to the clipboard. You may disable this effect entirely by setting the action code of the event to `¯1`. You may also disable the copy operation by returning 0 from a callback function.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows:

|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GridCopy'` or 191|
|`[3]`|Start|2-element integer vector or matrix containing the row, column address(es) of the top left cell(s) in the selected block(s)|
|`[4]`|End|2-element integer vector or matrix containing the row, column address(es) of the bottom right cell(s) in the selected block|
|`[5]`|Values|2-element nested vector. The first element is a matrix containing the values of the selected block(s) of cells. This is the data that will be copied to the clipboard. The second element is a Boolean matrix containing the values of the [CellSet](../properties/cellset.md) property for the selected block(s) of cells.|

Note that the values of Start and End are sensitive to the index origin, `⎕IO`.

If more than one block of cells is selected, Start and End are matrices whose rows identify the start and end cells of each of the selected blocks, and Data is the contents of the selected blocks catenated along the appropriate dimension according to their relative positions in the Grid.

You may copy cells under program control by calling GridCopy as a method.

To copy a specific block of cells to the clipboard whether or not they are selected, you must specify the Start and End parameters. For example, the following expression will copy the 3x3 block of cells in the top-left of the Grid (`⎕IO` is 1) to the clipboard:
```apl
     Gridname.GridCopy (1 1) (3 3)
```

If you omit these parameters, the currently selected block of cells will be copied to the clipboard. If no cells are selected, the entire contents of the Grid will be copied. That is:
```apl
     Gridname.GridCopy ⍬
```

The data copied to the clipboard is registered in Dyalog (APL internal), Wk3 (Lotus), XlTable (Excel) and tab/new-line delimited text formats.
