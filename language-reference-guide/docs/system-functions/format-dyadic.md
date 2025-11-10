<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>

<h1 class="heading"><span class="name">Format (Dyadic)</span> <span class="command">R←X ⎕FMT Y</span></h1>

`Y` must be a simple array of rank not exceeding two, or a non-simple scalar or vector whose items are simple arrays of rank not exceeding two.  The simple arrays in `Y` must be homogeneous, either character or numeric. All numeric values in `Y` must be simple; if `Y` contains any complex numbers, dyadic `⎕FMT` will generate a `DOMAIN ERROR`. `X` must be a simple character vector.  `R` is a simple character matrix.

`X` is a format specification that defines how columns of the simple arrays in `Y` are to appear.  A simple scalar in `Y` is treated as a one-element matrix.  A simple vector in `Y` is treated as a one-column matrix.  Each column of the simple arrays in `Y` is formatted in left-to-right order according to the format specification in `X` taken in left-to-right order and used cyclically if necessary.

`R` has the same number of rows as the longest column (or implied column) in `Y`, and the number of columns is determined from the format specification.

The **format specification** consists of a series of control phrases, with adjacent phrases separated by a single comma, selected from the following:

|--------------|-------------------|
|`rAw`         |Alphanumeric format|
|`rEw.s`       |Scaled format      |
|`rqFw.d`      |Decimal format     |
|`rqG⍞pattern⍞`|Pattern            |
|`rqIw`        |Integer format     |
|`Tn`          |Absolute tabulation|
|`Xn`          |Relative tabulation|
|`⍞t⍞`         |Text insertion     |


(Alternative surrounding pairs for Pattern or Text insertion are   `< >, ⊂ ⊃, ⎕ ⎕`  or `¨ ¨`.)

**where**

|---|---|
|`r`|is an optional repetition factor indicating that the format phrase is to be applied to r columns of `Y`|
|`q`|is an optional usage of qualifiers or affixtures from those described below.|
|`w`|is an integer value specifying the total field width per column of `Y` , including any affixtures.|
|`s`|is an integer value specifying the number of significant digits in Scaled format; `s` must be less than `w-1`|
|`d`|is an integer value specifying the number of places of decimal in Decimal format; `d` must be less than `w` .|
|`n`|is an integer value specifying a tab position relative to the notional left margin (for `T` -format) or relative to the last formatted position (for `X` -format) at which to begin the next format.|
|`t`|is any arbitrary text excluding the surrounding character pair.  Double quotes imply a single quote in the result.|
|`pattern`|see following section **G format**|



**Qualifiers q are as follows**


|---|---|
|`B`|leaves the field blank if the result would otherwise be zero.|
|`C`|inserts commas between triads of digits starting from the rightmost digit of the integer part of the result.|
|`Km`|scales numeric values by `1Em` where m is an integer; negation may be indicated by `¯` or - preceding the number.|
|`L`|left justifies the result in the field width.|
|`Ov⍞t⍞`|replaces specific numeric value `v` with the text `t` .|
|`S⍞p⍞`|substitutes standard characters. `p` is a string of pairs of symbols enclosed between any of the Text Insertion delimiters; the first of each pair is the standard symbol, and the second is the symbol to be substituted. Standard symbols are:<br>`*` overflow fill character<br>`.` decimal point<br>`,` triad separator for `C` qualifier<br>`0` fill character for `Z` qualifier<br>`_` loss of precision character<br>`¯` high minus symbol|
|`Z`|fills unused leading positions in the result with zeros (and commas if `C` is also specified).|
|`9`|digit selector|


**Affixtures are as follows**


|---|---|
|`M⍞t⍞`|prefixes negative results with the text t instead of the negative sign.|
|`N⍞t⍞`|post-fixes negative results with the text `t`|
|`P⍞t⍞`|prefixes positive or zero results with the text `t` .|
|`Q⍞t⍞`|post-fixes positive or zero results with the text `t` .|
|`R⍞t⍞`|presets the field with the text `t` which is repeated as necessary to fill the field.  The text will be replaced in parts of the field filled by the result, including the effects of other qualifiers and affixtures except the `B` qualifier|

The surrounding affixture delimiters may be replaced by the alternative pairs described for Text Insertion.

<h2 class="example">Examples</h2>

A vector is treated as a column:
```apl
      'I5' ⎕FMT 10 20 30
   10
   20
   30
```

The format specification is used cyclically to format the columns of the right argument:
```apl
      'I3,F5.2' ⎕FMT 2 4⍴⍳8
  1 2.00  3 4.00
  5 6.00  7 8.00
```

The columns of the separate arrays in the items of a non-simple right argument are formatted in order.  Rows in a formatted column beyond the length of the column are left blank:
```apl
      '2I4,F7.1' ⎕FMT (⍳4)(2 2⍴ 0.1×⍳4)
   1   0    0.2
   1   0    0.4
   3
   4
```

Characters are right justified within the specified field width, unless the `L` qualifier is specified:
```apl
      'A2' ⎕FMT 1 6⍴'SPACED'
 S P A C E D
```

If the result is too wide to fit within the specified width, the field is filled with asterisks:
```apl
      'F5.2' ⎕FMT 0.1×5 1000 ¯100
  0.50
*****
*****
```

