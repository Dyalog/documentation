---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ATX ATX
</div>

<h1 class="heading"><span class="name">Extended Attributes</span> <span class="command">R←X ⎕ATX Y</span></h1>

This function provides information about a name in a workspace, including its usage, history, restrictions, role and origin.

!!! note
    To retrieve this information for an unnamed value, wrap `⎕ATX` in a dfn and use the name `⍵`, for example `{60⎕ATX'⍵'}`

`Y` can be a simple character scalar, a simple or enclosed character vector, or a vector of character scalars and vectors  (as least one must be a character vector) of the name(s) for which information is required.

`X` can be a scalar or a vector indicating the information required:

|Group|`X`|Meaning|Default|
|---|---|---|---|
|Identity|0|Name|`''`|
|Syntax|10|Function result ( `0` : none or not a function, `1` : explicit, `¯1` : shy)|`0`|
|      |11|Function valence ( `0` : niladic, `1` : monadic, `2` : dyadic, `¯2` : ambivalent)|`0`|
|_    _|12|Operator valence: ( `0` : not an operator, `1` : monadic, `2` : dyadic)|`0`|
|Last edit|20|Author of last edit|`''`|
|         |21|Number of days passed between 1899-12-31 at 00:00 UTC and last edit (includes fractional days)|`0`|
|         |22|Local timestamp at last edit (format is the 7-item vector described by `⎕TS` . See [Timestamp](ts.md) )|`⍬`|
|_       _|23|Number of bytes required for storage without sharing|`0`|
|Restrictions|30|Source can be displayed|`¯1`|
|            |31|Execution can be suspended mid-execution|`¯1`|
|_          _|32|Responds to weak interrupt|`¯1`|
|Class[^1]|40|Syntactic supra-class ( `¯1` : invalid name, `0` : undefined, `1` : label, `2` : variable, `3` : function, `4` : operator, `8` : event, `9` : object)|`¯1`|
|      |41|Syntactic sub-class ( `0` : none, `1` : traditional/plain, `2` : field/dynamic/instance, `3` : property/derived/primitive, `4` : class, `5` : interface, `6` : external, `7` : external interface)|`0`|
|_     _|42|Full syntactic class (sum of supra- and sub-class)|`¯1`|
|Source|50|File name|`''`|
|      |51|File encoding|`''`|
|      |52|File checksum|`''`|
|      |53|File line separators ( `13` : Carriage Return, `10` : Line Feed, `13 10` : Carriage Return followed by Line Feed, `133` : New Line, `11` : Vertical Tab, `12` : Form Feed, `8232` : Line Separator, `8233` : Paragraph Separator)|`⍬`|
|      |54|Definition's offset from top|`0`|
|_    _|55|Number of lines in definition|`0`|
|Definition|60|Verbatim source (as typed)|`0⍴⊂''`|
|          |61|Normalised source (with AUTOFORMAT=1 and TABSTOPS=4)|`0⍴⊂''`|
|_        _|62|Most precise available source (verbatim with fallback to normalised)|`0⍴⊂''`|



`R` depends on the combination of `X` and `Y`:


|&nbsp;                            ||`X`                                                                                                   ||
|-----------------------------------|------------------------------|---------------------------------------------|--------------------------|
|&nbsp;                            ||Scalar                        | Vector |
|`Y`                                |Simple character scalar/vector|Requested value (not enclosed)               |Vector of requested values|
|                                   |Enclosed character vector     |Requested value (enclosed)                   |Scalar containing vector of requested values|
|_-                               -_|Vector of character scalars/vectors|Vector of requested values              |Outer shape from `⍴⍺` , inner shape from `⍴⍵`|


<h2 class="example">Examples</h2>
```apl
      Att
10 11 12 20 23 30 31 32 40 41 42 50 51 52 53 54 55

```
```apl

      foo←{⍵ ⍵}
      Att ⎕ATX 'foo'
┌─┬──┬─┬┬───┬──┬──┬──┬─┬─┬───┬┬┬┬┬─┬─┐
│1│¯2│0││616│¯1│¯1│¯1│3│2│3.2│││││0│0│
└─┴──┴─┴┴───┴──┴──┴──┴─┴─┴───┴┴┴┴┴─┴─┘

```
```apl

      x←42
      Att ⎕ATX 'x'
┌─┬─┬─┬┬──┬──┬──┬──┬─┬─┬───┬┬┬┬┬─┬─┐
│0│0│0││32│¯1│¯1│¯1│2│1│2.1│││││0│0│
└─┴─┴─┴┴──┴──┴──┴──┴─┴─┴───┴┴┴┴┴─┴─┘

```
```apl

      10 11 12 30 31 32 40 41 42 ⎕ATX 'x' 'foo'
┌───┬────┬───┬─────┬─────┬─────┬───┬───┬───────┐
│0 1│0 ¯2│0 0│¯1 ¯1│¯1 ¯1│¯1 ¯1│2 3│1 2│2.1 3.2│
└───┴────┴───┴─────┴─────┴─────┴───┴───┴───────┘

```
```apl
      2 ⎕FIX'foo ← {' '⍵ ⍵ }'
      60 61 ⎕ATX 'foo'
┌───────────────┬──────────────────┐
│┌───────┬─────┐│┌──────┬─────────┐│
││foo ← {│⍵ ⍵ }│││ foo←{│     ⍵ ⍵}││
│└───────┴─────┘│└──────┴─────────┘│
└───────────────┴──────────────────┘

```
```apl
      src←':namespace c' ':endnamespace' '' 'range←{⍺↓⍳⍵}'
      2 ⎕FIX src
      55 54 ⎕ATX'c' 'range'
┌───┬───┐
│2 1│0 3│
└───┴───┘

```
```apl
      2 1↑¨0 3↓¨⊂src
┌────────────────────────────┬──────────────┐
│┌────────────┬─────────────┐│┌────────────┐│
││:namespace c│:endnamespace│││range←{⍺↓⍳⍵}││
│└────────────┴─────────────┘│└────────────┘│
└────────────────────────────┴──────────────┘
```

[^1]: Names in the Class group that can return `¯1` (meaning "invalid name") might return a different value in future versions of Dyalog, including values that are not currently possible and ones that deviate from the current `⎕NC` values.