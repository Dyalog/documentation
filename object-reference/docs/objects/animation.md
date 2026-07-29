# <span>Animation</span> <span>Object</span>

**Purpose:** The Animation object displays simple animations from basic .AVI files or resources.

**Description**

The Animation object displays simple animations from basic .AVI files or resources.

The Animation object can only play AVI files or resources that have no sound and can only display uncompressed AVI files or .AVI files that have been compressed using Run-Length Encoding (RLE).

For more sophisticated animations, you may use the Windows Media Player (OCX).

To display an AVI file, you must first use the [AnimOpen](../methodorevents/animopen.md) method to open it. If the [AutoPlay](../properties/autoplay.md) property is set to 1, the animation will play immediately. Otherwise, only the first frame will be displayed.

The [Align](../properties/align.md) property may be `'None'` or `'Centre'` (`'Center'`). If [Align](../properties/align.md) is `'None'`, the Animation window is automatically resized to fit the AVI being played. If [Align](../properties/align.md) is `'Centre'`, the AVI is centred in the Animation window. If the window is too small, the AVI is clipped.

The [AnimPlay](../methodorevents/animplay.md) method may be used to play the animation and allows you to specify the start, number of frames, and repeat count.

The [AnimStop](../methodorevents/animstop.md) method causes the animation to stop.

The [AnimClose](../methodorevents/animclose.md) method closes the current AVI file and resets the contents of the object's window to its background colour.

The [AnimStarted](../methodorevents/animstarted.md) and [AnimStopped](../methodorevents/animstopped.md) events are reported when the animation starts and stops respectively.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md)

Children: [Bitmap](../objects/bitmap.md), [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Align](../properties/align.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [AutoPlay](../properties/autoplay.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [File](../properties/file.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Transparent](../properties/transparent.md), [Type](../properties/type.md), [Visible](../properties/visible.md)

Methods: [Animate](../methodorevents/animate.md), [AnimClose](../methodorevents/animclose.md), [AnimOpen](../methodorevents/animopen.md), [AnimPlay](../methodorevents/animplay.md), [AnimStop](../methodorevents/animstop.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [AnimStarted](../methodorevents/animstarted.md), [AnimStopped](../methodorevents/animstopped.md), [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md)
