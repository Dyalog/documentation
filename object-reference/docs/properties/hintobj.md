# <span>HintObj</span> <span>Property</span>

**Description**

The HintObj property is a character vector or ref that specifies the name of, or a ref to, an object in which the "help" message defined by the [Hint](hint.md) property is to be displayed. This message is displayed when the user positions the mouse pointer over the object. The [Hint](hint.md) is displayed by automatically setting the [Caption](caption.md) or [Text](text.md) property of the object named by HintObj.

The following types of object can therefore be used to display Hints: [Button](../objects/button.md), [Edit](../objects/edit.md), [Combo](../objects/combo.md), [Group](../objects/group.md), [Form](../objects/form.md), [Label](../objects/label.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md) and [Text](../objects/text.md). For a [StatusField](../objects/statusfield.md) that has both [Caption](caption.md) and [Text](text.md) properties, the text property is used for displaying hints.

When the user moves the mouse pointer away from the object, the [Caption](caption.md) or [Text](text.md) property of the object specified by HintObj is reset to an empty vector.

Note that if HintObj is empty, its value is inherited from its parent. Thus setting HintObj on a [Form](../objects/form.md) defines the default location for displaying [Hint](hint.md)s for all the controls in that [Form](../objects/form.md). Setting HintObj on [Root](../objects/root.md) defines the default location for hints for the entire application.

**Application**

Objects: [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [MenuItem](../objects/menuitem.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md), [ToolButton](../objects/toolbutton.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
