# <span>Spin</span> <span>Event 420</span>



**Applies To:** [Spinner](../objects/spinner.md), [UpDown](../objects/updown.md)

**Description**


If enabled, this event is generated when the user clicks one of the spin buttons in a [Spinner](../objects/spinner.md) object. The event is reported *before* the value of the Thumb property has been updated. You may disable the operation of the spin buttons by disabling this event. You may selectively prevent the user selecting a particular value by returning 0 from a callback function. You may also return a modified event message as a result in order to set the Thumb property to a different value.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|-----------|------------------------------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                                               |
|`[2]`|Event      |`'Spin'` or 420                                                                                       |
|`[3]`|Thumb value|Integer. The new value of the Thumb property resulting from the user pressing one of the spin buttons.|
|`[4]`|Adjustment |Integer. The amount by which the new value of the Thumb differs from its previous value.              |



