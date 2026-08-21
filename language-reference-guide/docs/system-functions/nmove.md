---
search:
  boost: 2
---

# <span>Native File Move</span> `{R}←X ⎕NMOVE Y`{{key}}

This function moves native files and directories from one or more sources specified by `Y` to a destination specified by  `X`. `⎕NMOVE` is similar to `⎕NCOPY` (see [Native File Copy ](ncopy.md)).

When possible `⎕NMOVE` *renames* files and directories, which effects a fast move when the source and destination are on the same file system. By default (see the `RenameOnly` option below), if `⎕NMOVE` is unable to rename files or directories, it instead copies them and deletes the originals.

`X` is a character vector that specifies the name of the destination.

`Y` is a character vector that specifies the name of the source, or a vector of character vectors containing zero or more sources.

Sources and destinations can be full or relative (to the current working directory) path names adhering to the operating system convention.

If `Y` specifies more than one source, `X` must be a character vector  that specifies an existent directory to which each of the sources in `Y` is to be moved.

The [shy](../../../programming-reference-guide/introduction/results#shy-results) result `R` contains count(s) of top-level items moved. If `Y` is a single source name, `R` is a scalar otherwise it is a vector of the same length as `Y`.

<h2 class="example">Examples</h2>

A number of possibilities exist, illustrated by the following examples. In all cases, if the source is a file, the file is moved. If the source is a directory, the directory and all of its contents are moved.

The source name must be an existent file or directory. If the destination name does not exist but its path name does exist, the source is moved to the destination name. If the destination name is an existing directory the source name is moved to that directory.

```apl
      ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

⍝ Rename the Session file
      ⊢'session.dlf' ⎕NMOVE 'default.dlf'
1
      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Move the Session file to backups directory
      ⊢'backups'⎕NMOVE'default.dlf'
1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf  
```

Each source name must specify a single file or directory which must exist. The destination name must be an existing directory. Each of the files and/or directories specified by the source base names are moved to the destination directory.

```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1

⍝ Move 2 files to backups directory
      ⊢'backups'⎕NMOVE'default.dlf' 'def_uk.dse'
1 1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf
backups/def_uk.dse 
```

## Variant Options

`⎕NMOVE` supports four variant options, specified using the _variant_ operator [`⍠`](../primitive-operators/variant.md), summarised in [](#variantoptionsfornmove), and described in detail beneath it. The principal option is `Wildcard`.

Table: Variant options for `⎕NMOVE` { #variantoptionsfornmove }

|Variant Option|Valid Values|Default|Effect|
|---|---|---|---|
|[`Wildcard`](#variant-option-wildcard)<br><small>principal</small>|`0` or `1`|`0`|Whether the names in `Y` are matched literally or as patterns.|
|[`IfExists`](#variant-option-ifexists)|`'Error'` or `'Skip'`|`'Error'`|What happens when a target file already exists.|
|[`RenameOnly`](#variant-option-renameonly)|`0` or `1`|`0`|What happens when the source cannot be renamed.|
|[`ProgressCallback`](#variant-option-progresscallback)|the name of a callback function|none|Reports progress during the move.|

### Variant Option: `Wildcard`

The `Wildcard` variant option (a Boolean) determines whether the name or names in `Y` are matched literally or as wildcard patterns.

|Value|Effect|
|---|---|
|`0` <small>(default)</small>|The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), can also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

When `Wildcard` is `1`, element(s) of `R` can be `0` or `>1`. If `Wildcard` is `0`, elements of `R` are always `1`.

<h4 class="example">Examples</h4>

The source name can include wildcard characters that match a number of existing files and/or directories. The destination name must be an existing directory. The files and/or directories that match the pattern specified by the source name are moved into the destination directory. If there are no matches, zero copies are made.

```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Move all files to backups directory
      ⊢'backups'(⎕NMOVE⍠'Wildcard' 1)'*.*'
3
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf        
backups/def_uk.dse         
backups/UserCommand20.cache
```

The destination name must be an existing directory. Each of the files and/or directories that match the patterns specified by the source names (if any) are moved to the destination directory.

```apl
      ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Move files to backups directory
      ⊢'backups'(⎕NMOVE⍠1)'d*' 'UserCommand20.cache'
2 1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf
backups/def_uk.dse
backups/UserCommand20.cache
```

### Variant Option: `IfExists`

The `IfExists` variant option determines what happens when a source file is to be moved to a target file that already exists. It does not apply to directories, only to the files within them.

|Value|Description|
|---|---|
|`'Error'` <small>(default)</small>|Existing files will not be overwritten and an error will be signalled.|
|`'Skip'`|Existing files will not be overwritten but the corresponding copy operation will be skipped (ignored).|

The following cases cause an error to be signalled regardless of the value of the `IfExists` variant.

- If the source specifies a directory and the destination specifies an existing file.
- If the source specifies a file and the same base name exists as a sub-directory in the destination.

### Variant Option: `RenameOnly`

The `RenameOnly` variant option (a Boolean) determines what happens when it is not possible to rename the source.

|---|---|
|`0` <small>(default)</small>|The source will be copied and the original deleted|
|`1`|The move will fail                                |

### Variant Option: `ProgressCallback`

The `ProgressCallback` variant option is described in the [Dyalog Programming Reference Guide](../../../programming-reference-guide/native-files#progress-callbacks). The following is specific to `⎕NMOVE`:

* The first element of the right argument to the callback function is the character vector `'⎕NMOVE'`.

## Note

When `⎕NMOVE` copies and deletes files:

- The operation will take longer to complete.
- File modification times will be preserved but other attributes such as file ownership might be changed.
- Read permissions will be needed on all files within a directory which is moved.
- If the operation fails at any point and an error is signalled it is possible that there might be files and/or directories left duplicated in both the source and destination. It is not possible that a file or directory might be removed from the source without having been copied to the destination.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NMOVE NMOVE
</div>
