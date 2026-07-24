# <span>MouseLeave</span> <span>Event 7</span>

**Description**

If enabled, this event is reported when the user moves the mouse pointer out of an object. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-----------|-------------------------------------|
|`[1]`|Object     |ref or character vector              |
|`[2]`|Event      |`'MouseLeave'` or 7                  |
|`[3]`|Object name|character vector (name of new object)|

This event is generated when the user moves the mouse pointer across the boundary and away from an object. The first element of the event message contains the name of the object that previously contained the mouse pointer and which generated the event when it crossed its boundary. The third element contains the name of the object which now contains the mouse pointer or is an empty vector if the mouse pointer is not now over a Dyalog APL/W object.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