Relative tabulation (`X`-format) identifies the starting position for the next format phrase relative to the finishing position for the previous format, or the notional left margin if none.  Negative values are permitted providing that the starting position is not brought back beyond the left margin.  Blanks are inserted in the result, if necessary:
```apl
      'I2,X3,3A1' ⎕FMT (⍳3)(2 3⍴'TOPCAT')
 1   TOP
 2   CAT
 3
```

Absolute tabulation (`T`-format) specifies the starting position for the next format relative to the notional left margin.  If position 0 is specified, the next format starts at the next free position as viewed so far.  Blanks are inserted into the result as required.  Over-written columns in the result contain the most recently formatted array columns taken in left-to-right order:
```apl
      X←'6I1,T5,A1,T1,3A1,T7,F5.1'
 
      X ⎕FMT (1 6⍴⍳6)('*')(1 3⍴'ABC')(22.2)
ABC4*6 22.2
```

If the number of specified significant digits exceeds the internal precision, low order digits are replaced by the symbol _:
```apl
      'F20.1' ⎕FMT 1E18÷3
3333333333333333__._
```

The Text Insertion format phrase inserts the given text repeatedly in all rows of the result:
```apl
      MEN←3 5⍴'FRED BILL JAMES'
      WOMEN←2 5⍴'MARY JUNE '
 
      '5A1,<|>' ⎕FMT MEN WOMEN
FRED |MARY |
BILL |JUNE |
JAMES|     |
```

The last example also illustrates that a Text Insertion phrase is used even though the data is exhausted.

The following example illustrates effects of the various qualifiers:
```apl
      X←'F5.1,BF6.1,X1,ZF5.1,X1,LF5.1,K3CS<.,,.>F10.1'
 
      X ⎕FMT ⍉5 3⍴¯1.5 0 25
 ¯1.5  ¯1.5 ¯01.5 ¯1.5   ¯1.500,0
  0.0       000.0 0.0         0,0
 25.0  25.0 025.0 25.0   25.000,0
```

Affixtures allow text to be included within a field.  The field width is not extended by the inclusion of affixtures.  `N` and `Q` affixtures shift the result to the left by the number of characters in the text specification.  Affixtures may be used to enclose negative results in parentheses in accordance with common accounting practice:
```apl
      'M<(>N<)>Q< >F9.2' ⎕FMT 150.3 ¯50.25 0 1114.9
  150.30
  (50.25)
    0.00
 1114.90
```

One or more format phrases may be surrounded by parentheses and preceded by an optional repetition factor.  The format phrases within parentheses will be re-used the given number of times before the next format phrase is used.  A Text Insertion  phrase will not be re-used if the last data format phrase is preceded by a closing parenthesis:
```apl
      'I2,2(</>,ZI2)' ⎕FMT 1 3⍴⌽100|3↑⎕TS
20/07/89
```

## G Format

Only the `B`, `K`, `S` and `O` qualifiers are valid with the `G` option

`⍞pattern⍞` is an arbitrary string of characters, excluding the delimiter characters.  Characters '9' and '`Z`' (unless altered with the `S` qualifier) are special and are known as **digit selectors**.

The result of a `G` format will have length equal to the length of the pattern.

The data is rounded to the nearest integer (after possible scaling). Each digit of the rounded data replaces one digit selector in the result.  If there are fewer data digits than digit selectors, the data digits are padded with leading zeros.  If there are more data digits than digit selectors, the result will be filled with asterisks.

A '9' digit selector causes a data digit to be copied to the result.

A 'Z' digit selector causes a non-zero data digit to be copied to the result.  A zero data digit is copied if and only if digits appear on each side of it.  Otherwise a blank appears.  Similarly text between digit selectors appears only if digits appear on each side of the text.  Text appearing before the first digit selector or after the last will always appear in the result.

<h2 class="example">Examples</h2>
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

An error will be reported if:

- Numeric data is matched against an `A` control phrase.
- Character data is matched against other than an `A` control phrase.
- The format specification is ill-formed.
- For an F control phrase, `d>w-2`
- For an E control phrase, `s>w-2`

## O Format Qualifier

The O format qualifier replaces a specific numeric value with a text string and may be used in conjunction with the E, F, I and G format phrases.

An O-qualifier consists of the letter "O" followed by the optional numeric value which is to be substituted (if omitted, the default is 0) and then the text string within pairs of symbols such as "`<>`". For example:

|----------------|-----------------------------------------------|
|`O - qualifier` |Description                                    |
|`O<nil>`        |Replaces the value 0 with the text "nil"       |
|`O42<N/A>`      |Replaces the value 42 with the text "N/A"      |
|`O0.001<1/1000>`|Replaces the value 0.001 with the text "1/1000"|

The replacement text is inserted into the field in place of the numeric value. The text is normally right-aligned in the field, but will be left-aligned if the L qualifier is also specified.

It is permitted to specify more than one O-qualifier within a single phrase.

The O-qualifier is `⎕CT` sensitive.

<h2 class="example">Examples</h2>

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

`⎕CT` and `⎕DCT` are  implicit arguments of `⎕FMT` with the O format qualifier.
