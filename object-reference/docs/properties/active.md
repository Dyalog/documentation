# <span>Active</span> <span>Property</span>

**Description**

This property specifies whether or not an object is currently responsive to user actions. It is a single number with the value 0 (object is inactive and does not generate events) or 1 (object is active and capable of generating events). The default is 1.

Setting Active to 0 disables the object (and all its children), even though the object may be referenced in the argument to [`⎕DQ`](../../../language-reference-guide/system-functions/dq). It is therefore possible to deactivate an object from a callback function.

In general, the text associated with an object whose Active property is 0 is displayed in grey.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [Splitter](../objects/splitter.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [Text](../objects/text.md), [Timer](../objects/timer.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
