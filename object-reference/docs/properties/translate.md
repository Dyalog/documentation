# <span>Translate</span> <span>Property</span>

**Description**

This property specifies whether or not character data is to be translated.

Translate applies to the Classic Edition only. In the Unicode Edition,
			its value is ignored.

Translate is a character vector whose values may be `'Inherit'`,
`'Translate'`, `'ANSI'` or `'None'`.

A value of `'Translate'` means that all
character property values and event parameters are translated to and from `⎕AV` using the current output translation table (WIN.DOT).

`'None'` means that character data is
passed between APL and the object with no translation.

If you set the value of the Translate property to `'ANSI'`,
APL does not attempt to resolve characters as they are typed by the user via the
Input Translate Table. Using Translate `'ANSI'` in combination with the appropriate value of [CharSet](charset.md) and the corresponding National Language keyboard will permit users to enter
strings in non-western languages.

`'Inherit'` means that the object
inherits its translation from its parent.

The default value for the Root and Printer objects is `'Translate'`,
and for most other objects it is `'Inherit'`.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Clipboard](../objects/clipboard.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [ImageList](../objects/imagelist.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [MenuItem](../objects/menuitem.md), [Metafile](../objects/metafile.md), [OCXClass](../objects/ocxclass.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [Separator](../objects/separator.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [Text](../objects/text.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
