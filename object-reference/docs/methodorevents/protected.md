# <span>Protected</span> <span>Event 470</span>



**Applies To:** [RichEdit](../objects/richedit.md)

**Description**


If enabled, this event is reported when the user attempts to alter protected text in a RichEdit. See [CharFormat](../properties/charformat.md) property.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'Protected'` or 470   |



