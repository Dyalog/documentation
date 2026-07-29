# <span>Border</span> <span>Property</span>

**Description**

This property specifies whether or not an object is displayed with a border around it. It is a single number with the value 0 (no border)1 (Border), or 2. The value 2 applies only to a [Form](../objects/form.md) and is used in combination with `('EdgeStyle' 'Dialog')` to obtain standard dialog box appearance

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), the value of the Border property is only relevant if [Sizeable](sizeable.md), [Moveable](moveable.md), [SysMenu](sysmenu.md), [MaxButton](maxbutton.md) and [MinButton](minbutton.md) are **all** 0.

## Note

The value of the Border property may only be assigned by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and may **not** be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws).

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBtn](../objects/tabbtn.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
