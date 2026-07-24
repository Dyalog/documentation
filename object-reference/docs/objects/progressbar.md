# <span>ProgressBar</span> <span>Object</span>

**Purpose:** The ProgressBar object is used to indicate the progress of a lengthy operation.

**Description**

The ProgressBar object is a window that an application can use to indicate the progress of a lengthy operation. The appearance of the bar in the ProgressBar is determined by the [ProgressStyle](../properties/progressstyle.md) property.

If ProgressStyle is `Normal` or `Smooth`, the  size of the bar, intended to indicate the amount of progress, is determined using the [Thumb](../properties/thumb.md) property in relation to its [Limits](../properties/limits.md) property, and/or using the [ProgressStep](../methodorevents/progressstep.md) method. This can be updated as appropriate in the application logic or by using a [Timer](timer.md).

The range of a ProgressBar is specified by the [Limits](../properties/limits.md) property. This is a 2-element integer vector defining its minimum and maximum values. The position of the filled rectangle is specified by the Thumb property. You can update the ProgressBar by using `⎕WS` to set the value of the [Thumb](../properties/thumb.md) directly, or by using the [ProgressStep](../methodorevents/progressstep.md) method. The latter causes the [Thumb](../properties/thumb.md) to be updated by the value of the [Step](../properties/step.md) property.

If you attempt to set the [Thumb](../properties/thumb.md) to a value greater than its maximum value (using either method) the behaviour depends upon the value of the [Wrap](../properties/wrap.md) property which is Boolean and has a default value of 1. If [Wrap](../properties/wrap.md) is 1, the value obtained when you set the Thumb property is given by the expression:
```apl
      LIMITS[1]+(1+LIMITS[2]-LIMITS[1])|THUMB-LIMITS[1]

```

where `THUMB` is the value to which you set the Thumb property and `LIMITS` is the value of the [Limits](../properties/limits.md) property. This causes the highlighted rectangle to begin filling again from the left.

If ProgressStyle is `Marquee`, the size of the bar is fixed and its position  changes with time according to the value of the [Interval](../properties/interval.md) property. The values of [Thumb](../properties/thumb.md), [Limits](../properties/limits.md), [Wrap](../properties/wrap.md) and [Step](../properties/step.md) are irrelevant.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Bitmap](../objects/bitmap.md), [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Icon](../objects/icon.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [Interval](../properties/interval.md), [KeepOnClose](../properties/keeponclose.md), [Limits](../properties/limits.md), [MethodList](../properties/methodlist.md), [Posn](../properties/posn.md), [ProgressStyle](../properties/progressstyle.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Step](../properties/step.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Thumb](../properties/thumb.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [Wrap](../properties/wrap.md)

Methods: [Animate](../methodorevents/animate.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [ProgressStep](../methodorevents/progressstep.md)

Events: [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
