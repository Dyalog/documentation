# <span>Input</span> <span>Property</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This property specifies objects to be associated with cells in a Grid.

These
objects may be of type [Button](../objects/button.md), [ColorButton](../objects/colorbutton.md),
[Combo](../objects/combo.md), [Edit](../objects/edit.md), [Label](../objects/label.md),
[Spinner](../objects/spinner.md) or [TrackBar](../objects/trackbar.md).
In addition, the Input property may specify instances of [OCXClass](../objects/ocxclass.md) objects (ActiveX controls) and [NetType](../objects/nettype.md) objects (.NET classes).

The Input property is either a single ref or a simple character scalar or
vector, or a vector of character vectors or refs. If it specifies a single
object, this will be associated with *all* of the cells in the [Grid](../objects/grid.md).
If it specifies a set of objects, these are mapped to individual cells through
the [CellTypes](celltypes.md) property.

When a cell becomes the current cell, its value (defined by the appropriate
element of the [Values](values.md) property) defines the
value of a *corresponding property* of the associated object The
property that corresponds to the value in the cell, depends upon the [Type](type.md) of the associated object as shown in the following table:

|Associate Object Type                                             |Corresponding Property                            |
|------------------------------------------------------------------|--------------------------------------------------|
|[Label](../objects/label.md)                                      |[Text](text.md)                                   |
|[Edit](../objects/edit.md)                                        |[Value](value.md)                                 |
|[Combo](../objects/combo.md)                                      |[Text](text.md)                                   |
|[Button](../objects/button.md) ( [Style](style.md) Push)          |[Caption](caption.md)                             |
|[Button](../objects/button.md) ( [Style](style.md) Radio or Check)|[State](state.md)                                 |
|[ColorButton](../objects/colorbutton.md)                          |[CurrentColor](currentcolor.md)                   |
|[Spinner](../objects/spinner.md)                                  |[Value](value.md)                                 |
|[TrackBar](../objects/trackbar.md)                                |[Thumb](thumb.md)                                 |
|[OCXClass](../objects/ocxclass.md)                                |Specified by [InputProperties](inputproperties.md)|
|[NetType](../objects/nettype.md)                                  |Specified by [InputProperties](inputproperties.md)|

In effect, the user inputs a new value into the current cell by changing the
corresponding property of its associated object. An associated object may be a *fixed* object that is *external* to the [Grid](../objects/grid.md) or a *floating* object that moves automatically from cell to cell. The latter is achieved by
creating the associated object as a *child* of the [Grid](../objects/grid.md).

If the associated object is an [Edit](../objects/edit.md) or [Combo](../objects/combo.md),
the user may change the [Text](text.md) property of the
object by typing, or, in the case of a [Combo](../objects/combo.md),
by selecting an item from a list. The new value of the [Text](text.md) property is then used to update the value in the cell (defined by the [Values](values.md) property of the [Grid](../objects/grid.md)) when the user moves on. If
the associated object is a radio button, the value in the cell (0 or 1) is
reflected by the [State](state.md) property of the [Button](../objects/button.md).
The user may click the [Button](../objects/button.md) on and off,
changing its [State](state.md) and thereby the
corresponding value in the cell.

If the associated object is a [ColorButton](../objects/colorbutton.md),
the corresponding elements of the [Values](values.md) property contain 3-element integer vectors which specify the RGB colour values.

If the associated object is an instance of an [OCXClass](../objects/ocxclass.md) object (ActiveX control) or a [NetType](../objects/nettype.md) object
(.NET class), the Grid uses the *default* property of the external object
if it has one. Alternatively, the [InputProperties](inputproperties.md) property is used to specify which property (or properties) of the external
object are to be mapped to elements of [Values](values.md).
If more than one property is specified, elements of [Values](values.md) are vectors.

If there is no object associated with a cell, or if its associated object is
a [Label](../objects/label.md) or a [Button](../objects/button.md) with [Style](style.md) Push, the cell is protected and
may not be changed by the user. When the current cell is thus protected, the
corresponding row and column titles are not indented as they are when the cell
may be edited.

If the associated object is a numeric [Edit](../objects/edit.md) or
[Label](../objects/label.md) ([FieldType](fieldtype.md) Numeric, LongNumeric, Currency, Date, LongDate or Time) the contents of the cell
are formatted accordingly, even when it is not the current cell. Thus a cell
associated with a [Label](../objects/label.md) with [FieldType](fieldtype.md) Date, always displays as a date.

If the associated object is a [Combo](../objects/combo.md) or [Button](../objects/button.md),
the appearance of a non-current cell is defined by the corresponding element of
the [ShowInput](showinput.md) property.

The following example illustrates the use of different types of object
specified by the Input and [ShowInput](showinput.md) properties:

![](../img/input.gif)
