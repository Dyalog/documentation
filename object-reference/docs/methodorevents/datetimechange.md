# <span>DateTimeChange</span> <span>Event 267</span>

**Applies To:** [DateTimePicker](../objects/datetimepicker.md)

**Description**

If enabled, this event is reported by a [DateTimePicker](../objects/datetimepicker.md) object when the user changes the [DateTime](../properties/datetime.md) value. This occurs when the user selects a new date from the drop-down calendar, or increments or decrements a date time element using the spinner buttons, or edits a datetime element using the keyboard. In the latter case, the event may not be generated until the input focus leaves the corresponding date time element.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 6-element vector as follows :

|-----|------|-------------------------|
|`[1]`|Object|ref or character vector  |
|`[2]`|Event |`'DateTimeChange'` or 267|
|`[3]`|IDN   |integer                  |
|`[4]`|Hour  |integer                  |
|`[5]`|Minute|integer                  |
|`[6]`|Second|integer                  |

This event is reported for information only and cannot be disabled or modified in any way. It is not possible to enqueue this event; set the DateTime value instead.

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).
