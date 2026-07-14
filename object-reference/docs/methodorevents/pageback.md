# <span>PageBack</span> <span>Event 353</span>

**Applies To:** [PropertyPage](../objects/propertypage.md)

**Description**

If enabled, this event is reported when the user switches from one [PropertyPage](../objects/propertypage.md) to another in a Wizard [PropertySheet](../objects/propertysheet.md) object by clicking its Back button. This event is reported by the old page *after* the page change has occurred and the page change may not be disabled by a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'PageBack'` or 353    |
