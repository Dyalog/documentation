---
search:
  boost: 2
---

# <span>Native File Name</span> `R←⎕NINFO Y`{{key}}

This function returns the name of one or more files or directories. `Y` may be:

- a numeric scalar containing the tie number of a native file
- a character vector or scalar containing a file or directory name that conforms to the naming rules of the host Operating System.
- a vector of character vectors and/or tie numbers

`R` is the name of the file or directory, as an enclosed character vector if `Y` refers to a single target or directory, or a vector of enclosed character vectors if `Y` refers to multiple targets. If `Y` contains a tie number, `R` contains the name by which the file was tied.

Use [dyadic `⎕NINFO`](ninfo-dyadic.md) to obtain additional file properties.

If the Wildcard option is not enabled (the default) then `Y` specifies exactly one file or directory and must exist. In this case each element in `R` is the name of that file. If the name in `Y` does not exist, the function signals an error. On non-Windows platforms `*` and `?` are treated as normal characters. On Microsoft Windows an error will be signalled since neither are valid characters for file or directory names.

If the Wildcard option is enabled, zero or more files and/or directories may match the pattern in `Y`. In this case each element in `R` is a vector of the names of the matching files. Note that no error will be signalled if no files match the pattern.

When using the **Wildcard** option, matching of names is done case insensitively on Windows and macOS, and case sensitively on other platforms. The names `.` and `..` are excluded from any matches. The order in which the names match is not defined.

## Variant Options

`⎕NINFO` may be applied using the _variant_ operator with the options **Wildcard** (the Principal option), **Recurse** and **ProgressCallback**.

### Wildcard Option (Boolean)

|---|---|
|`0` (default)|The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [`⎕NPARTS`](./nparts-monadic.md) ), may also contain the wildcard characters `?` and `*`. An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

!!! Hint "Hints and Recommendations"
    On a case-insensitive file system (default on Microsoft Windows and macOS), the canonical capitalisation of a filename can be obtained with `⊃⊃(⎕NINFO⍠1)filename`, though only the leaf name is canonicalised. For example:
    ```apl
          ⊃⊃(⎕NINFO⍠1)'/windows/inboxapps'
    /windows/InboxApps
    ```

### Recurse Option

|---|---|
|`0` (default)|the name(s) in `Y` are searched for only in the corresponding specified directory.|
|`1`|the name(s) in `Y` are searched for in the corresponding specified directory as well as all sub-directories. If **Wildcard** is also 1, the wild card search is performed recursively.|
|`1 n`|the name(s) in `Y` are searched for in the corresponding specified directory as well as its sub-directories to the n <sup>th</sup> -level sub-directory. If n is 0, no sub-directories are searched. If n is `¯1` all sub-directories are searched.|
|`2 (n)`|same as 1 but if any unreadable directories are encountered they are skipped (whereas if **Recurse** is `1 (n)` , `⎕NINFO` stops and generates an error).|

### ProgressCallback Option

The **ProgressCallback** variant option is described in the [Dyalog Programming Reference Guide](../../../programming-reference-guide/native-files#progress-callbacks). The following is specific to `⎕NINFO`:

* The first element of the right argument to the callback function is the character vector `'⎕NINFO'`.
* The third element of the right argument (the information namespace) contains an extra field named `Info`, which is a vector with the same length as the `Last` field. Each element of the `Info` vector contains the name of the corresponding file in `Last`.

## Note

On platforms other than Microsoft Windows, file names are exposed by the operating system using UTF-8 encoding, which Dyalog translates internally to characters.

In the Unicode Edition, if the UTF-8 encoding is invalid, Dyalog replaces each offending byte with a unique Unicode symbol (in the *Low Surrogate Area* of the Unicode charts) that is mapped back to the original byte by the other system functions (including `⎕NTIE` and `⎕NDELETE`) that take native file names as arguments. The display of a file name containing these mapped bytes may appear strange.

In the Classic Edition, offending bytes are replaced by the `?` symbol, which means that the names reported do not accurately identify the files.

<h2 class="example">Examples</h2>
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
      ⍴⊃(⎕NINFO⍠('Wildcard' 1)('Recurse' 0))Y
355
      ⍴⊃(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 0)))Y
355
      ⍴⊃(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 1)))Y
1333
      ⍴⊃(⎕NINFO⍠('Wildcard' 1)('Recurse' (1 3)))Y
4223
```

The following expression will return all Microsoft Word documents (`.docx` and `.doc`) in the current directory, searching recursively through any sub-directories:
```apl
     (⎕NINFO⍠('Recurse' 1)('Wildcard' 1))'*.docx' '*.doc'
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NINFO NINFO
</div>
