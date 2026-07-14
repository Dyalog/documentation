# <span>ScrollOpposite</span> <span>Property</span>

**Applies To:** [TabControl](../objects/tabcontrol.md)

**Description**

The ScrollOpposite property specifies that unneeded tabs scroll to the opposite side of a [TabControl](../objects/tabcontrol.md), when a tab is selected.

ScrollOpposite is a single number with the value 0 (normal scrolling) or 1 (scrolling to the opposite side); the default is 0.

The picture below illustrates a [TabControl](../objects/tabcontrol.md) with ScrollOpposite set to 1, after the user has clicked *Third Tab*.

![](../img/tab10.gif)

Setting ScrollOpposite to 1 implies that [MultiLine](multiline.md) is also 1. If you set ScrollOpposite to 1 in a `⎕WC` statement, the [MultiLine](multiline.md) property will automatically be set to 1, even if you try to set [MultiLine](multiline.md) to 0 in the same statement. If you subsequently change [MultiLine](multiline.md) back to 0 using `⎕WS`, this will work, but the effect is not useful and it is not supported.
