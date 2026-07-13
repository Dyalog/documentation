# <span>DateTimePicker</span> <span>Object</span>



[Parents](../parentlists/datetimepicker.md), [Children](../childlists/datetimepicker.md), [Properties](../proplists/datetimepicker.md), [Methods](../methodlists/datetimepicker.md), [Events](../eventlists/datetimepicker.md)



**Purpose:** The DateTimePicker object is an editable date/time field with an         optional drop-down Calendar.

**Description**


The DateTimePicker object represents the built-in Windows date and time
picker control. For most purposes, the DateTimePicker supersedes the use of
Label, Edit and Spinner objects for displaying and entering dates and times.
Unlike the Edit and Spinner objects, it is not possible for the user to enter an
invalid date or time into a DateTimePicker.



The Style property may be either `'Combo'`(the default) or `'UpDown'`. The former
provides a drop-down calendar that behaves in the same way as the Calendar
object and whose appearance and behaviour is controlled by a set of properties
namely CalendarCols, CircleToday, HasToday, MaxDate, MinDate, MonthDelta, Today
and WeekNumbers that are common to the Calendar. Note that the Style property may only be set when the object is created.


If Style is `'Combo'`, the Align property
specifies the horizontal alignment of the drop-down Calendar which may be `'Left'`(the default) or `'Right'`.


If Style is `'UpDown'`, the
DateTimePicker includes instead a pair of spinner buttons that allow the user to
increment and decrement values in the various sub-fields provided by the
control.


The [DateTime](../properties/datetime.md) property represents the
date and time value that is currently displayed in the object. This is a
4-element vector containing the IDN, hour, minutes and seconds respectively.


The FieldType property specifies one of a set of pre-defined date/time
formats to be used by the control. This is a character vector that may be empty
(the default), `'Date'`, `'DateCentury'`,
`'LongDate'`, `'Time'`or `'Custom'`. Specifying an empty vector is
the same as specifying `'Date'`. Note that `'DateCentury'` always displays a 4-digit year, regardless of the user's Windows settings.


If FieldType is set to `'Custom'`, the
format is defined by the [CustomFormat](../properties/customformat.md) property. CustomFormat is a character vector that may contain a mixture of
date/time format elements and body text.


The [HasCheckBox](../properties/hascheckbox.md) property is a
Boolean value (default 0) that specifies whether or not a checkbox is displayed
in the object. This allows the user to specify whether or not the date/time
displayed in the DateTimePicker is applicable.


