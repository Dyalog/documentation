---
search:
  boost: 2
---

# <span>Format Array</span> `R←X ⎕FMT Y`{{key}}

This function formats numbers and text as a character matrix, according to a format specification. [Monadic `⎕FMT`](fmt-monadic.md) uses the default display of an array instead of a format specification.

<h2 class="example">Example</h2>

```apl
      'I3,F5.2' ⎕FMT 2 4⍴⍳8
  1 2.00  3 4.00
  5 6.00  7 8.00
```

## Left Argument

`X` is a simple character vector containing a [format specification](#format-specification).

## Right Argument

`Y` is one of:

- a simple array of rank 2 or less
- a scalar or vector whose items are simple arrays of rank 2 or less

Each simple array is either entirely numeric or entirely character. A complex number signals `DOMAIN ERROR`.

A simple scalar is treated as a 1-by-1 matrix, and a simple vector as a matrix with one column.

<h3 class="example">Example</h3>

A vector is formatted as a column:

```apl
      'I5' ⎕FMT 10 20 30
   10
   20
   30
```

## Result

`R` is a simple character matrix. The columns of the simple arrays in `Y` are formatted in order, from left to right, by the phrases of the format specification, also taken from left to right and reused cyclically if necessary. `R` has as many rows as the longest column in `Y`, and as many columns as the format specification produces. A column that is shorter than the longest leaves the remaining rows of its field blank.

<h3 class="example">Example</h3>

`2I4` formats the vector and the first column of the matrix, and `F7.1` the second column of the matrix:

```apl
      '2I4,F7.1' ⎕FMT (⍳4)(2 2⍴0.1×⍳4)
   1   0    0.2
   2   0    0.4
   3
   4
```

## Format Specification

The format specification is a series of phrases, separated by single commas (`,`). Each phrase is one of the following:

|Phrase|Format|
|------|------|
|`rAw`|[Alphanumeric](#alphanumeric-format)|
|`rEw.s`|[Scaled](#numeric-formats)|
|`rqFw.d`|[Decimal](#numeric-formats)|
|`rqG⍞pattern⍞`|[Pattern](#pattern-format)|
|`rqIw`|[Integer](#numeric-formats)|
|`Tn`|[Absolute tabulation](#tabulation)|
|`Xn`|[Relative tabulation](#tabulation)|
|`⍞t⍞`|[Text insertion](#text-insertion)|

where:

|Parameter|Meaning|
|---------|-------|
|`r`|An optional repetition factor: the phrase is applied to `r` columns of `Y`|
|`q`|Optional [qualifiers](#qualifiers) and [affixtures](#affixtures)|
|`w`|The total width of the field for each column, including any affixtures|
|`s`|The number of significant digits in Scaled format, which must be less than `w-1`|
|`d`|The number of decimal places in Decimal format|
|`n`|A position at which the next phrase starts, counted from the left margin (`T`) or from the end of the previous phrase (`X`)|
|`t`|Any text that does not contain the delimiting characters|
|`pattern`|A [pattern](#pattern-format)|

The delimiters `⍞⍞` around text and patterns can be replaced by any of the pairs `<>`, `⊂⊃`, `⎕⎕`, and `¨¨`.

Phrases, qualifiers, and affixtures are case-sensitive, and must be in upper case.

### Repetition and Grouping

One or more phrases can be enclosed in parentheses, preceded by an optional repetition factor. The phrases within the parentheses are reused that number of times before the next phrase is used. A Text Insertion phrase is not reused if the last data phrase is followed by a closing parenthesis.

<h4 class="example">Example</h4>

```apl
      'I2,2(</>,ZI2)' ⎕FMT 1 3⍴⌽100|1989 7 20
20/07/89
```

## Numeric Formats

The Integer (`I`), Decimal (`F`), and Scaled (`E`) phrases format numbers, as integers, with `d` decimal places, and in scaled form with `s` significant digits, respectively. A result that is too wide for its field fills the field with asterisks.

<h3 class="example">Examples</h3>

```apl
      'F5.2' ⎕FMT 0.1×5 1000 ¯100
 0.50
*****
*****
      'E10.3' ⎕FMT 12345.678 0.000123 ¯5
 1.23E4
 1.23E¯4
¯5.00E0
```

If the number of digits specified exceeds the internal precision, the low-order digits are replaced by `_`:

```apl
      'F20.1' ⎕FMT 1E18÷3
3333333333333333__._
```

## Alphanumeric Format

The Alphanumeric (`A`) phrase formats characters, right-justified in the field unless the [`L` qualifier](#qualifiers) is specified.

<h3 class="example">Example</h3>

```apl
      'A2' ⎕FMT 1 6⍴'SPACED'
 S P A C E D
```

## Pattern Format

The Pattern (`G`) phrase formats a number according to a pattern, which is an arbitrary string of characters, excluding the delimiters. The characters `9` and `Z` (unless altered by the [`S` qualifier](#qualifiers)) are special, and are known as _digit selectors_. Only the `B`, `K`, `S`, and `O` qualifiers can be used with the `G` phrase.

The result has the same length as the pattern. The number is rounded to the nearest integer, after any scaling, and each digit replaces one digit selector. If there are fewer digits than digit selectors, the digits are padded with leading zeros; if there are more, the field is filled with asterisks.

- A `9` digit selector is replaced by the digit.
- A `Z` digit selector is replaced by a non-zero digit. A zero digit appears only if there are digits on both sides of it; otherwise, a blank appears.

Similarly, text between digit selectors appears only if there are digits on both sides of it. Text before the first digit selector or after the last always appears.

<h3 class="example">Examples</h3>

```apl
      'G⊂99/99/99⊃'⎕FMT 0 100 100 ⊥8 7 89
08/07/89
      'G⊂ZZ/ZZ/ZZ⊃'⎕FMT 80789 + 0 1
 8/07/89
 8/07/9
      'G⊂Andy ZZ Pauline ZZ⊃' ⎕FMT 2721.499 2699.5
Andy 27 Pauline 21
Andy 27
      ⍴⎕←'K2G⊂DM Z.ZZZ.ZZ9,99⊃' ⎕FMT 1234567.89 1234.56
DM 1.234.567,89
DM     1.234,56
2 15
```

## Tabulation

Relative tabulation (`X`) makes the next phrase start `n` positions after the end of the previous phrase, or after the left margin if there is none. `n` can be negative, provided that the next phrase does not start before the left margin. Blanks are inserted where necessary.

<h3 class="example">Example</h3>

```apl
      'I2,X3,3A1' ⎕FMT (⍳3)(2 3⍴'TOPCAT')
 1   TOP
 2   CAT
 3
```

Absolute tabulation (`T`) makes the next phrase start at position `n`, counted from the left margin. `T0` starts it at the next free position. Blanks are inserted where necessary, and a position that is formatted more than once contains the most recently formatted column.

<h3 class="example">Example</h3>

```apl
      X←'6I1,T5,A1,T1,3A1,T7,F5.1'
      X ⎕FMT (1 6⍴⍳6)('*')(1 3⍴'ABC')(22.2)
ABC4*6 22.2
```

## Text Insertion

A Text Insertion phrase inserts its text in every row of the result, even when the data is exhausted.

<h3 class="example">Example</h3>

```apl
      MEN←3 5⍴'FRED BILL JAMES'
      WOMEN←2 5⍴'MARY JUNE '
      '5A1,<|>' ⎕FMT MEN WOMEN
FRED |MARY |
BILL |JUNE |
JAMES|     |
```

## Qualifiers

|Qualifier|Effect|
|---------|------|
|`B`|Leaves the field blank if the result would otherwise be zero|
|`C`|Inserts commas between triads of digits, starting from the rightmost digit of the integer part of the result|
|`Km`|Scales numbers by `1Em`, where `m` is an integer; a negative `m` is written with `¯` or `-`|
|`L`|Left-justifies the result in the field|
|`Ov⍞t⍞`|Replaces the number `v` with the text `t`, as described in [O Qualifier](#o-qualifier)|
|`S⍞p⍞`|Substitutes characters: `p` is a series of pairs, in each of which the first is a standard character and the second is the character that replaces it. The standard characters are `*` (overflow fill), `.` (decimal point), `,` (triad separator for `C`), `0` (fill for `Z`), `_` (loss of precision), and `¯` (high minus)|
|`Z`|Fills unused leading positions in the result with zeros, and with commas if `C` is also specified|

<h3 class="example">Example</h3>

```apl
      X←'F5.1,BF6.1,X1,ZF5.1,X1,LF5.1,K3CS<.,,.>F10.1'
      X ⎕FMT ⍉5 3⍴¯1.5 0 25
 ¯1.5  ¯1.5 ¯01.5 ¯1.5   ¯1.500,0
  0.0       000.0 0.0         0,0
 25.0  25.0 025.0 25.0   25.000,0
```

The `S` qualifier can replace the APL high minus (`¯`) with the ASCII minus sign (`-`), as can the [`M` affixture](#affixtures) `M<->`:

```apl
      'S<¯->F7.2' ⎕FMT 150.3 ¯50.25 0
 150.30
 -50.25
   0.00
```

### O Qualifier

The `O` qualifier replaces a specific number with text, and can be used with the `E`, `F`, `I`, and `G` phrases. It consists of the letter `O`, followed by the optional number to replace (`0` if omitted), and then the text between delimiters:

|Qualifier|Effect|
|---------|------|
|`O<nil>`|Replaces `0` with the text `nil`|
|`O42<N/A>`|Replaces `42` with the text `N/A`|
|`O0.001<1/1000>`|Replaces `0.001` with the text `1/1000`|

The text replaces the number in the field. It is right-aligned, unless the `L` qualifier is also specified. A phrase can have more than one `O` qualifier.

The comparison with the number is tolerant. This means that [`⎕CT`](ct.md) and [`⎕DCT`](dct.md) are implicit arguments of `⎕FMT` with the `O` qualifier.

<h4 class="example">Examples</h4>

```apl
      'O<NIL>F7.2'⎕FMT 12.3 0 42.5
  12.30
    NIL
  42.50
      'O<NIL>LF7.2'⎕FMT 12.3 0 42.5
12.30
NIL
42.50
      'O<NIL>O42<N/A>I6'⎕FMT 12 0 42 13
    12
   NIL
   N/A
    13
      'O99<replace>F20.2'⎕FMT 99 100 101
             replace
              100.00
              101.00
```

## Affixtures

|Affixture|Effect|
|---------|------|
|`M⍞t⍞`|Prefixes a negative result with the text `t` instead of the negative sign|
|`N⍞t⍞`|Suffixes a negative result with the text `t`|
|`P⍞t⍞`|Prefixes a positive or zero result with the text `t`|
|`Q⍞t⍞`|Suffixes a positive or zero result with the text `t`|
|`R⍞t⍞`|Presets the field with the text `t`, repeated as necessary to fill it. The parts of the field that the result fills, including the effects of other qualifiers and affixtures except `B`, replace the text|

Affixtures are included within the field; they do not extend its width. The `N` and `Q` affixtures shift the result to the left by the number of characters in their text.

<h3 class="example">Example</h3>

Negative results are enclosed in parentheses, as is common in accounting:

```apl
      'M<(>N<)>Q< >F9.2' ⎕FMT 150.3 ¯50.25 0 1114.9
  150.30
  (50.25)
    0.00
 1114.90
```

## Errors

- A numeric column formatted by an `A` phrase, or a character column formatted by any other phrase, signals `DOMAIN ERROR`.
- A simple array of rank greater than 2 in `Y` signals `RANK ERROR`.
- An ill-formed format specification signals `FORMAT ERROR`. This includes an `E` phrase in which `s` is greater than `w-2`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>
