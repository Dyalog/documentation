# <span>SetSpinnerText</span> <span>Event 421</span>



**Applies To:** [Spinner](../objects/spinner.md)

**Description**


If enabled, this event is generated when the user clicks one of the spin buttons in a [Spinner](../objects/spinner.md) object. The event is reported *after* the value of the Thumb property has been updated but *before* the Text property has been changed. You may use this event to set the text in the [Spinner](../objects/spinner.md) dynamically instead of relying on it being updated automatically.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|-----------|------------------------------------------------------------------------------------------------------|
|`[1]`|Object     |ref or character vector                                                                               |
|`[2]`|Event      |`'SetSpinnerText'` or 421                                                                             |
|`[3]`|Thumb value|Integer. The new value of the Thumb property resulting from the user pressing one of the spin buttons.|
|`[4]`|Text       |The text that is about to be put into the edit field.                                                 |


The SetSpinnerText event is designed to allow you to dynamically set the text in the Spinner in response to a spin button. It might be used in circumstances where the set of items you wish to present to your user is not predictable in advance.



