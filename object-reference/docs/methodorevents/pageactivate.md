# <span>PageActivate</span> <span>Event 360</span>

**Description**

If enabled, this event is reported when the user switches from one [PropertyPage](../objects/propertypage.md) to another in a [PropertySheet](../objects/propertysheet.md) object. This event is reported by the new page *after* the page change has occurred and the page change may not be disabled by a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'PageActivate'` or 360|

You may select a particular page by calling PageActivate as a method, or by setting the [PageActive](../properties/pageactive.md) or [PageActiveObject](../properties/pageactiveobject.md) property of the [PropertySheet](../objects/propertysheet.md).

**Application**

Objects: [PropertyPage](../objects/propertypage.md)
