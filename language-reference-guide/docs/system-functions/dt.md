---
search:
  boost: 2
---

# <span>Date-time</span> `R←X ⎕DT Y`{{key}}

This function validates date-times, converts date-times between one representation and another, and converts date-times to and from text.

A date-time is a date and time of day represented by a *timestamp*, a *time number*, a *military time-zone character* or a *text-formatted datetime*.

- A *timestamp* is a date-time expressed as a multiple element numeric vector, of which there are several different sorts (principally `⎕TS` format).
- A *time number* is a date-time expressed as a scalar numeric value, of which there are several different sorts.
- A *military time zone character* is a scalar character that represents the current date-time ("now") in a particular time zone. For example, `'A'` represents the current date-time (UTC) + 1 hour.
- A *text-formatted datetime* is a date-time expressed as a character vector, formatted according to a *pattern* (see [Formatting patterns](#formatting-patterns) below).

`Y` is an array of any shape whose elements contain a timestamp, time number, military time zone character or text-formatted datetime, in any combination.

`X` describes the representation to which the elements of `Y` are to be converted (the output format) and, optionally, the representation of the elements of `Y` (the input format). For convenience these are referred to below as <code>X<sub>R</sub></code> and <code>X<sub>Y</sub></code>, respectively.

`X` can be a single element (<code>X<sub>R</sub></code>) or a 2-element vector (<code>X<sub>Y</sub> X<sub>R</sub></code>). Each of <code>X<sub>Y</sub></code> and <code>X<sub>R</sub></code> can be:

- an integer *date-time code* (see the tables below), or
- a character vector containing a *pattern* that describes how a datetime is formatted as text (see [Formatting patterns](#formatting-patterns) below).

When <code>X<sub>R</sub></code> is an integer it must be either `0` or a date-time code listed in the tables below. `0` specifies that the elements of `Y` are to be validated; a non-zero value specifies the date-time representation to which the elements of `Y` are to be converted. When <code>X<sub>R</sub></code> is a pattern, the elements of `R` are character vectors, each derived by formatting the corresponding element of `Y` as text according to the pattern.

<code>X<sub>Y</sub></code> can be omitted only when the elements of `Y` are Dyalog Date Numbers, `⎕TS`-style timestamps or military time zone characters. When <code>X<sub>Y</sub></code> is omitted, the numeric elements of `Y` are interpreted as follows:

- scalars are assumed to be time numbers of type Dyalog Date Number (code `1`)
- vectors are assumed to be `⎕TS` timestamps (code `¯1`)

When <code>X<sub>Y</sub></code> is an integer date-time code it explicitly specifies the date-time representation of the numeric elements of `Y`. When <code>X<sub>Y</sub></code> is a pattern, the corresponding character vectors in `Y` are matched against the pattern and the resulting date-times are returned in the representation given by <code>X<sub>R</sub></code> (see [Pattern matching rules](#pattern-matching-rules) below). A pattern <code>X<sub>Y</sub></code> cannot be omitted, even when the elements of `Y` are character vectors that could unambiguously be assumed to be text-formatted datetimes.

Text-formatted datetimes and patterns are character vectors; no scalar extension occurs when character scalars appear in `X` or `Y`. A single text-formatted datetime in `Y` must be enclosed (nested); an unenclosed character vector in `Y` is interpreted as a vector of military time zone characters. As a convenience, a simple (not nested) character vector `X` is implicitly enclosed and processed as <code>X<sub>R</sub></code>, so a pattern can be supplied on its own to format datetimes as text.

Character scalars in `Y` are always interpreted as meaning "now".

`R` is an array of the same shape as `Y`, where each element is a timestamp, time number, character vector or Boolean value as determined by <code>X<sub>R</sub></code> (the second or only element of `X`).

Time numbers in `R` can be of type DECF even if `⎕FR` is `645` if their magnitude can be too great to store precisely in a double. See the table below for the type numbers where this is so.

## Time Numbers

If a value in `X` is positive it indicates that a time number type is expected in `Y` or generated in `R`, as follows. Note that the last column indicated whether (Yes) or not (No) negative numbers are allowed.

|Group|Code|Description|Category|Date and time[^1] represented by 0 (Epoch)|Negative values allowed?[^8]|
|---|---|---|---|---|---|
|Dyalog APL              | `1` |Dyalog Date Number|Day count with fractional part|1899-12-31 00:00|Yes|
|_                      _| `2` |Dyalog component file time|Tick count 1÷60s ticks[^2]|1970-01-01 00:00|Yes|
|Other languages         | `10` |J (J nanosecond time)|Tick count[^3] 1ns ticks [^2]|2000-01-01 00:00|Yes|
|                        | `11` |Shakti K7|Tick count 1ms ticks[^2]|2024-01-01 00:00|Yes|
|                        | `12` |JavaScript / D / Q / Go UnixMilli |Tick count 1ms ticks[^2]|1970-01-01 00:00|Yes|
|                        | `13` |R (R chron format)|Day count with fractional part|1970-01-01 00:00|Yes|
|                        | `14` |Shakti K9|Tick count 1ms ticks[^2]|2001-01-01 00:00|Yes|
|                        | `15` |Go UnixMicro|Tick count 1µs ticks[^2]|1970-01-01 00:00|Yes|
|                        | `16` |Go UnixNano|Tick count 1ns ticks[^2]|1970-01-01 00:00|Yes|
|_                      _| `17` |APL+Win and APL64 workspace timestamp|Tick count 1μs ticks[^2]|1900-01-01 00:00|No|
|UNIX                    | `20` |Unix time|Tick count 1s ticks[^2]|1970-01-01 00:00|Yes|
|                        | `21` |Apollo NCS UUID|Tick count 4µs ticks[^2]|1980-01-01 00:00|No|
|_                      _| `22` |OSF DCE UUID|Tick count 1ns ticks[^2]|1582-10-15 00:00|No|
|Microsoft Windows       | `30` |Microsoft DOS date/time|Encoded broken-down time 2s resolution|N/A|No|
|                        | `31` |Microsoft Win32 FILETIME|Tick count[^3] 100ns ticks|1601-01-01 00:00|No|
|                        | `32` |Microsoft CLR DateTime (.NET)(Ticks property thereof)|Tick count [^3] 100ns ticks|0001-01-01 00:00|No|
|_                      _| `33` |Microsoft OLE Automation Date(also known as Variant Time)|Day count with fractional part|1899-12-30 00:00|Yes [^10]|
|Application             | `40` |Excel (1900 Date System)[^4] / Lotus 1-2-3|Day count with fractional part[^5]|1899-12-31 00:00[^6]|No|
|                        | `41` |Excel (1904 Date System)[^4]|Day count with fractional part|1904-01-01 00:00|No|
|                        | `42` |Stata statistics package|Tick count 1ms ticks[^2]|1960-01-01 00:00|Yes|
|                        | `43` |SPSS statistics package|Tick count 1s ticks[^2]|1582-10-14 00:00|No|
|_                      _| `44` |SAS|Tick count 1s ticks[^2]|1960-01-01 00:00|Yes|
|Julian Date and variants| `50` |Julian Date|Day count with fractional part|¯4717-11-24 12:00|No|
|                        | `51` |J (J dayno)|Day count with fractional part|1800-01-01 00:00|No|
|                        | `52` |Reduced Julian Date|Day count with fractional part|1858-11-16 12:00|Yes|
|                        | `53` |Modified Julian Date|Day count with fractional part|1858-11-17 00:00|Yes|
|                        | `54` |Dublin Julian Date|Day count with fractional part|1899-12-31 12:00|Yes|
|                        | `55` |CNES Julian Date|Day count with fractional part|1950-01-01 00:00|Yes|
|_                      _| `56` |CCSDS Julian Date|Day count with fractional part|1958-01-01 00:00|Yes|
|Decimal encoded[^9]     | `60` |Floating-point decimal encoded format Digits take the form yyyymmdd.hhmmss|Encoded broken-down time 1s resolution|N/A|No|
|_                      _| `61` |Integer decimal encoded format Digits take the form yyyymmddhhmmss(J digit time)|Encoded broken-down time 1s resolution|N/A|No|
|Misc. Operating Systems | `70` |AmigaOS|Tick count 1ms ticks[^2]|1978-01-01 00:00|No|

## Time Stamps

If a value in `X` is negative it indicates that a timestamp type is expected in `Y` or generated in `R`, as follows:

| Group                  | Code  | Description                                  | Max elements | Element contents[^11]                                        | Elided element implicit values (in Y)[^13] |
|------------------------|-------|----------------------------------------------|--------------|--------------------------------------------------------------|--------------------------------------------|
| APL 7-element vector   | `¯1`  | Millisecond precision (`⎕TS`)                | 7            | Year, month, day-of-month, hour, minute, second, millisecond | `1 1 1 0 0 0 0`                            |
|                        | `¯2`  | Microsecond precision                        | 7            | Year, month, day-of-month, hour, minute, second, microsecond | `1 1 1 0 0 0 0`                            |
|_                      _| `¯3`  | Nanosecond precision (J expanded digit time) | 7            | Year, month, day-of-month, hour, minute, second, nanosecond  | `1 1 1 0 0 0 0`                            |
| ISO components         | `¯10` | ISO day-of-year components                   | 6            | Year, day-of-year, hour, minute, second, microsecond         | `1 1 0 0 0 0`                            |
|_                      _| `¯11` | ISO day-of-week components                   | 7            | Year, week, day-of-week, hour, minute, second, microsecond   | `1 1 1 0 0 0 0`                              |
| Decimal encoded[^2]    | `¯20` | Decimal encoded date and time                | 2            | Decimal encoded date, decimal encoded time                   | `10101 0`                              |
| DateTimePicker         | `¯30` | DateTime format                              | 4            | International Day Number, hour, minute, second               | `0 0 0 0`                              |

## Military time zone characters

Any element in `Y` can be specified as a military time zone character and is implicitly replaced by the current time in the time zone they represent. The time zones are as follows:

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

## Formatting patterns

Either or both of <code>X<sub>R</sub></code> and <code>X<sub>Y</sub></code> can be a character vector containing a *pattern* which describes how a datetime is, or is to be, formatted as text.

When used as <code>X<sub>R</sub></code>, the pattern controls how each element of `Y` is formatted into a character vector in `R`. When used as <code>X<sub>Y</sub></code>, the same pattern describes the text supplied in `Y` and controls how it is matched and decoded into the representation given by <code>X<sub>R</sub></code> (see [Pattern matching rules](#pattern-matching-rules) below).

The formatting pattern allows a datetime to be converted to a highly user-configurable, plain text format. When a datetime is formatted, elements in the result are copies of the format pattern with format sequences replaced by the elements they represent.

The format sequences are intended to be visually reminiscent of the generated text. They use alphabetic characters easily associated with the substitution (for example `D`, `M` and `Y` for Day, Month and Year respectively) repeated one or more times to indicate format. Some sequences allow the first character to be replaced by a `_`, or the casing to be altered.

| Format letter | Length | Meaning | Variations | Example |
|---|---|---|---|---|
| <u>Y</u>ear | `YY` | Without century | `YY` | `19` |
|_   _| `YYYY` | With century | `YYYY` | `2019` |
| <u>M</u>onth | `M` | 1 or 2 digit numeric | `M` | `3` |
| | `MM` | 2 character numeric | `MM`<br>`_M` | `03`<br>` 3` |
| | `MMM` | Abbreviated name | `MMM`<br>`Mmm`<br>`mmm`<br>`_mm`[^14] | `MAR`<br>`Mar`<br>`mar`<br>`Mar` |
|_   _| `MMMM` | Full name | `MMMM`<br>`Mmmm`<br>`mmmm`<br>`_mmm`[^14] | `MARCH`<br>`March`<br>`march`<br>`March` |
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
| | `ddd` | Abbreviated name | `DDD`<br>`Ddd`<br>`ddd`<br>`_dd`[^14] | `MON`<br>`Mon`<br>`mon`<br>`Mon` |
|_   _| `dddd` | Full name | `DDDD`<br>`Dddd`<br>`dddd`<br>`_ddd`[^14] | `MONDAY`<br>`Monday`<br>`monday`<br>`Monday` |
| ISO <u>w</u>eek number | `w` | 1 or 2 digit numeric | `w` | `10` |
|_   _| `ww` | 2 character numeric | `ww`<br>`_w` | `10`<br>`10` |
| year of ISO <u>W</u>eek number[^15] | `WW` | Without century | `WW` | `19` |
|_   _| `WWWW` | With century | `WWWW` | `2019` |
| day of <u>y</u>ear | `y` | 1 to 3 digit numeric | `y` | `63` |
|_   _| `yy` | 3 character numeric | `yy`<br>`_y` | `063`<br>` 63` |
| <u>O</u>rdinal indicator[^16] for day of month | `O` | Short | `O`<br>`o` | `T`<br>`t` |
|_   _| `OO` | Full | `OO`<br>`Oo`<br>`oo` | `TH`<br>`Th`<br>`th` |
| hours in <u>t</u>welve hour clock | `t` | 1 or 2 digit numeric | `t` | `8` |
|_   _| `tt` | 2 character numeric | `tt`<br>`_t` | `08`<br>` 8` |
| AM/<u>P</u>M Indicator | `P` | Short | `P`<br>`p` | `A`<br>`a` |
|_   _| `PP` | Full | `PP`<br>`pp` | `AM`<br>`am` |

The upper and lower case letters, underscore `_`, dollar `$` and percent `%` are all reserved for introducing format sequences, even though not all currently have meaning. The remaining, non-reserved, characters are copied to the result unchanged, thus the format string `hh:mm` represents the hour of the day and minute of the hour with a colon between (for example `12:00`). All characters or sequences of characters can be delimited by `"` or `'` at any point in the format string to prevent them being interpreted as a part of a format sequence, and, within these delimiters, two adjacent delimiter characters produce a single delimiter.

Note: The characters `AaaaBbbb` consist of two adjacent format sequences because there is a sequence of As followed by a sequence of Bs. The characters `AaaaAaaa` consist of one format sequence because it only contains `A`s. It can be separated into two format sequences by inserting an empty `"` or `'` - delimited string, for example `Aaaa""Aaaa`.

## Language

Unless overridden, English is used for text substitutions. Different languages can be selected using the [Language variant option](#language-variant-option) and/or the use of language specifiers within the format pattern. In either case, the language is specified as either a two letter [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code in lower case (for example `en`) or as a five character language with an additional underscore and two character region in upper case (for example `en_GB`). Within the format pattern, `__xx__` (where `xx` is the two or five character specifier) will switch the language of the subsequent generated or matched text. Dictionaries for the following languages are built in:

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

## Predefined patterns

Any pattern can contain (in part or in whole) a named predefined pattern, which allows common date and time formats to be specified in abbreviated form. Predefined patterns can be specified on a per-language basis, allowing patterns to be tailored for the selected language.

Predefined patterns are included in a pattern using `%` delimiters. For example, `%ISO%` includes the named predefined pattern `ISO`.

The following global predefined pattern is built in:

| Name | Substitutes as |
| ---  | ---            |
| `ISO`  | `YYYY-MM-DD"T"hh:mm:ss` |

This list can be expanded in future.

Additional predefined patterns can be defined using the [Dictionary variant option](#dictionary-variant-option). Predefined patterns must not contain references to other predefined patterns.

## Pattern matching rules

When <code>X<sub>Y</sub></code> is a pattern, the corresponding character vectors in `Y` are matched against it and decoded into date-times. The following additional rules apply to the matching.

### Two digit years

Two digit years (i.e. those corresponding to the formatting pattern elements `YY` and `WW`) are by default interpreted according to the same rules used for `⎕SM` and GUI edit fields, which are configurable using the `YY_WINDOW` configuration parameter and described with [its documentation](../../windows-installation-and-configuration-guide/configuration-parameters/yy-window/).

### Ambiguities and precision

Formatting *to* a text-formatted datetime can be lossy — that is, the formatted text does not necessarily contain sufficient information to regenerate the original datetime. A pattern used to convert *from* a text-formatted datetime is not permitted to be ambiguous such that it would be possible to deduce multiple disjoint datetimes from text generated by it (for example, a pattern which contains a year and a day-of-month but no month, because there could be twelve disjoint dates for which the pattern would generate identical text). Such a pattern is rejected.

Patterns are, however, permitted to have limited precision (for example, a pattern which includes a date but no time elements, or a date plus only hour and minute time elements). Elements with lower significance than the least significant provided element can be elided and take a default value; this is analogous to the way `⎕DT` infers elements elided from timestamps.

There are three principal means of specifying a date:

- year, month, day-of-month
- year, day-of-year
- ISO-year-of-week, ISO-week, day-of-week

If a text-formatted datetime contains elements from more than one of these three principal formats then:

1. at least one of them must be unambiguous;
2. when more than one of them is unambiguous, the date is determined from the most precise one;
3. all element values must be consistent with the date so deduced.

Elided elements of a year, month, day-of-month date are all (including the year) implicitly `1`. Elided elements of times are all implicitly `0`.

Some combinations of variable-length substitutions can make particular texts impossible to parse unambiguously. For example, the pattern `MD` (1 to 2 digits of month immediately followed by 1 to 2 digits of day-of-month) formats both 3 December and 23 January as `123`, so the text `123` cannot be matched against `MD` and an error is signalled. Whether such an ambiguity actually arises depends on the text being parsed: the text `1231` can only mean 31 December and is matched without error. Where two or more variable-length numeric or alphanumeric substitutions are adjacent, place literal text between them that cannot be confused with the substitution text to avoid such ambiguities.

### Consistency

The formatted text is parsed and used to compute a datetime according to the given pattern, and must precisely match the text that would be produced if the resulting datetime were formatted using that same pattern. That is:

- The formatted text must contain valid substitution text where a format sequence appears in the pattern — for example, a full month name where `Mmmm` appears in the pattern.
- All other characters, including spaces and literal characters, must exactly match the pattern.
- All characters must be in the correct case.
- The elements in the formatted text must be consistent with one another. If the pattern contains the same element (or variations of the same element) more than once, they must have the same value in each case. Elements which are not independent must not be contradictory — for example, the text `Mon 5 Feb 2025` superficially appears to match the pattern `Ddd D Mmm YYYY` but is contradictory, because 5 February 2025 was a Wednesday, not a Monday.

If a pattern is rejected, or a text-formatted datetime cannot be matched against the pattern for any of the reasons above, a `DOMAIN ERROR` is signalled and an explanatory message is included.

## Variant options

`⎕DT` supports the `Language` and `Dictionary` variant options, specified using the [variant operator `⍠`](../primitive-operators/variant.md). Both apply only when <code>X<sub>Y</sub></code> and/or <code>X<sub>R</sub></code> are patterns.

### Language variant option

The `Language` variant option specifies the language used for formatting and matching datetimes and defaults to `'en'` (English). A language is named by a two or five character value (for example `'en'` or `'en_GB'`). The option value can be:

- a single character vector, which applies to whichever of <code>X<sub>Y</sub></code> and/or <code>X<sub>R</sub></code> are patterns; or
- a 2-element vector of two character vectors, which apply to <code>X<sub>Y</sub></code> and <code>X<sub>R</sub></code> respectively (each is used only if the corresponding value is a pattern).

The setting can be explicitly overridden within a format pattern using the `__xx__` specifier described under [Language](#language) above.

### Dictionary variant option

The `Dictionary` variant option specifies a namespace which contains additional or replacement names for the months etc. and/or predefined patterns, for languages and language regions. If <code>X<sub>Y</sub></code> and <code>X<sub>R</sub></code> are both patterns, the dictionary is applied to both.

At the top level there can be zero or more sub-namespaces with two or five character names, according to the rules for language and language regions. Within each of these, month names etc. are defined as follows:

| Named item | Description |
| --- | ---  |
| `MonthNames` | A twelve-element vector of character vectors containing the full names corresponding to January to December, respectively. |
| `ShortMonthNames` | A twelve-element vector of character vectors containing the short names corresponding to Jan to Dec, respectively. |
| `WeekdayNames` | A seven-element vector of character vectors containing the full names corresponding to Monday to Sunday, respectively. |
| `ShortWeekdayNames` | A seven-element vector of character vectors containing the full names corresponding to Mon to Sun, respectively. |
| `MorningAfternoon` | A two-element vector of character vectors containing the names corresponding to AM and PM, respectively. |
| `Ordinals` | A character vector containing the one ordinal used for all numbers in the range 1 to 31, or a thirty one-element vector of character vectors containing the ordinals for 1 to 31, respectively. |

Also at the top level of the dictionary namespace there can be a sub-namespace named `Patterns` and, within this, further sub-namespaces named `Global` and/or two or five character language names, containing definitions of predefined patterns. Predefined patterns are defined in the same way as the formatting pattern except that they must not contain references to other predefined patterns.

If the namespace contains a definition which is supplied built into the interpreter, it replaces the built-in one.

If a dictionary is incomplete (for example, is missing one of the expected named items, or one of the named items contains too few elements) an error is signalled only if the missing content would actually be needed.

See the [Dictionary](#dictionary) example below.

## Examples

### Dictionary { .example }

The following creates a dictionary defined by the namespace `dict`. See the [formatting examples](#formatting-datetimes) below for uses of this dictionary.

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

Note the following:

- In the example, the predefined pattern `ISOweek` is defined globally and is not redefined. It therefore has the same
  value for all languages. Similarly, `DateCompact` has the same value for all languages, but although the definition is
  global, it contains the pattern `MMM` and this will be substituted with the month name in the selected language.
- The predefined patterns `DateVerbose` is defined globally, and redefined for languages `fr` and `en_US`. The global
  definition will be used when any language other than `fr` and `en_US` is selected. If there was no global definition
  it would only be defined for `fr`, all regional variations of `fr`, and `en_US`.
- There is no explicit definition of patterns or names for language region `en_GB`. If this language is selected the
  definitions for `en` will be used.
- There is an explicit definition for `ShortMonthNames` for language region `en_US`. If this language is selected the
  definition of `ShortMonthNames` is as defined, and as for `en` for other names. As `en` is not defined in the
  dictionary, the built-in defaults are used.

### Timestamp to time number { .example }
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

### Time number to timestamp { .example }
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

### Time number to time number { .example }
```apl
      2 1 ⎕DT 3⊃⎕FRDCI 1 1
43886.48188
      1 ⎕DT 'J'
43886.48371
      ⍝ Local time is UTC-05:00
      3600÷⍨-/20 ⎕DT 'JZ'
¯5
```

### Timestamp to timestamp { .example }
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

### Formatting datetimes { .example }
```apl
      dt←1 ⎕DT ⊂2019 2 13 10 16 56
      dt
43508.42843
      'Dddd, DDoo Mmmm YYYY; hh:mm:ss' ⎕DT dt
┌───────────────────────────────────────┐
│Wednesday, 13th February 2019; 10:16:56│
└───────────────────────────────────────┘
      '__en__Dddd, DDoo Mmmm YYYY; hh:mm:ss' ⎕DT dt
┌───────────────────────────────────────┐
│Wednesday, 13th February 2019; 10:16:56│
└───────────────────────────────────────┘
      '"ISO date": %ISO%' ⎕DT dt
┌─────────────────────────────┐
│ISO date: 2019-02-13T10:16:56│
└─────────────────────────────┘
      '%DateVerbose%'(⎕DT⍠'Dictionary'dict) dt
┌───────────────────────┐
│the date is 13 Feb 2019│
└───────────────────────┘
```

### Parsing text formats { .example }
```apl
      'DD/MM/YYYY' 1 ⎕DT ⊂'13/02/2019'
43508
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

### Languages and dictionaries { .example }
```apl
      '__da__Dddd, DDoo mmmm YYYY; hh:mm:ss' ⎕DT dt
┌──────────────────────────────────┐
│Onsdag, 13. februar 2019; 10:16:56│
└──────────────────────────────────┘
      fmt←'Dddd, DDoo mmmm YYYY; hh:mm:ss'
      fmt(⎕DT⍠'Language' 'da') dt
┌──────────────────────────────────┐
│Onsdag, 13. februar 2019; 10:16:56│
└──────────────────────────────────┘
      '%DateVerbose%'(⎕DT⍠('Dictionary' dict)('Language' 'en_US')) dt
┌─────────────────────────┐
│the date is Feb. 13, 2019│
└─────────────────────────┘
      '__cy__Dddd, DDoo mmmm YYYY; hh:mm:ss'(⎕DT⍠'Dictionary' dict) dt
┌──────────────────────────────────────────┐
│Dydd Mercher, 13eg chwefror 2019; 10:16:56│
└──────────────────────────────────────────┘
      '__cy__%DateVerbose%'(⎕DT⍠'Dictionary' dict) dt
┌───────────────────────┐
│the date is 13 Chw 2019│
└───────────────────────┘
```

### Validation { .example }
```apl
      0 ⎕DT ⎕TS (2020 13 1) 'J' 'DT' #
1 0 1 0 0

      ¯30 0 ⎕DT⊂32000 15 10 0
1

      'DD/MM/YYYY' 0 ⎕DT '13/02/2019' '31/02/2019'
1 0

      'YYYY-MM-DD' 0 ⎕DT '1900-02-29' '2000-02-29'
0 1
```

[^1]: In the Proleptic Gregorian Calendar.
[^2]: There are the same number of ticks per day regardless of leap seconds.
[^3]: Generated as DECF values regardless of the setting of ⎕FR due to their magnitude.
[^4]: Excel supports two time number conventions. On Windows the 1900 Date System is the default and on macOS the 1904 Date System is the default. Both systems can use either convention and the convention in use is stored in the worksheet so that the platforms interoperate.
[^5]: Count includes the invalid date 1900-02-29.
[^6]: Microsoft Excel converts day 0 to the invalid date 1900-01-00.
[^7]: For negative numbers, the integral part counts backward from 1899-12-30 and the fractional part counts forward from  the date so reached.
[^8]: No date-time can represent a date earlier than ¯4713-01-01 00:00.
[^9]: Decimal encoded formats encode human-readable dates and times into a single number with the most significant part in the most significant decimal digit, for example 2020/01/23 (year/month/day) is encoded as 20200123, and 13:17:56 (hour:minute:second) is encoded as 131756. The date must be between 1 January 0001 and 31 December 9999 in the Proleptic Gregorian Calendar.
[^10]: For negative numbers, the integral part counts backward from 1899-12-30 and the fractional part counts forward from the date so reached.
[^11]: All dates must be between 1 January 0001 and 28 February 4000 in the Proleptic Gregorian Calendar.
[^12]: Decimal encoded formats encode human-readable dates and times into a single number with the most significant part in the most significant decimal digit, for example 2020/01/23 (year/month/day) is encoded as 20200123, and 13:17:56 (hour:minute:second) is encoded as 131756.
[^13]: If a timestamp has fewer than the maximum number of elements, the remaining elements take the default values shown.
[^14]: Natural sentence case, which can be specified for `M` (month name) and `d` (day name) only, causes the text to be substituted in the case which is natural for the language; some languages (for example, English) always capitalise the first letter of day and month names whereas others (for example, French) do not.
[^15]: Dates at the start of the year can be in the final week of the previous year, and dates at the end of the year can be in the first week of the following year.
[^16]: An ordinal indicator is a character or group of characters following a numeral, such as (in English) the suffixes -st, -nd, -rd, -th as in 1st, 2nd, 3rd, 4th.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DT DT 1200⌶
</div>
