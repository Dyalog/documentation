# <span>Splitter</span> <span>Object</span>

[Parents](../parentlists/splitter.md), [Children](../childlists/splitter.md), [Properties](../proplists/splitter.md), [Methods](../methodlists/splitter.md), [Events](../eventlists/splitter.md)

**Purpose:** The Splitter object divides a container into resizable panes.

**Description**

The Splitter divides the client area of a [Form](form.md) or [SubForm](subform.md) into resizable panes. Each pane created this way may be empty or be occupied by a single object. If the object in a pane is itself a container object, such as a [SubForm](subform.md), it may have a number of other controls within it.

A single Splitter may manage the geometry of 0, 1 or 2 other objects, which, together with the Splitter itself, share the same parent. The two objects are named by the [SplitObj1](../properties/splitobj1.md) and [SplitObj2](../properties/splitobj2.md) properties respectively.

A Splitter may manage objects of the following types:

|----------|--------|--------|---------|-----------|--------|
|Button    |Calendar|Combo   |Edit     |Grid       |Group   |
|Label     |List    |ListView|MDIClient|ProgressBar|RichEdit|
|Scroll    |Spinner |Static  |StatusBar|SubForm    |TabBar  |
|TabControl|ToolBar |TrackBar|TreeView |UpDown     |&nbsp;  |

If [Style](../properties/style.md) is `'Vert'` (the default), the Splitter is drawn vertically in its parent with the first object ([SplitObj1](../properties/splitobj1.md)) positioned to its left, and the second object ([SplitObj2](../properties/splitobj2.md)) to its right. [ See Splitter: Example 1.](../examples/splitter-example-1.md)

If [Style](../properties/style.md) is `'Horz'`, the Splitter is drawn horizontally in its parent with the first object ([SplitObj1](../properties/splitobj1.md)) positioned above, and the second object ([SplitObj2](../properties/splitobj2.md)) below.[ See Splitter: Example 2.](../examples/splitter-example-2.md)

The [Style](../properties/style.md) property must be set when the object is created with `⎕WC` and may not subsequently be changed using `⎕WS`.

The [Posn](../properties/posn.md) and [Size](../properties/size.md) properties are partially read-only, in that only one dimension of the value may be specified. If [Style](../properties/style.md) is `'Vert'`, you may specify the x-coordinate and the width of the Splitter, but you may not specify its y- coordinate nor its height. If [Style](../properties/style.md) is `'Horz'`, you may specify the y-coordinate and the width of the Splitter, but you may not specify its x-coordinate nor its length.

When the user positions the mouse pointer directly over the Splitter object, the cursor changes (by default) to a double-headed arrow (direction in accordance with [Style](../properties/style.md)). The user may now depress the left mouse button and drag the Splitter to a new position, resizing the objects named by [SplitObj1](../properties/splitobj1.md) and [SplitObj2](../properties/splitobj2.md) in the process.

You can select a different cursor using the CursorObj property. Note that setting the CursorObj property to 0 selects the default cursor, which is the appropriate double-headed arrow.

When the user depresses the mouse button, the Splitter generates a [StartSplit](../methodorevents/startsplit.md) event. When the user releases the mouse button, the Splitter generates an [EndSplit](../methodorevents/endsplit.md) event. If full-drag is in effect, the Splitter also reports [Splitting](../methodorevents/splitting.md) events as it is dragged. All these events report the new or current position of the Splitter object and are provided for information only.

Note that the objects named by [SplitObj1](../properties/splitobj1.md) and [SplitObj2](../properties/splitobj2.md) and any sub-objects they contain will generate Configure events when they are resized by the Splitter.

## Alignment

The [Align](../properties/align.md) property specifies how a Splitter behaves when its parent is resized and may be `'None'`, `'Left'`, `'Right'`, `'Top'` or `'Bottom'`.

If [Align](../properties/align.md) is `'None'`, the Splitter moves as its parent is resized, so that it divides its parent in the same *proportions* as before. This is the default.

Any other value of [Align](../properties/align.md) attaches the Splitter to the corresponding edge of its parent. For example, if [Align](../properties/align.md) is `'Left'`, the width of the object to the *left* of the Splitter remains fixed when its parent is resized horizontally by the user.

Like the [Style](../properties/style.md) property, [Align](../properties/align.md) may be set only when the object is created with `⎕WC` and may not subsequently be changed using `⎕WS`.

## Using Multiple Splitters

If you want to divide a Form into more than 2 resizable panes, there are two possible approaches, each with its own different characteristics.

The first approach is a hierarchical one using SubForms. This example shows how you can create a Form containing three resizable Edit objects.

First, you create an Edit, a SubForm, and a Splitter as children of the *Form*, using the Splitter to divide the Form into two panes, one for the Edit and the other for the SubForm. Next, you create two Edit objects and a Splitter as children of the *SubForm*, using the second Splitter to divide the SubForm into two. You can continue with this approach to any reasonable depth. [ See Splitter: Example 3.](../examples/splitter-example-3.md)

Notice that, by default, when the first Splitter is shifted to the left, both panes in the SubForm expand equally.

The second approach is to create multiple Splitters *at the same level*, that is, owned by the same parent. [ See Splitter: Example 4.](../examples/splitter-example-4.md)

In this case, the third Edit object `F.E3` is unaffected by movement of the leftmost Splitter `F.S1`. Note also, that the first Splitter `F.S1` may not be dragged further right than the second Splitter `F.S2`.

Using the non-hierarchical approach, horizontal and vertical Splitters may be combined in interesting ways. This can also be achieved using nested SubForms, but at the expense of a complex object hierarchy.[ See Splitter: Example 5.](../examples/splitter-example-5.md)

Notice that in this example, with the exception of the last Splitter `F.S4`, it is necessary only to specify the [SplitObj1](../properties/splitobj1.md) property for each of the Splitters. The reason is that the first four Splitters only manage one object *directly*. For example, the object to the right of `F.S1` is in fact a horizontal Splitter `F.S2`. Dragging `F.S1` changes the length of `F.S2` which in turn changes the width of `F.E2`. and `F.E3`.

## Colliding Splitters

If you have two or more vertical Splitters or two or more horizontal Splitters in the same parent object, it is possible for the user to make the Splitters *collide*. This can occur by dragging one of the Splitters into the other, or, unless both Splitters have Align set to `'None'`, by shrinking the parent.

When Splitters collide, the object being dragged by the user (a Splitter or a border of the parent) takes precedence over the setting of Align, and temporarily *pushes* other Splitters along in its direction of travel. If and when the operation is reversed, the other Splitters are *pulled* back to their original positions.
