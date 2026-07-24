# <span>DateTimePicker</span> <span>Object</span>

**Purpose:** The DateTimePicker object is an editable date/time field with an         optional drop-down Calendar.

**Description**

The DateTimePicker object represents the built-in Windows date and time
picker control. For most purposes, the DateTimePicker supersedes the use of
Label, Edit and Spinner objects for displaying and entering dates and times.
Unlike the Edit and Spinner objects, it is not possible for the user to enter an
invalid date or time into a DateTimePicker.

The Style property may be either `'Combo'`(the default) or `'UpDown'`. The former
provides a drop-down calendar that behaves in the same way as the Calendar
object and whose appearance and behaviour is controlled by a set of properties
namely CalendarCols, CircleToday, HasToday, MaxDate, MinDate, MonthDelta, Today
and WeekNumbers that are common to the Calendar. Note that the Style property may only be set when the object is created.

If Style is `'Combo'`, the Align property
specifies the horizontal alignment of the drop-down Calendar which may be `'Left'`(the default) or `'Right'`.

If Style is `'UpDown'`, the
DateTimePicker includes instead a pair of spinner buttons that allow the user to
increment and decrement values in the various sub-fields provided by the
control.

The [DateTime](../properties/datetime.md) property represents the
date and time value that is currently displayed in the object. This is a
4-element vector containing the IDN, hour, minutes and seconds respectively.

The FieldType property specifies one of a set of pre-defined date/time
formats to be used by the control. This is a character vector that may be empty
(the default), `'Date'`, `'DateCentury'`,
`'LongDate'`, `'Time'`or `'Custom'`. Specifying an empty vector is
the same as specifying `'Date'`. Note that `'DateCentury'` always displays a 4-digit year, regardless of the user's Windows settings.

If FieldType is set to `'Custom'`, the
format is defined by the [CustomFormat](../properties/customformat.md) property. CustomFormat is a character vector that may contain a mixture of
date/time format elements and body text.

The [HasCheckBox](../properties/hascheckbox.md) property is a
Boolean value (default 0) that specifies whether or not a checkbox is displayed
in the object. This allows the user to specify whether or not the date/time
displayed in the DateTimePicker is applicable.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md)

Children: [Cursor](../objects/cursor.md), [Font](../objects/font.md), [Menu](../objects/menu.md), [MsgBox](../objects/msgbox.md), [TCPSocket](../objects/tcpsocket.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Align](../properties/align.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [Border](../properties/border.md), [CalendarCols](../properties/calendarcols.md), [ChildList](../properties/childlist.md), [CircleToday](../properties/circletoday.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [CustomFormat](../properties/customformat.md), [Data](../properties/data.md), [DateTime](../properties/datetime.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FieldType](../properties/fieldtype.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [HasCheckBox](../properties/hascheckbox.md), [HasToday](../properties/hastoday.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [KeepOnClose](../properties/keeponclose.md), [MaxDate](../properties/maxdate.md), [MethodList](../properties/methodlist.md), [MinDate](../properties/mindate.md), [MonthDelta](../properties/monthdelta.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Today](../properties/today.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [WeekNumbers](../properties/weeknumbers.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [DateToIDN](../methodorevents/datetoidn.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [IDNToDate](../methodorevents/idntodate.md)

Events: [Close](../methodorevents/close.md), [CloseUp](../methodorevents/closeup.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DateTimeChange](../methodorevents/datetimechange.md), [DragDrop](../methodorevents/dragdrop.md), [DropDown](../methodorevents/dropdown.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
