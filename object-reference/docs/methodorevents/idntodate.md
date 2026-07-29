# <span>IDNToDate</span> <span>Method 263</span>

**Description**

This method is used to convert a date from an [IDN](../miscellaneous/international-day-number.md) into `⎕TS` format (year, month, day). The corresponding day of the week is also obtained.

The argument to IDNToDate is a single item as follows:

|-----|---|-------|
|`[1]`|IDN|Integer|

The result is a 4-element integer vector containing the year, month, day, and weekday corresponding to the IDN that was specified.

The value of the 4<sup>th</sup> element, weekday, is an integer in the range 0-6 that specifies on which day of the week the specified date falls (0=Monday).

<h2 class="example">Example</h2>

```apl
      F.C.IDNToDate 36048
1998 9 11 4
```

**Application**

Objects: [Calendar](../objects/calendar.md), [DateTimePicker](../objects/datetimepicker.md), [Root](../objects/root.md)
