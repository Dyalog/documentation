# <span>FontList</span> <span>Property</span>



**Applies To:** [Printer](../objects/printer.md), [Root](../objects/root.md)

**Description**


The FontList property is a read-only property (you cannot set its value) that
provides a list of available fonts.


Its value is a vector (1 per font) of 8-element character vectors, each of
which is as follows :


|-----|------------------------------------------|
|`[1]`|Face name (character vector)              |
|`[2]`|Character height in "points" (integer)    |
|`[3]`|Fixed width or not (Boolean)              |
|`[4]`|Italic or not (Boolean)                   |
|`[5]`|Underline or not (Boolean)                |
|`[6]`|Weight (integer)                          |
|`[7]`|Angle of rotation (integer)               |
|`[8]`|Character set (see [CharSet](charset.md) )|

<h2 class="example">Example</h2>
```apl
       ↑'.'⎕WG'FontList'
 System                         16 0 0 0 700 0   0
 Terminal                       12 1 0 0 400 0 255
 Fixedsys                       15 1 0 0 400 0   0
 Roman                          37 0 0 0 400 0 255
 Script                         36 0 0 0 400 0 255
 Modern                         37 0 0 0 400 0 255
 Small Fonts                     3 0 0 0 400 0   0
 Courier                        13 1 0 0 400 0   0
 Serif                          13 0 0 0 400 0   0
 Dyalog Alt                     16 1 0 0 400 0   0
 Dyalog Std                     16 1 0 0 400 0   0
```


Note that the list of fonts obtained from FontList for a [Printer](../objects/printer.md) object will include TrueType fonts and printer fonts but will exclude screen
fonts. FontList for [Root](../objects/root.md) will include TrueType
fonts and screen fonts, but exclude printer-only fonts. The two lists will
therefore (typically) be different.



