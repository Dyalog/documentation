<h1 class="heading"><span class="name">Native File Information</span> <span class="command">R←{X}⎕NINFO Y</span></h1>

This function returns information about one or more files or directories. `Y` may  be:

- a numeric scalar containing the tie number of a native file
- a character vector or scalar containing a file or directory name that conforms to the naming rules of the host Operating System.
- a vector of character vectors and/or tie numbers

## Variant Options

`⎕NINFO` may be applied using the Variant operator with the options  Wildcard (the Principal option), Recurse and Follow.

## Wildcard Option (Boolean)

|---|---|
|0 { .shaded } |The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

## Recurse Option

|---|---|
|0 { .shaded } |the name(s) in `Y` are searched for only in the corresponding specified directory.|
|`1`|the name(s) in `Y` are searched for in the corresponding specified directory as well as all sub-directories. If Wildcard is also 1, the wild card search is performed recursively.|
|`1 n`|the name(s) in `Y` are searched for in the corresponding specified directory as well as its sub-directories to the n <sup>th</sup> -level sub-directory. If n is 0, no sub-directories are searched. If n is `¯1` all sub-directories are searched.|
|`2 (n)`|same as 1 but if any unreadable directories are encountered they are skipped (whereas if Recurse is `1 (n)` , `⎕NINFO` stops and generates an error).|

## Follow Option (Boolean)

|---|----------------------------------------------------------------------------------------|
|`0`|the properties reported are those of the symbolic link itself                           |
|1 { .shaded } |the properties reported for a symbolic link are those of the target of the symbolic link|

The optional left argument `X` is a simple numeric array containing values shown in the following table.

|`X`|Property|Default|
|---|---|---|
|`0`|Name of the file or directory, as a character vector. If `Y` is a tie number then this is the name which the file was tied.|&nbsp;|
|`1`|Type, as a numeric scalar: 0=Not known 1=Directory 2=Regular file 3=Character device 4=Symbolic link (only when Follow is 0) 5=Block device 6=FIFO (not Windows) 7=Socket (not Windows)|`0`|
|`2`|Size in bytes, as a numeric scalar|`0`|
|`3`|Last modification time, as a timestamp in `⎕TS` format|`7⍴0`|
|`4`|Owner user id, as a character vector – on Windows a SID, on other platforms a numeric userid converted to character format|`''`|
|`5`|Owner name, as a character vector|`''`|
|`6`|Whether the file or directory is hidden (1) or not (0), as a numeric scalar. On Windows, file properties include a "hidden" attribute; on non-Windows platforms a file or directory is implicitly considered to be hidden if its name begins with a "."|`¯1`|
|`7`|Target of symbolic link (when Type is 4)|`''`|
|`8`|Current position in the file. Always 0 if `Y` is a file name.|`0`|
|`9`|Last access time  in `⎕TS` format, when available|`7⍴0`|
|`10`|Creation time if available, otherwise the time of the last file status change in `⎕TS` format|`7⍴0`|
|`11`|Whether the file or directory can (1) or cannot (0) be read ( `¯1` if unknown)|`¯1`|
|`12`|Whether the file or directory can (1) or cannot (0) be written  ( `¯1` if unknown or for a directory under Windows)|`¯1`|
|`13`|Last modification time, as a UTC  Dyalog Date  Number.|`0`|
|`14`|Last access time  as a UTC Dyalog Date  Number, when available.|`0`|
|`15`|Creation time if available, otherwise the time of the last file status change  as a UTC Dyalog Date  Number.|`0`|

Note that the current file position identifies where `⎕NREAD` will next read from or `⎕NAPPEND` will next write to and is only pertinent when the corresponding value in `Y` is a tie number rather than a name. It will be reported as 0 for named files.

Each value in `X` identifies a property of the file(s) or directory(ies) identified by `Y` whose value is to be returned in the result `R`. If omitted, the default value of `X` is 0. Values in `X` may be specified in any order and duplicates are allowed. A value in `X` which is not defined in the table above will not generate an error but results in a `⍬` (Zilde) in the corresponding element of `R`.

`R` is the same shape as `X` and each element contains value(s) determined by the property specified in the corresponding element in `X`. The depth of `R` depends upon whether or not the Wildcard option is enabled. If, for any reason, the function is unable to obtain a property value, (for example, if the file is in use exclusively by another process) the default value shown in the last column is returned instead.

If the Wildcard option is not enabled (the default) then `Y` specifies exactly one file or directory and must exist.  In this case each element in `R` is a single property value for that file. If the name in `Y` does not exist, the function signals an error. On non-Windows platforms "*" and "?" are treated as normal characters. On Windows an error will be signalled since neither "*" nor "?" are valid characters for file or directory names.

