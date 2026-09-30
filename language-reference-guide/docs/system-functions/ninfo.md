---
search:
  boost: 2
---

# <span>Native File Information</span> `R←{X}⎕NINFO Y`{{key}}

This function reports and changes properties of files and directories, such as their size, type, owner, and timestamps, and can also list the contents of a directory.

## Syntax

`Y` names the files or directories to act on. `X` names the properties to report, or pairs a property with the value it is to be set to. If `X` is omitted, it is assumed to be `0`, which reports the name.

<h3 class="example">Example</h3>

Reporting the name, type, and size of a directory:

```apl
      0 1 2 ⎕NINFO 'c:/Users/Pete/Documents'
┌───────────────────────┬─┬──────┐
│c:/Users/Pete/Documents│1│163840│
└───────────────────────┴─┴──────┘
```

## Right Argument

`Y` can be:

- a numeric scalar containing the tie number of a native file
- a character vector or scalar containing a file or directory name that conforms to the naming rules of the host Operating System
- a vector of character vectors and/or tie numbers

!!! Warning "Warning"
    On platforms other than Microsoft Windows, file names are exposed by the operating system using UTF-8 encoding, which Dyalog translates internally to characters.
    
    In the Unicode Edition, if the UTF-8 encoding is invalid, Dyalog replaces each offending byte with a unique Unicode symbol (in the *Low Surrogate Area* of the Unicode charts) that is mapped back to the original byte by the other system functions (including `⎕NTIE` and `⎕NDELETE`) that take native file names as arguments. The display of a file name containing these mapped bytes might appear strange.
    
    In the Classic Edition, offending bytes are replaced by the `?` symbol, which means that the names reported do not accurately identify the files.

## Left Argument

