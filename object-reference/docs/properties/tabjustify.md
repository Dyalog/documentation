# <span>TabJustify</span> <span>Property</span>

**Description**

The TabJustify property specifies, the positions at which the picture and caption are drawn within each tab or button implemented by a [TabButton](../objects/tabbutton.md) in a TabControl object.

TabJustify is a character vector that may be `'Centre'`, `'Edge'`, or `'IconEdge'`. Its default value is `'Centre'`.

If TabJustify is `'Centre'`, the picture and caption are arranged in the centre of the [TabButton](../objects/tabbutton.md).

![](../img/tab13.gif)

If TabJustify is `'Edge'`, the picture and caption are together aligned to  the appropriate edge of the [TabButton](../objects/tabbutton.md) according to the value of Align.

![](../img/tab14.gif)

If TabJustify is set to `'IconEdge'`, the caption is drawn centrally and only picture is aligned to the edge.

![](../img/tab15.gif)

TabJustify is only honoured if fixed size tabs are in effect.

**Application**

Objects: [TabControl](../objects/tabcontrol.md)
