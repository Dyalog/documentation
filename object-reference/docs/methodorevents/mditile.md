# <span>MDITile</span> <span>Method 111</span>

**Description**

This method causes the [MDIClient](../objects/mdiclient.md) object to organise its child [Form](../objects/form.md)s as a row or column. To permit the user to carry out this action, it is recommended that a suitable callback function or expression is attached to a [MenuItem](../objects/menuitem.md) or [Button](../objects/button.md). The callback function or expression should then call the MDITile method.

Note that because there are restrictions concerning the minimum height and width of a window, MS-Windows does not necessarily respond as requested. If the [MDIClient](../objects/mdiclient.md) is itself of insufficient size, or if it contains a large number of child [Form](../objects/form.md)s, Windows may choose to tile the [Form](../objects/form.md)s in a row when a column was specified or vice versa. It may also choose to ignore the event entirely.

The argument to MDITile is `⍬`, or a single item as follows:

|-----|---------|---------------------------|
|`[1]`|Tile Mode|0 (vertical)<br/>1 (horizontal)|

If the argument is `⍬`, the *Tile Mode* defaults to 0.

**Application**

Objects: [MDIClient](../objects/mdiclient.md)
