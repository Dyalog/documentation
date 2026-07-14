# <span>GetDayStates</span> <span>Event 266</span>

**Applies To:** [Calendar](../objects/calendar.md)

**Description**

If enabled, this event is reported when a [Calendar](../objects/calendar.md) object requires the APL program to provide *day state* information for the range of dates it is about to display.

The [Calendar](../objects/calendar.md) object displays day numbers using either the normal or the bold font attribute. However, it does not store this information beyond the month or months currently displayed.

When the [Calendar](../objects/calendar.md) control scrolls (and potentially at other times), it generates a GetDayStates event to ask you (the APL program) to tell it which of the dates that are about to be shown, should be displayed using the bold font attribute.

If you wish any dates to be displayed using the bold font attribute, you **must** attach a callback function to this event which returns day state information in its result.

By default, all dates are displayed using the normal font attribute, so you need only do this if you want any dates highlighted in bold.

You may not disable or nullify the operation that caused GetDayStates to fire by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :

|-----|----------|--------------------------|
|`[1]`|Object    |ref or character vector   |
|`[2]`|Event     |`'GetDayStates'` or 266   |
|`[3]`|First Date|an integer (IDN)          |
|`[4]`|Last Date |an integer (IDN)          |
|`[5]`|Bold Dates|an integer vector of IDNs.|

When the callback function is invoked, the 3<sup>rd</sup> and 4<sup>th</sup> elements of the event message contain IDNs for the first and last date in the range of dates that the [Calendar](../objects/calendar.md) object is about to display. The 5<sup>th</sup> element of the event message contains those IDNs *within this range of dates* that the [Calendar](../objects/calendar.md) control already knows are to be displayed using the bold font attribute. This will typically be empty.

The result of your callback function should be the same event message with only the 5<sup>th</sup> element modified in any way. This should contain the IDNs of the dates (within the range specified by the 3<sup>rd</sup> and 4<sup>th</sup> elements) that are to be displayed using the bold font attribute.

<h2 class="example">Example</h2>

Suppose that you keep a variable `BOLD_DATES` in the [Calendar](../objects/calendar.md) object. This variable is a vector of IDN values that defines those dates that the user has somehow identified as special and that you wish to display in bold, The following callback function could be applied:
```apl
    ∇ MSG←DAYSTATES MSG;MASK;⎕IO
[1]   ⍝ Callback function for the GetDayStates event
[2]   ⍝ Object (⊃MSG) contains a variable BOLD_DATES
[3]   ⍝ that defines ALL the IDNs that are to be displayed in bold
[4]   ⍝ We need to return only those that fall within the range
[5]   ⍝ of dates that are about to be displayed by the Calendar
[6]    ⎕CS⊃MSG
[7]    ⎕IO←1
[8]    MASK←BOLD_DATES≥3⊃MSG
[9]    MASK←MASK∧BOLD_DATES≤4⊃MSG
[10]   MSG[5]←⊂MASK/BOLD_DATES
     ∇
```

You may also set the font attribute for particular days by calling GetDayStates as a method.

For example, to set the bold attribute for IDN 36048 (11 September 1998) in a [Calendar](../objects/calendar.md) object called `'F.CAL1'`, you could execute the expression:
```apl
      F.CAL1.GetDayStates 36048 36048 36048
```

To *clear* the bold attribute for the same day:
```apl
      F.CAL1.GetDayStates 36048 36048 ⍬
```

Note that the [Calendar](../objects/calendar.md) object will ignore any IDNs you specify that are outside the range of dates that it is currently displaying.
