# <span>MouseEnter</span> <span>Event 6</span>

**Description**

If enabled, this event is reported when the user moves the mouse pointer into (over) an object. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-----------|------------------------------------------|
|`[1]`|Object     |ref or character vector                   |
|`[2]`|Event      |`'MouseEnter'` or 6                       |
|`[3]`|Object name|character vector (name of previous object)|

This event is generated when the user moves the mouse pointer across the boundary and into an object. The first element of the event message is the name of the object over which the mouse pointer now resides. The 3rd element of the event message contains the name of the object that was previously under the mouse pointer, or is an empty vector if the mouse pointer was not previously over a Dyalog APL/W object.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
