---
search:
  boost: 2
---

# <span>Atomic Vector Unicode Mapping</span> `⎕AVU`

`⎕AVU` lists the Unicode code points of the characters of the [atomic vector](av.md), `⎕AV`. It defines the content of `⎕AV` in the Unicode Edition, and is used to [translate](#translation) characters between the Unicode Edition and the Classic Edition.

!!! Legacy "Legacy"
    `⎕AVU` is retained for backwards compatibility purposes. It is relevant only to the Classic Edition, and to data that the Unicode Edition exchanges with the Classic Edition or with versions earlier than 12.0.

<h2 class="example">Example</h2>

The namespaces `Std` and `Russian` in the workspace [`avu`](#character-representation) have their own values of `⎕AVU`, and therefore their own layouts of `⎕AV`:

```apl
      'Std' 'Russian'⎕CY'avu'
      Std.⎕AV[97+⍳26]
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
      Russian.⎕AV[97+⍳26]
ЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ
      ⎕AV[97+⍳26]
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
```

## Value

`⎕AVU` is a simple integer vector of 256 distinct Unicode code points, each in the range `0` to `65535`. Each item is the code point of the character in the same position of `⎕AV`.

The value in a clear workspace corresponds to the _Dyalog Alt_ output translate table and font of the Classic Edition.

## Character Representation

The Classic Edition, and Dyalog APL versions earlier than 12.0, store each character as its position in `⎕AV`. When a character is displayed or printed, the output translate table, which is user-configurable, translates this position into the position of a symbol in an extended ASCII font. Extended ASCII fonts typically agree on positions 0 to 127, but have different symbols in positions 128 to 255, and some of them are APL fonts. The symbol that appears on the screen or on the printed page therefore depends on both the output translate table and the font.

The Classic Edition provides two fonts, and therefore two layouts of `⎕AV`, for the development environment: _Dyalog Std_, with the APL underscored alphabet, and _Dyalog Alt_, without it. In Dyalog Alt, `⎕AV[97+⍳26]` contains accented letters instead.

The workspace `avu` contains the namespaces `Alt`, `Std`, and `Russian`, whose values of `⎕AVU` give the corresponding layouts of `⎕AV`. Its namespace `v12_1` contains the same three namespaces, with the values of `⎕AVU` in version 12.1.

Unicode does not contain the underscored letters. Dyalog APL maps the [underscored alphabet](underscored-alphabetic-characters.md) onto Unicode's circled letters, `⎕UCS 9397+⍳26`, which APL fonts such as _APL385 Unicode_ display as underscored letters.

!!! Hint "Hints and Recommendations"
    Most Unicode fonts display the underscored alphabet as circled letters. To avoid confusion, Dyalog Ltd recommends removing underscored characters from APL applications.

## Translation

The Unicode Edition translates characters between their Unicode code points and their positions in `⎕AV` when it:

- loads or copies a workspace saved by the Classic Edition or by a version earlier than 12.0
- reads characters from, or writes characters to, a non-Unicode component file
- reads or writes a native file with conversion code 82
- receives data type 82 from a TCP socket

The Classic Edition makes the same translation when it:

- loads or copies a workspace saved by the Unicode Edition
- reads characters from, or writes characters to, a Unicode component file
- receives data type 80, 160, or 320 from a TCP socket

The translation applies to character data and to the comments in the [`⎕OR`](or.md) of a function. Data from a workspace saved by version 12.0 or later is translated with the value of `⎕AVU` in the root of that workspace, `#.⎕AVU`. All other translation uses the value of `⎕AVU` in the current namespace.

A character that is not in `⎕AV` cannot be translated, and signals `TRANSLATION ERROR`. A component file whose [`U` property](fprops.md) is `0` is non-Unicode:

```apl
      'chars'⎕FCREATE 1
      ('U' 0)⎕FPROPS 1
1
      'abc'⎕FAPPEND 1
      'αβγ'⎕FAPPEND 1
TRANSLATION ERROR: Unicode character ⎕UCS 945 (U+03B1) not in ⎕AVU
      'αβγ'⎕FAPPEND 1
           ∧
```

A function that localises `⎕AVU` can read characters that were written with a different atomic vector. Here, the file holds the characters at `⎕AV[97+⍳26]`, which the Classic Edition displays as the underscored alphabet with the Dyalog Std font. Copying `Std.⎕AVU` from the workspace `avu` sets the local value:

```apl
      ⎕AV[97+⍳26]⎕FAPPEND 1
      ∇ R←ReadStd;⎕AVU
[1]    'Std.⎕AVU'⎕CY'avu'
[2]    R←⎕FREAD 1 2
      ∇
      ⎕FREAD 1 2
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
      ReadStd
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
```

## Scope

`⎕AVU` has [namespace scope](system-functions-by-category.md#system-variables). This means that each namespace has its own value, which a new namespace takes from its parent. A defined function or operator can localise `⎕AVU`, which keeps its value until it is assigned.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AVU AVU
</div>
