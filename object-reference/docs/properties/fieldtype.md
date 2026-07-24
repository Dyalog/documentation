# <span>FieldType</span> <span>Property</span>

**Description**

The FieldType property controls data conversion, formatting and validation.

For [Edit](../objects/edit.md), [Label](../objects/label.md) and [Spinner](../objects/spinner.md) objects, FieldType controls how the [Value](value.md) property of these objects is interpreted.

FieldType is a character vector. If it is empty (the default), the [Text](../objects/text.md) or [Label](../objects/label.md) object is a standard text object with no special formatting or, in the case of an [Edit](../objects/edit.md), no input validation. For a [DateTimePicker](../objects/datetimepicker.md), an empty FieldType implies the default which is `'Date'`.

For a [DateTimePicker](../objects/datetimepicker.md), FieldType may be one of the following:

|---------------|--------------------------------------------------------------------------------------|
|`'Date'`       |Uses Windows "short date" format                                                      |
|`'DateCentury'`|Uses Windows "short date" format but with a 4-digit year regardless of user preference|
|`'LongDate'`   |Uses Windows "long date" format                                                       |
|`'Time'`       |Uses Windows time format                                                              |
|`'Custom'`     |Uses a special format defined by the CustomFormat property                            |

The value of the date or time is represented by the [DateTime](datetime.md) property. Note that all validation is performed by the object itself, and it is impossible to enter an invalid value.

For an [Edit](../objects/edit.md), [Label](../objects/label.md) and [Spinner](../objects/spinner.md), if FieldType is defined, the contents of the object are defined by its [Value](value.md) property, which is a number, rather than by its [Text](text.md) property, and special formatting and validation rules are applied. FieldType may be one of the following :

|---------------|----------------------------------------------------------------|
|`'Numeric'`    |Simple numeric formatting and validation                        |
|`'LongNumeric'`|Uses Windows number format                                      |
|`'Date'`       |Uses Windows "short date" format                                |
|`'LongDate'`   |Uses Windows "long date" format                                 |
|`'Currency'`   |Uses Windows currency format                                    |
|`'Time'`       |Uses Windows time format                                        |
|`'Char'`       |No validation, forces [Value](value.md) to be a character vector|

FieldType `'Char'` only affects an [Edit](../objects/edit.md) object. When the user enters data into a standard single-line [Edit](../objects/edit.md) object, the [Value](value.md) property is set to a number if the contents are numeric, or to a character vector if the contents do not represent a valid number. If FieldType is `'Char'`, the [Value](value.md) property is always set to a character vector, regardless of the type of the field contents.

If FieldType is `'Numeric'`, the object displays the number defined by its [Value](value.md) property rounded to the number of decimal places specified by its [Decimals](decimals.md) property. The decimal separator character used will be as specified by the Number format in the user's International Control Panel settings. If the object is an [Edit](../objects/edit.md) object, the user is prevented from entering anything but a valid number. The number of decimal digits is also restricted to [Decimals](decimals.md). When the user "leaves" the object, the number is re-formatted.

If FieldType is `'LongNumeric'`, the object displays the number specified by its [Value](value.md) property according to the Number format in the user's International Control Panel settings. This format specifies the 1000 separator, decimal separator, decimal digits and whether or not a leading zero is inserted. If the object is an [Edit](../objects/edit.md) object, the user is prevented from entering anything but a valid number. However, the character specified for the 1000 separator is ignored and may be entered anywhere in the number. When the user "leaves" the object, the number is re-formatted correctly.

If the FieldType is `'Currency'`, the object displays the number specified by its [Value](value.md) property according to the Currency format in the user's International Control Panel settings. This specifies the currency symbol and placement, the way in which a negative value is displayed, and the number of decimal places. If the object is an [Edit](../objects/edit.md) object, the user is restricted to entering a "reasonable" value. When the user leaves the object, the number is reformatted correctly.

If the FieldType is `'Date'`, the [Value](value.md) property represents the number of days since January 1st 1900 and is displayed using the "short date" format specified by the user's International Control Panel settings. If the object is an [Edit](../objects/edit.md) object, the user is restricted to entering a "reasonable" date. The object will accept any numeric triplet separated by slash(/), colon (:) or space characters but checks that the day number and month number lie in the range 1-31 and 1-12 respectively and will not allow the user to enter a digit that would invalidate this. (Note that the position within the triplet of the day, month and year are as specified by the Windows short date format). However, the user is not prevented from entering an invalid date such as 31st September.

If the FieldType is `'LongDate'`, the [Value](value.md) property represents the number of days since January 1st 1900 and is displayed using the "long date" format specified by  the user's International Control Panel settings. If the object is an [Edit](../objects/edit.md) object, its appearance and behaviour automatically switches to FieldType `'Date'` when it has the input focus and back again when it loses the focus. This allows the user to edit or input a date in a more convenient form.

If the FieldType is `'Time'`, the [Value](value.md) property represents the number of seconds since midnight and is displayed using the time format specified by the user's International Control Panel settings.

When the user attempts to move the input focus away from the object, the contents are validated. If they cannot be converted to a valid number, date, or time, the object generates a [BadValue](../methodorevents/badvalue.md) event, or, if the object is associated with a [Grid](../objects/grid.md), the [Grid](../objects/grid.md) (and not the [Edit](../objects/edit.md) object) generates a [CellError](../methodorevents/cellerror.md) event. See the descriptions of these events for further details.

Note that for [Edit](../objects/edit.md), [Label](../objects/label.md) and [Spinner](../objects/spinner.md) objects, FieldType may only be specified when you create an object using `⎕WC`.

**Application**

Objects: [ButtonEdit](../objects/buttonedit.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Label](../objects/label.md), [Spinner](../objects/spinner.md)
