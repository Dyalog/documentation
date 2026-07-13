# <span>SplitObj2</span> <span>Property</span>



**Applies To:** [Splitter](../objects/splitter.md)

**Description**


The SplitObj2 property specifies the name of, or ref to, one of up to two objects managed by a [Splitter](../objects/splitter.md) object. The object must be one of the following types:


|----------|--------|--------|---------|-----------|--------|
|Button    |Calendar|Combo   |Edit     |Grid       |Group   |
|Label     |List    |ListView|MDIClient|ProgressBar|RichEdit|
|Scroll    |Spinner |Static  |StatusBar|SubForm    |TabBar  |
|TabControl|ToolBar |TrackBar|TreeView |UpDown     |&nbsp;  |


If the [Style](style.md) property of the [Splitter](../objects/splitter.md) is `'Vert'`, the object specified by SplitObj2 is initially positioned at (0 x), where x is half the width of the parent plus the Size of the [Splitter](../objects/splitter.md), and sized to occupy the space in its parent to the right of the [Splitter](../objects/splitter.md), with the [Splitter](../objects/splitter.md) itself attached to its left edge.


If the [Style](style.md) property of the [Splitter](../objects/splitter.md) is `'Horz'`, the object specified by SplitObj2 is initially positioned at (y 0), where y is half the height of the parent plus the Size of the [Splitter](../objects/splitter.md), and sized to occupy the space in its parent below the [Splitter](../objects/splitter.md), with the [Splitter](../objects/splitter.md) itself attached to its top edge.


If SplitObj2 is empty, the [Splitter](../objects/splitter.md) manages the single object specified by [SplitObj1](splitobj1.md) and the space to the right or below the [Splitter](../objects/splitter.md) is empty or controlled by a second [Splitter](../objects/splitter.md).



