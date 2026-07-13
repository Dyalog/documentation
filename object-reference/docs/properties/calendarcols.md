# <span>CalendarCols</span> <span>Property</span>



**Applies To:** [Calendar](../objects/calendar.md), [DateTimePicker](../objects/datetimepicker.md)

**Description**


The CalendarCols property specifies the colours used for various elements in the [Calendar](../objects/calendar.md) object.


CalendarCols is a 6-element integer vector whose elements specify the colours as follows:


|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Background colour displayed between months                                                                                                                                      |
|`[2]`|Background colour displayed within the month.                                                                                                                                   |
|`[3]`|Text colour within a month                                                                                                                                                      |
|`[4]`|Background colour displayed in the calendar's title                                                                                                                             |
|`[5]`|Colour used to display text within the calendar's title                                                                                                                         |
|`[6]`|Colour used to display header day and trailing day text. Header and trailing days are the days from the previous and following months that appear on the current month calendar.|


Each element of CalendarCols may be 0 (which means default colour), a negative singleton that specifies a particular Windows colour, or a 3-element integer vector of RGB values.


Note: At the time of writing, setting the first element of CalendarCols has no effect. Dyalog believes this to be a Windows problem that may be corrected in due course.



