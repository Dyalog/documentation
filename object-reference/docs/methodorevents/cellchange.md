# <span>CellChange</span> <span>Event 150</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

If enabled, this event is reported when the user changes the contents of a cell in a [Grid](../objects/grid.md) object and then attempts to move to another cell or to another control outside the [Grid](../objects/grid.md).

The purpose of this event is to give the application the opportunity to perform additional validation before the update occurs (and to prevent it if necessary) or to update other cells in the [Grid](../objects/grid.md) as a result of the change.

The default action for the CellChange event is to update the appropriate element of the [Values](../properties/values.md) property with the new data. This action can be disabled by returning 0 from the attached callback function. Notice however, that the user is not prevented from moving away from the cell. If you are using this event to perform additional validation and you require the user to correct the data before moving away, you may force the user back to the cell in question using the  [CellMove](./cellmove.md) method.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is an 8-element vector as follows:

|-----|-----------------|-------------------------------------------------------------------------|
|`[1]`|Object           |ref or character vector                                                  |
|`[2]`|Event            |`'CellChange'` or 150                                                    |
|`[3]`|Cell row         |integer                                                                  |
|`[4]`|Cell column      |integer                                                                  |
|`[5]`|New data         |number or character array                                                |
|`[6]`|Object name      |character vector (name of object to which the user has transferred focus)|
|`[7]`|New cell (row)   |integer                                                                  |
|`[8]`|New cell (column)|integer                                                                  |

If the user moves to another cell in the [Grid](../objects/grid.md), the 6th element of the event message is the name of the [Grid](../objects/grid.md) object and elements 7 and 8 specify the new cell address (`⎕IO` dependent).

If the user switches the input focus to another control or selects a [MenuItem](../objects/menuitem.md), the 6th element of the event message contains the name of that control or [MenuItem](../objects/menuitem.md). If the user switches to another application, the 6th element of the event message is an empty character vector. In all these cases, the 7th and 8th elements are 0.

The 5th element of the event message contains the data value that will be used to update the [Values](../properties/values.md) property. This will be numeric if the [FieldType](../properties/fieldtype.md) of the associated [Edit](../objects/edit.md) object is Numeric, LongNumeric, Date, LongDate or Time. Otherwise, it will be a character array.

An application can update an individual cell in the Grid under program control by calling CellChange as a method. If so, the *New object*, *New cell row* and *New cell column* parameters may be omitted.
