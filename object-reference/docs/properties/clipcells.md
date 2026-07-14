# <span>ClipCells</span> <span>Property</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This property determines whether or not the [Grid](../objects/grid.md) displays partial cells. The default is 1. If you set ClipCells to 0, the [Grid](../objects/grid.md) displays only complete cells and automatically fills the space between the last visible cell and the edge of the [Grid](../objects/grid.md) with the [GridBCol](gridbcol.md) colour.

The first picture below shows a default [Grid](../objects/grid.md) (ClipCells is 1) in which the third column of data is in fact incomplete (clipped), although this is by no means apparent to the user. The second picture shows the effect on the [Grid](../objects/grid.md) of setting ClipCells to 0 which prevents such potential confusion.

![](../img/clip1.gif)

![](../img/clip2.gif)
