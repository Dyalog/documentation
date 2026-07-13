# <span>AutoConf</span> <span>Property</span>

[**Applies To**](../propertyapplies/autoconf.md)

**Description**


This property determines what happens to an object when its **parent** is resized, and how resizing an object affects its children. It may take one of the following values; the default is 3.



|---|-------------------------------------------------------------|
|0  |Ignore resize by parent. Do not propagate resize to children.|
|1  |Accept resize by parent. Do not propagate resize to children.|
|2  |Ignore resize by parent. Propagate resize to children.       |
|3  |Accept resize by parent. Propagate resize to children.       |


If AutoConf is 0 or 2, the object's **physical** size (in pixels) and position (in pixels) relative to the top left corner of its parent remains unchanged when its parent is resized. If the object has `'Prop'` or `'User'` co-ordinates, the values of its [Posn](posn.md) and [Size](size.md) properties will change as a result.


If AutoConf is 1 or 3, by default, the object is physically reconfigured when its parent is resized such that its **relative** size and position within its parent remain unchanged. If the object has `'Pixel'` co-ordinates, the values of its [Posn](posn.md) and [Size](size.md) properties will change as a result. Note that this default processing can be prevented by inhibiting the [Configure](../methodorevents/configure.md) (31) Event.


If AutoConf is 0 or 1 and the object is resized, either by its parent or directly by the user, it does **not** attempt to physically reconfigure its children. This means that if the children have `'Prop'` or `'User'` co-ordinates, the values of their [Posn](posn.md) and [Size](size.md) co-ordinates will change as a result.


If AutoConf is 2 or 3 and the object is resized, either by its parent or directly by the user, it propagates a [Configure](../methodorevents/configure.md) (31) Event to each of its children. By default this means that the object's children will be physically reconfigured so that they maintain their relative positions and sizes within it. If their co-ordinate system is `'Pixel'`, the values of their [Posn](posn.md) and [Size](size.md) properties will change as a result.


!!! note
    Additional or alternative control may be imposed by inhibiting the [Configure](../methodorevents/configure.md) (31) Event. This can be done either by setting the event's "action" code to `¯1` or by returning a 0 from a callback function attached to it.


