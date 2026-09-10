---
search:
  boost: 2
---

# <span>Datetime</span> `R←X ⎕DT Y`{{key}}

This function validates datetimes and converts datetimes between one representation and another, including textual representations.

## Syntax

`Y` is an array of datetimes to be validated or converted. `X` specifies the representation to convert them to (or flags them for validation) and, optionally, the representation in which they are supplied.

<h3 class="example">Examples</h3>

Converting a `⎕TS`-style timestamp to a Dyalog Date Number, then back to a timestamp:

```apl
      1 ⎕DT ⊂2019 2 13 10 16 56
43508.42843
      ¯1 ⎕DT 43508.42843
┌──────────────────────┐
│2019 2 13 10 16 56 352│
└──────────────────────┘
```

Converting the current "Zulu time" ([UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)) to ISO format, then checking if two ISO format dates are valid:

```apl
      '%ISO%' ⎕DT 'Z'
┌───────────────────┐
│2026-08-12T03:23:46│
└───────────────────┘
      '%ISO%' 0 ⎕DT '2026-08-12T03:23:46' '2026-02-29T03:23:46'
1 0
```

## Datetimes

A *datetime* is a date and time in one of the representations listed in [](#representations):

Table: Datetime representations { #representations }

| Representation | Data type | Example |
| --- | --- | --- |
| [*Time number*](#time-numbers) | scalar number | `46245.1415` |
| [*Timestamp*](#timestamps) | numeric vector | `2026 8 12 3 23 46 0` |
| [*Military time zone character*](#military-time-zone-characters) | scalar character | `'Z'` |
| [*Text-formatted datetime*](#text-formatted-datetimes) | character vector | `'2026-08-12T03:23:46'` |

There are multiple sorts of each of these.

## Right Argument

`Y` is an array of any shape whose elements are [datetimes](#datetimes), in any combination of representations.

<h3 class="example">Example</h3>

Validating datetimes in various formats (two [time numbers](#time-numbers), two [timestamps](#timestamps), and two [military time zone characters](#military-time-zone-characters)):

```apl
      0 ⎕DT 46245 ¯1E7 (2026 8 12) (2026 2 29) 'B' 'b'
1 0 1 0 1 0
```

A single timestamp or text-formatted datetime in `Y` must be enclosed (nested); an unenclosed (simple) vector in `Y` is interpreted as a vector of time numbers or military time zone characters. No scalar extension occurs when character scalars appear in `X` or `Y`.

<h3 class="example">Examples</h3>

Validating a single (invalid) timestamp and a single (valid) text-formatted datetime:

```apl
      0 ⎕DT ⊂2026 2 29
0
      'Mmm D, YYYY' 0 ⎕DT ⊂'Aug 12, 2026'
1
```

## Left Argument

`X` describes the representation to which the elements of `Y` are to be converted and, optionally, the representation according to which the elements of `Y` are to be interpreted.

`X` can be a single element (<code>X<sub>R</sub></code>) or a 2-element vector (<code>X<sub>Y</sub> X<sub>R</sub></code>). Each of <code>X<sub>Y</sub></code> (the [input format](#input-formats)) and <code>X<sub>R</sub></code> (the [output format](#output-formats)) can be:

- a positive integer time number code from [](#timenumbersorts)
- a negative integer timestamp code from [](#timestampsorts)
- a character vector [*formatting pattern*](#formatting-patterns)

In addition, <code>X<sub>R</sub></code> can be `0` to [validate](#validating-datetimes) the datetimes in `Y`.

<h3 class="example">Examples</h3>

Find the current [Unix time](https://en.wikipedia.org/wiki/Unix_time), then convert it to a `⎕TS`-style timestamp:

```apl
      20 ⎕DT 'Z'
1786521710
      20 ¯1 ⎕DT 1786521710
┌──────────────────┐
│2026 8 12 8 1 50 0│
└──────────────────┘
```

As a convenience, a simple (not nested) character vector `X` is implicitly enclosed and processed as <code>X<sub>R</sub></code>.

<h3 class="example">Example</h3>

```apl
      'YYYY-MM-DD hh:mm:ss' ⎕DT 'Z'
┌───────────────────┐
│2026-08-12 07:59:39│
└───────────────────┘
```

### Input Formats

<code>X<sub>Y</sub></code> must be either an integer or a character vector.

Table: Input formats { #inputformats }

| <code>X<sub>Y</sub></code> | `Y` |
| --- | --- |
| positive integer code from [](#timenumbersorts) | time numbers interpreted accordingly |
| negative integer code from [](#timestampsorts) | timestamps interpreted accordingly |
| [formatting pattern](#formatting-patterns) | text-formatted datetime [matched](#pattern-matching-rules) accordingly |

<code>X<sub>Y</sub></code> can be omitted when the elements of `Y` are Dyalog Date Numbers, `⎕TS`-style timestamps, or military time zone characters. A formatting pattern <code>X<sub>Y</sub></code> cannot be omitted, even when the elements of `Y` are character vectors that could unambiguously be assumed to be text-formatted datetimes. When <code>X<sub>Y</sub></code> is omitted, the elements of `Y` are interpreted according to [](#inputinterpretation):

Table: Input element interpretation { #inputinterpretation }

| Element of `Y` | Interpretation |
| --- | --- |
| scalar number | Dyalog Date Number (code `1` from [](#timenumbersorts)) |
| numeric vector | `⎕TS`-style timestamp (code `¯1` from [](#timestampsorts)) |
| scalar character | military time zone character |

### Output Formats

<code>X<sub>R</sub></code> must be either an integer or a character vector.

Table: Output formats { #outputformats }

| <code>X<sub>R</sub></code> | `R` |
| --- | --- |
| `0` | `1` for valid datetimes, `0` for invalid datetimes |
| positive integer code from [](#timenumbersorts) | datetimes converted to specified time number |
| negative integer code from [](#timestampsorts) | datetimes converted to specified timestamps |
| [formatting pattern](#formatting-patterns) | datetimes formatted as text accordingly |

<h3 class="example">Examples</h3>

```apl
      0 ⎕DT (2026 02 28) (2026 02 29)
1 0
      1 ⎕DT 'Z'
46245.34112
      ¯1 ⎕DT 'Z'
┌─────────────────────┐
│2026 8 12 8 11 14 590│
└─────────────────────┘
      'D Mmm "''"YY'⎕DT'Z'
┌──────────┐
│12 Aug '26│
└──────────┘
```

## Result

`R` is an array of the same shape as `Y`, where each element is a [time number](#time-numbers), [timestamp](#timestamps), [text-formatted datetime](#text-formatted-datetimes), or Boolean validity value, as determined by the [output format](#output-formats).

Time numbers in `R` can be [128-bit decimal floating point values](../../programming-reference-guide/introduction/128-bit-decimal-floating-point.md) even when [`⎕FR`](fr.md) is `645` if their magnitudes could be too great to store precisely as 64-bit binary floating point values. See [](#timenumbersorts) for the time numbers where this is so.

!!! Warning "Warning"
    Performing arithmetic on such time numbers while `⎕FR` is `645` can lose precision or signal `DOMAIN ERROR`. To handle them accurately, set `⎕FR` to `1287` (128-bit decimal) first.

## Time Numbers

A *time number* is a [datetime](#datetimes) expressed as a scalar number.

A positive number in `X` indicates that time numbers are expected in `Y` or generated in `R`.

The supported time number sorts are identified by a code, listed in [](#timenumbersorts):

Table: Time numbers { #timenumbersorts }

|Code|Description|Category|Epoch[^1]|<0?[^2]|
|---|---|---|---|---|
|Dyalog APL|||||
| `1` |Dyalog Date Number|Day count with fractional part|1899-12-31 00:00|Yes|
| `2` |Dyalog component file time|Tick count 1÷60&nbsp;s ticks[^3]|1970-01-01 00:00|Yes|
|Other languages|||||
| `10` |J (J nanosecond time)|Tick count[^4] 1&nbsp;ns ticks[^3]|2000-01-01 00:00|Yes|
| `11` |Shakti K7|Tick count 1&nbsp;ms ticks[^3]|2024-01-01 00:00|Yes|
| `12` |JavaScript / D / Q / Go UnixMilli |Tick count 1&nbsp;ms ticks[^3]|1970-01-01 00:00|Yes|
| `13` |R (R chron format)|Day count with fractional part|1970-01-01 00:00|Yes|
| `14` |Shakti K9|Tick count 1&nbsp;ms ticks[^3]|2001-01-01 00:00|Yes|
| `15` |Go UnixMicro|Tick count 1&nbsp;µs ticks[^3]|1970-01-01 00:00|Yes|
| `16` |Go UnixNano|Tick count 1&nbsp;ns ticks[^3]|1970-01-01 00:00|Yes|
| `17` |APL+Win and APL64 workspace timestamp|Tick count 1μs ticks[^3]|1900-01-01 00:00|No|
|UNIX|||||
| `20` |Unix time|Tick count 1&nbsp;s ticks[^3]|1970-01-01 00:00|Yes|
| `21` |Apollo NCS UUID|Tick count 4µs ticks[^3]|1980-01-01 00:00|No|
| `22` |OSF DCE UUID|Tick count 1&nbsp;ns ticks[^3]|1582-10-15 00:00|No|
|Microsoft Windows|||||
| `30` |Microsoft DOS date/time|Encoded broken-down time 2&nbsp;s resolution|N/A|No|
| `31` |Microsoft Win32 FILETIME|Tick count[^4] 100&nbsp;ns ticks|1601-01-01 00:00|No|
| `32` |Microsoft CLR DateTime (.NET) (ticks property thereof)|Tick count [^4] 100&nbsp;ns ticks|0001-01-01 00:00|No|
| `33` |Microsoft OLE Automation Date (also known as Variant Time)|Day count with fractional part|1899-12-30 00:00|Yes [^5]|
|Application|||||
| `40` |Excel (1900 Date System)[^6] / Lotus 1-2-3|Day count with fractional part[^7]|1899-12-31 00:00[^8]|No|
| `41` |Excel (1904 Date System)[^6]|Day count with fractional part|1904-01-01 00:00|No|
| `42` |Stata statistics package|Tick count 1&nbsp;ms ticks[^3]|1960-01-01 00:00|Yes|
| `43` |SPSS statistics package|Tick count 1&nbsp;s ticks[^3]|1582-10-14 00:00|No|
| `44` |SAS|Tick count 1&nbsp;s ticks[^3]|1960-01-01 00:00|Yes|
|Julian Date and variants|||||
| `50` |Julian Date|Day count with fractional part|¯4714-11-24 12:00|No|
| `51` |J (J dayno)|Day count with fractional part|1800-01-01 00:00|No|
| `52` |Reduced Julian Date|Day count with fractional part|1858-11-16 12:00|Yes|
| `53` |Modified Julian Date|Day count with fractional part|1858-11-17 00:00|Yes|
| `54` |Dublin Julian Date|Day count with fractional part|1899-12-31 12:00|Yes|
| `55` |CNES Julian Date|Day count with fractional part|1950-01-01 00:00|Yes|
| `56` |CCSDS Julian Date|Day count with fractional part|1958-01-01 00:00|Yes|
|Decimal encoded[^9]|||||
| `60` |Floating-point decimal encoded format of the form `yyyymmdd.hhmmss`|Encoded broken-down time 1&nbsp;s resolution|N/A|No|
| `61` |Integer decimal encoded format of the form `yyyymmddhhmmss` (J digit time)|Encoded broken-down time 1&nbsp;s resolution|N/A|No|
|Misc. Operating Systems|||||
| `70` |AmigaOS|Tick count 1&nbsp;ms ticks[^3]|1978-01-01 00:00|No|

<h4 class="example">Example</h4>

Converting Dyalog Date Numbers to Unix times:

```apl
      20 ⎕DT 0 45000
¯2209075200 1678924800
```

Converting a Dyalog component file time to the form `yyyymmdd.hhmmss`:

```apl
      tn←'test' ⎕FCREATE 0
      cn←'hi' ⎕FAPPEND tn
      ⎕PP←16
      2 60 ⎕DT 3⊃⎕FRDCI tn cn
20260812.083544
```

## Timestamps

A *timestamp* is a [datetime](#datetimes) expressed as a numeric vector.

A negative number in `X` indicates that timestamps are expected in `Y` or generated in `R`.

The supported timestamp sorts are identified by a code, listed in [](#timestampsorts):

Table: Timestamps { #timestampsorts }

| Code  | Description                                  | Max elements | Element contents[^10]                                        | Elided elements[^11] |
|-------|----------------------------------------------|--------------|--------------------------------------------------------------|--------------------------------------------|
| APL 7-element vector ||||
| `¯1`  | Millisecond precision (`⎕TS`)                | 7            | Year, month, day-of-month, hour, minute, second, millisecond | `1 1 1 0 0 0 0`                            |
| `¯2`  | Microsecond precision                        | 7            | Year, month, day-of-month, hour, minute, second, microsecond | `1 1 1 0 0 0 0`                            |
| `¯3`  | Nanosecond precision (J expanded digit time) | 7            | Year, month, day-of-month, hour, minute, second, nanosecond  | `1 1 1 0 0 0 0`                            |
| ISO components ||||
| `¯10` | ISO day-of-year components                   | 6            | Year, day-of-year, hour, minute, second, microsecond         | `1 1 0 0 0 0`                            |
| `¯11` | ISO day-of-week components                   | 7            | Year, week, day-of-week, hour, minute, second, microsecond   | `1 1 1 0 0 0 0`                              |
| Decimal encoded[^9] ||||
| `¯20` | Decimal encoded date and time                | 2            | Decimal encoded date, decimal encoded time                   | `10101 0`                              |
| DateTimePicker ||||
| `¯30` | DateTime format                              | 4            | International Day Number, hour, minute, second               | `0 0 0 0`                              |

<h4 class="example">Examples</h4>

Converting `⎕TS`-style timestamps to decimal encoded date and time:

```apl
      ¯20 ⎕DT (2026 8 12 10 49 25 ⋄ 2026 8 12 10 49 27 ⋄ 2026 8 12 10 49 52)
┌───────────────┬───────────────┬───────────────┐
│20260812 104925│20260812 104927│20260812 104952│
└───────────────┴───────────────┴───────────────┘
```

Elided trailing elements take the default values given in [](#timestampsorts):

```apl
      1 ⎕DT ⊂⍬
¯693594
      1 ⎕DT ⊂1 1 1 0 0 0 0
¯693594
```

Converting between a Dyalog Date Number and the DateTime format (code `¯30`):

```apl
      1 ¯30 ⎕DT 44217.63465
┌──────────────┐
│44217 15 13 53│
└──────────────┘
      ¯30 1 ⎕DT⊂44217 15 13 54
44217.63465
```

Converting ISO year and day-of-year to year, week, and day-of-week:

```apl
      3↑¨¯10 ¯11 ⎕DT (2026 1 ⋄ 2026 224)
┌────────┬─────────┐
│2026 1 4│2026 33 3│
└────────┴─────────┘
```

## Military Time Zone Characters

A *military time zone character* is a scalar character that represents the current [datetime](#datetimes) ("now") in a particular time zone.

Military time zone characters can only appear in `Y`. Any element in `Y` can be specified as a military time zone character and is implicitly replaced by the current time in the time zone they represent.

The supported military time zone characters are listed in [](#timezones):

Table: Military time zones { #timezones }

|Character|Time zone name|Time zone |
|---------|--------------|----------|
|A        |Alpha         |UTC+1    |
|B        |Bravo         |UTC+2    |
|C        |Charlie       |UTC+3    |
|D        |Delta         |UTC+4    |
|E        |Echo          |UTC+5    |
|F        |Foxtrot       |UTC+6    |
|G        |Golf          |UTC+7    |
|H        |Hotel         |UTC+8    |
|I        |India         |UTC+9    |
|J        |Juliet        |local time|
|K        |Kilo          |UTC+10   |
|L        |Lima          |UTC+11   |
|M        |Mike          |UTC+12   |
|N        |November      |UTC-1    |
|O        |Oscar         |UTC-2    |
|P        |Papa          |UTC-3    |
|Q        |Quebec        |UTC-4    |
|R        |Romeo         |UTC-5    |
|S        |Sierra        |UTC-6    |
|T        |Tango         |UTC-7    |
|U        |Uniform       |UTC-8    |
|V        |Victor        |UTC-9    |
|W        |Whisky        |UTC-10   |
|X        |X-ray         |UTC-11   |
|Y        |Yankee        |UTC-12   |
|Z        |Zulu          |UTC      |

The resolutions of system clocks vary by platform.

<h4 class="example">Example</h4>

The following expression returns UTC in `⎕TS`-form (`⎕TS` gives local time):

```apl
      ⊃¯1 ⎕DT 'Z'
2026 8 10 19 9 12 120
```

The following expression computes how many hours the local time is offset from UTC (equivalent to [`⎕SYSTEM.OS.UTCOffset`](system.md#os)):

```apl
      24×-/1 ⎕DT 'J' 'Z'
2
```

## Text-Formatted Datetimes

A *text-formatted datetime* is a datetime expressed as a character vector, formatted according to a [*formatting pattern*](#formatting-patterns).

### Formatting Patterns

A *formatting pattern* specifies how a datetime is expressed as a text-formatted datetime.

Either or both of <code>X<sub>R</sub></code> and <code>X<sub>Y</sub></code> can be a character vector containing a formatting pattern.

When used as <code>X<sub>R</sub></code>, the formatting pattern controls how each element of `Y` is formatted into a character vector in `R`. When used as <code>X<sub>Y</sub></code>, the same formatting pattern describes the text supplied in `Y` and controls how it is matched and decoded into the representation given by <code>X<sub>R</sub></code> (see [Pattern-matching Rules](#pattern-matching-rules)).

The formatting pattern allows a datetime to be converted to a user-configurable plain-text format. When a datetime is formatted, elements in the result are copies of the formatting pattern with format sequences replaced by the elements they represent.

The format sequences are intended to be visually reminiscent of the generated text. They use alphabetic characters easily associated with the substitution (for example `D`, `M`, and `Y` for Day, Month, and Year respectively) repeated one or more times to indicate format. Some sequences allow the first character to be replaced by a `_`, or the casing to be altered.

Table: Formatting sequences { #formatseq }

| Format letter | Length | Meaning | Variations | Example |
|---|---|---|---|---|
| <u>Y</u>ear | `YY` | Without century | `YY` | `19` |
|_   _| `YYYY` | With century | `YYYY` | `2019` |
| <u>M</u>onth | `M` | 1 or 2 digit numeric | `M` | `3` |
| | `MM` | 2 character numeric | `MM`<br>`_M` | `03`<br>` 3` |
| | `MMM` | Abbreviated name | `MMM`<br>`Mmm`<br>`mmm`<br>`_mm`[^12] | `MAR`<br>`Mar`<br>`mar`<br>`Mar` |
|_   _| `MMMM` | Full name | `MMMM`<br>`Mmmm`<br>`mmmm`<br>`_mmm`[^12] | `MARCH`<br>`March`<br>`march`<br>`March` |
| <u>D</u>ay of month | `D` | 1 or 2 digit numeric | `D` | `4` |
|_   _| `DD` | 2 character numeric | `DD`<br>`_D` | `04`<br>` 4` |
| <u>h</u>ours | `h` | 1 or 2 digit numeric | `h` | `8` |
|_   _| `hh` | 2 character numeric | `hh`<br>`_h` | `08`<br>` 8` |
| <u>m</u>inutes | `m` | 1 or 2 digit numeric | `m` | `5` |
|_   _| `mm` | 2 character numeric | `mm`<br>`_m` | `05`<br>` 5` |
| <u>s</u>econds | `s` | 1 or 2 digit numeric | `s` | `0` |
|_   _| `ss` | 2 character numeric | `ss`<br>`_s` | `00`<br>` 0` |
| <u>f</u>ractional seconds | `f` | 1 digit precision | `f` | `5` |
| | `ff` | 2 digit precision | `ff` | `55` |
| | `fff` | 3 digit precision | `fff` | `555` |
| | `ffff` | 4 digit precision | `ffff` | `5555` |
| | `fffff` | 5 digit precision | `fffff` | `55555` |
|_   _| `ffffff` | 6 digit precision | `ffffff` | `555555` |
| <u>d</u>ay of week | `d` | Numeric (1-7) | `d` | `1` |
| | `ddd` | Abbreviated name | `DDD`<br>`Ddd`<br>`ddd`<br>`_dd`[^12] | `MON`<br>`Mon`<br>`mon`<br>`Mon` |
|_   _| `dddd` | Full name | `DDDD`<br>`Dddd`<br>`dddd`<br>`_ddd`[^12] | `MONDAY`<br>`Monday`<br>`monday`<br>`Monday` |
| ISO <u>w</u>eek number | `w` | 1 or 2 digit numeric | `w` | `10` |
|_   _| `ww` | 2 character numeric | `ww`<br>`_w` | `10`<br>`10` |
| year of ISO <u>W</u>eek number[^13] | `WW` | Without century | `WW` | `19` |
|_   _| `WWWW` | With century | `WWWW` | `2019` |
| day of <u>y</u>ear | `y` | 1 to 3 digit numeric | `y` | `63` |
|_   _| `yy` | 3 character numeric | `yy`<br>`_y` | `063`<br>` 63` |
| <u>O</u>rdinal indicator[^14] for day of month | `O` | Short | `O`<br>`o` | `T`<br>`t` |
|_   _| `OO` | Full | `OO`<br>`Oo`<br>`oo` | `TH`<br>`Th`<br>`th` |
| hours in <u>t</u>welve hour clock | `t` | 1 or 2 digit numeric | `t` | `8` |
|_   _| `tt` | 2 character numeric | `tt`<br>`_t` | `08`<br>` 8` |
| AM/<u>P</u>M Indicator | `P` | Short | `P`<br>`p` | `A`<br>`a` |
|_   _| `PP` | Full | `PP`<br>`pp` | `AM`<br>`am` |

The upper and lower case letters, underscore `_`, dollar `$`, and percent `%` are all reserved for introducing format sequences, even though not all currently have meaning. The remaining, non-reserved, characters are copied to the result unchanged; this means that the format string `hh:mm` represents the hour of the day and minute of the hour, separated by a colon (for example `12:00`). All characters or sequences of characters can be delimited by `"` or `'` at any point in the format string to prevent them from being interpreted as a part of a format sequence, and, within these delimiters, two adjacent delimiter characters produce a single delimiter.

For example, the characters `AaaaBbbb` consist of two adjacent format sequences because there is a sequence of `A`s followed by a sequence of `B`s. The characters `AaaaAaaa` consist of one format sequence because it only contains `A`s. It can be separated into two format sequences by inserting an empty `"`- or `'`-delimited string, for example, `Aaaa""Aaaa`.

<h4 class="example">Example</h4>

```apl
      'Dddd, DDoo Mmmm YYYY; hh:mm:ss' ⎕DT ⊂2019 2 13 10 16 56
┌───────────────────────────────────────┐
│Wednesday, 13th February 2019; 10:16:56│
└───────────────────────────────────────┘
```

### Language

Unless overridden, English is used for text substitutions. Different languages can be selected using the [`Language` variant option](#variant-option-language) and/or the use of language specifiers within the formatting pattern. In either case, the language is specified as either a two letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code in lower case (for example, `en`) or as a five character language with an additional underscore and two character region in upper case (for example, `en_GB`). Within the formatting pattern, `__xx__` (where `xx` is the two or five character specifier) will switch the language of the subsequent generated or matched text. [](#languages) shows the languages that are built into the interpreter.

Table: Built-in languages { #languages }

| ISO 639-1 | Language |
| --- | ---  |
| da | Danish |
| de | German |
| el | Greek |
| en | English |
| es | Spanish |
| fi | Finnish |
| fr | French |
| it | Italian |
| ja | Japanese |
| nb | Norwegian Bokmål |
| nl | Dutch |
| nn | Norwegian Nynorsk |
| pl | Polish |
| pt | Portuguese |
| ru | Russian |
| sv | Swedish |
| zh | Chinese |

<h4 class="example">Example</h4>

```apl
      '__de__Dddd, DDoo Mmmm YYYY; hh:mm:ss' ⎕DT ⊂2019 2 13 10 16 56
┌────────────────────────────────────┐
│Mittwoch, 13. Februar 2019; 10:16:56│
└────────────────────────────────────┘
```

### Predefined Patterns

Any formatting pattern can contain (in part or in whole) a named *predefined pattern*, which allows common date and time formats to be specified in abbreviated form. Predefined patterns can be specified for each language, allowing patterns to be tailored for the selected language.

Predefined patterns are included in a formatting pattern using `%` delimiters. For example, `%ISO%` includes the named predefined pattern `ISO`.

The following global predefined pattern is built into the interpreter:

Table: Predefined patterns built into the interpreter { #patterns }

| Name | Substitutes as |
| ---  | ---            |
| `ISO`  | `YYYY-MM-DD"T"hh:mm:ss` |

Additional predefined patterns can be defined using the [`Dictionary` variant option](#variant-option-dictionary). Predefined patterns must not contain references to other predefined patterns.

<h4 class="example">Example</h4>

```apl
      '"ISO date": %ISO%' ⎕DT ⊂2019 2 13 10 16 56
┌─────────────────────────────┐
│ISO date: 2019-02-13T10:16:56│
└─────────────────────────────┘
```

### Pattern-Matching Rules

When <code>X<sub>Y</sub></code> is a formatting pattern, character vectors in `Y` are matched against it.

<h3 class="example">Examples</h3>

```apl
      'DD/MM/YYYY' ¯1 ⎕DT ⊂'13/02/2019'
┌─────────────────┐
│2019 2 13 0 0 0 0│
└─────────────────┘
      'Dddd, DDoo Mmmm YYYY; hh:mm:ss' ¯1 ⎕DT ⊂'Wednesday, 13th February 2019; 10:16:56'
┌────────────────────┐
│2019 2 13 10 16 56 0│
└────────────────────┘
      '__da__Dddd, DDoo mmmm YYYY' 1 ⎕DT ⊂'Onsdag, 13. februar 2019'
43508
```

The following additional rules apply to the matching.

#### Two-Digit Years

Two digit years (that is, those corresponding to the formatting pattern elements `YY` and `WW`) are, by default, interpreted according to the same rules used for `⎕SM` and GUI edit fields, which are configurable using the [`YY_WINDOW`](../../../windows-installation-and-configuration-guide/configuration-parameters/yy-window/) configuration parameter.

<h4 class="example">Example</h4>

```apl
      'DD.MM.YY' 'YYYY-MM-DD' ⎕DT⊂'12.08.26'
┌──────────┐
│2026-08-12│
└──────────┘
```

#### Ambiguities and Precision

Formatting *to* a text-formatted datetime can be _lossy_, that is, the formatted text does not necessarily contain sufficient information to regenerate the original datetime. A formatting pattern used to convert *from* a text-formatted datetime is not permitted to be ambiguous, that is, it must not be possible to deduce multiple disjoint datetimes from text generated by it (for example, a formatting pattern which contains a year and a day-of-month but no month, because there could be twelve disjoint dates for which the formatting pattern would generate identical text). Such a formatting pattern is rejected.

Formatting patterns are, however, permitted to have limited precision (for example, a formatting pattern that includes a date but no time elements, or a date plus only hour and minute time elements). Elements with lower significance than the least significant provided element can be elided and take a default value; this is analogous to the way `⎕DT` infers elements elided from timestamps.

There are three principal means of specifying a date:

- year, month, day-of-month
- year, day-of-year
- ISO-year-of-week, ISO-week, day-of-week

If a text-formatted datetime contains elements from more than one of these three principal formats, then:

1. at least one of them must be unambiguous;
2. when more than one of them is unambiguous, the date is determined from the most precise one;
3. all element values must be consistent with the date so deduced.

Elided elements of a year, month, day-of-month date are all (including the year) implicitly `1`. Elided elements of times are all implicitly `0`.

Some combinations of variable-length substitutions can make particular texts impossible to parse unambiguously. For example, the formatting pattern `MD` (1 to 2 digits of month immediately followed by 1 to 2 digits of day-of-month) formats both 3 December and 23 January as `123`, so the text `123` cannot be matched against `MD` and an error is signalled. Whether such an ambiguity actually arises depends on the text being parsed: the text `1231` can only mean 31 December and is matched without error. Where two or more variable-length numeric or alphanumeric substitutions are adjacent, you can place literal text between them that cannot be confused with the substitution text to avoid such ambiguities.

#### Consistency

The formatted text is parsed and used to compute a datetime according to the given formatting pattern, and must precisely match the text that would be produced if the resulting datetime were formatted using that same formatting pattern. That is:

- The formatted text must contain valid substitution text where a format sequence appears in the formatting pattern – for example, a full month name where `Mmmm` appears in the formatting pattern.
- All other characters, including spaces and literal characters, must exactly match the formatting pattern.
- All characters must be in the correct case.
- The elements in the formatted text must be consistent with one another. If the formatting pattern contains the same element (or variations of the same element) more than once, they must have the same value in each case. Elements that are not independent must not be contradictory. For example, the text `Mon 5 Feb 2025` superficially appears to match the formatting pattern `Ddd D Mmm YYYY` but is contradictory, because 5 February 2025 was a Wednesday, not a Monday.

If a formatting pattern is rejected, or a text-formatted datetime cannot be matched against the formatting pattern for any of the reasons above, a `DOMAIN ERROR` is signalled and an explanatory message is included.

## Validating Datetimes

When <code>X<sub>R</sub></code> is `0`, `⎕DT` validates the elements of `Y` instead of converting them, interpreting each according to <code>X<sub>Y</sub></code>. `R` is a Boolean with a `1` for each element of `Y` that represents a valid datetime and a `0` for each that does not.

<h3 class="example">Examples</h3>

Validating a mixture of representations, one of which is not a datetime at all:

```apl
      0 ⎕DT ⎕TS (2020 13 1) 'J' 'DT' #
1 0 1 0 0
```

Validating text-formatted datetimes. 1900 was not a leap year, but 2000 was:

```apl
      'YYYY-MM-DD' 0 ⎕DT '1900-02-29' '2000-02-29'
0 1
```

## Variant Options

`⎕DT` has two variant options, `Language` and `Dictionary`, specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md) and summarised in [](#variantoptionsfordt). They apply only when <code>X<sub>Y</sub></code> and/or <code>X<sub>R</sub></code> are formatting patterns.

Table: Variant options for `⎕DT` { #variantoptionsfordt }

|Variant Option|Valid Values|Effect|
|---|---|---|
|[`Language`](#variant-option-language)|`'en'` (Default), or another two- or five-character language name such as `'en_GB'`|The language used for formatting and matching datetimes.|
|[`Dictionary`](#variant-option-dictionary)|a namespace|Additional or replacement month names and predefined patterns.|

### Variant Option: `Language`

The `Language` variant option specifies the language used for formatting and matching datetimes and defaults to `'en'` (English). A language is named by a two or five character value (for example `'en'` or `'en_GB'`). The value can be one of the following:

- a single character vector, which applies to whichever of <code>X<sub>Y</sub></code> and/or <code>X<sub>R</sub></code> are formatting patterns.
- A 2-element vector of two character vectors, which apply to <code>X<sub>Y</sub></code> and <code>X<sub>R</sub></code> respectively (each is used only if the corresponding value is a formatting pattern).

The setting can be explicitly overridden within a formatting pattern using the `__xx__` specifier described under [Language](#language).

<h4 class="example">Examples</h4>

```apl
      '__da__Dddd, DDoo mmmm YYYY; hh:mm:ss' ⎕DT ⊂2019 2 13 10 16 56
┌──────────────────────────────────┐
│Onsdag, 13. februar 2019; 10:16:56│
└──────────────────────────────────┘
      fmt←'Dddd, DDoo mmmm YYYY; hh:mm:ss'
      fmt ⎕DT⍠'Language' 'da' ⊂2019 2 13 10 16 56
┌──────────────────────────────────┐
│Onsdag, 13. februar 2019; 10:16:56│
└──────────────────────────────────┘
```

### Variant Option: `Dictionary`

The `Dictionary` variant option specifies a namespace that contains additional or replacement names for the months (and so on) and/or predefined patterns, for languages and language regions. If <code>X<sub>Y</sub></code> and <code>X<sub>R</sub></code> are both formatting patterns, the dictionary is applied to both.

At the top level there can be zero or more sub-namespaces with two or five character names, according to the rules for language and language regions. Within each of these, month names (and so on) are defined as shown in [](#names).

Table: Names { #names }

| Named item | Description |
| --- | ---  |
| `MonthNames` | A twelve-element vector of character vectors containing the full names corresponding to January to December, respectively. |
| `ShortMonthNames` | A twelve-element vector of character vectors containing the short names corresponding to Jan to Dec, respectively. |
| `WeekdayNames` | A seven-element vector of character vectors containing the full names corresponding to Sunday to Saturday, respectively. |
| `ShortWeekdayNames` | A seven-element vector of character vectors containing the short names corresponding to Sun to Sat, respectively. |
| `MorningAfternoon` | A two-element vector of character vectors containing the names corresponding to AM and PM, respectively. |
| `Ordinals` | A character vector containing the one ordinal used for all numbers in the range 1 to 31, or a thirty one-element vector of character vectors containing the ordinals for 1 to 31, respectively. |

The top level of the dictionary namespace can contain a sub-namespace named `Patterns` and, within this, further sub-namespaces named `Global` and/or two or five character language names, containing definitions of predefined patterns. Predefined patterns are defined in the same way as the formatting pattern except that they must not contain references to other predefined patterns.

If the namespace contains a definition that is supplied built into the interpreter, it replaces the built-in one.

If a dictionary is incomplete (for example, is missing one of the expected named items, or one of the named items contains too few elements), an error is signalled if the missing content would be needed.

<h4 class="example">Example</h4>

The following creates a dictionary defined by the namespace `dict`, used in the examples that follow.

```apl
dict←(
  Patterns: (
    Global: (
      ISOweek: 'YYYY-"W"ww'
      DateCompact: 'D-MMM-YYYY'
      DateVerbose: '"the date is" DD _mm YYYY'
    )
    fr: ( DateVerbose: '"la date est le" DD mmm YYYY' )
    en_US: ( DateVerbose: '"the date is" Mmm DD, YYYY' )
  )
  en_US: (
    ShortMonthNames: (
      'Jan.' ⋄ 'Feb.' ⋄ 'Mar.' ⋄ 'Apr.' ⋄ 'May' ⋄ 'June'
      'July' ⋄ 'Aug.' ⋄ 'Sept.' ⋄ 'Oct.' ⋄ 'Nov.' ⋄ 'Dec.'
    )
  )
  cy: (
    MonthNames: (
      'Ionawr' ⋄ 'Chwefror' ⋄ 'Mawrth' ⋄ 'Ebrill' ⋄ 'Mai' ⋄ 'Mehefin'
      'Gorffennaf' ⋄ 'Awst' ⋄ 'Medi' ⋄ 'Hydref' ⋄ 'Tachwedd' ⋄ 'Rhagfyr'
    )
    ShortMonthNames: (
      'Ion' ⋄ 'Chw' ⋄ 'Maw' ⋄ 'Ebr' ⋄ 'Mai' ⋄ 'Meh'
      'Gor' ⋄ 'Awst' ⋄ 'Medi' ⋄ 'Hyd' ⋄ 'Tach' ⋄ 'Rhag'
    )
    WeekdayNames: (
      'Dydd Sul' ⋄ 'Dydd Llun' ⋄ 'Dydd Mawrth' ⋄ 'Dydd Mercher'
      'Dydd Iau' ⋄ 'Dydd Gwener' ⋄ 'Dydd Sadwrn'
    )
    ShortWeekdayNames: (
      'Sul' ⋄ 'Llun' ⋄ 'Maw' ⋄ 'Mer' ⋄ 'Iau' ⋄ 'Gwen' ⋄ 'Sad'
    )
    MorningAfternoon: ( 'yb' ⋄ 'yh' )
    Ordinals: (
      'af' ⋄ 'il' ⋄ 'ydd' ⋄ 'ydd' ⋄ 'ed' ⋄ 'ed' ⋄ 'fed' ⋄ 'fed' ⋄ 'fed'
      'fed' ⋄ 'eg' ⋄ 'fed' ⋄ 'eg' ⋄ 'eg' ⋄ 'fed' ⋄ 'eg' ⋄ 'eg' ⋄ 'fed'
      'eg' ⋄ 'fed' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain'
      'ain' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain' ⋄ 'ain'
    )
  )
)
```

In the above example:

- the predefined pattern `ISOweek` is defined globally and is not redefined. This means that it has the same value for all languages. Similarly, `DateCompact` has the same value for all languages, but although the definition is global, it contains the formatting pattern `MMM` and this will be substituted with the month name in the selected language.
- The predefined patterns `DateVerbose` is defined globally, and redefined for languages `fr` and `en_US`. The global definition will be used when any language other than `fr` and `en_US` is selected. If there was no global definition it would only be defined for `fr`, all regional variations of `fr`, and `en_US`.
- There is no explicit definition of patterns or names for language region `en_GB`. If this language is selected, the definitions for `en` will be used.
- There is an explicit definition for `ShortMonthNames` for language region `en_US`. If this language is selected, the definition of `ShortMonthNames` is as defined, and as for `en` for other names. As `en` is not defined in the dictionary, the built-in defaults are used.

```apl
      '%DateVerbose%' ⎕DT⍠'Dictionary'dict ⊂2019 2 13 10 16 56
┌───────────────────────┐
│the date is 13 Feb 2019│
└───────────────────────┘
      '%DateVerbose%' ⎕DT⍠('Dictionary' dict ⋄ 'Language' 'en_US') ⊂2019 2 13 10 16 56
┌─────────────────────────┐
│the date is Feb. 13, 2019│
└─────────────────────────┘
      '__cy__Dddd, DDoo mmmm YYYY; hh:mm:ss' ⎕DT⍠'Dictionary' dict ⊂2019 2 13 10 16 56
┌──────────────────────────────────────────┐
│Dydd Mercher, 13eg chwefror 2019; 10:16:56│
└──────────────────────────────────────────┘
      '__cy__%DateVerbose%' ⎕DT⍠'Dictionary' dict ⊂2019 2 13 10 16 56
┌───────────────────────┐
│the date is 13 Chw 2019│
└───────────────────────┘
```

[^1]: The epoch is the datetime represented by `0` in the [proleptic Gregorian calendar](https://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar).
[^2]: Are negative values allowed? No datetime can represent a date earlier than ¯4714-11-24 00:00:00.
[^3]: There are the same number of ticks per day regardless of leap seconds.
[^4]: Due to their possible magnitude, these are generated as [128-bit decimal floating point values](../../programming-reference-guide/introduction/128-bit-decimal-floating-point.md) regardless of the setting of [`⎕FR`](fr.md).
[^5]: For negative numbers, the integral part counts backward from 1899-12-30 and the fractional part counts forward from the date so reached.
[^6]: Excel supports two time number conventions. On Windows the 1900 Date System is the default and on macOS the 1904 Date System is the default. Both systems can use either convention and the convention in use is stored in the worksheet so that the platforms interoperate.
[^7]: Count includes the invalid date 1900-02-29.
[^8]: Microsoft Excel converts day 0 to the invalid date 1900-01-00.
[^9]: Decimal encoded formats encode human-readable dates and times into a single number with the most significant part in the most significant decimal digit, for example 2020-01-23 is encoded as 20200123, and 13:17:56 is encoded as 131756. The date must be between 1 January 0001 and 31 December 9999 in the proleptic Gregorian calendar.
[^10]: All dates must be between 1 January 0001 and 28 February 4000 in the proleptic Gregorian calendar.
[^11]: If a timestamp in `Y` has fewer than the maximum number of elements, the remaining elements take the default values shown.
[^12]: Natural sentence case, which can be specified for `M` (month name) and `d` (day name) only, causes the text to be substituted in the case which is natural for the language; some languages (for example, English) always capitalise the first letter of day and month names whereas others (for example, French) do not.
[^13]: Dates at the start of the year can be in the final week of the previous year, and dates at the end of the year can be in the first week of the following year.
[^14]: An ordinal indicator is a character or group of characters following a numeral, such as the English suffixes -st, -nd, -rd, and -th in 1st, 2nd, 3rd, and 4th.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DT DT 1200⌶
</div>
