<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NINFO NINFO
</div>

<h1 class="heading"><span class="name">Native File Information</span> <span class="command">R←{X}⎕NINFO Y</span></h1>

This function queries or sets information about one or more files or directories. `Y` may be:

- a numeric scalar containing the tie number of a native file
- a character vector or scalar containing a file or directory name that conforms to the naming rules of the host Operating System.
- a vector of character vectors and/or tie numbers

Optionally, `X` specifies properties of the files/directories identifed in `Y`. `X` can be an array of any shape; the shape determines whether the specified properties are queried or set:

- If `X` is a simple numeric array, the properties are queried. In this case, the values of `X` correspond to properties of the file/directory specified in `Y` that are to be queried, as defined in the following table.
- If some or all of the elements in `X` are nested vectors, the properties are set. In this case, the values of `X` correspond to properties of the file/directory specified in `Y` that are to be set, as defined in the following table, with appropriate corresponding values to which those properties should be set. Not all file properties are settable. 

If `X` is not defined, it is assumed to be `0`.

|`X`|Property|Default|Settable|
|---|---|---|---|
|`0`|Name of the file or directory, as a character vector. If `Y` is a tie number then this is the name which the file was tied.|&nbsp;|No|
|`1`|Type, as a numeric scalar: 0=Not known 1=Directory 2=Regular file 3=Character device 4=Symbolic link (only when Follow is 0) 5=Block device 6=FIFO (not Windows) 7=Socket (not Windows)|`0`|No|
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

The values in `X` are processed in ravel order. Duplicates are allowed.

The returned value `R` has the same shape as `X` (if the **Wildcard** variant option has been specified, the depth will change – see below). The content of `R` depends on whether properties were queried or set:

- If properties were queried:
    - each element of `R` is the value of the property identified by the corresponding value of `X`.
    - if a value in `X` is not defined in the table above, the corresponding `R` value is `⍬` (Zilde).
    - if more than one file/directory is specified in `Y`, the element of `R` corresponding to each element of `X` contains the property values for each of the files/directories specified in `Y`.
- If properties were set:
    - each element of `R` is the new value of the property identified by the corresponding value of `X`.
    - if the value in `X` does not specify a property that is defined in the table above and settable, or if the new value specified for the property is not valid, an error will be signalled.
    - if more than one file/directory is specified in `Y`, the element of `R` corresponding to each element of `X` contains the new property values for each of the files/directories specified in `Y`.

If a property value cannot be obtained, the default value (shown in the table above) is returned for that property.

If the Wildcard option is not enabled (the default) then `Y` specifies exactly one file or directory and must exist. In this case each element in `R` is a single property value for that file. If the name in `Y` does not exist, the function signals an error. On non-Windows platforms "*" and "?" are treated as normal characters. On Microsoft Windows an error will be signalled since neither are valid characters for file or directory names.

If the Wildcard option is enabled, zero or more files and/or directories may match the pattern in `Y`. In this case each element in `R` is a vector of property values for each of the files. Note that no error will be signalled if no files match the pattern.

When using the **Wildcard** option, matching of names is done case insensitively on Windows and macOS, and case sensitively on other platforms. The names '.' and '..' are excluded from any matches. The order in which the names match is not defined.

## Variant Options

`⎕NINFO` may be applied using the _variant_ operator with the options **Wildcard** (the Principal option), **Recurse**, **Follow** and **ProgressCallback**.

### Wildcard Option (Boolean)

|---|---|
|0 { .shaded } |The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

### Recurse Option

|---|---|
|0 { .shaded } |the name(s) in `Y` are searched for only in the corresponding specified directory.|
|`1`|the name(s) in `Y` are searched for in the corresponding specified directory as well as all sub-directories. If **Wildcard** is also 1, the wild card search is performed recursively.|
|`1 n`|the name(s) in `Y` are searched for in the corresponding specified directory as well as its sub-directories to the n <sup>th</sup> -level sub-directory. If n is 0, no sub-directories are searched. If n is `¯1` all sub-directories are searched.|
|`2 (n)`|same as 1 but if any unreadable directories are encountered they are skipped (whereas if **Recurse** is `1 (n)` , `⎕NINFO` stops and generates an error).|

### Follow Option (Boolean)

|---|----------------------------------------------------------------------------------------|
|`0`|the properties reported are those of the symbolic link itself                           |
|1 { .shaded } |the properties reported for a symbolic link are those of the target of the symbolic link|


### ProgressCallback Option

The **ProgressCallback** variant option is described in the [Dyalog Programming Reference Guide](../../../programming-reference-guide/native-files#progress-callbacks). The following is specific to `⎕NINFO`:

* The first element of the right argument to the callback function is the character vector `'⎕NINFO'`.
* The third element of the right argument (the information namespace) contains an extra field named `Info`, which is a vector with the same length as the `Last` field. Each element of the `Info` vector contains the information requested by the `⎕NINFO` call for the corresponding filename in `Last`.

## Note

On platforms other than Microsoft Windows, file names are exposed by the operating system using UTF-8 encoding, which Dyalog translates internally to characters.

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
      (⎕NINFO⍠'Recurse' 1)'find'
┌──────────────────────┐
│┌───────┬───────┬────┐│
││d1/find│d2/find│find││
│└───────┴───────┴────┘│
└──────────────────────┘
```

The next set of examples illustrates the use of the **Recurse** variant option to limit the sub-directory depth.
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

The following expression "touches" files, that is, it sets their last modification time to the current UTC time:

```apl
      (⊂13(1 ⎕DT'Z'))(⎕NINFO⍠1)'*.txt'
┌───────────────────────┐
│45719.53226 45719.53226│
└───────────────────────┘
```

!!! note
    Of the file timestamps which are reported by the operating system, only the last modification time should be considered reliable and portable. Neither the access time or creation time are well supported across all platforms. Furthermore, they may not accurately reflect the actual time that the operation occurred.
