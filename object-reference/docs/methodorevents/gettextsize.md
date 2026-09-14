# <span>GetTextSize</span> <span>Method 146</span>

The GetTextSize method obtains the size of the bounding rectangle of a text item in a given font. The result is given in the co-ordinate system of the object in question. This method is useful for positioning Text objects.

GetTextSize duplicates the functionality of the TextSize property. It is recommended that you use GetTextSize instead of TextSize which may be removed in a future release of Dyalog APL.

The argument to GetTextSize is a 1 or 2-element array as follows:

|-----|---------|----------------|
|`[1]`|Text item|character array |
|`[2]`|Font|character vector naming a [Font](../objects/font.md) object, or a reference to one|

When you invoke GetTextSize you give the text item in whose size you are interested and, optionally, a Font object. The Font can be given either by name or as a reference, as shown in the second and third examples below respectively. The text item can be a simple scalar, a vector, or a matrix. If the Font is omitted, the result is given using the current font for the object in question.

<h2 class="example">Examples</h2>
```apl
      'F'⎕WC'Form'
      F.GetTextSize'Hello World'
2.407407407 5.729166667

      'FNT1'⎕WC'Font' 'Arial' 72
      F.GetTextSize'Hello World' 'FNT1'
2.962962963 8.020833333

      'FNT2'⎕WC'Font' 'Arial' 16 0 0 0 400 0
      F.GetTextSize'Hello World'FNT2
2.962962963 6.979166667

      F.Coord←'Pixel'
      F.FontObj←'FNT1'
      F.GetTextSize'Hello World'
72 335
```

## Application

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Bitmap](../objects/bitmap.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [Printer](../objects/printer.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabControl](../objects/tabcontrol.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
