<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DT DT
</div>

<h1 class="heading"><span class="name">Date-time</span> <span class="command">R←X ⎕DT Y</span></h1>

This function validates date-times or converts date-times between one format and another.

A date-time is a date and time of day represented by a *timestamp*, a *time number* or a *military time-zone character*.

- A *timestamp* is a date-time expressed as a multiple element numeric vector, of which there are several different sorts (principally `⎕TS` format).
- A *time number* is a date-time expressed as a scalar numeric value, of which there are several different sorts.
- A *military time zone character* is a scalar character that represents the current date-time ("now") in a particular time zone. For example, `'A'` represents the current date-time (UTC) + 1 hour.

`Y` is an array of any shape whose elements contain a timestamp, time number or military time zone character, in any combination.

`X` may be a single integer value or a 2-element integer vector.

When `X` is a single integer value, it must be either 0 or a date-time code listed in the tables below. 0 specifies that the elements of `Y` are to be validated. A non-zero value specifies the date-time representation to which the elements of `Y` are to be converted. In this case, the numeric elements of `Y` are interpreted as follows:

- scalars are assumed to be time numbers of type Dyalog Date Number (code 1)
- vectors are assumed to be `⎕TS` timestamps (code ¯1)

When `X` is a 2-element integer vector, `X[1]` is a date-time code that explicitly specifies the date-time representation of the numeric elements in `Y`. `X[2]` is either 0 or a date-time code listed in the tables below. 0 specifies that the elements of `Y` are to be validated. A non-zero value specifies the date-time representation to which the elements of `Y` are to be converted.

Character scalars in `Y` are always interpreted as meaning "now".

`R` is an array of the same shape as `Y`, where each element is either a timestamp, time number or Boolean value as determined by the second or only element in `X`.

Time numbers in `R` may be of type DECF even if `⎕FR` is 645 if their magnitude can be too great to store precisely in a double. See the table below for the type numbers where this is so.

## Time Numbers

If a value in `X` is positive it indicates that a time number type is expected in `Y` or generated in `R`, as follows. Note that the last column indicated whether (Yes) or not (No) negative numbers are allowed.

|Group|Code|Description|Category|Date and time[^1] represented by 0 (Epoch)|Negative values allowed?[^8]|
|---|---|---|---|---|---|
|Dyalog APL              |1 |Dyalog Date Number|Day count with fractional part|1899-12-31 00:00|Yes|
|_                      _|2 |Dyalog component file time|Tick count 1÷60s ticks[^2]|1970-01-01 00:00|Yes|
|Other languages         |10|J (J nanosecond time)|Tick count[^3] 1ns ticks [^2]|2000-01-01 00:00|Yes|
|                        |11|Shakti K7|Tick count 1ms ticks[^2]|2024-01-01 00:00|Yes|
|                        |12|JavaScript / D / Q / Go UnixMilli |Tick count 1ms ticks[^2]|1970-01-01 00:00|Yes|
|                        |13|R (R chron format)|Day count with fractional part|1970-01-01 00:00|Yes|
|                        |14|Shakti K9|Tick count 1ms ticks[^2]|2001-01-01 00:00|Yes|
|                        |15|Go UnixMicro|Tick count 1µs ticks[^2]|1970-01-01 00:00|Yes|
|                        |16|Go UnixNano|Tick count 1ns ticks[^2]|1970-01-01 00:00|Yes|
|_                      _|17|APL+Win and APL64 workspace timestamp|Tick count 1μs ticks[^2]|1900-01-01 00:00|No|
|UNIX                    |20|Unix time|Tick count 1s ticks[^2]|1970-01-01 00:00|Yes|
|                        |21|Apollo NCS UUID|Tick count 4µs ticks[^2]|1980-01-01 00:00|No|
|_                      _|22|OSF DCE UUID|Tick count 1ns ticks[^2]|1582-10-15 00:00|No|
|Microsoft Windows       |30|Microsoft DOS date/time|Encoded broken-down time 2s resolution|N/A|No|
|                        |31|Microsoft Win32 FILETIME|Tick count[^3] 100ns ticks|1601-01-01 00:00|No|
|                        |32|Microsoft CLR DateTime (.NET)(Ticks property thereof)|Tick count [^3] 100ns ticks|0001-01-01 00:00|No|
|_                      _|33|Microsoft OLE Automation Date(also known as Variant Time)|Day count with fractional part|1899-12-30 00:00|Yes [^10]|
|Application             |40|Excel (1900 Date System)[^4] / Lotus 1-2-3|Day count with fractional part[^5]|1899-12-31 00:00[^6]|No|
|                        |41|Excel (1904 Date System)[^4]|Day count with fractional part|1904-01-01 00:00|No|
|                        |42|Stata statistics package|Tick count 1ms ticks[^2]|1960-01-01 00:00|Yes|
|                        |43|SPSS statistics package|Tick count 1s ticks[^2]|1582-10-14 00:00|No|
|_                      _|44|SAS|Tick count 1s ticks[^2]|1960-01-01 00:00|Yes|
|Julian Date and variants|50|Julian Date|Day count with fractional part|¯4717-11-24 12:00|No|
|                        |51|J (J dayno)|Day count with fractional part|1800-01-01 00:00|No|
|                        |52|Reduced Julian Date|Day count with fractional part|1858-11-16 12:00|Yes|
|                        |53|Modified Julian Date|Day count with fractional part|1858-11-17 00:00|Yes|
|                        |54|Dublin Julian Date|Day count with fractional part|1899-12-31 12:00|Yes|
|                        |55|CNES Julian Date|Day count with fractional part|1950-01-01 00:00|Yes|
|_                      _|56|CCSDS Julian Date|Day count with fractional part|1958-01-01 00:00|Yes|
|Decimal encoded[^9]     |60|Floating-point decimal encoded format Digits take the form yyyymmdd.hhmmss|Encoded broken-down time 1s resolution|N/A|No|
|_                      _|61|Integer decimal encoded format Digits take the form yyyymmddhhmmss(J digit time)|Encoded broken-down time 1s resolution|N/A|No|
|Misc. Operating Systems |70|AmigaOS|Tick count 1ms ticks[^2]|1978-01-01 00:00|No|

