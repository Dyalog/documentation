# <span>MsgBtn2</span> <span>Event 62</span>



**Applies To:** [MsgBox](../objects/msgbox.md)

**Description**


If enabled, this event is reported when the user responds to a [MsgBox](../objects/msgbox.md) object by clicking its second (from the left) button. The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows:


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'MsgBtn2'` or 62      |



