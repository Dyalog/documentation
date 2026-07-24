# <span>Sizeable</span> <span>Property</span>

**Description**

This property determines whether or not an object can be directly resized by the user once it has been created by [`⎕WC`](../../../language-reference-guide/system-functions/wc).

It is a single number with the value 0 (the object cannot be resized by the user) or 1 (the object may be resized by the user). The default is 1.

For a [Form](../objects/form.md) , [HTMLRenderer](../objects/htmlrenderer.md) or [SubForm](../objects/subform.md), the Sizeable property may only be set by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and cannot subsequently be altered using [`⎕WS`](../../../language-reference-guide/system-functions/ws). An attempt to do so generates a `NONCE ERROR`. For a [Form](../objects/form.md) or [HTMLRenderer](../objects/htmlrenderer.md), the default value is 1 and the object occupies a standard resizeable window with a border. Note that the value of Sizeable is independent of the values of the [MaxButton](maxbutton.md) and [MinButton](minbutton.md) properties, so that a [Form](../objects/form.md) or [HTMLRenderer](../objects/htmlrenderer.md) with [MaxButton](maxbutton.md) 1 can be maximised even though its Sizeable property is 0.

For other objects, the default value of the Sizeable property is 0. However, setting it to 1 (which may be done dynamically using [`⎕WS`](../../../language-reference-guide/system-functions/ws)) allows the user to resize it with the mouse.

In all these cases, when the user resizes an object, the object will generate a [Configure](../methodorevents/configure.md) (31) event.

Sizeable also applies to the [Locator](../objects/locator.md) object. In this case, a value of 1 implies "rubberbanding" and a value of 0 means "no rubberbanding". See [Locator](../objects/locator.md) object for further details.

**Application**

Objects: [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Locator](../objects/locator.md), [ProgressBar](../objects/progressbar.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
