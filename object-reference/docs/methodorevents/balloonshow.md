# <span>BalloonShow</span> <span>Event 861</span>

**Applies To:** [SysTrayItem](../objects/systrayitem.md)

**Description**

If enabled, this event is reported by an [SysTrayItem](../objects/systrayitem.md) object when a BalloonTip is displayed using the [ShowBalloonTip](showballoontip.md) method.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'BalloonShow'` or 861 |

This event is reported for information only and cannot be disabled or modified in any way
