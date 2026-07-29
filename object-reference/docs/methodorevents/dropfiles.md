# <span>DropFiles</span> <span>Event 450</span>

**Description**

If enabled, this event is reported when the user drags a file icon or a set of file icons and drops them onto the object. The system takes no action other than to report the event.

Note that the event is only reported if [AcceptFiles](../properties/acceptfiles.md) is set to 1.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :

|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'DropFiles'` or 450|
|`[3]`|Files|Vector of character vectors containing the file names.|
|`[4]`|Item number|Integer. The index of the item within the object onto which the file(s) was dropped. Applies only to objects that have an [Items](../properties/items.md) property such as List, [ListView](../objects/listview.md) and [TreeView](../objects/treeview.md) .|
|`[5]`|Shift state|Integer. Sum of 1=shift key, 2=Ctrl key, 4=Alt key|

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
