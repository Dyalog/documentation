# The Co-ordinate System

Each object has a Coord property that determines the units in which its Posn and Size properties are expressed. For full details, see [Coord](../../../object-reference/properties/coord).

Coord may be set to one of the following values :

|---|---|
|`'Inherit'`|this means that the object assumes the same co-ordinate system as its parent. This is the default for all objects except the Root object.|
|`'Prop'`|the position and size of the object are expressed as a percentage of the dimensions of its parent.|
|`'Pixel'`|The position and size of the object are expressed in pixels, which are interpreted as either `'ScaledPixel'` or `'RealPixel'` according to the value of the DYALOG_PIXEL_TYPE parameter.|
|`'ScaledPixel'`|The position and size of the object are expressed in pixels but these metrics are scaled according to the user's chosen scaling factor.|
|`'RealPixel'`|The position and size of the object are expressed in pixels.|
|`'User'`|the position and size of the object are expressed in units defined by the YRange and XRange properties of the object's parent.|
|`'Cell'`|the position and size of the object are expressed in cell coordinates (applies only to Grid and its graphical children).|

By default, the value of Coord for the Root object is `'Prop'`. For all other objects, the default is `'Inherit'`. This means that the default co-ordinate system is a proportional one.

You can change Coord from one value to another as you require. It only affects the units in which Size and Posn are currently expressed. The physical position and size are unaffected. Note that if you set Posn and/or Size in the same `⎕WC` or `⎕WS` statement as you set Coord, it is the **old** value of Coord that is applied.

The co-ordinate system is also independent of the way in which objects are reconfigured when their parent is resized. This is perhaps not immediately obvious, as it might be expected that objects which are specified using Pixel co-ordinates will be unaffected when their parent is resized. This is not necessarily the case as the manner in which objects respond to their parent being resized is determined **independently** by the AutoConf and Attach properties.

The User co-ordinate system is useful not only to automate scaling for graphics, but also to perform scrolling. This is possible because XRange and YRange define not just the scale along each axis, but also the position of the origin of the co-ordinate system in the parent window.
