# <span>CellOver</span> <span>Event 160</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user moves the mouse pointer whilst over a cell in a [Grid](../objects/grid.md).



There is no default action for this event.



The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is an 9 element vector as follows :


|-----|-----------|-------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                                              |
|`[2]`|Event      |`'CellOver'` or 160                                                                                  |
|`[3]`|Y          |y-position of mouse (number)                                                                         |
|`[4]`|X          |x-position of mouse (number)                                                                         |
|`[5]`|Button     |button pressed (number)<br/>1 = left button<br/>2 = right button<br/>4 = middle button |
|`[6]`|Shift State|sum of shift key codes (number)<br/>1 = Shift key is down<br/>2 = Ctrl key is down<br/>4 = Alt key is down|
|`[7]`|Cell row   |integer                                                                                              |
|`[8]`|Cell column|integer                                                                                              |
|`[9]`|Title index|integer                                                                                              |



The y and x position of the mouse are reported relative to the top-left corner of the [Grid](../objects/grid.md).


The cell row and column are `⎕IO` dependent


If the user moves the mouse pointer over a row *title*, the value reported for the column is `¯1`, and the value reported for Title index is the index of that row title in [RowTitles](../properties/rowtitles.md), or, if [RowTitles](../properties/rowtitles.md) is not defined, the row number. Column titles are handled in a similar fashion.


