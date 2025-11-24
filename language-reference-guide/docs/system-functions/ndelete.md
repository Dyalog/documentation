---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NDELETE NDELETE
</div>

<h1 class="heading"><span class="name">Native File Delete</span> <span class="command">{R}←{X}⎕NDELETE Y</span></h1>

This function deletes files and directories.

`Y` is a character vector or scalar containing a single file or directory name, or a vector of character vectors containing zero or more file or directory names. Names must conform to the naming rules of the host Operating System.

The optional left argument `X` is a numeric scalar; valid values are  shown in the following table. If omitted, its default value is 0.

|---|------------------------------------------------------------------------------------------|
|0 { .shaded } |Each file or directory with the given name must exist.                                    |
|`1`|If the file or directory with the given name does not exist then no action is taken. The result `R` may be used to determine whether the file or directory was deleted or not.|
|`2`|If a name identifies a non-empty directory it, and all its contents, are to be deleted.   |
|`3`|Combination of 1 and 2.                                                                   |

`R` is a numeric count of top-level entities deleted when processing the corresponding name in `Y`. If `Y` specifies a single name,  `R` is a scalar. If `Y` is a vector of character vectors   `R` is a vector  with the same length as `Y`.

## Variant Options

`⎕NDELETE` may be applied using the  Variant operator with the Wildcard option.

## Wildcard Option (Boolean)

|---|---|
|0 { .shaded } |The name or names in `Y` identifies a specific file name.|
|`1`|The name or names in `Y` that specify the *base name* and *extension* (see [File Name Parts](./nparts.md)), may also contain the wildcard characters "?" and "*". An asterisk is a substitute for any 0 or more characters in a file name or extension; a question-mark is a substitute for any single character.|

Note that when Wildcard is 1, element(s) of `R` can  be 0 or `>1`. If Wildcard is 0, elements of `R` are always 1.

If `Y` specifies the name of a  symbolic link, `⎕NDELETE` deletes that symbolic link;   the target of the symbolic link is unaffected.

<h2 class="example">Examples</h2>
```apl

      ⎕NEXISTS'/Users/Pete/Documents/temp/t1/t2'
1
      ⊢⎕NDELETE'/Users/Pete/Documents/temp/t1/t2'
1
      ⊢⎕NDELETE'/Users/Pete/Documents/temp/t1/t2'
FILE NAME ERROR: Invalid file or directory name ("The system cannot find the file specified.")
      ⊢⎕NDELETE'/Users/Pete/Documents/temp/t1/t2'
     ∧

```
```apl

      ⊢1 ⎕NDELETE'/Users/Pete/Documents/temp/t1/t2'
0
      ⊢⎕NDELETE 'temp1' 'temp2'
1 1
      ⊢⎕MKDIR'temp1' 'temp2'
1 1
       ⊢(⎕NDELETE⍠1)'t*'
2
```
```apl
      ⊢⎕MKDIR'temp1'
1
      ⊢'Hello World' ⎕NPUT 'temp1/hw.txt'
13
      ⊢⎕NDELETE 'temp1'
FILE ACCESS ERROR: temp1: Unable to delete directory ("The directory is not empty.")
      ⊢⎕NDELETE'temp1'
       ∧
      ⊢2 ⎕NDELETE 'temp1'
1

```


If the file is in use or the current user is not authorised to delete it, `⎕NDELETE` will not succeed but will instead generate a `FILE ACCESS ERROR`.

## Note


When multiple names are specified they are processed in the order given. If an error occurs at any point whilst deleting files or directories, processing will immediately stop and an error will be signalled. The operation is not atomic; the directory contents may be partially deleted before this happens. In the event of an error there will be no result and therefore no indication of how many files were deleted before the error occurred.


