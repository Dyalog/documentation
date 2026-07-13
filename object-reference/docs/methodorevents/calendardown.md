# <span>CalendarDown</span> <span>Event 271</span>



**Applies To:** [Calendar](../objects/calendar.md)

**Description**


If enabled, this event is reported when the user depresses the left mouse
button over a [Calendar](../objects/calendar.md) object.


This event is reported for information alone. You may not disable or nullify
the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.


The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 5-element
vector as follows :


|-----|------------|--------------------------------------------------|
|`[1]`|Object      |ref or character vector                           |
|`[2]`|Event       |`'CalendarDown'` or 271                           |
|`[3]`|Item Number |integer (see below)                               |
|`[4]`|Mouse Button|integer                                           |
|`[5]`|Shift State |integer. Sum of 1=shift key, 2=ctrl key, 4=Alt key|
|`[6]`|Element Type|integer (see below)                               |



The 6<sup>th</sup> element of the event message is one of the following values:


If the value of the 6<sup>th</sup> element of the event message is 2
(CALENDARDATE), the 3<sup>rd</sup> element is the corresponding date reported as
an [IDN](../miscellaneous/international-day-number.md).


If the value of the 6<sup>th</sup> element of the event message is 5
(CALENDARDAY), the 3<sup>rd</sup> element is the index of the corresponding
weekday (0-6).


If the value of the 6<sup>th</sup> element of the event message is 6
(CALENDARWEEKNUM), the 3<sup>rd</sup> element is the date of the first
(leftmost) day in the corresponding week, reported as an [IDN](../miscellaneous/international-day-number.md).


Otherwise, the 3<sup>rd</sup> element of the event message is 0.


