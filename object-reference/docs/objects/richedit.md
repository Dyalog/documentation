# <span>RichEdit</span> <span>Object</span>

**Purpose:** The RichEdit object is a multi-line text editor that provides a wide range of word-processing capabilities.

**Description**

A RichEdit object is a window in which the user can enter and edit text. The text can be assigned character and paragraph formatting. It is implemented using the Microsoft Windows RichEdit Version 1.0 control, although  embedded OLE objects are not supported.

The RichEdit object provides a programming interface for formatting text. However, your application must implement any user interface components necessary to make formatting operations available to the user. For example, your program can set the colour and font of a particular block of text, but the RichEdit itself provides no facilities for the user to do this directly. It is up to you to provide these.

The [File](../properties/file.md) property specifies the name of a file associated with the object. Data in the file is assumed to be in rich text format, and the default extension for the file is .RTF. You can read the file into the object by calling [FileRead](../methodorevents/fileread.md) and you can write the contents to the file by calling [FileWrite](../methodorevents/filewrite.md). You can also print the contents of the object by calling [RTFPrint](../methodorevents/rtfprint.md).

The [Text](../properties/text.md) property may be used to set or retrieve the text of the RichEdit, but ignores formatting information. [Text](../properties/text.md) may set using a simple character vector, a simple matrix, or a vector of vectors. If  [Text](../properties/text.md) is specified by a matrix or by a vector of vectors, "new-line" characters are automatically added at the end of each line in the RichEdit control.

The user may insert a "new-line" character in the text by pressing Ctrl-Enter. If [Text](../properties/text.md) was set by a matrix, it is returned as a matrix. Otherwise it is returned as a vector of vectors. "New-line" characters are not returned. If [Text](../properties/text.md) was not specified  by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or  [`⎕WS` ](../../../language-reference-guide/system-functions/ws)it is returned  an empty matrix (`1 0⍴''`).

The [RTFText](../properties/rtftext.md) property  may be used to set or retrieve the contents of the RichEdit, including text and formatting.

The [PageWidth](../properties/pagewidth.md) property defines the width of the text within the object. Text entered into the object is automatically wrapped according to [PageWidth](../properties/pagewidth.md). This property also defines the width when the text is printed.

You can set the default character format or the format of a particular block of text using the [CharFormat](../properties/charformat.md) property. If there is no selection, setting [CharFormat](../properties/charformat.md) defines the default character format that applies at the current insertion position and establishes the appearance of all of the text (font, colour, size etc.) that the user subsequently enters here. If there *is* a selection, setting [CharFormat](../properties/charformat.md) sets the character format for the selected block of text.

The [WordFormat](../properties/wordformat.md) property is similar to [CharFormat](../properties/charformat.md) except that is sets the format for the selected word(s) or, if there is no selection, for the word containing the insertion point.

The [ParaFormat](../properties/paraformat.md) property defines the paragraph formatting which includes alignment, indentation and the location of tab stops. When you set [ParaFormat](../properties/paraformat.md) with `⎕WS`, the formatting is applied to the current selection. If there is no selection, it defines the default paragraph formatting at the insertion point.

All of the dimensions used for text and paragraph formatting are specified in [Twips](../miscellaneous/twips.md). You can convert from pixels to [Twips](../miscellaneous/twips.md) and vice versa using the DevCaps property of either Root or the Printer object as appropriate.

The behaviour of the Enter key is defined by the [ WantsReturn](../properties/wantsreturn.md) property. If
[ WantsReturn](../properties/wantsreturn.md) is 1 (the default), the Enter key inputs a new line into the RichEdit object. If
[ WantsReturn](../properties/wantsreturn.md) is 0 the Enter key is ignored by the RichEdit object and may instead generate a Select event on a Button. In this case the user must press Ctrl+Enter to input a new line.

The user may copy and paste information (in RTF format) between a RichEdit object and the Windows clipboard. The Clipboard object also has an [RTFText](../properties/rtftext.md) property that supports RTF format

If the user attempts to alter text that is protected (see[ CharFormat](../properties/charformat.md)) the RichEdit object reports a [Protected](../methodorevents/protected.md) event.

