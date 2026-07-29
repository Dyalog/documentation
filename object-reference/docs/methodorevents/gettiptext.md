# <span>GetTipText</span> <span>Event 325</span>

**Description**

If enabled, this event is reported by a [TreeView](../objects/treeview.md) or [ListView](../objects/listview.md) object just before it displays a tip for a specific row.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :

|-----|-------------|------------------------------------------------------------|
|`[1]`|Object       |ref or character vector                                     |
|`[2]`|Event        |`'GetTipText'` or 325                                       |
|`[3]`|Item index   |Integer ( `⎕IO` dependent)                                  |
|`[4]`|SubItem index|Integer ( `⎕IO` dependent, currently always equal to `⎕IO` )|
|`[5]`|TipText      |The text to be displayed.                                   |

Modifying and returning the 5<sup>th</sup> element of the argument to the callback function allows the application to change the displayed tip.

The text can be set to a character array of rank 2 or less.

The default processing for the event is to display the default tip (if there is one).

The associated callback is run **immediately** while the windows notification is still on the stack. See [High-Priority Callback Functions](../../../interface-guide/introduction/high-priority-callbacks).

**Application**

Objects: [ListView](../objects/listview.md), [TreeView](../objects/treeview.md)
