# <span>AnimStopped</span> <span>Event 295</span>

**Applies To:** [Animation](../objects/animation.md)

**Description**

If enabled, this event is reported by an [Animation](../objects/animation.md) object just after an AVI clip has stopped playing

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'AnimStopped'` or 295 |

This event is reported for information only and cannot be disabled or modified in any way.
