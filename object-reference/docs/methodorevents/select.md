# <span>Select</span> <span>Event 30</span>

**Description**

For a [Button](../objects/button.md) with [Style](../properties/style.md)`'Push'` this event is generated when the user "pushes" the button. This can be done by clicking the left mouse button, or by pressing the Enter key or the space bar when the [Button](../objects/button.md) has the focus. The Select event can also be generated when the [Button](../objects/button.md) does not have the focus, by pressing the Enter key when its [Default](../properties/default.md) property is 1 or by pressing the ESC key when its [Cancel](../properties/cancel.md) property is 1.

For a [Button](../objects/button.md) with [Style](../properties/style.md)`'Radio'` or `'Check'` this event is generated when the user toggles the button from one state to another. This can be achieved by clicking the left mouse button or by pressing the space bar when the [Button](../objects/button.md) has the focus.

For a [Combo](../objects/combo.md) or [List](../objects/list.md) object, a Select event is generated when the user selects an item from the list, whether by pressing the arrow keys or by clicking the left mouse button.

For a [MenuItem](../objects/menuitem.md), a Select event is generated when the user chooses the item.

For all other objects, this event is generated when the user presses the keys associated with the object's [Accelerator](../properties/accelerator.md) property.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |Event code             |

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [Clipboard](../objects/clipboard.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [Cursor](../objects/cursor.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Icon](../objects/icon.md), [Image](../objects/image.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [Metafile](../objects/metafile.md), [Poly](../objects/poly.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [Text](../objects/text.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
