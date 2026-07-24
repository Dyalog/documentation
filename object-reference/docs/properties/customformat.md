# <span>CustomFormat</span> <span>Property</span>

**Description**

Specifies a custom format for the date/time display in a [DateTimePicker](../objects/datetimepicker.md).

CustomFormat is a character vector that may contain a mixture of date/time format elements and body text. The date/time elements are replaced  by the actual date/time values when the object is displayed. The body text is displayed *as-is*. Note that CustomFormat may only be specified when the [DateTimePicker](../objects/datetimepicker.md) object is created.

The date/time elements are defined by the following groups of characters, notice that they are case-sensitive:

|Element|Description                                                                      |
|-------|---------------------------------------------------------------------------------|
|d      |The one- or two-digit day.                                                       |
|dd     |The two-digit day. Single-digit day values are preceded by a zero.               |
|ddd    |The three-character weekday abbreviation.                                        |
|dddd   |The full weekday name.                                                           |
|h      |The one- or two-digit hour in 12-hour format.                                    |
|hh     |The two-digit hour in 12-hour format. Single-digit values are preceded by a zero.|
|H      |The one- or two-digit hour in 24-hour format.                                    |
|HH     |The two-digit hour in 24-hour format. Single-digit values are preceded by a zero.|
|m      |The one- or two-digit minute.                                                    |
|mm     |The two-digit minute. Single-digit values are preceded by a zero.                |
|M      |The one- or two-digit month number.                                              |
|MM     |The two-digit month number. Single-digit values are preceded by a zero.          |
|MMM    |The three-character month abbreviation.                                          |
|MMMM   |The full month name.                                                             |
|t      |The one-letter AM/PM abbreviation (that is, AM is displayed as "A").             |
|tt     |The two-letter AM/PM abbreviation (that is, AM is displayed as "AM").            |
|yy     |The last two digits of the year (that is, 1996 would be displayed as "96").      |
|yyyy   |The full year (that is, 1996 would be displayed as "1996").                      |

The body text is defined by sub-strings contained within single quotes. For example, to display the current date with the format "Today is: 04:22:31 Tuesday Mar 23, 1996", the format string is defined as follows:
```apl
      CustomFormat
'Today is: 'hh':'m':'s dddd MMM dd', 'yyyy
```

To include a single quote in your body text, use two consecutive single quotes. For example, to produce output that looks like: "Don't forget Mar 23, 1996", CustomFormat should be specified as follows:
```apl
        CustomFormat
'Don''t forget' MMM dd',' yyyy
```

!!! note
    Non-format characters that are not delimited by single quotes will result in unpredictable display by the [DateTimePicker](../objects/datetimepicker.md) object.

**Application**

Objects: [DateTimePicker](../objects/datetimepicker.md)
