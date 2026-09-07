---
search:
  boost: 2
---

# <span>Format Date-time</span> `R←X(1200⌶)Y`{{key}}

!!! Info "Information"
    `1200⌶` has been deprecated and is scheduled for removal in a future release; its functionality can instead be achieved using [`⎕DT`](../../system-functions/dt.md). For information on how to identify uses of `1200⌶` in your existing codebase, see the [Release Notes](../../..//release-notes/announcements/deprecated-functionality/#identifying-deprecated-functionality-in-executed-code).


`Y` is a numeric array of any shape, where every element contains a Dyalog Date Number that represents a date between 1
January 0001 and 31 December 9999 in the [Proleptic Gregorian Calendar](https://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar).

`X` is a character scalar or vector specifying a pattern with which the elements in `Y` should be formatted.

`R` is an array of the same shape as `Y`, whose elements are enclosed character vectors.

## Formatting Pattern in `X`

The formatting pattern allows a time number to be converted to a highly user-configurable, plain text format. When a
time number is formatted, elements in the result are copies of the format pattern with format sequences replaced by the
elements they represent.

The format sequences are intended to be visually reminiscent of the generated text. They use alphabetic characters
easily associated with the substitution (e.g. `D`, `M` and `Y` for Day, Month and Year respectively) repeated one or
more times to indicate format. As noted below, some sequences allow the first character to be replaced by a `_`, or the casing to be altered.

| Format letter | Length | Meaning | Variations | Example |
|---|---|---|---|---|
| <u>Y</u>ear | `YY` | Without century | `YY` | `19` |
|_   _| `YYYY` | With century | `YYYY` | `2019` |
| <u>M</u>onth | `M` | 1 or 2 digit numeric | `M` | `3` |
| | `MM` | 2 character numeric | `MM`<br>`_M` | `03`<br>` 3` |
| | `MMM` | Abbreviated name | `MMM`<br>`Mmm`<br>`mmm`<br>`_mm`[^1] | `MAR`<br>`Mar`<br>`mar`<br>`Mar` |
|_   _| `MMMM` | Full name | `MMMM`<br>`Mmmm`<br>`mmmm`<br>`_mmm`[^1] | `MARCH`<br>`March`<br>`march`<br>`March` |
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
| | `ddd` | Abbreviated name | `DDD`<br>`Ddd`<br>`ddd`<br>`_dd`[^1] | `MON`<br>`Mon`<br>`mon`<br>`Mon` |
|_   _| `dddd` | Full name | `DDDD`<br>`Dddd`<br>`dddd`<br>`_ddd`[^1] | `MONDAY`<br>`Monday`<br>`monday`<br>`Monday` |
| ISO <u>w</u>eek number | `w` | 1 or 2 digit numeric | `w` | `10` |
|_   _| `ww` | 2 character numeric | `ww`<br>`_w` | `10`<br>`10` |
| year of ISO <u>W</u>eek number[^2] | `WW` | Without century | `WW` | `19` |
|_   _| `WWWW` | With century | `WWWW` | `2019` |
| day of <u>y</u>ear | `y` | 1 to 3 digit numeric | `y` | `63` |
|_   _| `yy` | 3 character numeric | `yy`<br>`_y` | `063`<br>` 63` |
| <u>O</u>rdinal indicator[^3] for day of month | `O` | Short | `O`<br>`o` | `T`<br>`t` |
|_   _| `OO` | Full | `OO`<br>`Oo`<br>`oo` | `TH`<br>`Th`<br>`th` |
| hours in <u>t</u>welve hour clock | `t` | 1 or 2 digit numeric | `t` | `8` |
|_   _| `tt` | 2 character numeric | `tt`<br>`_t` | `08`<br>` 8` |
| AM/<u>P</u>M Indicator | `P` | Short | `P`<br>`p` | `A`<br>`a` |
|_   _| `PP` | Full | `PP`<br>`pp` | `AM`<br>`am` |

[^1]: Natural sentence case, which can be specified for `M` (month name) and `d` (day name) only, causes the text to be substituted in the case which is natural for the language; some languages (for example, English) always capitalise the first letter of day and month names whereas others (for example, French) do not.
[^2]: Dates at the start of the year can be in the final week of the previous year, and dates at the end of the year can be in the first week of the following year.
[^3]: An ordinal indicator is a character or group of characters following a numeral, such as (in English) the suffixes -st, -nd, -rd, -th as in 1st, 2nd, 3rd, 4th.

The upper and lower case letters, underscore `_`, dollar `$` and percent `%` are all reserved for introducing format
sequences, even though not all currently have meaning. The remaining, non-reserved, characters are copied to the result
unchanged, thus the format string `hh:mm` represents the hour of the day and minute of the hour with a colon between (
e.g. `12:00`). All characters or sequences of characters may be delimited by `"` or `'` at any point in the format
string to prevent them being interpreted as a part of a format sequence, and, within these delimiters, two adjacent
delimiter characters produce a single delimiter.

Note: The characters `AaaaBbbb` consist of two adjacent format sequences because there is a sequence of As followed by a
sequence of Bs. The characters `AaaaAaaa` consist of one format sequence because it only contains `A`s. It can be
separated into two format sequences by insering an empty `"` or `'` - delimited string, e.g. `Aaaa""Aaaa`.

## Language

Unless overridden, English is used for text substitutions. Different languages may be selected using the Language
variant option and/or the use of language specifiers within the format pattern. In either case, the language is
specified as either a two letter ISO 639-1 language code in lower case (e.g. en) or as a five character language with an
additional underscore and two character region in upper case (e.g. en_GB). Within the format pattern, __xx__ (where xx
is the two or five character specifier) will switch the language of the subsequent generated text. Dictionaries for the
following languages are built in:

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

Any pattern can contain (in part or in whole) a named predefined pattern, which allows common date and time formats to
be specified in abbreviated form. Predefined patterns may be specified on a per-language basis, allowing patterns to be
tailored for the selected language.

Predefined patterns are included in a pattern using `%` delimiters. For example, `%ISO%` includes the named predefined
pattern `ISO`.

The following global predefined pattern is built in:

| Name                                                      | Substitutes as |
|-----------------------------------------------------------| ---  |
| ISO  | YYYY-MM-DD"T"hh:mm:ss |

This list may be expanded in future.

Additional predefined patterns may be defined using the Dictionary variant option. Predefined patterns must not contain
references to other predefined patterns.

## Variant Options

The Language variant option specifies the language used for formatting datetimes and defaults to `'en'` (English). The
option value is a two or five character name (e.g. `'en'` or `'en_GB'`). The setting may be explicitly overridden in the
format pattern.

The Dictionary variant option specifies a namespace which contains additional or replacement names for the months etc.
and/or predefined patterns, for languages and language regions.

At the top level there may be zero or more sub-namespaces with two or five character names, according to the rules for
language and language regions. Within each of these, month names etc. are defined as follows:

| Named item | Description |
| --- | ---  |
| MonthNames | A twelve-element vector of character vectors containing the full names corresponding to January to December, respectively. |
| ShortMonthNames | A twelve-element vector of character vectors containing the short names corresponding to Jan to Dec, respectively. |
| WeekdayNames | A seven-element vector of character vectors containing the full names corresponding to Monday to Sunday, respectively. |
| ShortWeekdayNames | A seven-element vector of character vectors containing the full names corresponding to Mon to Sun, respectively. |
| MorningAfternoon | A two-element vector of character vectors containing the names corresponding to AM and PM, respectively. |
| Ordinals | A character vector containing the one ordinal used for all numbers in the range 1 to 31, or a thirty one-element vector of character vectors containing the ordinals for 1 to 31, respectively. |

Also at the top level of the dictionary namespace there may be a sub-namespace named Patterns and within this further
sub-namespaces named `Global` and/or two or five character language names, containing definitions of predefined
patterns. Predefined patterns are defined in the same way as the formatting pattern except that they may not contain
references to other predefined patterns.

If the namespace contains a definition which is supplied built into the interpreter, it replaces the built-in one.

If a dictionary is incomplete (e.g. is missing one of the expected named items, or one of the named items contains too
few elements) an error is signalled only if the missing content would actually be needed.

## Example dictionary

The following creates a dictionary defined by the namespace `dict`. See the formatting examples below
for uses of this dictionary.

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

## Note the following

- In the example, the predefined pattern `ISOweek` is defined globally and is not redefined. It therefore has the same
  value for all languages. Similarly, `DateCompact` has the same value for all languages, but although the definition is
  global, it contains the pattern `MMM` and this will be substituted with the month name in the selected language.
- The predefined patterns `DateVerbose` is defined globally, and redefined for languages `fr` and `en_US`. The global
  definition will be used when any language other than `fr` and `en_US` is selected. If there was not global definition
  it would only be defined for `fr`, all regional variations of `fr`, and `en_US`.
- There is no explicit definition of patterns or names for language region `en_GB`. If this language is selected the
  definitions for `en` will be used.
- There is an explicit definition for `ShortMonthNames` for language region `en_US`. If this language is selected the
  definition of `ShortMonthNames` is as defined, and as for `en` for other names. As `en` is not defined in the
  dictionary, the built-in defaults are used.

In the following examples:

```apl
      tn←1 ⎕DT ⊂2019 2 13 10 16 56
      tn
43508.42843

```

## English

```apl
      'Dddd, DDoo Mmmm YYYY; hh:mm:ss' (1200⌶) tn
 Wednesday, 13th February 2019; 10:16:56

      '__en__Dddd, DDoo Mmmm YYYY; hh:mm:ss' (1200⌶) tn
 Wednesday, 13th February 2019; 10:16:56

      '"ISO date": %ISO%' (1200⌶) tn
 ISO date: 2019-02-13T10:16:56

      '%DateVerbose%'(1200⌶⍠'Dictionary'dict) tn
 the date is 13 Feb 2019
```

## English (US)

```apl
     fmt←'%DateVerbose%'
     fmt (1200⌶⍠('Dictionary'dict)('Language' 'en_US'))tn
 the date is Feb. 13, 2019 

```

## Danish

```apl
      '__da__Dddd, DDoo mmmm YYYY; hh:mm:ss' (1200⌶) tn
 Onsdag, 13. februar 2019; 10:16:56

      fmt←'Dddd, DDoo mmmm YYYY; hh:mm:ss'
      fmt(1200⌶⍠'Language' 'da') tn
 Onsdag, 13. februar 2019; 10:16:56 

```

## Welsh (using the dictionary defined above)

```apl
      fmt←'__cy__Dddd, DDoo mmmm YYYY; hh:mm:ss' 
      fmt (1200⌶⍠'Dictionary' dict) tn
 Dydd Mercher, 13eg chwefror 2019; 10:16:56 

      '__cy__%DateVerbose%' (1200⌶⍠'Dictionary' dict) tn
 the date is 13 Chw 2019
```

<!-- Hidden search keywords -->
<div style="display: none;">
  1200⌶
</div>
