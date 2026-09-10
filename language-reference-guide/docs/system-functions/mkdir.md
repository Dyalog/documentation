---
search:
  boost: 2
---

# <span>Create Directory</span> `{R}←{X}⎕MKDIR Y`{{key}}

This function creates new directories.

`Y` is a character vector or scalar containing a single directory name, or a vector of character vectors containing zero or more directory names. Names must conform to the naming rules of the host Operating System.

By default, for each name in `Y` the path must exist and the base name must not exist (see [File Name Parts](nparts.md)), otherwise an error is signalled. The optional left argument `X` and the variant option `Unique` can be used to amend this behaviour.

The result `R` reports what was created. Both its form and whether it is [shy](../../../programming-reference-guide/introduction/results#shy-results) depend on the [`Unique` variant option](#variant-option-unique).

The optional left argument `X` is a numeric scalar that modifies the default behaviour when the base name in `Y` already exists and/or the path in `Y` does not already exist:

| `X` | Effect on Behaviour |
|---|---|
| `0` <small>(default)</small> | The base name in `Y` must not exist and the path in `Y` must exist, otherwise an error is signalled.                                                                           |
|`1`|No action is taken if a directory specified by `Y` already exists (the return value indicates whether a new directory was created). Has no effect when the variant option `Unique` is set.|
|`2`|Any part of the *paths* specified in `Y` which does not already exist will be created in preparation of creating the corresponding directory.                                               |
|`3`|Combination of `1` and `2`.                                                                                                                                                                     |

If a directory cannot be created (for example, if a directory with that name already exists, or write access is denied), then an error is signalled.

<h2 class="example">Examples</h2>
```apl

      ⎕NEXISTS '/Users/Pete/Documents/temp'
0
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
1
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
FILE NAME ERROR: /Users/Pete/Documents/temp: Already exists
      ⎕←⎕MKDIR '/Users/Pete/Documents/temp'
        ∧

      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
FILE NAME ERROR: /Users/Pete/Documents/temp/t1/t2: Unable to create directory
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
        ∧

      ⎕←2 ⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
1

      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
FILE NAME ERROR: /Users/Pete/Documents/temp/t1/t2: Already exists
      ⎕←⎕MKDIR'/Users/Pete/Documents/temp/t1/t2'
        ∧

      ⎕←⎕MKDIR'temp1' 'temp2'
1 1
```

When multiple names are specified, they are processed in the order given. If an error occurs at any point whilst creating directories, processing immediately stops and an error is signalled. The operation is not atomic; some directories might be created before this happens. In the event of an error, there is no result and therefore no indication of how many directories were created before the error occurred.

## Variant Options

`⎕MKDIR` supports one variant option, `Unique`. There is no principal option.

### Variant Option: `Unique`

The `Unique` variant option (a Boolean) specifies whether the base name (see [File Name Parts](nparts.md)) in `Y` is modified so that the name is unique, that is, does not already exist. It also determines the form of the result, which is shy when `Unique` is `0` and not shy when it is `1`. The default is `0`.

Table: The `Unique` variant option { #uniqueoptionformkdir }

| `Unique` | Effect on Behaviour | `R` when `Y` is a single name | `R` when `Y` is a vector of names |
|---|---|---|---|
|`0` <small>(default)</small>|The directory named in `Y` is created.|a scalar `1` if a directory was created, or `0` if not|a vector of `1`s and `0`s with the same length as `Y`|
|`1`|The name in `Y` is extended with random characters to make it unique, and that directory is created.|a character vector containing the name of the directory that was created|a vector of character vectors with the same length as `Y`|

<h4 class="example">Example</h4>

```apl
      (⎕MKDIR⍠'Unique'1)'/Users/Pete/Documents/temp/t1/t2'
/Users/Pete/Documents/temp/t1/t2djM0X8
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MKDIR MKDIR
</div>
