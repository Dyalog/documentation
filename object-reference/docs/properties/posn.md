# <span>Posn</span> <span>Property</span>

[**Applies To**](../propertyapplies/posn.md)

**Description**


With the exception of [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md) and [Separator](../objects/separator.md) objects, Posn is a 2-element numeric vector specifying the y-position and x-position respectively of the top-left corner of the object relative to its parent. For a [Form](../objects/form.md), Posn specifies its position on the screen. The units are defined by the [Coord](coord.md) property.


When specifying Posn for [`⎕WC`](../../../language-reference-guide/system-functions/wc), you can allow the y-position or x-position to assume a default value by giving the corresponding element a value of `⍬`.


Using [`⎕WS`](../../../language-reference-guide/system-functions/ws), if you want to set the y-position, but not the x-position, or vice-versa, you should specify `⍬` for the item you don't want to change.


For [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md) and [Separator](../objects/separator.md) objects, Posn is a single integer that specifies the position at which the object is to be **inserted** in its parent. For example, to add a new [MenuItem](../objects/menuitem.md) between the third and fourth items in an existing [Menu](../objects/menu.md), you would specify its Posn as 4. For these objects, the value of Posn returned by [`⎕WG`](../../../language-reference-guide/system-functions/wg) is the current index of the object within its parent.



