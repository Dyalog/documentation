<!-- Hidden search keywords -->
<div style="display: none;">
  1200⌶
</div>

<h1 class="heading"><span class="name">Format Date-time</span><span class="command">R←X(1200⌶)Y</span></h1>

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

<table>
    <thead>
        <tr>
            <th class="text-left">Format letter</th>
            <th class="text-left">Length</th>
            <th class="text-left">Meaning</th>
            <th class="text-left">Variations</th>
            <th class="text-left">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>Y</ins>ear</td>
            <td class="Dyalog">YY</td>
            <td>Without century</td>
            <td class="Dyalog">YY</td>
            <td class="Dyalog">19</td>
        </tr>
        <tr>
            <td class="Dyalog">YYYY</td>
            <td>With century</td>
            <td class="Dyalog">YYYY</td>
            <td class="Dyalog">2019</td>
        </tr>
        <tr>
            <td rowspan="4" style="vertical-align: middle;">
                <ins>M</ins>onth</td>
            <td class="Dyalog">M</td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">M</td>
            <td class="Dyalog">3</td>
        </tr>
        <tr>
            <td class="Dyalog">MM</td>
            <td>2 character numeric</td>
            <td class="Dyalog">MM<br />_M</td>
            <td class="Dyalog">03<br />&nbsp;3</td>
        </tr>
        <tr>
            <td class="Dyalog">MMM</td>
            <td>Abbreviated name</td>
            <td class="Dyalog">MMM<br />Mmm<br />mmm<br />_mm<sup>1</sup></td>
            <td class="Dyalog">MAR<br />Mar<br />mar<br />Mar</td>
        </tr>
        <tr>
            <td class="Dyalog">MMMM </td>
            <td>Full name </td>
            <td class="Dyalog">MMMM<br />Mmmm<br />mmmm<br />_mmm<sup>1</sup></td>
            <td class="Dyalog">MARCH<br />March<br />march<br />March</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>D</ins>ay of month</td>
            <td class="Dyalog">D</td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">D</td>
            <td class="Dyalog">4</td>
        </tr>
        <tr>
            <td class="Dyalog">DD</td>
            <td>2 character numeric</td>
            <td class="Dyalog">DD<br />_D</td>
            <td class="Dyalog">04<br />&nbsp;4</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>h</ins>ours</td>
            <td class="Dyalog">h</td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">h</td>
            <td class="Dyalog">8</td>
        </tr>
        <tr>
            <td class="Dyalog">hh</td>
            <td>2 character numeric</td>
            <td class="Dyalog">hh<br />_h</td>
            <td class="Dyalog">08<br />&nbsp;8</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>m</ins>inutes</td>
            <td class="Dyalog">m </td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">m</td>
            <td class="Dyalog">5</td>
        </tr>
        <tr>
            <td class="Dyalog">mm</td>
            <td>2 character numeric</td>
            <td class="Dyalog">mm<br />_m</td>
            <td class="Dyalog">05<br />&nbsp;5</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>s</ins>econds</td>
            <td class="Dyalog">s</td>
            <td>1 or 2 digit numeric </td>
            <td class="Dyalog">s</td>
            <td class="Dyalog">0</td>
        </tr>
        <tr>
            <td class="Dyalog">ss </td>
            <td>2 character numeric </td>
            <td class="Dyalog">ss<br />_s</td>
            <td class="Dyalog">00<br />&nbsp;0</td>
        </tr>
        <tr>
            <td rowspan="6" style="vertical-align: middle;">
                <ins>f</ins>ractional seconds</td>
            <td class="Dyalog">f</td>
            <td>1 digit precision</td>
            <td class="Dyalog">f</td>
            <td class="Dyalog">5</td>
        </tr>
        <tr>
            <td class="Dyalog">ff</td>
            <td>2 digit precision</td>
            <td class="Dyalog">ff</td>
            <td class="Dyalog">55</td>
        </tr>
        <tr>
            <td class="Dyalog">fff</td>
            <td>3 digit precision</td>
            <td class="Dyalog">fff</td>
            <td class="Dyalog">555</td>
        </tr>
        <tr>
            <td class="Dyalog">ffff</td>
            <td>4 digit precision</td>
            <td class="Dyalog">ffff</td>
            <td class="Dyalog">5555</td>
        </tr>
        <tr>
            <td class="Dyalog">fffff</td>
            <td>5 digit precision</td>
            <td class="Dyalog">fffff</td>
            <td class="Dyalog">55555</td>
        </tr>
        <tr>
            <td class="Dyalog">ffffff</td>
            <td>6 digit precision</td>
            <td class="Dyalog">ffffff</td>
            <td class="Dyalog">555555</td>
        </tr>
        <tr>
            <td rowspan="3" style="vertical-align: middle;">
                <ins>d</ins>ay of week</td>
            <td class="Dyalog">d </td>
            <td>Numeric (1-7)</td>
            <td class="Dyalog">d</td>
            <td class="Dyalog">1</td>
        </tr>
        <tr>
            <td class="Dyalog">ddd</td>
            <td>Abbreviated name</td>
            <td class="Dyalog">DDD<br />Ddd<br />ddd<br />_dd<sup>1</sup></td>
            <td class="Dyalog">MON<br />Mon<br />mon<br />Mon</td>
        </tr>
        <tr>
            <td class="Dyalog">dddd</td>
            <td>Full name</td>
            <td class="Dyalog">DDDD<br />Dddd<br />dddd<br />_ddd<sup>1</sup></td>
            <td class="Dyalog">MONDAY<br />Monday<br />monday<br />Monday</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">ISO <ins>w</ins>eek number</td>
            <td class="Dyalog">w</td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">w</td>
            <td class="Dyalog">10</td>
        </tr>
        <tr>
            <td class="Dyalog">ww</td>
            <td>2 character numeric</td>
            <td class="Dyalog">ww<br />_w</td>
            <td class="Dyalog">10<br />10</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">year of ISO<br /><ins>W</ins>eek<br />number<sup>2</sup></td>
            <td class="Dyalog">WW</td>
            <td>Without century</td>
            <td class="Dyalog">WW</td>
            <td class="Dyalog">19</td>
        </tr>
        <tr>
            <td class="Dyalog">WWWW</td>
            <td>With century</td>
            <td class="Dyalog">WWWW</td>
            <td class="Dyalog">2019</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">day of <ins>y</ins>ear</td>
            <td class="Dyalog">y</td>
            <td>1 to 3 digit numeric</td>
            <td class="Dyalog">y</td>
            <td class="Dyalog">63</td>
        </tr>
        <tr>
            <td class="Dyalog">yy</td>
            <td>3 character numeric</td>
            <td class="Dyalog">yy<br />_y</td>
            <td class="Dyalog">063<br />&nbsp;63</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">
                <ins>O</ins>rdinal indicator<sup>3</sup><br />for day of month</td>
            <td class="Dyalog">O</td>
            <td>Short</td>
            <td class="Dyalog">O<br />o</td>
            <td class="Dyalog">T<br />t</td>
        </tr>
        <tr>
            <td class="Dyalog">OO</td>
            <td>Full</td>
            <td class="Dyalog">OO<br />Oo<br />oo</td>
            <td class="Dyalog">TH<br />Th<br />th</td>
        </tr>
        <tr>
            <td rowspan="2" style="vertical-align: middle;">hours in <ins>t</ins>welve<br />hour clock</td>
            <td class="Dyalog">t</td>
            <td>1 or 2 digit numeric</td>
            <td class="Dyalog">t</td>
            <td class="Dyalog">8</td>
        </tr>
        <tr>
            <td class="Dyalog">tt</td>
            <td>2 character numeric</td>
            <td class="Dyalog">tt<br />_t</td>
            <td class="Dyalog">08<br />&nbsp;8</td>
        </tr>
        <tr>
            <td rowspan="2">AM/<ins>P</ins>M Indicator</td>
            <td class="Dyalog">P</td>
            <td>Short</td>
            <td class="Dyalog">P<br />p</td>
            <td class="Dyalog">A<br />a</td>
        </tr>
        <tr>
            <td class="Dyalog">PP</td>
            <td>Full</td>
            <td class="Dyalog">PP<br />pp</td>
            <td class="Dyalog">AM<br />am<br /></td>
        </tr>
    </tbody>
</table>

**Footnotes**

1. Natural sentence case, which may be specified for M(month name) and d(day
name) only, causes the text to be substituted in the case which is natural for
the language; some languages (for example, English) always capitalise the
first letter of day and month names whereas others (for example, French) do
not.
2. Dates at the start of the year may be in the final week of the previous year,
and dates at the end of the year may be in the first week of the following year.
3. An ordinal indicator is a character or group of characters following a numeral,
such as (in English) the suffixes -st, -nd, -rd, -th as in 1st, 2nd, 3rd, 4th.

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

The following creates a dictionary defined by the namespace `dict` using JSON text. See the formatting examples below
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
