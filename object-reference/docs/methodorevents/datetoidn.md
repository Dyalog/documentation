# <span>DateToIDN</span> <span>Method 264</span>

**Description**

This method is used to convert a date from `⎕TS` format into an [IDN](../miscellaneous/international-day-number.md) suitable for use in a [Calendar](../objects/calendar.md) object.

The argument to DateToIDN is a 3-element array as follows:

|-----|-----|-------|
|`[1]`|Year |Integer|
|`[2]`|Month|Integer|
|`[3]`|Day  |Integer|

DateToIDN will also accept a single enclosed argument containing these values. In either case, if you specify more than 3 numbers, excess elements they will be ignored.

<h2 class="example">Examples</h2>
```apl
      F.C.DateToIDN 1998 9 11
36048
      F.C.DateToIDN ⊂1998 9 11
36048
      F.C.DateToIDN ⎕TS
36048
      F.C.DateToIDN,⎕TS
36048
```

**Application**

Objects: [Calendar](../objects/calendar.md), [DateTimePicker](../objects/datetimepicker.md), [Root](../objects/root.md)