If the Wildcard option is enabled,  zero or more files and/or directories may match the  pattern in `Y`. In this case each element in `R` is a vector of property values for each of the files. Note that  no error will be signalled if no files match the pattern.

When using the Wildcard option, matching of names is done case insensitively on Windows and macOS, and case sensitively on other platforms. The names '.' and '..' are excluded from any matches. The order in which the names match is not defined.

## ProgressCallback Option

The `ProgressCallback` option is described in the [programming reference guide](../../../programming-reference-guide/native-files/#progress-callbacks). The details specific to `⎕NINFO` are listed below.

* The first element of the right argument to the callback function is the character vector `⎕NINFO`.
* The third element of the right argument (the information namespace) contains an extra field named `Info`, which is a vector with the same length as the `Last` field; one item per item being processed. The elements of the `Info` vector contains the information requested by the `⎕NINFO` call.
* The scan phase is relatively more expensive in `⎕NINFO` callbacks compared to `⎕NCOPY` callbacks. If the value of the `Limit` field is not required to be accurate, the user may consider disabling the scan phase.

## Note

On non-Windows platforms, file names are exposed by the Operating System using UTF-8 encoding which Dyalog translates internally to characters.

In the Unicode Edition, if the UTF-8 encoding is invalid, Dyalog replaces each offending byte with a unique Unicode symbol (in the *Low Surrogate Area* of the Unicode charts) that is mapped back to the original byte by the other system functions (including `⎕NTIE` and `⎕NDELETE`) that take native file names as arguments. The display of a file name containing these mapped bytes may appear strange.

In the Classic Edition, offending bytes are replaced by the `?` symbol, which means that the names reported do not accurately identify the files.

<h2 class="example">Examples</h2>
```apl

      (0 1 2) ⎕NINFO 'c:/Users/Pete/Documents'
┌→───────────────────────────────────┐
│ ┌→──────────────────────┐          │
│ │c:/Users/Pete/Documents│ 1 163840 │
│ └───────────────────────┘          │
└∊───────────────────────────────────┘

```
```apl
      ⊃1⎕NPARTS '' ⍝ current working directory
c:/Users/Pete/
      (⎕NINFO⍠1)'D*'
┌─────────────────────────────────────┐
│┌───────┬─────────┬─────────┬───────┐│
││Desktop│Documents│Downloads│Dropbox││
│└───────┴─────────┴─────────┴───────┘│
└─────────────────────────────────────┘

```
```apl
      (⎕NINFO⍠1)'Documents/*.zip'
┌──────────────────────┐
│┌────────────────────┐│
││Documents/dyalog.zip││
│└────────────────────┘│
└──────────────────────┘

```
```apl
      ⍪ (0,⍳6) ⎕NINFO 'Documents/dyalog.zip'
┌──────────────────────────────────────────────┐
│Documents/dyalog.zip                          │
├──────────────────────────────────────────────┤
│2                                             │
├──────────────────────────────────────────────┤
│3429284                                       │
├──────────────────────────────────────────────┤
│2016 1 22 16 43 58 0                          │
├──────────────────────────────────────────────┤
│S-1-5-21-2756282986-1198856910-2233986399-1001│
├──────────────────────────────────────────────┤
│HP/Pete                                       │
├──────────────────────────────────────────────┤
│0                                             │
└──────────────────────────────────────────────┘

```
```apl
      ⊃1⎕NPARTS '' ⍝ current working directory
C:/Users/Pete/Documents/Dyalog APL-64 16.0 Unicode Files/
      (⎕NINFO⍠1)'*.*'
┌──────────────────────────────────────────────────────┐
│┌───────────┬──────────┬─────────┬───────────────────┐│
││default.dlf│def_uk.dse│jsonx.dws│UserCommand20.cache││
│└───────────┴──────────┴─────────┴───────────────────┘│
└──────────────────────────────────────────────────────┘

```
```apl
      ⊢ ⎕MKDIR 'd1' 'd2'
1 1
      'a'∘⎕NPUT¨'find' 'd1/find' 'd1/nofind' 'd2/find'
      (⎕ninfo⍠'Recurse' 1)'find'
┌──────────────────────┐
│┌───────┬───────┬────┐│
││d1/find│d2/find│find││
│└───────┴───────┴────┘│
└──────────────────────┘
```

The next set of examples, illustrate the use of the Recurse variant option to limit the sub-directory depth.
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

The following expression will return all Word document (`.docx` and `.doc`) in the current directory, searching recursively through any sub-directories:
```apl
     (⎕NINFO⍠('Recurse' 1)('Wildcard' 1))'*.docx' '*.doc'
```

!!! note
    Of the file timestamps which are reported by the operating system, only the last modification time should be considered reliable and portable. Neither the access time or creation time are well supported across all platforms. Furthermore, they may not accurately reflect the actual time that the operation occurred.


