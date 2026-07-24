# <span>TabIndex</span> <span>Property</span>

**Description**

The TabIndex property reports the `⎕IO`-dependent relative position of a child object within the list of child objects owned by its parent. If `N` is the number of children owned by an object, TabIndex is an integer between `⎕IO` and `(N-~⎕IO)`. The sequence of objects in this list is also used as the tabbing sequence, that is, if the input focus is on the first child in the list, pressing Tab moves the input focus to the next child in the list.

When you create a child object, it is inserted in the list at the position specified by its TabIndex property. If TabIndex is omitted, it is appended to the end of the list.

If you subsequently change TabIndex, the object is moved to the corresponding position in the list.

Naturally, if you specify a value of TabIndex that is greater than the number of existing children, the object is inserted at or moved to the end of the list.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
