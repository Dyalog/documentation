# Drag and Drop

Dyalog APL/W provides built-in support for drag/drop operations through the Dragable property. This applies to all objects for which drag/drop is appropriate.

The default value of Dragable is 0 which means that the object cannot be drag/dropped. To enable drag/drop, you can set it to 1 or 2. A value of 1 means that the user drags a box that represents the bounding rectangle of the object. In general, a value of 2 means that the user drags the outline of the object itself, whether or not it is rectangular. However, there are two exceptions. For a Text object, `('Dragable' 2)` means that the user drags the text itself. For an Image object that contains an Icon, `('Dragable' 2)` means that the user drags the icon itself, and not just its outline.

If Dragable is 1 or 2, the user may drag/drop the object using the mouse.

When the user drops an object, the default processing for the event is:

1. If the object is dropped over its parent, it is moved to the new location.
2. If the object is dropped over an object other than its parent, the dragged object remains where it is.

If you enable the DragDrop event (11) on all eligible objects, you can control what happens explicitly. If an object is dropped onto a new parent, you can move it by first deleting it and then recreating it. Note that you must give it a new name to reflect its new parentage. Note too that the DragDrop event reports co-ordinates relative to the object being dropped **on**, so it is easy to rebuild the object in the correct position and with the correct size.

An alternative to using the built-in drag/drop operation is to do it yourself with the Locator object. This is no less efficient and has the advantage that you can choose which mouse button you use. It can also be used to move a group of objects. However, the Locator only supports a rectangular or elliptical outline.
