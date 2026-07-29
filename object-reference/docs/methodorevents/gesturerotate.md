# <span>GestureRotate</span> <span>Event 495</span>

**Description**

This event is reported when the user touches  two fingers on an object and twists them clockwise or anticlockwise.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows :

|---|---|---|
|`[1]`|Object|ref or character vector|
|`[2]`|Event|`'GestureRotate'` or 495|
|`[3]`|Flags|integer which reports the state of the gesture|
|`[4]`|Location|2-element integer vector containing the y and x-position respectively of the  point midway between the two fingers. These are reported in pixel coordinates relative to the origin of the screen.|
|`[5]`|Angle|a scalar number which represents the angle of rotation of the twist measured in radians `(0 → ○2` ) from the x-axis in a counter-clockwise direction.|

The Flags parameter [3] which reports the state of the Gesture, is an integer with the value 0, 1 (*GF_BEGIN*),or 4 (*GF_END*) with the following meanings:

|----------|-----|------------------------|
|Name      |Value|Description             |
|&nbsp;    |0    |A gesture is in progress|
|`GF_BEGIN`|1    |A gesture is starting.  |
|`GF_END`  |4    |A gesture has finished. |

When the user first touches two fingers on an object and begins to twist, the object generates a GestureRotate event with a `Flags` parameter of 1 (`GF_BEGIN`). As the user continues to twist his fingers, the object generates a series of GestureRotate events with a `Flags` parameter of 0. When the user lifts one or both fingers away, the object generates a final GestureRotate event, with a `Flags` parameter of 4 (`GF_END`).

No other event will be reported between the start and end of a series of GestureRotate events.

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).

Returning zero from the callback disables any default handling by the operating system.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Group](../objects/group.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [Spinner](../objects/spinner.md), [SubForm](../objects/subform.md), [TreeView](../objects/treeview.md)