You may print the contents of a RichEdit object using the [RTFPrint](../methodorevents/rtfprint.md) method. You may display a print set-up dialog box using the [RTFPrintSetup](../methodorevents/rtfprintsetup.md) method.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Group](../objects/group.md), [PropertyPage](../objects/propertypage.md), [SubForm](../objects/subform.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Bitmap](../objects/bitmap.md), [Circle](../objects/circle.md), [Cursor](../objects/cursor.md), [Ellipse](../objects/ellipse.md), [Font](../objects/font.md), [Icon](../objects/icon.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md), [Text](../objects/text.md), [Timer](../objects/timer.md)

Properties: [Accelerator](../properties/accelerator.md), [AcceptFiles](../properties/acceptfiles.md), [Active](../properties/active.md), [Attach](../properties/attach.md), [AutoConf](../properties/autoconf.md), [BCol](../properties/bcol.md), [Border](../properties/border.md), [Changed](../properties/changed.md), [CharFormat](../properties/charformat.md), [ChildList](../properties/childlist.md), [Coord](../properties/coord.md), [CursorObj](../properties/cursorobj.md), [Data](../properties/data.md), [Dragable](../properties/dragable.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [File](../properties/file.md), [FontObj](../properties/fontobj.md), [Handle](../properties/handle.md), [Hint](../properties/hint.md), [HintObj](../properties/hintobj.md), [HScroll](../properties/hscroll.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PageWidth](../properties/pagewidth.md), [ParaFormat](../properties/paraformat.md), [Posn](../properties/posn.md), [PropList](../properties/proplist.md), [Redraw](../properties/redraw.md), [RTFText](../properties/rtftext.md), [SelText](../properties/seltext.md), [Size](../properties/size.md), [Sizeable](../properties/sizeable.md), [TabIndex](../properties/tabindex.md), [Text](../properties/text.md), [Tip](../properties/tip.md), [TipObj](../properties/tipobj.md), [Translate](../properties/translate.md), [Type](../properties/type.md), [Visible](../properties/visible.md), [VScroll](../properties/vscroll.md), [WantsReturn](../properties/wantsreturn.md), [WordFormat](../properties/wordformat.md)

Methods: [Animate](../methodorevents/animate.md), [ChooseFont](../methodorevents/choosefont.md), [Detach](../methodorevents/detach.md), [FileRead](../methodorevents/fileread.md), [FileWrite](../methodorevents/filewrite.md), [GetFocus](../methodorevents/getfocus.md), [GetFocusObj](../methodorevents/getfocusobj.md), [GetTextSize](../methodorevents/gettextsize.md), [RTFPrint](../methodorevents/rtfprint.md), [RTFPrintSetup](../methodorevents/rtfprintsetup.md)

Events: [Change](../methodorevents/change.md), [Close](../methodorevents/close.md), [Configure](../methodorevents/configure.md), [ContextMenu](../methodorevents/contextmenu.md), [Create](../methodorevents/create.md), [DragDrop](../methodorevents/dragdrop.md), [DropFiles](../methodorevents/dropfiles.md), [DropObjects](../methodorevents/dropobjects.md), [Expose](../methodorevents/expose.md), [FontCancel](../methodorevents/fontcancel.md), [FontOK](../methodorevents/fontok.md), [GesturePan](../methodorevents/gesturepan.md), [GesturePressAndTap](../methodorevents/gesturepressandtap.md), [GestureRotate](../methodorevents/gesturerotate.md), [GestureTwoFingerTap](../methodorevents/gesturetwofingertap.md), [GestureZoom](../methodorevents/gesturezoom.md), [GotFocus](../methodorevents/gotfocus.md), [Help](../methodorevents/help.md), [KeyPress](../methodorevents/keypress.md), [LostFocus](../methodorevents/lostfocus.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseEnter](../methodorevents/mouseenter.md), [MouseLeave](../methodorevents/mouseleave.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md), [MouseWheel](../methodorevents/mousewheel.md), [Protected](../methodorevents/protected.md), [Select](../methodorevents/select.md)
