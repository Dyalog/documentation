# <span>AsChild</span> <span>Property</span>



**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**


The AsChild property is a Boolean (default 0) indicating how the [HTMLRenderer](../objects/htmlrenderer.md) object is displayed. AsChild must be set when the object is created and may not subsequently be changed.


If AsChild is 0 (the default) the [HTMLRenderer](../objects/htmlrenderer.md) is displayed in a separate top-level window. If the [HTMLRenderer](../objects/htmlrenderer.md) is  created (with AsChild 0) as a child of another object it still appears as a separate window and its Size and Posn relate to the screen rather than to its parent object. However, it is a member of its parent object's hierarchy and will disappear when its parent is closed.


If AsChild is 1, the [HTMLRenderer](../objects/htmlrenderer.md) must be created as a child of a valid parent type other than Root (which is not supported) and is displayed in a sub-window within its parent.


This property only applies to Microsoft Windows. On other platforms it is ignored.



