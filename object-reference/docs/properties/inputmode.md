# <span>InputMode</span> <span>Property</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This property determines editing behaviour and the action of the cursor movement keys when the user changes the contents of a Grid using a *floating*[ Edit](../objects/edit.md) or DropEdit [Combo](../objects/combo.md) control.




InputMode is a character vector with one of the following values:


|----------------|-----------------------------------------------------------------------------------------------------------|
|`'Scroll'`      |The cursor keys move around the Grid; the user may switch to *InCell* mode                                 |
|`'InCell'`      |The cursor keys move within the Input object; the mode reverts to *Scroll* when the user selects a new cell|
|`'AlwaysScroll'`|The cursor keys move around the Grid; the user may not switch to *InCell* mode                             |
|`'AlwaysInCell'`|The cursor keys move within the Input object, even when the user moves to a new cell                       |
|`'AutoEdit'`    |See below                                                                                                  |



By default, the input mode is *Scroll*. In this mode, cursor movement keys are actioned by the Grid itself and used to move from cell to cell. The user may switch to *InCell* mode by double-clicking or by pressing the key defined by [InputModeKey](inputmodekey.md) (the default is "F2").


In *InCell* mode, all cursor movement keys are actioned by the Input object and typically move the cursor around *within* the Input object and do not switch between cells. When the user switches to a different cell, InputMode reverts to *Scroll* mode


If InputMode is *AlwaysScroll* or *AlwaysInCell*, the user remains permanently in either *Scroll* or *InCell* mode respectively.


If InputMode is `'AutoEdit'`, the behaviour of a cell that contains a floating Input field is as follows:


When the user enters the cell, the contents are selected (and highlighted).At this stage, the cursor movement keys move to an adjacent cell. If the user presses a (valid) data key, that character replaces the current contents of the cell.


If the user presses F2 (or the key defined by the [InputModeKey](inputmodekey.md) property), the data is de-selected and unhighlighted and the cursor is placed at the rightmost end of the data.


In either case, the left and right cursor keys now move the cursor within the current data string, but skip to the adjacent cell from the beginning or end of the data. This behaviour differs from *InCell* mode in which the cursor movement keys *stick* at the end of the data.


