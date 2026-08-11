# <span>Wrap</span> <span>Property</span>

The Wrap property is Boolean and has a default value of 1.

For a [ListView](../objects/listview.md) it specifies whether or not long labels (specified by the Items property) may be wrapped or not.

For a [ProgressBar](../objects/progressbar.md) object it determines whether or not the object starts over again when it reaches its upper limit. In particular, if Wrap is 1, the value obtained when you set the Thumb property is given by the expression: `LIMITS[1]+THUMB|LIMITS[2]` where `THUMB` is the value to which you set the Thumb property and `LIMITS` is the value of the Limits property.

For a [Spinner](../objects/spinner.md) or an [UpDown](../objects/updown.md), Wrap determines what happens when the value reaches its upper or lower limit. If Wrap is 1, the value wraps around to its opposite limit; otherwise it sticks.

## Application

Objects: [ListView](../objects/listview.md), [ProgressBar](../objects/progressbar.md), [Spinner](../objects/spinner.md), [UpDown](../objects/updown.md)
