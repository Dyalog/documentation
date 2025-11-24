---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MKDIR MKDIR
</div>






<h1 class="heading"><span class="name">Make Directory</span> <span class="command">{R}←{X}⎕MKDIR Y</span></h1>



This function creates new directories.


`Y` is a character vector or scalar containing a single directory name, or a vector of character vectors containing zero or more directory names. Names must conform to the naming rules of the host Operating System.


By default, for each name in `Y` the path must exist and the base name must not exist (see [File Name Parts](nparts.md)), otherwise an error is signalled. The optional left argument `X` and the variant option **Unique** can be used to amend this behaviour.

The result `R` depends on the value of the variant option **Unique**. If  **Unique** is not present, it is assumed to have a value of `0`.

| Unique | Result `R` |
|--------|------------|
|` 0`    | If `Y` specifies a single name, the shy result `R` is a scalar `1` if a directory was created or `0` if not. If `Y` is a vector of character vectors, `R` is a vector of `1`s and `0`s with the same length as `Y`. |
| `1`    | If `Y` specifies a single name, the shy result `R` is a character vector containing the name of the directory that was created. If `Y` is a vector of character vectors, `R` is a vector of character vectors with the same length as `Y`. |

The optional left argument `X` is a numeric scalar that modifies the default behaviour when the base name in `Y` already exists and/or the path in `Y` does not already exist. If omitted, it is assumed to be 0. Possible values and the effect that they have on the default behaviour are:

|---|---|
| `0` {.shaded} | The base name in `Y` must not exist and the path in `Y` must exist, otherwise an error is signalled.                                                                           |
|`1`|No action is taken if a directory specified by `Y` already exists (the return value indicates whether a new directory was created). Has no effect when the variant option **Unique** is set.|
|`2`|Any part of the *paths* specified in `Y` which does not already exist will be created in preparation of creating the corresponding directory.                                               |
|`3`|Combination of 1 and 2.                                                                                                                                                                     |

## Variant Options

`⎕MKDIR` may be applied using the variant operator with the option **Unique**. There is no primary option.

## Unique Option (Boolean)
The **Unique** option specifies whether the base name (see [File Name Parts](nparts.md)) in `Y` is modified so that the name is unique (does not already exist).

| Unique            | Effect on Behaviour  |
|-------------------|----------------------|
|` 0`   { .shaded } | The directory named in `Y` will be created. |
| `1`               | The name in `Y` is modified by extending the base name with random characters and the directory is created. The name of the directory is returned in the result `R`. |

If a directory cannot be created (for example, if a directory with that name already exists, or write access is denied) then an error is signalled.

<h2 class="example">Examples</h2>
```apl

      ⎕NEXISTS '/Users/Pete/Documents/temp'
0
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
1
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
FILE NAME ERROR: Directory exists
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp'
     ∧

      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
FILE NAME ERROR: Unable to create directory ("The system cannot find the path specified.")
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
     ∧

      ⎕←2 ⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
1

      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
FILE NAME ERROR: /Users/Pete/Documents/temp/t1/t2: Already exists
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
        ∧

      ⎕←(⎕MKDIR⍠'Unique'1)'/Users/Pete/Documents/temp/t1/t2'
/Users/Pete/Documents/temp/t1/t2djM0X8

      ⊢⎕MKDIR'temp1' 'temp2'
1 1
```

!!! note
    When multiple names are specified they are processed in the order given. If an error occurs at any point whilst creating directories, processing will immediately stop and an error will be signalled. The operation is not atomic; some directories may be created before this happens. In the event of an error there will be no result and therefore no indication of how many directories were created before the error occurred.


