# <span>Combo</span> <span>Object</span>

**Purpose:** This object combines an input area with a list box and allows the user to enter a selection by typing text or by choosing an item from the list.

**Description**

Three types of Combo box are provided by the [Style](../properties/style.md) property which may be `'Drop'` (the default), `'Simple'` or `'DropEdit'`.

The [Items](../properties/items.md) property specifies the list of items which are displayed in the list box and from which the user can choose.

The [SelItems](../properties/selitems.md) property is a Boolean vector which specifies which (if any) of the items is selected. When the user chooses an item from the list, it is copied to the edit field and a [Select](../methodorevents/select.md) event is generated. At this point you may use [SelItems](../properties/selitems.md) to identify the chosen item. You can also use [SelItems](../properties/selitems.md) to pre-select the contents of the edit field.

If the [Style](../properties/style.md) is `'Simple'` or `'DropEdit'`, the user may type text into the edit field. In these cases, the contents of the edit field may also be specified or queried using the [Text](../properties/text.md) property.

Note that if the user first selects an item from the list box, then changes it in the edit field, the entry in the list box is automatically deselected. There is therefore no conflict between the value of [Text](text.md) and the value of [SelItems](../properties/selitems.md).

!!! warning
    Windows truncates the contents of the edit field (reflected in the value of the Text property) to 510 characters.

For a Combo with [Style ](../properties/style.md)`'Simple'`, the [Index](../properties/index-property.md) property specifies or reports the position of [Items](../properties/items.md) in the list box as a positive integer value. If [Index](../properties/index-property.md) has the value "n", it means that the "n<sup>th</sup>" item in [Items](../properties/items.md) is displayed on the top line in the list box. Note that [Index](../properties/index-property.md) can only be set using [`⎕WS`](../../../language-reference-guide/system-functions/ws) and **not** by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and is ignored if all the [Items](../properties/items.md) fit in the list box. The default value for [Index](../properties/index-property.md) is `⎕IO`.

The [SelText](../properties/seltext.md) property identifies the portion of the edit field that is highlighted. It is not applicable to a Combo with [Style ](../properties/style.md)`'Drop'` as the user cannot enter or change data in its edit field.

The height of a Combo object with [Style ](../properties/style.md)`'Drop'` or `'DropEdit'` is defined in a manner that is different from other objects. The height of the edit field is fixed, and is dependent only upon the size of the font. The height of the associated drop-down list box is determined by the [Rows](../properties/rows.md) property. The first element of the [Size](../properties/size.md) property (height) is ignored. For a Simple combo box (whose listbox is permanently displayed), the overall height is determined by the first element of [Size](../properties/size.md). [Rows](../properties/rows.md) is a "read-only" property.

The [VScroll](../properties/vscroll.md) property specifies whether or not a vertical scrollbar is provided. The default value 0 means no scrollbar, setting [VScroll](../properties/vscroll.md) to `¯1` or `¯2` specifies that the Combo has a vertical scrollbar.

If the [Style](../properties/style.md) is `'Simple'` or `'DropEdit'`, the [HScroll](../properties/hscroll.md) property determines whether or not the edit field may be scrolled. If [HScroll](../properties/hscroll.md) is 0, the data is not scrollable, and the user cannot enter more characters once the field is full. If [HScroll](../properties/hscroll.md) is `¯1` or `¯2` the field is scrollable, and there is no limit on the number of characters that can be entered. In neither case however is a horizontal scrollbar provided. If [Style](../properties/style.md) is `'Drop'`, the user is not allowed to enter data into the edit field anyway, and the value of [HScroll](../properties/hscroll.md) is ignored.

[VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.

Note that when you change the [Items](../properties/items.md) property using [`⎕WS`](../../../language-reference-guide/system-functions/ws), the [Text](text.md), [SelItems](../properties/selitems.md) and [SelText](../properties/seltext.md) properties are all reset to their default values.

The Combo object will report a [Select](../methodorevents/select.md) event (if enabled) when the user chooses an item from the list box. It will generate a [Change](../methodorevents/change.md) event (if enabled) when the user manually alters the contents of the edit field and then changes the focus to another object.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [HasClearButton](../properties/hasclearbutton.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [Index](../properties/index-property.md), [Items](../properties/items.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Rows](../properties/rows.md), [SelItems](../properties/selitems.md), [SelText](../properties/seltext.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Text](../properties/text.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Change](../methodorevents/change.md), [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropDown](../methodorevents/dropdown.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
