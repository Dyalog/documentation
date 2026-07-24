# <span>List</span> <span>Object</span>

**Purpose:** Allows the user to select one or more items from a list.

**Description**

The [Items](../properties/items.md) property is either a vector of character vectors or a character matrix, and determines the items in the List.

The size and position of the area used to display the list is defined by [Size](../properties/size.md) and [Posn](../properties/posn.md). If [Size](../properties/size.md) is not chosen to represent an exact number of lines of text, the bottom line of text may be clipped.

The [Index](../properties/index-property.md) property specifies or reports the position of [Items](../properties/items.md) in the list box as a positive integer value. If [Index](../properties/index-property.md) has the value "n", it means that the "nth" item in [Items](../properties/items.md) is displayed on the top line in the list box. However, it is ignored if all the [Items](../properties/items.md) fit within the List object. Note that [Index](../properties/index-property.md) can only be set using [`⎕WS`](../../../language-reference-guide/system-functions/ws) and not by [`⎕WC`](../../../language-reference-guide/system-functions/wc). The default value for [Index](../properties/index-property.md) is `⎕IO`.

The [Style](../properties/style.md) property may be `'Single'` (the default) or `'Multi'`. `'Single'` allows only a single item to be selected. `'Multi'` allows several items to be chosen. In either case, if the [Select](../methodorevents/select.md) event is enabled, it is generated whenever the selection changes. If [Style](../properties/style.md) is `'Multi'` the List will generate a [Select](../methodorevents/select.md) event every time an item is added to the selected list.

Under Windows, you may select or de-select multiple items in a List object by pressing the Ctrl key at the same time as pressing the left mouse button.

The [SelItems](../properties/selitems.md) property is a Boolean vector with one element per element or row in [Items](../properties/items.md) and indicates which (if any) of the items is currently selected (and highlighted).

The [VScroll](../properties/vscroll.md) property determines whether or not the list has a scrollbar. Its possible values are :

|----|---------------------|
|`¯2`|scrollbar if required|
|`¯1`|scrollbar if required|
|`0` |no scrollbar         |

Note that data in a List is always scrollable if there are more items than will fit in the box. [VScroll](../properties/vscroll.md) determines ONLY whether or not a scrollbar is provided.

The [MultiColumn](../properties/multicolumn.md) property is a Boolean value that specifies whether or not the List object displays its items in columns. The default is 0 which produces a single-column display. If [MultiColumn](../properties/multicolumn.md) is 1, the List object displays its items in columns whose width is defined by the [ColumnWidth](../properties/columnwidth.md) property.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [ChildList](../properties/childlist.md), [ColumnWidth](../properties/columnwidth.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [Index](../properties/index-property.md), [Items](../properties/items.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [MultiColumn](../properties/multicolumn.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [SelItems](../properties/selitems.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [SortItems](../properties/sortitems.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
