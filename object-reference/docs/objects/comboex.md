# <span>ComboEx</span> <span>Object</span>

**Purpose:** The ComboEx object is an extended version of the Combo object that provides additional features including item images

**Description**

The ComboEx object is a ComboBox that supports item images and indenting. It is a superset of the [Combo](combo.md) object and supports all its functionality. For further details, see ["Combo"](combo.md).

For most purposes, you can use the ComboEx object in place of the [Combo](combo.md) object whether or not you make use of the extended features of the ComboEx.

Like the basic [Combo](combo.md), the list of text items in the ComboEx is specified by the [Items](../properties/items.md) property. You may associate images with each of the text items using the [ImageListObj](../properties/imagelistobj.md), [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) properties.

To do so, [ImageListObj](../properties/imagelistobj.md) specifies the name of an ImageList object that contains a set of images. [ImageIndex](../properties/imageindex.md) and [SelImageIndex](../properties/selimageindex.md) map individual images from the ImageList to each of the text items specified by Items. [ImageIndex](../properties/imageindex.md) specifies the image to be displayed when the item is not selected; [SelImageIndex](../properties/selimageindex.md) specifies the image to be displayed when the item is selected.

The [Indents](../properties/indents.md) property specifies the amount by which each of the items are indented in units of 10 pixels

The appearance of the items is additionally controlled by the [EditImage](../properties/editimage.md) and [EditImageIndent](../properties/editimageindent.md) properties. These are Boolean and their effect is summarised in the table below. Notice that Images are displayed only if both these properties are set to 1 (which is the default).

There are certain restrictions that apply to a ComboEx object with Style `'Simple'`, namely:

- images and indents do not apply to the edit control portion of the object.
- the object may not redraw properly if [EditImage](../properties/editimage.md) and/or [EditImageIndent](../properties/editimageindent.md) are set to 0 or if [CaseSensitive](../properties/casesensitive.md) or [PathWordBreak](../properties/pathwordbreak.md) are set to 1.
- [PathWordBreak](../properties/pathwordbreak.md) does not work.

|&nbsp;|EditImageIndent||
|---|---|---|
|EditImage|0|1|
|0|No images displayed, item text is indented as specified by [Indents](../properties/indents.md)|No images displayed, item text is indented as specified by [Indents](../properties/indents.md) plus the width of the images in ImageList|
|1|No images displayed, item text is indented as specified by [Indents](../properties/indents.md)|Images are displayed, items are indented as specified by [Indents](../properties/indents.md)|

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [CaseSensitive](../properties/casesensitive.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [EditImage](../properties/editimage.md), [EditImageIndent](../properties/editimageindent.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [HasClearButton](../properties/hasclearbutton.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [ImageIndex](../properties/imageindex.md), [ImageListObj](../properties/imagelistobj.md), [Indents](../properties/indents.md), [Index](../properties/index-property.md), [Items](../properties/items.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PathWordBreak](../properties/pathwordbreak.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Rows](../properties/rows.md), [SelImageIndex](../properties/selimageindex.md), [SelItems](../properties/selitems.md), [SelText](../properties/seltext.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Text](../properties/text.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropDown](../methodorevents/dropdown.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
