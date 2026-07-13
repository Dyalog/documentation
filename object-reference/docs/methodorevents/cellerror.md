# <span>CellError</span> <span>Event 157</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, this event is reported when the user inserts invalid data into the [Edit](../objects/edit.md) object associated with a cell in a [Grid](../objects/grid.md) object and then attempts to move to another cell or to another control outside the [Grid](../objects/grid.md). It is also reported if the user selects a [MenuItem](../objects/menuitem.md).


The default action for the CellError event is to sound the bell (beep). This action can be disabled by returning 0 from the attached callback function. Whatever the result of the callback, the user will be prevented from moving to another cell in the [Grid](../objects/grid.md) and the [CurCell](../properties/curcell.md) and [Values](../properties/values.md) properties will remain unchanged. The user is not prevented from switching to any other control or to another application. However, if and when the user returns to the [Grid](../objects/grid.md), the current cell ([CurCell](../properties/curcell.md)) remains the invalid one and the user may not select a different one until the invalid data in the cell has been corrected. If you wish to allow the user to move to another cell without correcting the data, you may do so by generating a [CellMove](./cellmove.md) event explicitly. However, the [Values](../properties/values.md) property will remain unchanged and the invalid contents of the [Edit](../objects/edit.md) object will simply be discarded.



The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq) or supplied as the right argument to your callback function, is an 8-element vector as follows:


|-----|-----------------|-------------------------------------------------------------------------|
|`[1]`|Object           |ref or character vector                                                  |
|`[2]`|Event            |`'CellError'` or 157                                                     |
|`[3]`|Cell row         |integer                                                                  |
|`[4]`|Cell column      |integer                                                                  |
|`[5]`|Invalid data     |character vector                                                         |
|`[6]`|Object name      |character vector (name of object to which the user has transferred focus)|
|`[7]`|New cell (row)   |integer                                                                  |
|`[8]`|New cell (column)|integer                                                                  |



If the user moves to another cell in the [Grid](../objects/grid.md), the 6th element of the event message is the name of the [Grid](../objects/grid.md) object and elements 7 and 8 specify the cell address (`⎕IO` dependent).


If the user switches the input focus to another control or selects a [MenuItem](../objects/menuitem.md), the 6th element of the event message contains the name of that control or [MenuItem](../objects/menuitem.md). If the user switches to another application, the 6th element of the event message is an empty character vector. In all these cases, the 7th and 8th elements are 0.


The 5th element of the event message contains the character vector in the [Text](../objects/text.md) property of the associated [Edit](../objects/edit.md) object which is inconsistent with its [FieldType](../properties/fieldtype.md).


