# <span>ClickComment</span> <span>Method 225</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, a ClickComment event is generated when the user clicks the mouse in a comment window of a [Grid](../objects/grid.md).


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'ClickComment'` or 225|
|`[3]`|Row   |integer                |
|`[4]`|Column|integer                |


The event message reports the co-ordinates of the cell. The default action is to raise the comment window so that it appears above all other, potentially overlapping, comment windows.


Note that if the comment window relates to a row or column *title*, the value reported in element [3] or [4] of the event message is `¯1`.



