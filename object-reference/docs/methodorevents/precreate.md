# <span>PreCreate</span> <span>Event 534</span>



**Applies To:** [ActiveXControl](../objects/activexcontrol.md)

**Description**


If enabled, this event is reported when an instance of an [ActiveXControl](../objects/activexcontrol.md) is created. The PreCreate event is generated at the point the *instance* is made.


An ActiveXControl also generates a [Create](./create.md) event, which occurs *after* the PreCreate event at the point when the host application requires the instance to appear visually.


Note that at the time that PreCreate is generated, the [ActiveXControl](../objects/activexcontrol.md) does not have a window.


This event is reported for information alone. You may not disable or nullify the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'PreCreate'` or 534   |



