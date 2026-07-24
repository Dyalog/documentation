# <span>SplitObj1</span> <span>Property</span>

**Description**

The SplitObj1 property specifies the name of, or ref to, one of up to two objects managed by a [Splitter](../objects/splitter.md) object. The object must be one of the following types:

|----------|--------|--------|---------|-----------|--------|
|Button    |Calendar|Combo   |Edit     |Grid       |Group   |
|Label     |List    |ListView|MDIClient|ProgressBar|RichEdit|
|Scroll    |Spinner |Static  |StatusBar|SubForm    |TabBar  |
|TabControl|ToolBar |TrackBar|TreeView |UpDown     |&nbsp;  |

If the [Style](style.md) property of the [Splitter](../objects/splitter.md) is `'Vert'`, the object specified by SplitObj1 is positioned at (0 0) and sized to occupy the space in its parent to the left of the [Splitter](../objects/splitter.md), with the [Splitter](../objects/splitter.md) itself attached to its right edge.

If the [Style](style.md) property of the [Splitter](../objects/splitter.md) is `'Horz'`, the object specified by SplitObj1 is positioned at (0 0) and sized to occupy the space in its parent above the [Splitter](../objects/splitter.md), with the [Splitter](../objects/splitter.md) itself attached to its bottom edge.

If SplitObj1 is empty, the [Splitter](../objects/splitter.md) manages the single object specified by [SplitObj2](splitobj2.md) and the space to the left or above the [Splitter](../objects/splitter.md) is empty or controlled by another [Splitter](../objects/splitter.md).

**Application**

Objects: [Splitter](../objects/splitter.md)
