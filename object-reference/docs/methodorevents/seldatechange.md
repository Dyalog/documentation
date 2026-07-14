# <span>SelDateChange</span> <span>Event 265</span>

**Applies To:** [Calendar](../objects/calendar.md)

**Description**

If enabled, this event is reported when the user changes the date, or range of dates, that is selected in a [Calendar](../objects/calendar.md) object. This event is also reported when the [Calendar](../objects/calendar.md) object is scrolled and the selection changes automatically to another month.

This event is reported for information alone. You may not disable or nullify the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :

|-----|----------|------------------------|
|`[1]`|Object    |ref or character vector |
|`[2]`|Event     |`'SelDateChange'` or 265|
|`[3]`|First Date|an integer (IDN)        |
|`[4]`|Last Date |an integer (IDN)        |
