# <span>ChooseFont</span> <span>Method 240</span>

**Description**

This method is used to display the standard Windows font selection dialog box.

The argument to ChooseFont is `⍬` or a 1 or 2-element array as follows:

|-----|------------|---------------------------|
|`[1]`|Printer name|character scalar or vector.|
|`[2]`|Modify flag |0 or 1.                    |

If the argument is `⍬` or the first element of the argument is `''`, the user is offered a list of fonts suitable for use on the screen. If not, the user is offered a choice of fonts suitable for the specified [Printer](../objects/printer.md) object. If you omit the 2nd element, the modify flag defaults to 0.

The dialog box is initialised with the properties of the [Font](../objects/font.md) object specified in the first element of the event message.

When the user presses the "OK" button, the "Cancel" button or closes the dialog box, ChooseFont terminates. Its result is either 0 (user pressed "Cancel") or a 2-element vector. In the latter case, the first element is an 8-element array that describes the selected font as described below, and the second element is a 3-element RGB colour vector.

|-----|--------------------------------------------------------|
|`[1]`|Face name of selected font (character vector)           |
|`[2]`|Character height in pixels (integer)                    |
|`[3]`|Fixed width or not (Boolean)                            |
|`[4]`|Italic or not (Boolean)                                 |
|`[5]`|Underline or not (Boolean)                              |
|`[6]`|Weight (integer)                                        |
|`[7]`|Angle of rotation (integer)                             |
|`[8]`|Character set (see [CharSet](../properties/charset.md) )|

If the modify flag was 1, the [Font](../objects/font.md) object is redefined to match the user's selections and all the objects that reference the [Font](../objects/font.md) are redrawn.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Font](../objects/font.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [RichEdit](../objects/richedit.md), [Root](../objects/root.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBtn](../objects/tabbtn.md), [Text](../objects/text.md), [TipField](../objects/tipfield.md), [TreeView](../objects/treeview.md)
