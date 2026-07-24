# <span>DropDown</span> <span>Event 45</span>

**Description**

If enabled, this event is reported when the user clicks the drop-down button in a  [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [ColorButton](../objects/colorbutton.md), [DateTimePicker](../objects/datetimepicker.md) or [Menu](../objects/menu.md) object, just before the drop-down list, colour selection, calendar or -menu is displayed.

For a [Button](../objects/button.md) this event only applies if the Style of the [Button](../objects/button.md) is `Split`. For such a [Button](../objects/button.md) and for the [ButtonEdit](../objects/buttonedit.md) object there is no default processing for the event and it is the responsibility of the programmer to take appropriate action in a call-back function.

For a [DateTimePicker](../objects/datetimepicker.md) this event only applies if the Style of the [DateTimePicker](../objects/datetimepicker.md) is `'Combo'`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'DropDown'` or 45     |

This event is reported for information only and cannot be disabled or modified in any way.

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).

**Application**

Objects: [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [DateTimePicker](../objects/datetimepicker.md), [Menu](../objects/menu.md)
