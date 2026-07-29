# <span>LostFocus</span> <span>Event 41</span>

**Description**

If enabled, this event is generated when the user transfers the keyboard focus away from the object in question.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-----------|-------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                      |
|`[2]`|Event      |`'LostFocus'` or 41                                          |
|`[3]`|Object name|character vector (name of object that has received the focus)|

If the focus is transferred to a window that is not part of the Dyalog APL GUI Interface, the third element is an empty vector.

The LostFocus event is generated **after** the focus has changed. The default processing is therefore to take no action. However, if you inhibit the event by returning a 0 from your callback function, the focus is automatically restored to the object that had lost it.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [SubForm](../objects/subform.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md)
