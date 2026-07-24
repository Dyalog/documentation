# <span>Edit</span> <span>Object</span>

**Purpose:** Allows user to enter or edit data.

**Description**

The value of the [Style](../properties/style.md) property, which may be `'Single'` or `'Multi'`, determines whether the object presents a single-line data entry field or an area for viewing and editing a large block of text.

## Single-Line Edit

The [FieldType](../properties/fieldtype.md) property (which applies only to a single-line Edit object) is either an empty vector (the default) or specifies the type of the field as reflected by its [Value](../properties/value.md) property. If [FieldType](../properties/fieldtype.md) is empty, the [Value](../properties/value.md) of the field may be a number or a character vector, according to the contents defined by its [Text](../properties/text.md) property (this is always a character vector).

The [Align](../properties/align.md) property, which applies only to single-line Edit objects, specifies the vertical alignment of the text. It may be `'None'` (the default), `'Centre'` or `'Center'`. [Align](../properties/align.md) may only be set when the object is created and may not subsequently be changed.

If [FieldType](../properties/fieldtype.md) is `'Char'` the [Value](../properties/value.md) of the field is forced to be a character vector, even if the contents defined by its [Text](../properties/text.md) property is entirely numeric.

If [FieldType](../properties/fieldtype.md) is `'Numeric'`, `'LongNumeric'`, `'Currency'`, `'Date'`, `'LongDate'`, or `'Time'` the [Value](../properties/value.md) contains a number. For fields of these types, basic validation is provided during user input. The field is revalidated when the user attempts to "leave" it and at this point the object will generate a [BadValue](../methodorevents/badvalue.md) event if its contents are inconsistent with its [FieldType](../properties/fieldtype.md).

Note that when an Edit object is used as the [Input](../properties/input.md) property of a [Grid](grid.md), it is the [Value](../properties/value.md) of the Edit object (and not its [Text](../properties/text.md) property) that is used to update the [Values](../properties/values.md) property (that is, the contents of) the [Grid](grid.md) when the user moves away from the cell.

The [MaxLength](../properties/maxlength.md) property defines the maximum number of characters that the user may enter into the object.

The [ValidIfEmpty](../properties/validifempty.md) property may be 0 (the default) or 1 and specifies whether or not the Edit field is deemed to be valid if it is empty.

The [Password](../properties/password.md) property specifies the character that is displayed in response to the user typing a character. Normally, [Password](../properties/password.md) is empty (the default) and the object displays the character that was entered. However, if you set [Password](../properties/password.md) to (say) an asterisk (*) this symbol will be displayed instead of the characters the user has entered. Note however that the [Text](../properties/text.md) and [Value](../properties/value.md) properties will reflect what the user typed.

