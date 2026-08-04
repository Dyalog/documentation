---
search:
  boost: 2
---

# <span>Create Directory</span> `{R}←⎕MKDIR Y`{{key}}

This function creates new directories.

`Y` is a character vector or scalar containing a single directory name, or a vector of character vectors containing zero or more directory names. Names must conform to the naming rules of the host Operating System.

For each name in `Y` the path must exist and the base name must not exist (see [Native File Exists](nexists.md)), otherwise an error is signalled. Use the variant option **Unique** or [dyadic `⎕MKDIR`](mkdir-dyadic.md) to handle these cases.

The **Unique** option specifies whether the base name (see [File Name Parts](nparts-monadic.md)) in `Y` is modified so that the name is unique (does not already exist). The shy result `R` depends on the value of **Unique**:

| Unique | Effect on Behaviour | `R` when `Y` is Single Name | `R` when `Y` is Vector of Names |
|--------|---------------------|-----------------------------|---------------------------------|
| `0` (default) | The directory named in `Y` will be created. | a scalar `1` if a directory was created or `0` if not | a vector of `1`s and `0`s with the same length as `Y` |
| `1` | The name in `Y` is modified by extending the base name with random characters and the directory is created. The name of the directory is returned in the result `R`. | a character vector containing the name of the directory that was created | a vector of character vectors with the same length as `Y` |

If a directory cannot be created (for example, if a directory with that name already exists, or write access is denied) then an error is signalled.

<h2 class="example">Examples</h2>

```apl
      ⎕NEXISTS '/Users/Pete/Documents/temp'
0
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
1
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
FILE NAME ERROR: /Users/Pete/Documents/temp: Already exists
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp'
        ∧

      ⎕←(⎕MKDIR⍠'Unique'1)'/Users/Pete/Documents/temp'
/Users/Pete/Documents/tempdjM0X8

      ⊢⎕MKDIR'temp1' 'temp2'
1 1
```

!!! note
    When multiple names are specified they are processed in the order given. If an error occurs at any point whilst creating directories, processing will immediately stop and an error will be signalled. The operation is not atomic; some directories may be created before this happens. In the event of an error there will be no result and therefore no indication of how many directories were created before the error occurred.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MKDIR MKDIR
</div>
