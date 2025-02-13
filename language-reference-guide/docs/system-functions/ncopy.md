




<h1 class="heading"><span class="name">Native File Copy</span> <span class="command">{R}←X ⎕NCOPY Y</span></h1>



This function copies native files and directories from one or more sources specified by `Y` to a destination specified by `X`. `⎕NCOPY` is similar to `⎕NMOVE` (see [Native File Move](nmove.md)).


`X` is a character vector that specifies the name of the destination.


`Y` is a character vector that specifies the name of the source, or a vector of character vectors containing zero or more sources.


Source and destination path names may be full or relative (to the current working directory) path names which adhere to the operating system conventions.



If `X` specifies an existent directory then each source in `Y` is copied into that directory, otherwise `X` specifies the name of the copy. `X` must specify an existent directory if the source contains multiple names or if the Wildcard option is set.


The shy result `R` contains count(s) of top-level items copied. If `Y` is a single source name, `R` is a scalar otherwise it is a vector of the same length as `Y`.

## Variant Options


`⎕NCOPY` may be applied using the   Variant operator with the options Wildcard (the Principal option), IfExists, PreserveAttributes and ProcessCallback.

## Wildcard Option (Boolean)


|---|---|
|0 { .shaded } |The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [NParts](./nparts.md) ), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|


Note that when Wildcard is 1, element(s) of `R` can  be 0, 1 or `>1`. If Wildcard is 0, elements of `R` are always 1.


## IfExists Option


The IfExists variant option determines what happens when a source file is to be copied to a target file that already exists. It does not apply to directories, only to the files within them.


|Value             |Description                                                                                        |
|------------------|---------------------------------------------------------------------------------------------------|
|'Error' { .shaded } |Existing files will not be overwritten and an error will be signalled. This is the default                                                                        |
|`'Skip'`          |Existing files will not be overwritten but the corresponding copy operation will be skipped (ignored).                                                            |
|`'Replace'`       |Existing files will be overwritten.                                                                                                                               |
|`'ReplaceIfNewer'`|Existing files may be overwritten if, and only if, the corresponding source file is newer (more recently modified) than the existing one, otherwise it is skipped.|



The following cases cause an error to be signalled  regardless of the value of the IfExists variant.

- If the source specifies a directory and the destination specifies an existing file.
- If the source specifies a file and the same base name exists as a sub-directory in the destination.

## PreserveAttributes Option (Boolean)


The PreserveAttributes variant option determines whether or not file attributes are preserved. It does not apply to directories, only to files.


|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0 { .shaded } |file attributes are not preserved.                                                                                                                                                         |
|`1`|where possible, copied files will be given at least the same modification time as the source. Other file attributes will be preserved as permitted by the operating system and file system.|


Note also that when files are copied across file systems, the different file systems may have different timestamp granularity and the timestamps may not be exactly the same.


<h2 class="example">Examples</h2>


There are a number of possibilities which are illustrated below. In all cases,  if the source is a file, a copy of the file is created. If the source is a directory, a copy of the directory and all its contents is created.

### Examples (single source, Wildcard is 0)


- The source name must be an existent file or directory.
- If the destination name does not exist but its path name does exist, the source is copied to the destination name.
- If the destination name is an existing directory the copy is created within that directory with the base name of the source.
```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/
 
⍝ Make a named back-up of the Session file
      ⊢'session.bak' ⎕NCOPY 'default.dlf'
```
```apl

1
      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
 ⍝ Copy the Session file to backups directory
      ⊢'backups'⎕NCOPY'default.dlf'
1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf  
```


### Examples (single source, Wildcard is 1)

- The source name may include wildcard characters which matches a number of existing files and/or directories. The destination name must be an existing directory.
- The files and/or directories that match the pattern specified by the source name are copied into the destination directory. If there are no matches, zero copies are made.
```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Copy all files to backups directory
      ⊢'backups'(⎕NCOPY⍠'Wildcard' 1)'*.*'
3
```
```apl

      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf        
backups/def_uk.dse         
backups/UserCommand20.cache
  

```



### Examples (multiple sources, Wildcard is 0)

- Each source name must specify a single file or directory which must exist. The destination name must be an existing directory.
- Copies of each of the files and/or directories specified by the source base names are made in the destination directory.
```apl
       ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Copy 2 files to backups directory
      ⊢'backups'⎕NCOPY'default.dlf' 'def_uk.dse'
1 1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf
backups/def_uk.dse 

```



### Examples (multiple sources, Wildcard is 1)

- The destination name must be an existing directory.
- Copies of each of the files and/or directories that match the patterns specified by the source names (if any) are made in the destination directory.
```apl
      ⊃1 ⎕NPARTS ''
i:/Documents/Dyalog APL-64 17.0 Unicode Files/

      ⊢ ⎕MKDIR 'backups' ⍝ Make a backups directory
1
⍝ Copy files to backups directory
      ⊢'backups'(⎕NCOPY⍠1)'d*' 'UserCommand20.cache'
2 1
      ↑⊃0 (⎕NINFO⍠1) 'backups\*'
backups/default.dlf
backups/def_uk.dse
backups/UserCommand20.cache
```

## ProgressCallback Option

The `ProgressCallback` option is described in the [programming reference guide](../../../programming-reference-guide/native-files/#progress-callbacks). The details specific to `⎕NCOPY` are listed below.

* The first element of the right argument to the callback function is the character vector `⎕NCOPY`.

## Notes

- The special directories `.` and `..` can never be copied into an existing directory.
- If any source name is a symbolic link it is dereferenced; that is, the source or directory it references is copied rather than the link itself.
- In the result `R`, a directory together with all its contents is counted once. A directory may be partially copied if the IfExists option is set to `'Replace'` or `'ReplaceIfNewer'`).
- If an error occurs during the copy process then processing will immediately stop and an error will be signalled. The operation is not atomic; some items may be copied before this happens. In the event of an error there will be no result and therefore no indication of how many names were copied before the error occurred.