# <span>Redraw</span> <span>Property</span>

[**Applies To**](../propertyapplies/redraw.md)

**Description**

The Redraw property specifies whether or not APL automatically redraws an object when it is exposed or when any of its properties change in a way that would affect its appearance.

The value reported by the Redraw property is a Boolean value; 1 means that APL automatically redraws the object when necessary (the default); 0 means that APL does not redraw the object.

Setting Redraw to 0 or 1 affects only whether or not APL will redraw the object from then on.

Setting Redraw to 2 has the same effect as setting it to 1, but the object is also redrawn immediately. Note that no child object is redrawn.

Setting Redraw to 3 has the same effect as setting it to 1, but the object and its children are redrawn immediately.
