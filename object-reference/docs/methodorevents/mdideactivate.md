# <span>MDIDeactivate</span> <span>Event 43</span>



**Applies To:** [SubForm](../objects/subform.md)

**Description**


This event is generated when the user activates a different [SubForm](../objects/subform.md) that is the child of an [MDIClient](../objects/mdiclient.md), thereby de-activating the current one which causes this event. This occurs when the user clicks the left mouse button in another [SubForm](../objects/subform.md) or selects it from the menu nominated for this purpose (see [MDIMenu](../properties/mdimenu.md) property). You may also call MDIDeactivate as a method.


Note that this event is reported after the action has taken place and cannot be disabled by returning 0 from a callback function or by setting its action code to `¯1`.


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :


|-----|-----------|-----------------------|
|`[1]`|Object     |ref or character vector|
|`[2]`|Event      |`'MDIDeactivate'` or 43|
|`[3]`|Object name|character vector       |


Note that the 3rd element of the event message contains the name of the [SubForm](../objects/subform.md) that has now been made the active one in the same [MDIClient](../objects/mdiclient.md).



