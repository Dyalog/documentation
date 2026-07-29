# <span>Undo</span> <span>Method 170</span>

**Description**

This method is used to undo the previous change in a [Grid](../objects/grid.md) object.

The [Grid](../objects/grid.md) object maintains a buffer of the most recent 8 changes made by the user since the [Values](../properties/values.md) property was last set by [`⎕WC`](../../../language-reference-guide/system-functions/wc) or [`⎕WS`](../../../language-reference-guide/system-functions/ws).

Your application can restore these changes one by one by calling the Undo method on the [Grid](../objects/grid.md). The Undo method restores the most recent change made by the user and removes that change from the undo stack.

It is therefore not possible to "undo an undo".

The argument to Undo is `⍬`, or a single item as follows :

|-----|-----------------|-------|
|`[1]`|Number of changes|integer|

If called with an argument of `⍬`, the default value for the *Number of changes* is 1. This restores the most recent change.

**Application**

Objects: [Grid](../objects/grid.md)
