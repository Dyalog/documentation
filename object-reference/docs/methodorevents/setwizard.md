# <span>SetWizard</span> <span>Event 365</span>



**Applies To:** [PropertySheet](../objects/propertysheet.md)

**Description**


If enabled, this event is reported when the user has clicked the Next or Back button in a [PropertySheet](../objects/propertysheet.md) with Style `'Wizard'`. This action also generates PageNext (or PageBack) and PageDeactivate and PageActivate events. The SetWizard event is the final event to be reported as a result of this action, and is the only one that is affected by the result of a callback function. The event message reports the active/inactive state of the 3 page changing buttons (Back, Next and Finish) that should result from the action. Note that the Next and Finish buttons occupy the same position and are mutually exclusive.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :


|-----|-------------------|-----------------------|
|`[1]`|Object             |ref or character vector|
|`[2]`|Event              |`'SetWizard'` or 365   |
|`[3]`|Active state Back  |0 or 1                 |
|`[4]`|Active state Next  |0 or 1                 |
|`[5]`|Active state Finish|0 or 1                 |
|`[6]`|Finish caption     |character vector       |


You may alter the state of the buttons by changing elements [3-5] of the event message and returning it as a result of your callback. You may also set the state of the buttons at any time by calling SetWizard as a method.


When the event is reported by `⎕DQ`, element 6 is an empty vector. If you modify it and return it in the result of a callback, the caption of the Finish button changes accordingly and the Back and Next buttons disappear. This happens regardless of the states you specified in elements [3-5].