## Time Stamps

If a value in `X` is negative it indicates that a timestamp type is expected in `Y` or generated in `R`, as follows:

| Group                  | Code  | Description                                  | Max elements | Element contents[^11]                                        | Elided element implicit values (in Y)[^13] |
|------------------------|-------|----------------------------------------------|--------------|--------------------------------------------------------------|--------------------------------------------|
| APL 7-element vector   | `¯1`  | Millisecond precision (`⎕TS`)                | 7            | Year, month, day-of-month, hour, minute, second, millisecond | `1 1 1 0 0 0 0`                            |
|                        | `¯2`  | Microsecond precision                        | 7            | Year, month, day-of-month, hour, minute, second, microsecond | `1 1 1 0 0 0 0`                            |
|_                      _| `¯3`  | Nanosecond precision (J expanded digit time) | 7            | Year, month, day-of-month, hour, minute, second, nanosecond  | `1 1 1 0 0 0 0`                            |
| ISO components         | `¯10` | ISO day-of-year components                   | 6            | Year, day-of-year, hour, minute, second, microsecond         | `1 1 0 0 0 0 0`                            |
|_                      _| `¯11` | ISO day-of-week components                   | 7            | Year, week, day-of-week, hour, minute, second, microsecond   | `1 1 0 0 0 0`                              |
| Decimal encoded[^2]    | `¯20` | Decimal encoded date and time                | 2            | Decimal encoded date, decimal encoded time                   | `1 0 1 0 1 0`                              |
| DateTimePicker         | `¯30` | DateTime format                              | 7            | International Day Number, hour, minute, second               | `1 1 1 0 0 0`                              |

## Military time zone characters

Any element in `Y` may be specified as a military time zone character and is implicitly replaced by the current time in the time zone they represent. The time zones are as follows:

|Character|Time zone name|Time zone |
|---------|--------------|----------|
|A        |Alpha         |UTC +1    |
|B        |Bravo         |UTC +2    |
|C        |Charlie       |UTC +3    |
|D        |Delta         |UTC +4    |
|E        |Echo          |UTC +5    |
|F        |Foxtrot       |UTC +6    |
|G        |Golf          |UTC +7    |
|H        |Hotel         |UTC +8    |
|I        |India         |UTC +9    |
|J        |Juliet        |Local time|
|K        |Kilo          |UTC +10   |
|L        |Lima          |UTC +11   |
|M        |Mike          |UTC +12   |
|N        |November      |UTC -1    |
|O        |Oscar         |UTC -2    |
|P        |Papa          |UTC -3    |
|Q        |Quebec        |UTC -4    |
|R        |Romeo         |UTC -5    |
|S        |Sierra        |UTC -6    |
|T        |Tango         |UTC -7    |
|U        |Uniform       |UTC -8    |
|V        |Victor        |UTC -9    |
|W        |Whisky        |UTC -10   |
|X        |X-ray         |UTC -11   |
|Y        |Yankee        |UTC -12   |
|Z        |Zulu          |UTC +0    |

