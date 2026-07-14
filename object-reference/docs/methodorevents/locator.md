# <span>Locator</span> <span>Event 80</span>

**Applies To:** [Locator](../objects/locator.md)

**Description**

If enabled, this event is generated when the user releases a mouse button, or presses any key (other than a cursor movement key) during a [`⎕DQ`](../../../language-reference-guide/system-functions/dq) on a [Locator](../objects/locator.md) object.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 9-element vector as follows :

|-----|------------|-------------------------------------------------------------------------------------------------------------------|
|`[1]`|Object      |ref or character vector                                                                                            |
|`[2]`|Event       |`'Locator'` or 80                                                                                                  |
|`[3]`|Y           |y-position of [Locator](../objects/locator.md) after [`⎕DQ`](../../../language-reference-guide/system-functions/dq)|
|`[4]`|X           |x-position of [Locator](../objects/locator.md) after [`⎕DQ`](../../../language-reference-guide/system-functions/dq)|
|`[5]`|H           |height of [Locator](../objects/locator.md) after [`⎕DQ`](../../../language-reference-guide/system-functions/dq)    |
|`[6]`|W           |width of [Locator](../objects/locator.md) after [`⎕DQ`](../../../language-reference-guide/system-functions/dq)     |
|`[7]`|Mouse Button|number of the button which was released (0 if keystroke)                                                           |
|`[8]`|Keystroke   |character scalar or vector containing the "Input Code" for the key that terminated the operation                   |
|`[9]`|Shift state |integer scalar                                                                                                     |