The [HScroll](../properties/hscroll.md) property determines whether or not the data may be scrolled. If [HScroll](../properties/hscroll.md) is 0, the data is not scrollable, and the user cannot enter more characters once the field is full. If [HScroll](../properties/hscroll.md) is `¯1` or `¯2` the field is scrollable, and there is no limit on the number of characters that can be entered. In neither case however is a horizontal scrollbar provided. [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.

## Multi-Line Edit

If the [Style](../properties/style.md) is `'Multi'`, [Text](../properties/text.md) may set using a simple character vector, a simple matrix, or a vector of vectors. If  [Text](../properties/text.md) is specified by a matrix or by a vector of vectors, "new-line" characters are automatically added at the end of each line in the Edit control.

The user may insert a "new-line" character in the text by pressing Ctrl-Enter. If [Text](../properties/text.md) was set by a matrix, it is returned as a matrix. Otherwise it is returned as a vector of vectors. "New-line" characters are not returned. If [Text](../properties/text.md) was not specified  by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or  [`⎕WS`](../../../language-reference-guide/system-functions/ws) it is returned  an empty matrix (`1 0⍴''`). However,  if [Text](../properties/text.md) was not specified, but the user types and then empties the field, it is returned as an empty nested array  (`,⊂''`)

The [Justify](../properties/justify.md) property determines whether the text in a multi-line Edit object is `'Left'`, `'Right'`, or `'Centre'` justified. Setting [Justify](../properties/justify.md) to `'Centre'` or `'Right'` also forces word-wrapping and disables horizontal scrolling, whatever the value of [HScroll](../properties/hscroll.md). Note that the keyword `'Centre'` may also be spelled `'Center'`. [Justify](../properties/justify.md) may only be specified when the object is created using `⎕WC`.

If [Justify](../properties/justify.md) is `'Left'`, the [HScroll](../properties/hscroll.md) property determines whether or not text may be scrolled horizontally. If [HScroll](../properties/hscroll.md) is set to `¯2`, each individual line may be any length, but the object does not have a horizontal scrollbar. Sideways scrolling is achieved using the cursor keys, or by typing. If [HScroll](../properties/hscroll.md) is `¯1`, each individual line may be of any length and the object will have a horizontal scrollbar. If [HScroll](../properties/hscroll.md) is `0`, lines are automatically "word-wrapped" at the right edge of the object. This means that the number of lines displayed may be greater than the number of lines implied by the rows of the matrix or the number of vectors supplied. In particular, if you specify a single long vector, it will be broken up into lines for you on the display, but still returned as a single vector by [`⎕WG`](../../../language-reference-guide/system-functions/wg).

The [VScroll](../properties/vscroll.md) property determines whether or not data may be scrolled vertically and whether or not the object has a vertical scrollbar. A value of `0` inhibits scrolling; `¯2` means scrollable, without a scrollbar; `¯1` means scrollable with a scrollbar. [VScroll](../properties/vscroll.md) may only be set when the object is created and may not subsequently be changed.

The setting of [Justify](../properties/justify.md) forces word-wrapping.

The [SelText](../properties/seltext.md) property identifies the portion of the text that is selected. It may be used to pre-select (and highlight) a part of the text, or to report the part of the text selected by the user. [SelText](../properties/seltext.md) is a 2-element integer vector which specifies the start and end of the selected area. Its structure depends upon the nature of the data specified by [Text](../properties/text.md). See the description of [SelText](../properties/seltext.md) for details.

If the user changes any data in the field **and** attempts to change focus to another object, the Edit object will generate a [Change](../methodorevents/change.md) event. You can use this to validate the new data in the field.

## Note

For full functionality (in particular, for the [Cue](../properties/cue.md) property to apply), the Edit object requires that  [Native Look and Feel ](../miscellaneous/windows-xp-look-and-feel.md)

 is enabled.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Align](../properties/align.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Changed](../properties/changed.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [Cue](../properties/cue.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Decimals](../properties/decimals.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FieldType](../properties/fieldtype.md), [FontObj](../properties/fontobj.md), [FormatString](../properties/formatstring.md), [Handle](../properties/handle.md), [HasClearButton](../properties/hasclearbutton.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [Justify](../properties/justify.md), [KeepOnClose](../properties/keeponclose.md), [MaxLength](../properties/maxlength.md), [MethodList](../properties/methodlist.md), [Password](../properties/password.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [ReadOnly](../properties/readonly.md), [Redraw](../properties/redraw.md), [SelText](../properties/seltext.md), [ShowCueWhenFocused](../properties/showcuewhenfocused.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [Style](../properties/style.md), [TabIndex](../properties/tabindex.md), [Text](../properties/text.md), [TextSize](../properties/textsize.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [ValidIfEmpty](../properties/validifempty.md), [Value](../properties/value.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md), [WantsReturn](../properties/wantsreturn.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md)

Events: [BadValue](../methodorevents/badvalue.md), [Change](../methodorevents/change.md), [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyError](../methodorevents/keyerror.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Select](../methodorevents/select.md)