`X` can be an array of any shape. Each of its elements selects a property from [](#properties), and its depth decides what happens to that property: a simple numeric element reports the property's value, while a nested element is a property and the value it is to be set to. The table also shows which properties can be set, and what is reported when a value cannot be obtained.

Table: Available properties { #properties }

|`X`|Property|Default|Settable|
|---|---|---|---|
|`0`|Name of the file or directory, as a character vector. If `Y` is a tie number, then this is the name which the file was tied.|`''`|No|
|`1`|Type, as a numeric scalar: 0=Not known 1=Directory 2=Regular file 3=Character device 4=Symbolic link (only when `Follow` is `0`) 5=Block device 6=FIFO (not Windows) 7=Socket (not Windows)|`0`|No|
|`2`|Size in bytes, as a numeric scalar|`0`|Yes|
|`3`|Last modification time, as a timestamp in `⎕TS` format|`7⍴0`|No|
|`4`|Owner user id, as a character vector – on Windows a SID, on other platforms a numeric userid converted to character format|`''`|No|
|`5`|Owner name, as a character vector|`''`|No|
|`6`|Whether the file or directory is hidden (1) or not (0), as a numeric scalar. On Windows, file properties include a "hidden" attribute; on non-Windows platforms a file or directory is implicitly considered to be hidden if its name begins with a "."|`¯1`|Windows only|
|`7`|Target of symbolic link (when Type is 4)|`''`|No|
|`8`|Current position in the file. This identifies where `⎕NREAD` would next read from or `⎕NAPPEND` would next write to, and is only pertinent when the corresponding value in `Y` is a tie number. It is reported as `0` for named files and directories.|`0`|Yes|
|`9`|Last access time  in `⎕TS` format, when available|`7⍴0`|No|
|`10`|Creation time if available, otherwise the time of the last file status change in `⎕TS` format|`7⍴0`|No|
|`11`|Whether the file or directory can (1) or cannot (0) be read ( `¯1` if unknown)|`¯1`|No|
|`12`|Whether the file or directory can (1) or cannot (0) be written  ( `¯1` if unknown or for a directory under Windows)|`¯1`|No|
|`13`|Last modification time, as a UTC  Dyalog Date Number.|`0`|Yes|
|`14`|Last access time, as a UTC Dyalog Date Number, when available.|`0`|Yes|
|`15`|Creation time if available, otherwise the time of the last file status change  as a UTC Dyalog Date  Number.|`0`|Windows only|

!!! Info "Information"
    Of the file timestamps which are reported by the operating system, only the last modification time should be considered reliable and portable. Neither the access time or creation time are well supported across all platforms. Furthermore, they might not accurately reflect the actual time that the operation occurred.

The values in `X` are processed in ravel order. Duplicates are allowed, so one call can both set a property and report it: an element that queries a property reports the value left by any earlier element that set it.

<h3 class="example">Example</h3>

The size of a newly created empty file is reported, set, and reported again:

```apl
      ''⎕NPUT'test'
      2 (2 9) 2 ⎕NINFO'test'
0 9 9
```

## Result

Each value in `R` reports a property: the value it holds if the corresponding element of `X` selected it for reporting, or its new value if that element set it. Where the element of `X` does not appear in [](#properties), the value is `⍬`; where it cannot be obtained, the default shown in the table is reported instead. Attempting to set a property that is not settable, or to give one a value that is not valid, signals an error.

`R` is built from up to three levels, as summarised in [](#resultstructure):

1. If `Y` is a vector of names and tie numbers, `R` has the shape of `Y`, and each of its elements describes one of them. If `Y` is a single name or tie number, this level is absent.
2. Within that, the shape is that of `X`, holding one value for each property selected.
3. If the [`Wildcard`](#variant-option-wildcard) variant option is `1`, each of those values is a vector holding one value for each name that matched, in place of the single value it would otherwise be.

Table: Structure of the result { #resultstructure }

|`Y`|`Wildcard`|`⍴R`|Each element of `R`|
|---|---|---|---|
|a single name or tie number|`0`|`⍴X`|a property value|
|a single name or tie number|`1`|`⍴X`|a vector of property values, one per matching name|
|a vector of names and tie numbers|`0`|`⍴Y`|an array of shape `⍴X`, holding that item's property values|
|a vector of names and tie numbers|`1`|`⍴Y`|an array of shape `⍴X`, each of whose elements is a vector of property values, one per matching name|

A single name and a one-element vector containing that name therefore give different structures, because it is the depth of `Y` that adds the first level, not the number of files.

<h3 class="example">Examples</h3>

The name and size of one file, then of two, then of every file matching a pattern, then of those matching each of two patterns:

```apl
      ''⎕NPUT'a.txt'
      'hello'⎕NPUT'b.txt'
      0 2 ⎕NINFO'a.txt'
┌─────┬─┐
│a.txt│0│
└─────┴─┘
      0 2 ⎕NINFO'a.txt' 'b.txt'
┌─────────┬─────────┐
│┌─────┬─┐│┌─────┬─┐│
││a.txt│0│││b.txt│6││
│└─────┴─┘│└─────┴─┘│
└─────────┴─────────┘
      0 2 (⎕NINFO⍠1)'*.txt'
┌─────────────┬───┐
│┌─────┬─────┐│6 0│
││b.txt│a.txt││   │
│└─────┴─────┘│   │
└─────────────┴───┘
      0 2 (⎕NINFO⍠1)'a*' 'b*'
┌───────────┬───────────┐
│┌───────┬─┐│┌───────┬─┐│
││┌─────┐│0│││┌─────┐│6││
│││a.txt││ ││││b.txt││ ││
││└─────┘│ │││└─────┘│ ││
│└───────┴─┘│└───────┴─┘│
└───────────┴───────────┘
```

Note that the third result groups by property while the second groups by file, and that the matches are not in the order the pattern might suggest: `Wildcard` does not define an order.

## Variant Options

`⎕NINFO` is controlled by four variant options, specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md), summarised in [](#variantoptionsforninfo), and described in detail beneath it.

Table: Variant options for `⎕NINFO` { #variantoptionsforninfo }

|Variant Option|Valid Values|Effect|
|---|---|---|
|[`Wildcard`](#variant-option-wildcard)<br><small>principal</small>|`0` <small>(default)</small>|The names in `Y` identify specific files.|
|_-                                    -_|`1`|The names in `Y` can contain the wildcard characters `?` and `*`.|
|[`Recurse`](#variant-option-recurse)|`0` <small>(default)</small>|Only the specified directory is searched.|
|_-                                    -_|`1`|The specified directory and its sub-directories are searched.|
|[`Follow`](#variant-option-follow)|`1` <small>(default)</small>|For a symbolic link, the target's properties are reported.|
|_-                                    -_|`0`|The symbolic link's own properties are reported.|
|[`ProgressCallback`](#variant-option-progresscallback)|the name of a callback function|A function is called periodically during a long operation.|

### Variant Option: `Wildcard`

`Wildcard`, the principal option, is Boolean:

|Value|Effect|
|---|---|
|`0` <small>(default)</small>|The name or names in `Y` identify a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [`⎕NPARTS`](nparts.md)) can also contain the wildcard characters `?` and `*`. An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

When `Wildcard` is `0`, `Y` names exactly one file or directory, which must exist, and each element of `R` is a single property value for it. If the name does not exist, the function signals an error. On platforms other than Microsoft Windows, `*` and `?` are ordinary characters; on Microsoft Windows an error is signalled, because neither is valid in a name.

When `Wildcard` is `1`, zero or more files and directories might match the pattern in `Y`, and each element of `R` is a vector of property values, one per match. No error is signalled when nothing matches.

Names are matched case insensitively on Microsoft Windows and macOS, and case sensitively on other platforms. The names `.` and `..` are never matched, and the order of the matches is not defined.

!!! Hint "Hints and Recommendations"
    Where matching is case insensitive, `⊃⊃(⎕NINFO⍠1)name` reports the capitalisation the file system actually holds, whatever capitalisation `name` uses. Only the leaf name is canonicalised this way.

    ```apl
          ⊃⊃(⎕NINFO⍠1)'/windows/inboxapps'
    /windows/InboxApps
    ```

<h4 class="example">Examples</h4>

```apl
      ⊃1⎕NPARTS '' ⍝ current working directory
c:/Users/Pete/
      (⎕NINFO⍠1)'D*'
┌─────────────────────────────────────┐
│┌───────┬─────────┬─────────┬───────┐│
││Desktop│Documents│Downloads│Dropbox││
│└───────┴─────────┴─────────┴───────┘│
└─────────────────────────────────────┘

      (⎕NINFO⍠1)'Documents/*.zip'
┌──────────────────────┐
│┌────────────────────┐│
││Documents/dyalog.zip││
│└────────────────────┘│
└──────────────────────┘

      ⊃1⎕NPARTS '' ⍝ current working directory
C:/Users/Pete/Documents/Dyalog APL-64 16.0 Unicode Files/
      (⎕NINFO⍠1)'*.*'
┌──────────────────────────────────────────────────────┐
│┌───────────┬──────────┬─────────┬───────────────────┐│
││default.dlf│def_uk.dse│jsonx.dws│UserCommand20.cache││
│└───────────┴──────────┴─────────┴───────────────────┘│
└──────────────────────────────────────────────────────┘
```

The following expression "touches" files, that is, it sets their last modification time to the current UTC time:

```apl
      (⊂13(1 ⎕DT'Z'))(⎕NINFO⍠1)'*.txt'
┌───────────────────────┐
│45719.53226 45719.53226│
└───────────────────────┘
```

### Variant Option: `Recurse`

The `Recurse` variant option determines whether, and to how many levels, sub-directories are searched.

|Value|Effect|
|---|---|
|`0` <small>(default)</small>|The name(s) in `Y` are searched for only in the corresponding specified directory.|
|`1`|The name(s) in `Y` are searched for in the corresponding specified directory as well as all sub-directories. If `Wildcard` is also `1`, the wildcard search is performed recursively.|
|`1 n`|The name(s) in `Y` are searched for in the corresponding specified directory as well as its sub-directories to the `n`th-level sub-directory. If `n` is `0`, no sub-directories are searched. If `n` is `¯1`, all sub-directories are searched.|
|`2`|As `1`, but any unreadable directories encountered are skipped rather than stopping `⎕NINFO` with an error.|
|`2 n`|As `1 n`, but any unreadable directories encountered are skipped rather than stopping `⎕NINFO` with an error.|

<h4 class="example">Examples</h4>

```apl
      ⎕←⎕MKDIR 'd1' 'd2'
1 1
      'a'⎕NPUT¨'find' 'd1/find' 'd1/nofind' 'd2/find'
      (⎕NINFO⍠'Recurse' 1)'find'
┌──────────────────────┐
│┌───────┬───────┬────┐│
││d1/find│d2/find│find││
│└───────┴───────┴────┘│
└──────────────────────┘
```

The next set of examples illustrates the use of the `Recurse` variant option to limit the sub-directory depth.

```apl
      Y←'d:\bouzouki\*.*'
      ⍴⊃0(⎕NINFO⍠('Wildcard' 1)('Recurse' 0))Y
355
      ⍴⊃0(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 0)))Y
355
      ⍴⊃0(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 1)))Y
1333
      ⍴⊃0(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 3)))Y
4223
```

The following expression will return all Microsoft Word documents (`.docx` and `.doc`) in the current directory, searching recursively through any sub-directories:

```apl
     (⎕NINFO⍠('Recurse' 1)('Wildcard' 1))'*.docx' '*.doc'
```

### Variant Option: `Follow`

`Follow` is Boolean:

|Value|Effect|
|---|---|
|`0`|The properties reported are those of the symbolic link itself.|
|`1` <small>(default)</small>|The properties reported for a symbolic link are those of the target of the symbolic link.|

### Variant Option: `ProgressCallback`

The `ProgressCallback` variant option is described in the [Dyalog Programming Reference Guide](../../programming-reference-guide/native-files.md#progress-callbacks). The following is specific to `⎕NINFO`:

* The first element of the right argument to the callback function is the character vector `'⎕NINFO'`.
* The third element of the right argument (the information namespace) contains an extra field named `Info`, which is a vector with the same length as the `Last` field. Each element of the `Info` vector contains the information requested by the `⎕NINFO` call for the corresponding filename in `Last`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NINFO NINFO
</div>
