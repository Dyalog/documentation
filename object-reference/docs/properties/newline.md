# <span>NewLine</span> <span>Property</span>



**Applies To:** [CoolBand](../objects/coolband.md)

**Description**


The NewLine property specifies whether or not a [CoolBand](../objects/coolband.md) occupies the same row as an existing [CoolBand](../objects/coolband.md), or is displayed on a new line within its [CoolBar](../objects/coolbar.md) parent.


NewLine is a single number with the value 0 (same row) or 1 (new row); the default is 1.


The value of NewLine in the first [CoolBand](../objects/coolband.md) in a [CoolBar](../objects/coolbar.md) is always 1, even if you specify it to be 0.


When the user drags a [CoolBand](../objects/coolband.md) to another row, the value of its NewLine property, and that of any other [CoolBand](../objects/coolband.md) affected by the move, will change.


You may move a [CoolBand](../objects/coolband.md) to the previous or next row by changing its NewLine property (using `⎕WS` )from 1 to 0, or from 0 to 1 respectively.



