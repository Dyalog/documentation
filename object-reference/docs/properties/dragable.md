# <span>Dragable</span> <span>Property</span>

[**Applies To**](../propertyapplies/dragable.md)

**Description**

This property determines whether or not an object may be the subject of a "drag and drop" operation.

Dragable is a single number with the value 0, 1 or 2. A value of 0 (which is the default) means that the object may not be drag/dropped. A value of 1 means that the object may be drag/dropped and that during the "drag" operation, a box representing the bounding rectangle around the object is displayed on the screen. A value of 2 means that the **outline** of the object is displayed as the object is dragged, or, if the object is an [Image](../objects/image.md) with a [Picture](picture.md) property containing the name of an [Icon](../objects/icon.md) object, the icon itself is displayed as it is dragged. For rectangular non-graphical objects, values of 1 and 2 are equivalent.

If an object is Dragable, the user may drag it by positioning the mouse pointer within the object, depressing the left mouse button, then moving the mouse with the button held down. During the drag operation, the mouse pointer is automatically changed to a "drag" symbol. The object is "dropped" by releasing the left mouse button. The effect depends upon where it is dropped, and on the action associated with the [DragDrop](../methodorevents/dragdrop.md) event for the object under the mouse pointer (if any).

If there is no object under the mouse pointer, the "drag and drop" operation is ignored. Otherwise, the object under the mouse pointer generates a [DragDrop](../methodorevents/dragdrop.md) event.

If the object under the mouse pointer is the parent of the object that has been "dragged and dropped", the default action is for the system to move that object to the new location within its parent. If you wish to allow your user to freely move an object within its parent [Form](../objects/form.md) or [Group](../objects/group.md), simply set its Dragable property to 1; the system will take care of the rest. If you want to allow the user to move an object, but you want to know about it when it happens, you can associate a callback function to the [DragDrop](../methodorevents/dragdrop.md) event that queries the new position. To permit the operation to complete, the callback function should either not return a result or it should return something other than a scalar 0. To selectively disable movement, your callback function should return a scalar 0 in circumstances when the "drop" is not to be permitted.

If the object under the mouse pointer is not the parent of the object being dragged, the default action is for the system to ignore the operation. However, by enabling the [DragDrop](../methodorevents/dragdrop.md) event, your application can of course take whatever action is appropriate, including perhaps moving the dragged object to a new parent.

Note that a Dragable object does not generate a [Configure](../methodorevents/configure.md) (31) event when it is dragged and dropped.