The resolutions of system clocks vary by platform.

## Examples 

### Timestamp to time number conversion { .example }
```apl
      ¯1 1 ⎕DT ⊂⎕TS
43886.48039
      1 ⎕DT ⊂⎕TS
43886.48039
      1 ⎕DT ⎕TS 'J'
43886.48039 43886.48039

      1 ⎕DT ⊂⍬ ⍝ cf Elided element implicit values
¯693594
      1 ⎕DT ⊂1 1 1 0 0 0 0
¯693594
       ¯30 1 ⎕DT⊂(44217 15 13 54)
44217.63465

```

### Time number to timestamp conversion { .example }
```apl
      1 ¯1 ⎕DT 0 43508.42843
┌──────────────────┬──────────────────────┐
│1899 12 31 0 0 0 0│2019 2 13 10 16 56 352│
└──────────────────┴──────────────────────┘
      ¯1 ⎕DT 0 43508.42843
┌──────────────────┬──────────────────────┐
│1899 12 31 0 0 0 0│2019 2 13 10 16 56 352│
└──────────────────┴──────────────────────┘
      2 ¯1 ⎕DT 3⊃⎕FRDCI 1 1
┌──────────────────────┐
│2020 2 26 11 33 54 466│
└──────────────────────┘
      1 ¯30 ⎕DT 44217.63465
┌──────────────┐
│44217 15 13 53│
└──────────────┘
```

### Time number to time number conversion { .example }
```apl
      2 1 ⎕DT 3⊃⎕FRDCI 1 1
43886.48188
      1 ⎕DT 'J'
43886.48371
      ⍝ Local time is UTC-05:00
      3600÷⍨-/20 ⎕DT 'JZ'
¯5
```

### Timestamp to timestamp conversions { .example }
```apl
      ¯30 ⎕DT ⊂⎕TS
┌─────────────┐
│44216 16 5 46│
└─────────────┘
      
      ¯30 ¯1 ⎕DT⊂32000 15 10 0
┌───────────────────┐
│1987 8 12 15 10 0 0│
└───────────────────┘
```

### Validation { .example }
```apl
      0 ⎕DT ⎕TS (2020 13 1) 'J' 'DT' #
1 0 1 0 0

      ¯30 0 ⎕DT⊂32000 15 10 0
1
```

[^1]: In the Proleptic Gregorian Calendar.
[^2]: There are the same number of ticks per day regardless of leap seconds.
[^3]: Generated as DECF values regardless of the setting of ⎕FR due to their magnitude.
[^4]: Excel supports two time number conventions. On Windows the 1900 Date System is the default and on macOS the 1904 Date System is the default. Both systems can use either convention and the convention in use is stored in the worksheet so that the platforms interoperate.
[^5]: Count includes the invalid date 1900-02-29.
[^6]: Microsoft Excel converts day 0 to the invalid date 1900-01-00.
[^7]: For negative numbers, the integral part counts backward from 1899-12-30 and the fractional part counts forward from  the date so reached.
[^8]: No date-time may represent a date earlier than ¯4713-01-01 00:00.
[^9]: Decimal encoded formats encode human-readable dates and times into a single number with the most significant part in the most significant decimal digit, for example 2020/01/23 (year/month/day) is encoded as 20200123, and 13:17:56 (hour:minute:second) is encoded as 131756. The date must be between 1 January 0001 and 31 December 9999 in the Proleptic Gregorian Calendar.
[^10]: For negative numbers, the integral part counts backward from 1899-12-30 and the fractional part counts forward from the date so reached.
[^11]: All dates must be between 1 January 0001 and 28 February 4000 in the Proleptic Gregorian Calendar.
[^12]: Decimal encoded formats encode human-readable dates and times into a single number with the most significant part in the most significant decimal digit, for example 2020/01/23 (year/month/day) is encoded as 20200123, and 13:17:56 (hour:minute:second) is encoded as 131756.
[^13]: If a timestamp has fewer than the maximum number of elements, the remaining elements take the default values shown.
