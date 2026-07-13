# <span>FireOnce</span> <span>Property</span>



**Applies To:** [Timer](../objects/timer.md)

**Description**


This property specifies one-off  behaviour for a [Timer](../objects/timer.md) object. It has the value 0, 1 or 2.


Setting FireOnce to 1, will cause the [Timer](../objects/timer.md) to generate a single event and no more unless it is reset. After generating the single event, FireOnce is automatically set to 2 and this change occurs prior to the invocation of a callback function.


Setting FireOnce to 2 will cause the [Timer](../objects/timer.md) to behave as if it has already raised its single event.


FireOnce honours the value of the [Active](active.md) property but does not change it. So setting FireOnce to 1 when [Active](active.md) is 0 will not immediately cause an event. If [Active](active.md) is subsequently set to 1, the single [Timer](../methodorevents/timer.md) event will then occur.



