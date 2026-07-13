# <span>CellDblClick</span> <span>Event 163</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user double-clicks a mouse button whilst over a cell in a [Grid](../objects/grid.md). The purpose of this event is to allow an application to enable some special action on double-click. This event may not be disabled.


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 9 element vector as follows :


|-----|-----------|-----------------------------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                                              |
|`[2]`|Event      |`'CellDblClick'` or 163                                                                              |
|`[3]`|Y          |y-position of mouse (number)                                                                         |
|`[4]`|X          |x-position of mouse (number)                                                                         |
|`[5]`|Button     |button pressed (number) 1 = left button 2 =        right button 4 = middle button                    |
|`[6]`|Shift State|sum of shift key codes (number) 1 = Shift key        is down 2 = Ctrl key is down 4 = Alt key is down|
|`[7]`|Cell row   |integer                                                                                              |
|`[8]`|Cell column|integer                                                                                              |
|`[9]`|Title index|integer                                                                                              |


The y and x position of the mouse are reported relative to the top-left corner of the [Grid](../objects/grid.md).


The cell row and column are `⎕IO` dependent


If the user clicks over a row *title*, the value reported for the column is `¯1`, and the value reported for Title index is the index of that row title in [RowTitles](../properties/rowtitles.md), or, if [RowTitles](../properties/rowtitles.md) is not defined, the row number. Column titles are handled in a similar fashion.



