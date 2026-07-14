# <span>TabObj</span> <span>Property</span>

**Applies To:** [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [TabControl](../objects/tabcontrol.md)

**Description**

TabObj is a ref or a character vector.

TabObj associates a [SubForm](../objects/subform.md) with a [TabBtn](../objects/tabbtn.md) or a [TabButton](../objects/tabbutton.md) object. Selecting the associated [TabBtn](../objects/tabbtn.md) or [TabButton](../objects/tabbutton.md) causes the [SubForm](../objects/subform.md) to be given the input focus.

For a [SubForm](../objects/subform.md), it specifies the name of, or ref to, a [TabBtn](../objects/tabbtn.md) or [TabButton](../objects/tabbutton.md) object that is to be associated with the [SubForm](../objects/subform.md). When referenced or queried using `⎕WG`, TabObj returns a name if it was specified by a name, or a ref if it was specified by a ref.

For [TabBtn](../objects/tabbtn.md) and [TabButton](../objects/tabbutton.md) objects, TabObj is a read-only property that contains a ref to the associated [SubForm](../objects/subform.md).

For a [TabBar](../objects/tabbar.md) or [TabControl](../objects/tabcontrol.md), TabObj is a read-only property that contains a ref to the currently selected [TabBtn](../objects/tabbtn.md) or [TabButton](../objects/tabbutton.md).
