# <span>ColorButton</span> <span>Object</span>

**Purpose:** The ColorButton object allows the user to select a colour.

**Description**

The ColorButton object displays a coloured box, with an optional drop down button. When the user clicks the ColorButton with the left mouse button, a colour selection drop-down appears below it, allowing the user to select a new colour.

The [CurrentColor](../properties/currentcolor.md) property (default 0 0 0) is a 3-element integer vector that specifies and reports the RGB value of the currently selected colour.

The [DefaultColors](../properties/defaultcolors.md) property is a nested matrix which specifies the RGB values of the colours shown in the colour selection box. The shape of [DefaultColors](../properties/defaultcolors.md) determines the number of rows and columns in the colour selection drop-down. Each element of [DefaultColors](../properties/defaultcolors.md) is a 3-element integer vector specifying an RGB colour value.

The [OtherButton](../properties/otherbutton.md) property is Boolean and specifies whether or not the user can select a colour using the Windows colour selection dialog box.

If [OtherButton](../properties/otherbutton.md) is 1 (the default), the final row of the colour selection drop-down contains a button labelled "Other…". If the user clicks this button, the standard Windows colour selection dialog box is displayed, allowing the user to select any colour that the computer can render.

If [OtherButton](../properties/otherbutton.md) is 0, the button labelled "Other…" is not present and the user is restricted to the choice of colours provided by the [DefaultColors](../properties/defaultcolors.md) property.

The [CustomColors](../properties/customcolors.md) property is a 1-row, 16-column nested matrix which specifies the RGB values of the Colours displayed in the *Custom colors* section of the Windows colour selection dialog box. Each element of [CustomColors](../properties/customcolors.md) is a 3-element integer vector specifying an RGB colour value.

The [ShowDropDown](../properties/showdropdown.md) property is Boolean (default 1) and specifies whether or not a drop-down button is displayed in the ColorButton object.

When the user clicks a ColorButton with the left mouse button, the object generates a [DropDown](../methodorevents/dropdown.md) event just before it displays the colour selection drop-down. This event may be used to set the [DefaultColors](../properties/defaultcolors.md) and/or [CustomColors](../properties/customcolors.md) properties dynamically.

When the user selects a new colour, the ColorButton generates a [ColorChange](../methodorevents/colorchange.md) event.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md)

Children: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md)

Properties: [Accelerator](../properties/accelerator.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CurrentColor](../properties/currentcolor.md), [CursorObj](../properties/cursorobj.md), [CustomColors](../properties/customcolors.md), [Data](../properties/data.md), [DefaultColors](../properties/defaultcolors.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [OtherButton](../properties/otherbutton.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [ShowDropDown](../properties/showdropdown.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [TabIndex](../properties/tabindex.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [Animate](../methodorevents/animate.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Close](../methodorevents/close.md), [ColorChange](../methodorevents/colorchange.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropDown](../methodorevents/dropdown.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md)
