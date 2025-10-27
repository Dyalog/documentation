<h1 class="heading"><span class="name">Display of Arrays</span></h1>

Simple scalars and vectors are displayed in a single line beginning at the left margin. A number is separated from the next adjacent element by a single space.

```apl
      3
3
      ⍳4
1 2 3 4
```

## Print Precision

The [`⎕PP`](../../../../language-reference-guide/system-functions/pp/) system variable determines the number of significant digits to be printed. The fractional part of the number is rounded in the last digit if it cannot be represented within the print precision. Leading zeros, and trailing zeros after a decimal point, are omitted, as are decimal points for integers.

```apl
      0.1 1.0 1.12
0.1 1 1.12

      'A' 2 'B' 'C'
A 2 BC

      ÷3 2 6
0.3333333333 0.5 0.1666666667
```

If a number cannot be fully represented in `⎕PP` significant digits, or if the number requires more than five leading zeros after the decimal point, it is represented in scaled form. The mantissa displays up to `⎕PP` significant digits, omitting trailing zeros.

```apl
      ⎕PP←3

      123 1234 12345 0.12345 0.00012345 0.00000012345
123 1.23E3 1.23E4 0.123 0.000123 1.23E¯7
```

## Simple Matrices

Simple matrices are displayed in rectangular form, with one line for each matrix row.

```apl
      2 4⍴'HANDFIST'
HAND
FIST

      1 2 3 ∘.× 6 2 5
 6 2  5
12 4 10
18 6 15
```

All elements in a column are displayed in the same format, but the format and width for the column is determined independently of other columns.

A column is treated as numeric if it contains any numeric elements.
Numeric columns are right-justified; others are left-justified.
Numeric columns are separated from their neighbours by a single column of blanks.

A numeric column aligns any decimal points or E characters (for scaled formats), adding trailing zeros to the mantissae if necessary. Integers are right-adjusted one place to the left of any decimal points.
```apl
      2 3⍴2 4 6.1 8 10.24 12
2  4     6.1
8 10.24 12

      2 4⍴4 'A' 'B' 5 ¯0.000000003 'C' 'D' 123.56
 4E0  AB   5
¯3E¯9 CD 123.56
```

## Non-simple Arrays

In the display of non-simple arrays, each element is displayed within a rectangle such that the rows and columns of the array are aligned.  Simple items within the array are displayed as above.  For non-simple items, this rule is applied recursively, with one space added on each side of the enclosed element for each level of nesting.

```apl
      ⍳3
1 2 3

      ⊂⍳3
 1 2 3

      ⊂⊂⍳3
  1 2 3

      ('ONE' 1) ('TWO' 2) ('THREE' 3) ('FOUR' 4)
  ONE  1   TWO  2   THREE  3   FOUR  4

      ['ONE' 1 'TWO' 2 ⋄ 'THREE' 3 'FOUR' 4]
 ONE    1  TWO   2
 THREE  3  FOUR  4
```

## Multi-dimensional Arrays

Multi-dimensional arrays are displayed in rectangular planes.  Planes are separated by one blank line, and hyper-planes of higher dimensions are separated by increasing numbers of blank lines.  In all other respects, multi-dimensional arrays are displayed in the same manner as matrices.

```apl
      2 3 4⍴⍳24
 1  2  3  4
 5  6  7  8
 9 10 11 12

13 14 15 16
17 18 19 20
21 22 23 24

      3 1 1 3⍴'THEREDFOX'
THE


RED


FOX
```

The power of this form of display is made apparent when formatting informal reports.

```apl
      AREAS←'West' 'Central' 'East'
      PRODUCTS←'Biscuits' 'Cakes' 'Buns' 'Rolls'

      SALES←[
        50  5.25   75
       250 20.15  900
       500 80.98  650
      1000 90.03 1200
      ]

      ' ' PRODUCTS ⍪., AREAS SALES
            West  Central  East
 Biscuits     50     5.25    75
 Cakes       250    20.15   900
 Buns        500    80.98   650
 Rolls      1000    90.03  1200
```

## Array Notation

