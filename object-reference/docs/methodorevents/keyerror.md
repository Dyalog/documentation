# <span>KeyError</span> <span>Event 23</span>

**Description**

If enabled, this event is generated when the user presses and releases a key
on the keyboard that is invalid for the FieldType of the object and has been
ignored. This event is reported for information only and you may not disable it
or modify it in any way.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq),
or supplied as the right argument to your callback function, is a 6-element
vector as follows :

|-----|--------------|-----------------------|
|`[1]`|Object        |ref or character vector|
|`[2]`|Event         |`'KeyError'` or 23     |
|`[3]`|Character     |character scalar       |
|`[4]`|Character code|integer scalar         |
|`[5]`|Key Number    |integer scalar         |
|`[6]`|Shift state   |integer scalar         |

In the Classic Edition, the resolution of the keystroke to a character (in `⎕AV`)
is performed using the Input Translate Table. In the Unicode Edition, the
resolution is performed by the Operating System.

In the Unicode Edition, the Character Code is the Unicode code point of the
character that the user entered. In the Classic Edition, it is a number in the
range 0-255 which specifies the ASCII character that would normally be generated
by the keystroke, and is independent of the Input Translate Table. If there is
no corresponding ASCII character, the ASCII code reported is 0.

The key number is the physical key number reported by Windows when the key is
pressed.

The Shift State indicates which (if any) of the Shift, Ctrl and Alt keys are
down at the same time as the key is pressed. It is the sum of the following
numbers :

Thus a Shift State of 3 indicates that the user has pressed the key in
conjunction with both the Shift and Ctrl keys. A Shift State of 0 indicates that
the user pressed the key on its own.

**Application**

Objects: [ButtonEdit](../objects/buttonedit.md), [Edit](../objects/edit.md), [Spinner](../objects/spinner.md)
