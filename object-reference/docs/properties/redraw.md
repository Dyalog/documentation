# <span>Redraw</span> <span>Property</span>

**Description**

The Redraw property specifies whether or not APL automatically redraws an object when it is exposed or when any of its properties change in a way that would affect its appearance.

The value reported by the Redraw property is a Boolean value; 1 means that APL automatically redraws the object when necessary (the default); 0 means that APL does not redraw the object.

Setting Redraw to 0 or 1 affects only whether or not APL will redraw the object from then on.

Setting Redraw to 2 has the same effect as setting it to 1, but the object is also redrawn immediately. Note that no child object is redrawn.

Setting Redraw to 3 has the same effect as setting it to 1, but the object and its children are redrawn immediately.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
