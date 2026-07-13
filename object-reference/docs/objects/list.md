# <span>List</span> <span>Object</span>

[Parents](../parentlists/list.md), [Children](../childlists/list.md), [Properties](../proplists/list.md), [Methods](../methodlists/list.md), [Events](../eventlists/list.md)

**Purpose:** Allows the user to select one or more items from a list.

**Description**

The [Items](../properties/items.md) property is either a vector of character vectors or a character matrix, and determines the items in the List.

The size and position of the area used to display the list is defined by [Size](../properties/size.md) and [Posn](../properties/posn.md). If [Size](../properties/size.md) is not chosen to represent an exact number of lines of text, the bottom line of text may be clipped.

The [Index](../properties/index-property.md) property specifies or reports the position of [Items](../properties/items.md) in the list box as a positive integer value. If [Index](../properties/index-property.md) has the value "n", it means that the "nth" item in [Items](../properties/items.md) is displayed on the top line in the list box. However, it is ignored if all the [Items](../properties/items.md) fit within the List object. Note that [Index](../properties/index-property.md) can only be set using [`⎕WS`](../../../language-reference-guide/system-functions/ws) and not by [`⎕WC`](../../../language-reference-guide/system-functions/wc). The default value for [Index](../properties/index-property.md) is `⎕IO`.

The [Style](../properties/style.md) property may be `'Single'` (the default) or `'Multi'`. `'Single'` allows only a single item to be selected. `'Multi'` allows several items to be chosen. In either case, if the [Select](../methodorevents/select.md) event is enabled, it is generated whenever the selection changes. If [Style](../properties/style.md) is `'Multi'` the List will generate a [Select](../methodorevents/select.md) event every time an item is added to the selected list.

Under Windows, you may select or de-select multiple items in a List object by pressing the Ctrl key at the same time as pressing the left mouse button.

The [SelItems](../properties/selitems.md) property is a Boolean vector with one element per element or row in [Items](../properties/items.md) and indicates which (if any) of the items is currently selected (and highlighted).

The [VScroll](../properties/vscroll.md) property determines whether or not the list has a scrollbar. Its possible values are :

|----|---------------------|
|`¯2`|scrollbar if required|
|`¯1`|scrollbar if required|
|`0` |no scrollbar         |

Note that data in a List is always scrollable if there are more items than will fit in the box. [VScroll](../properties/vscroll.md) determines ONLY whether or not a scrollbar is provided.

The [MultiColumn](../properties/multicolumn.md) property is a Boolean value that specifies whether or not the List object displays its items in columns. The default is 0 which produces a single-column display. If [MultiColumn](../properties/multicolumn.md) is 1, the List object displays its items in columns whose width is defined by the [ColumnWidth](../properties/columnwidth.md) property.
