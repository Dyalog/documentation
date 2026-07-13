# <span>Spinner</span> <span>Object</span>



[Parents](../parentlists/spinner.md), [Children](../childlists/spinner.md), [Properties](../proplists/spinner.md), [Methods](../methodlists/spinner.md), [Events](../eventlists/spinner.md)



**Purpose:** The Spinner object allows the user to enter a value, using an [UpDown](updown.md) object to adjust it as required.

**Description**


The Spinner object is a special Dyalog APL composite object that consists of an edit field and a pair of spin buttons. The user may enter a value by typing in the edit field and may adjust the value with the spin buttons. The Spinner may cycle through a pre-defined set of values specified by the [Items](../properties/items.md) property or through a range of values specified by the [Limits](../properties/limits.md) property. The [FieldType](../properties/fieldtype.md) property supports all of the standard data types, that is, Char, Numeric, LongNumeric, Currency, Date, LongDate, and Time.



The [Limits](../properties/limits.md) property is a 2-element numeric vector that specifies the minimum and maximum value of the object. The [Step](../properties/step.md) property specifies the amount by which the value is incremented or decremented by the spin buttons. The current value in the object is defined by the [Thumb](../properties/thumb.md) and [Value](../properties/value.md) properties, which are usually identical. If [ReadOnly](../properties/readonly.md) is 0, the user may type a value into the edit field which will be validated and converted according to the [FieldType](../properties/fieldtype.md). In this case, the [Value](../properties/value.md) and the [Thumb](../properties/thumb.md) properties may be different.


An *alternative* way to use the Spinner object is to specify the [Items](../properties/items.md) property. This defines a discrete set of values through which the user may cycle, and the object behaves rather like a [Combo](combo.md) without a drop-down list. In this case, the [Limits](../properties/limits.md) property is automatically set to `(1,⊃⍴Items),` [Thumb](../properties/thumb.md) refers to the *index* into the list of [Items](../properties/items.md), and [Step](../properties/step.md) specifies the amount by which this index is updated by the spin buttons. For example, if you set [Step](../properties/step.md) to 3, the spin buttons would display every third item. The [Items](../properties/items.md) property may be a character matrix, a vector of character vectors, or a numeric vector and will be formatted according to the [FieldType](../properties/fieldtype.md). For example, if you wanted the user to select one of a set of specific dates, you would set the [FieldType](../properties/fieldtype.md) to Date or LongDate and the [Items](../properties/items.md) property to the day numbers (since 1 January 1900) corresponding to the dates you require. The [ReadOnly](../properties/readonly.md) property specifies whether or not the user may enter data into the edit field. A value typed in by the user will be converted and formatted according to the [FieldType](../properties/fieldtype.md) but need not correspond to a value in Items.


In operation, the value in the Spinner is adjusted by the [Step](../properties/step.md) each time one of the spin buttons is clicked. If the user holds a spin button down, the value is adjusted at the rate defined for the keyboard repeat rate. Furthermore, the size of each adjustment is increased according to the length of time the button stays depressed. After 1 second, the amount is increased to `(2 × Step)`. after 2 seconds, to `(4 × Step)`, after 3 seconds to `(8 × Step)` and so forth until the  amount of adjustment exceeds one quarter of the range `(Limits[2]⍎Limits[1])`.


When the value in the spinner reaches its top or bottom limit, it will wrap around to the opposite limit if the value of the [Wrap](../properties/wrap.md) property is 1 (the default). Otherwise it will stick.


The [MaxLength](../properties/maxlength.md) property defines the maximum number of characters that the user may type into the edit field. The [Decimals](../properties/decimals.md) property specifies the number of decimal places to which a numeric value is displayed and applies only if the [FieldType](../properties/fieldtype.md) is Numeric or LongNumeric.


The Spinner generates two special events, [Spin](../methodorevents/spin.md) and [SetSpinnerText](../methodorevents/setspinnertext.md). The [Spin](../methodorevents/spin.md) event is generated each time the value of the [Thumb](../properties/thumb.md) is about to be updated and reports the new value and the difference between it and the current value. You may prevent the [Thumb](../properties/thumb.md) from being updated by returning 0 from a callback function, or you may alter the new value of the [Thumb](../properties/thumb.md) by returning a modified message. The [SetSpinnerText](../methodorevents/setspinnertext.md) event is generated after the [Thumb](../properties/thumb.md) has been reset but *before* the edit field has been updated. It reports the new value of the [Thumb](../properties/thumb.md) and the text that is about to be written into the edit field. By returning a modified event message from a callback, this event allows your application to respond *dynamically* to the spin buttons and to control the text in the edit field directly.


Like an [Edit](edit.md) object, the Spinner has a [Changed](../properties/changed.md) property and generates a Change event when loses the focus after the value of its Text and/or [Thumb](../properties/thumb.md) property has been altered.


If [FieldType](../properties/fieldtype.md) is Numeric, LongNumeric, Currency, Date, LongDate or Time, the Spinner will generate a [BadValue](../methodorevents/badvalue.md) event when it loses the focus if the text in the edit field (that is, the Text property) is in conflict with the [FieldType](../properties/fieldtype.md) property and cannot be converted to an appropriate number, or is outside the range specified by the [Limits](../properties/limits.md) property. If the edit field is empty, a [BadValue](../methodorevents/badvalue.md) event will be generated if [ValidIfEmpty](../properties/validifempty.md) is 0, but not if it is set to 1.


