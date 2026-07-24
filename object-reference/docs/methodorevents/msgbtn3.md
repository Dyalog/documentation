# <span>MsgBtn3</span> <span>Event 63</span>

**Description**

If enabled, this event is reported when the user responds to a [MsgBox](../objects/msgbox.md) object by clicking its third (from the left) button. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows:

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'MsgBtn3'` or 63      |

**Application**

Objects: [MsgBox](../objects/msgbox.md)
