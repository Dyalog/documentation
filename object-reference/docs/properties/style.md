# <span>Style</span> <span>Property</span>

[**Applies To**](../propertyapplies/style.md)

**Description**

This property determines a particular style of object within the general
category of [Type](type.md).

It is a character vector whose value depends upon the type of object.

For a [Button](../objects/button.md), Style may be `'Push'`,
`'Radio'`, `'Check'`, `'Toggle'`, `'CommandLink'` or `'Split'`.

`'Push'` specifies that the button
appears and behaves like a pushbutton (sometimes also called a command button).

`'Radio'` means that the button is
displayed as a small circle accompanied by a description. When the button is
selected, the circle is filled in. In a group of buttons with Style `'Radio'` that share the same parent, only one of them may be selected. This style of
button is generally known as a "radio-button" or an "option
button".

`'Check'` or `'Toggle'` means that the button is
displayed as a small box accompanied by a description. When the button is
selected a cross appears in the box. This style of button is known as a
"check-box".

`'CommandLink'` means that the button has an icon displayed to the left of its [Caption](caption.md), the appearance of which is controlled by the  [Elevated](elevated.md) property. 
**Note that this feature only applies if Native Look and Feel 

 is enabled.**

`'Split'` specifies a `'Push'` button with an additional drop-down button, similar to that provided by a [Combo](../objects/combo.md) object. 
**Note that this feature only applies if Native Look and Feel 

 is enabled.**

For a [Calendar](../objects/calendar.md) object, The Style property
may be either `'Single'` (the default) or `'Multi'`.
If Style is `'Single'`, the user may select
a single date. If Style is `'Multi`', the
user may select a contiguous range of dates.

For a [Combo](../objects/combo.md) or [ComboEx](../objects/comboex.md) object, Style may be `'Simple'` `'DropEdit'` or `'Drop'` (the default). `'Simple'` specifies a simple combo box in which the associated list box is displayed at
all times. The other two styles provide list boxes which "drop down"
when the user clicks on a symbol displayed to the right of the [Combo](../objects/combo.md)'s
edit field. A `'DropEdit'` Style allows the
user to type (anything) in the edit field. A `'Drop'` Style forces the contents of the edit field to be either empty or
one of the choices specified by [Items](items.md).

For a [DateTimePicker](../objects/datetimepicker.md), Style may be
either `'Combo'` (the default) or `'UpDown'`.

For an [Edit](../objects/edit.md) object, Style may be `'Single'` or `'Multi'`. If Style is `'Single'` the object displays only a single line of text and the user may not enter any
more lines. If the Style is `'Multi'` the
number of lines displayed is governed by the [Rows](rows.md) or [Size](size.md) property and the user may insert, add
or delete lines as desired.

For [FileBox](../objects/filebox.md), [List](../objects/list.md),
and [ListView](../objects/listview.md) objects, Style may be `'Single'` or `'Multi'`. If the Style is `'Single'`only one file or item can be selected. If Style is `'Multi'`,
several files or items can be selected.

For an [Icon](../objects/icon.md), Style may be `'Large'` (the default) or `'Small'` and specifies the
size of the icon (32x32 or 16x16) to be loaded from a file.

For a [Locator](../objects/locator.md), Style may be `'Point'`,
`'Rect'` (the default), `'Line'` or `'Ellipse'`. It specifies the shape that
is drawn as the user moves the mouse.

For a [MenuItem](../objects/menuitem.md), Style may be `'Check'` (the default) or `'Radio'`. The latter
specifies that within a contiguous block of such MenuItems, only one may have [Checked](checked.md) set to 1. Setting [Checked](checked.md) to 1 on any item
in that group automatically sets [Checked](checked.md) to
0 on the others. A radio style [MenuItem](../objects/menuitem.md) that
is checked has a small radio dot drawn to the left of its Caption.

For a [MsgBox](../objects/msgbox.md), the Style property determines
the type of icon which is displayed in it. This is a character vector with one
of the following values:

|---------|------------------------|
|`'Msg'`  |no icon (the default)   |
|`'Info'` |information message icon|
|`'Query'`|query (question) icon   |
|`'Warn'` |warning icon            |
|`'Error'`|critical error icon     |

For a [Static](../objects/static.md) object, Style defines its
appearance, and may be one of:

|----------------------------|------------------------|
|`'BlackFrame'`              |`'BlackBox'`            |
|`'GreyFrame' or 'GrayFrame'`|`'GreyBox' or 'GrayBox'`|
|`'WhiteFrame'`              |`'WhiteBox'`            |

A [StatusField](../objects/statusfield.md) may be used to monitor
the state of a key on the keyboard. If so, its Style property determines the key
it monitors and may be one of the following:

|----------|--------------------------------------|
|CapsLock  |Monitors state of Caps Lock key       |
|ScrollLock|Monitors state of Scroll Lock key     |
|NumLock   |Monitors state of Num Lock key        |
|KeyMode   |Monitors the keyboard mode (APL/ASCII)|
|InsRep    |Monitors the state of the Insert key  |

For a [Splitter](../objects/splitter.md), the Style property
specifies the orientation of the [Splitter](../objects/splitter.md) and may be `'Vert'` (the default) or `'Horz'`.

For a [TabControl](../objects/tabcontrol.md), the Style property
determines the appearance of its [TabButton](../objects/tabbutton.md) children, and may be `'Tabs'` (the default),
`'Buttons'` or `'FlatButtons'`.

For a [TCPSocket](../objects/tcpsocket.md), Style is a character
vector that specifies the type of data transmitted or received by the socket; it
may be `'Char'`, `'Raw'`,
or `'APL'`. The value APL is valid only if
the [SocketType](sockettype.md) is '`Stream'`.

For a [ToolButton](../objects/toolbutton.md), the Style property
specifies the behaviour of the button and may be `'Push'` (the default), `'Check'`, `'Radio'`,
`'DropDown'`, or `'Separator'`.

For a [ToolControl](../objects/toolcontrol.md), the Style property
determines the appearance of its [ToolButton](../objects/toolbutton.md) children and may be `'Buttons'`, `'FlatButtons'` (the default), `'List'` or `'FlatList'`.

For a [TrackBar](../objects/trackbar.md), the Style property
determines the appearance and behaviour of the TrackBar and may be `'Standard'` (the default) or `'Selection'`.
