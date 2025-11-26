<h1 class="heading"><span class="name">Attach</span> <span class="right">Property</span></h1>

[**Applies To**](../propertyapplies/attach.md)

**Description**


This property specifies how an object responds to its parent being resized by the user (but not by altering the [Size](size.md) property). It is a 4-element vector of character vectors which defines how each of the four edges of the object moves in response to a resize request made by the parent. Note that this property is only effective if the value of [AutoConf](autoconf.md) on the parent is 2 or 3 and [AutoConf](autoconf.md) for the object itself is 1 or 3.




The 4 elements of Attach refer to the Top, Left, Bottom and Right edges of the object respectively. Their values may be defined as follows :


|Element|Value     |Meaning                                                       |
|-------|----------|--------------------------------------------------------------|
|`[1]`  |`'Top'`   |top edge of object attached to *top* edge of parent.          |
|&nbsp; |`'Bottom'`|top edge of object attached to *bottom* edge of parent.       |
|&nbsp; |`'None'`  |top edge of object is not attached to its parent              |
|`[2]`  |`'Left'`  |left edge of object is attached to *left* edge of parent      |
|&nbsp; |`'Right'` |left edge of object is attached to *right* edge of parent     |
|&nbsp; |`'None'`  |left edge of object is not attached to its parent             |
|`[3]`  |`'Top'`   |bottom edge of object is attached to *top* edge of parent.    |
|&nbsp; |`'Bottom'`|bottom edge of object is attached to *bottom* edge of parent. |
|&nbsp; |`'None'`  |bottom edge of object is not attached to its parent           |
|`[4]`  |`'Left'`  |right edge of object is attached to *left* edge of parent     |
|&nbsp; |`'Right'` |right edge of object is attached to *right* edge of its parent|
|&nbsp; |`'None'`  |right edge of object is not attached to its parent            |



If an edge of the object is attached to an edge of its parent, its position in absolute (pixel) terms remains fixed relative to that edge when its parent is resized. Thus if [Coord](coord.md) is `'Pixel'`, the corresponding [Posn](posn.md) or [Size](size.md) property of the object remains unaffected by the resize. If [Coord](coord.md) has any other value, the value of [Posn](posn.md) or [Size](size.md) will change.


If an edge of the object is *not* attached to its parent, its absolute position (in pixels) will change in proportion to the size change (in the corresponding direction) of its parent. Thus if [Coord](coord.md) is `'Pixel'`, the corresponding [Posn](posn.md) or [Size](size.md) property of the object will change as a result of the resize. If [Coord](coord.md) has any other value, the value of [Posn](posn.md) or [Size](size.md) will be unaffected.


The default value of Attach is `('None' 'None' 'None' 'None')`. This causes the object to reposition and resize itself in proportion to its parent.


Some objects have an [Align](align.md) property which, among other things, provides a quick way to set their Attach property. Examining this mechanism may help to further explain how the Attach property works. Setting [Align](align.md) to `'Top'` has the effect of setting Attach to `('Top' 'Left' 'Top' 'Right')`. Attaching the top edge of the object to the top edge of its parent causes the object to remain at a fixed distance from the top edge of its parent. The additional measure of attaching its bottom edge to the top edge of its parent causes the height of the object to remain fixed. Attaching the left and right edges of the object to the corresponding edges of its parent causes the object to shrink and expand as the parent is resized horizontally. If you position the object at (0 0) and set its width to be the same as the width of its parent, you have an object that always occupies the entire length of its parent, yet remains of fixed height. This is precisely the behaviour required for a [ToolBar](../objects/toolbar.md) or a top [Scroll](../objects/scroll.md) Bar. For further details, see [Align](align.md) property.


