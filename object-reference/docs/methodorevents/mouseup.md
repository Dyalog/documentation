# <span>MouseUp</span> <span>Event 2</span>

**Description**

If enabled, this event is reported when the user releases one of the mouse buttons. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|-----------|---------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                    |
|`[2]`|Event      |`'MouseUp'` or 2                                                           |
|`[3]`|Y          |y-position of mouse (number)                                               |
|`[4]`|X          |x-position of mouse (number)                                               |
|`[5]`|Button     |button released (number) 1 = left button 2 = right button 4 = middle button|
|`[6]`|Shift State|sum of shift key codes (number) 1 = Shift key is down 2 = Ctrl key is down |

In a graphical object ([Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Image](../objects/image.md), [Marker](../objects/marker.md), [Poly](../objects/poly.md) and [Rect](../objects/rect.md)), the position of the mouse is reported relative to the top-left corner of its bounding rectangle.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Circle](../objects/circle.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Ellipse](../objects/ellipse.md), [Form](../objects/form.md), [Group](../objects/group.md), [Image](../objects/image.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Marker](../objects/marker.md), [MDIClient](../objects/mdiclient.md), [Poly](../objects/poly.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [Rect](../objects/rect.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [Text](../objects/text.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
