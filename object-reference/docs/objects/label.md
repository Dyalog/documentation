# <span>Label</span> <span>Object</span>

**Purpose:** Displays static text.

**Description**

This object displays a text label, a number, a date or a time value.

If [FieldType](../properties/fieldtype.md) is empty, the Label displays the text defined by its [Caption](../properties/caption.md) property. If the [Caption](../properties/caption.md) property contains one or more linefeed characters (`⎕UCS 10`) the Label becomes a multi-line Label which is top-left justified and automatically wraps on white-space characters (such as space and tab) to fit in the width provided.

If [FieldType](../properties/fieldtype.md) is `'Numeric'`, `'LongNumeric'`, `'Currency'`, `'Date'`, `'LongDate'`, or `'Time'` the Label converts and formats the number defined by its [Value](../properties/value.md) property and displays this instead. See [FieldType](../properties/fieldtype.md) property for details.

The [Border](../properties/border.md) property determines whether or not the label has a border. A value of 0 means no border (the default). A value of 1 means that a 1-pixel border is drawn around the label.

By default, the value of the [EdgeStyle](../properties/edgestyle.md) property for a Label is `'None'` and the value of [BCol](../properties/bcol.md) is 0 which is normally white, or grey if the parent object has a 3-dimensional appearance. You can change its appearance by setting [EdgeStyle](../properties/edgestyle.md) and/or [BCol](../properties/bcol.md) to different values.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Decimals](../properties/decimals.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FieldType](../properties/fieldtype.md), [FontObj](../properties/fontobj.md), [FormatString](../properties/formatstring.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [Justify](../properties/justify.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [TabIndex](../properties/tabindex.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Value](../properties/value.md), [Visible](../properties/visible.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [Help](../methodorevents/help.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
