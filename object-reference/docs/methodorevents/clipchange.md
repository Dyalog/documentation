# <span>ClipChange</span> <span>Event 120</span>

**Applies To:** [Clipboard](../objects/clipboard.md)

**Description**

If enabled, this event is reported when another application changes the contents of the Windows clipboard.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'ClipChange'` or 120  |