Arrays (including namespaces) can be displayed in the session using [array notation](array-notation.md). This mode is enabled using the `]APLAN.Output` user command. For example:
```apl
      SALES
  50  5.25   75
 250 20.15  900
 500 80.98  650
1000 90.03 1200
      ]APLAN.Output ON
'Was OFF'
      SALES
[               
   50  5.25   75
  250 20.15  900
  500 80.98  650
 1000 90.03 1200
]               
```
In the [Microsoft Windows IDE](../../../../windows-ui-guide) it can also be toggled on and off using the ![](../../img/session_arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon on the Session toolbar.

To enable the display of output using array notation when starting a Dyalog session, set the [APLAN_FOR_OUTPUT](../../../../windows-installation-and-configuration-guide/configuration-parameters/aplan-for-output) configuration parameter to `1`.

## Print Width

If the display of an array is wider than the print width, as defined by the [`⎕PW`](../../../../language-reference-guide/system-functions/pw/) system variable, it will be folded at or before `⎕PW` and the folded portions indented six spaces.  The display of a simple numeric or mixed array may be folded at a width less than `⎕PW` so that individual numbers are not split across a page boundary.

```apl
      ⎕PW←40
 
      ?3 20⍴100
54 22  5 68 68 94 39 52 84  4  6 53 68
85 53 10 66 42 71 92 77 27  5 74 33 64
66  8 64 89 28 44 77 48 24 28 36 17 49
       1  39  7 42 69 49 94
      76 100 37 25 99 73 76
      90  91  7 91 51 52 32
```

## The `]Disp` User Command

The user command `]Disp` illustrates the specified array, with borders indicating sub-array shape and type. For example:

```apl
      ]Disp 'ABC' [1 2 3 4 ⋄]
┌→──┬───────┐
│ABC│1 2 3 4↓
└──→┴~─────→┘
```
```apl
      ]Disp (' ',PRODUCTS),AREAS⍪SALES ⍝ see above
┌→───────┬────┬───────┬────┐
↓        │West│Central│East│
├────────┼───→┼──────→┼───→┤
│Biscuits│ 50 │ 5.25  │ 75 │
├───────→┼~───┼~──────┼~───┤
│ Cakes  │250 │ 20.15 │900 │
├───────→┼~───┼~──────┼~───┤
│  Buns  │500 │ 80.98 │650 │
├───────→┼~───┼~──────┼~───┤
│ Rolls  │1000│ 90.03 │1200│
└───────→┴~───┴~──────┴~───┘
```
This is similar to displaying array with `]Boxing on -style=mid` (see [The `]Boxing` User Command](#boxing) below).

An explanation of the symbols that appear in the borders can be seen by running `]Disp -??`

## The `]Display` User Command

The user command `]Display` illustrates the specified array, with borders indicating array and sub-array shape and type. For example:

```apl
      ]Display 'ABC' [1 2 3 4 ⋄]
┌→────────────────┐
│ ┌→──┐ ┌→──────┐ │
│ │ABC│ ↓1 2 3 4│ │
│ └───┘ └~──────┘ │
└∊────────────────┘
```
```apl
      ]Display (' ',PRODUCTS),AREAS⍪SALES ⍝ see above
┌→───────────────────────────────────┐
↓            ┌→───┐ ┌→──────┐ ┌→───┐ │
│            │West│ │Central│ │East│ │
│ -          └────┘ └───────┘ └────┘ │
│ ┌→───────┐                         │
│ │Biscuits│ 50     5.25      75     │
│ └────────┘                         │
│ ┌→────┐                            │
│ │Cakes│    250    20.15     900    │
│ └─────┘                            │
│ ┌→───┐                             │
│ │Buns│     500    80.98     650    │
│ └────┘                             │
│ ┌→────┐                            │
│ │Rolls│    1000   90.03     1200   │
│ └─────┘                            │
└∊───────────────────────────────────┘
```
This is similar to displaying array with `]Boxing on -style=max` (see [The `]Boxing` User Command](#boxing) below).

An explanation of the symbols that appear in the borders can be seen by running `]Display -??`

## The `]Boxing` User Command { #boxing }

The user command `]Boxing` changes how nested arrays are displayed in the Session. The following examples show different settings.

```apl
      ]Boxing on -style=min
Was OFF -style=min

      'ABC' [1 2 3 4 ⋄]
┌───┬───────┐
│ABC│1 2 3 4│
└───┴───────┘

      ]Boxing on -style=mid
Was ON -style=min

      'ABC' [1 2 3 4 ⋄]
┌→──┬───────┐
│ABC│1 2 3 4↓
└──→┴~─────→┘

      ]Boxing on -style=max
┌→────────────────┐
│Was ON -style=mid│
└─────────────────┘

      'ABC' [1 2 3 4 ⋄]
┌→────────────────┐
│ ┌→──┐ ┌→──────┐ │
│ │ABC│ ↓1 2 3 4│ │
│ └───┘ └~──────┘ │
└∊────────────────┘

      ]Boxing on -style=min
Was ON -style=max
      ]Boxing off
Was ON

      'ABC' [1 2 3 4 ⋄]
 ABC  1 2 3 4
```
Information about all the options and explanation of the symbols that appear in the borders can be seen by running `]Display -??`

