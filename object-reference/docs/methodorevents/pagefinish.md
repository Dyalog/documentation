# <span>PageFinish</span> <span>Event 355</span>

**Applies To:** [PropertyPage](../objects/propertypage.md)

**Description**

If enabled, this event is reported when the user clicks the Finish button in a Wizard [PropertySheet](../objects/propertysheet.md). This event is reported by current (last) [PropertyPage](../objects/propertypage.md). The event is reported for information only and cannot be affected by a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'PageFinish'` or 355  |
