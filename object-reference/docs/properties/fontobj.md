# <span>FontObj</span> <span>Property</span>

**Description**

The FontObj property associates a font with an object. It specifies either the name of or a ref to a [Font](../objects/font.md) object

If unspecified, the default value for FontObj is an empty character vector. For most objects, this setting implies that the font used in the object is **inherited** from its parent object. However, [CoolBar](../objects/coolbar.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [StatusBar](../objects/statusbar.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), and [ToolControl](../objects/toolcontrol.md) objects do not inherit their font.

Note that the default value of FontObj for [Root](../objects/root.md) is also an empty character vector and that this implies the Windows default GUI font, which is a Windows user preference setting.

Note however that it is not currently possible to specify the font for [Menu](../objects/menu.md) and [MenuItem](../objects/menuitem.md) objects which are the direct descendants of a [MenuBar](../objects/menubar.md). Nor is it possible to specify the font used for the [Caption](caption.md) in a [Form](../objects/form.md).

**Application**

Objects: [ActiveXContainer](../objects/activexcontainer.md), [ActiveXControl](../objects/activexcontrol.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [MenuItem](../objects/menuitem.md), [Printer](../objects/printer.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabControl](../objects/tabcontrol.md), [Text](../objects/text.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md)
