# <span>GridDelete</span> <span>Event 193</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user presses Delete and there are selected cells in the [Grid](../objects/grid.md). The default action of the event is to empty the selected cells. You may disable this effect entirely by setting the action code of the event to `¯1`. You may also disable the delete operation by returning 0 from a callback function.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 4-element vector as follows:

|-----|------|------------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Object|ref or character vector                                                                                                       |
|`[2]`|Event |`'GridDelete'` or 193                                                                                                         |
|`[3]`|Start |2-element integer vector or matrix containing the row, column address(es) of the top left cell(s) in the selected block(s)    |
|`[4]`|End   |2-element integer vector or matrix containing the row, column address(es) of the bottom right cell(s) in the selected block(s)|

Note that the values of Start and End are sensitive to the index origin, `⎕IO`.

If more than one block of cells is selected, Start and End are matrices whose rows identify the start and end cells of each of the selected blocks.
