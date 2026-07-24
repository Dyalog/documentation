# <span>Expose</span> <span>Event 32</span>

**Description**

If enabled, this event is reported when part or all of the object's window is exposed to view. Under normal circumstances, APL repaints the exposed region automatically. However, if you have drawn unnamed graphical objects (which are **not** managed by APL) you should use this event to redraw them when required. Note that APL will itself repaint any **named** objects in the region before reporting the event.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|------|-----------------------------------------------|
|`[1]`|Object|ref or character vector                        |
|`[2]`|Event |`'Expose'` or 32                               |
|`[3]`|Y     |y-position of top-left corner of exposed region|
|`[4]`|X     |x-position of top-left corner of exposed region|
|`[5]`|H     |height of exposed region                       |
|`[6]`|W     |width of exposed region                        |

This event **cannot** be disabled by setting its action code to `¯1`. Similarly, setting the result of a callback function to 0 has no effect on it.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
