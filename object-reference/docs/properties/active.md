# <span>Active</span> <span>Property</span>

[**Applies To**](../propertyapplies/active.md)

**Description**

This property specifies whether or not an object is currently responsive to user actions. It is a single number with the value 0 (object is inactive and does not generate events) or 1 (object is active and capable of generating events). The default is 1.

Setting Active to 0 disables the object (and all its children), even though the object may be referenced in the argument to [`⎕DQ`](../../../language-reference-guide/system-functions/dq). It is therefore possible to deactivate an object from a callback function.

In general, the text associated with an object whose Active property is 0 is displayed in grey.
