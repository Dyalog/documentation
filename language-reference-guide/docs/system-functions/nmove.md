<h1 class="heading"><span class="name">Native File Move</span> <span class="command">{R}←X ⎕NMOVE Y</span></h1>

This function moves native files and directories from one or more sources specified by `Y` to a destination specified by  `X`. `⎕NMOVE` is similar to `⎕NCOPY` (see [Native File Copy ](ncopy.md)).

When possible `⎕NMOVE` *renames* files and directories, which effects a fast move when the source and destination are on the same file system. By default (see RenameOnly option below), if `⎕NMOVE` is unable to rename files or directories, it instead copies them and deletes the originals.

`X` is a character vector that specifies the name of the destination.

`Y` is a character vector that specifies the name of the source, or a vector of character vectors containing zero or more sources.

Sources and destinations may be full or relative (to the current working directory) path names adhering to the operating system convention.

If `Y` specifies more than one source, `X` must be a character vector  that specifies an existent directory to which each of the sources in `Y` is to be moved.

The shy result `R` contains count(s) of top-level items moved. If `Y` is a single source name, `R` is a scalar otherwise it is a vector of the same length as `Y`.

## Variant Options

`⎕NMOVE` may be applied using the  Variant operator with the options Wildcard (the Principal option), IfExists, RenameOnly and ProcessCallback.

## Wildcard Option (Boolean)

|---|---|
|0 { .shaded } |The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

Note that when Wildcard is 1, element(s) of `R` can  be 0 or `>1`. If Wildcard is 0, elements of `R` are always 1.

## IfExists Option

The IfExists variant option determines what happens when a source file is to be copied to a target file that already exists. It does not apply to directories, only to the files within them.

|Value   |Description                                                                                           |
|--------|------------------------------------------------------------------------------------------------------|
|'Error' { .shaded } |Existing files will not be overwritten and an error will be signalled.                                |
|`'Skip'`|Existing files will not be overwritten but the corresponding copy operation will be skipped (ignored).|

The following cases cause an error to be signalled  regardless of the value of the IfExists variant.

- If the source specifies a directory and the destination specifies an existing file.
- If the source specifies a file and the same base name exists as a sub-directory in the destination.

## RenameOnly Option (Boolean)

The RenameOnly option  determines what happens when it is not possible to rename the source.

|---|--------------------------------------------------|
|0 { .shaded }  |The source will be copied and the original deleted|
|`1`|The move will fail                                |

<h2 class="example">Examples</h2>

A number of possibilities exist, illustrated by the following examples. In all cases, if the source is a file, the file is moved. If the source is a directory, the directory and all of its contents are moved.

### Examples (single source, Wildcard is 0)

- The source name must be an existent file or directory.
- If the destination name does not exist but its path name does exist, the source is moved to the destination name.
- If the destination name is an existing directory the source name is moved to that directory.
```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/
 
⍝ Rename the Session file
      ⊢'session.dlf' ⎕NMOVE 'default.dlf'
```

```apl

1
      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
 ⍝ Move the Session file to backups directory
      ⊢'backups'⎕NMOVE'default.dlf'
1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf  
```

### Examples (single source, Wildcard is 1)

- The source name may include wildcard characters which matches a number of existing files and/or directories. The destination name must be an existing directory.
- The files and/or directories that match the pattern specified by the source name are moved into the destination directory. If there are no matches, zero copies are made.
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

### Examples (multiple sources, Wildcard is 0)

- Each source name must specify a single file or directory which must exist. The destination name must be an existing directory.
- Each of the files and/or directories specified by the source base names are moved to the destination directory.
```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
```
```apl

⍝ Move 2 files to backups directory
      ⊢'backups'⎕NMOVE'default.dlf' 'def_uk.dse'
1 1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf
backups/def_uk.dse 
```

### Examples (multiple sources, Wildcard is 1)

- The destination name must be an existing directory.
- Each of the files and/or directories that match the patterns specified by the source names (if any) are moved to the destination directory.
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

## ProgressCallback Option

The `ProgressCallback` option is described in the [programming reference guide](../../../programming-reference-guide/native-files/#progress-callbacks). The details specific to `⎕NMOVE` are listed below.

* The first element of the right argument to the callback function is the character vector `⎕NMOVE`.

## Note

When `⎕NMOVE` copies and deletes files:

- The operation will take longer to complete.
- File modification times will be preserved but other attributes such as file ownership may be changed.
- Read permissions will be needed on all files within a directory which is moved.
- If the operation fails at any point and an error is signalled it is possible that there may be files and/or directories left duplicated in both the source and destination. It is not possible that a file or directory may be removed from the source without having been copied to the destination.