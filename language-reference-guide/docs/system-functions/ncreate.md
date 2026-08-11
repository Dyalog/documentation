---
search:
  boost: 2
---

# <span>Native File Create</span> `{R}←X ⎕NCREATE Y`{{key}}

This function creates a new file. Under Windows the file is opened with mode 66 (see [Native File Tie](ntie.md)). Under non-Windows operating systems the current umask will specify the file permissions. The name of the new file is specified by the left argument `X` which must be a simple character vector or scalar containing a valid pathname for the file.

`Y` is 0 or a negative integer value that specifies an (unused) tie number by which the file can subsequently be referred. If `Y` is 0, the system allocates the first (closest to zero) available tie number which is returned as the result.

The [shy](../../../programming-reference-guide/introduction/results#shy-results) result of `⎕NCREATE` is the tie number of the new file.

## Variant Options

`⎕NCREATE` supports two variant options, `Unique` and `IfExists`, summarised in [](#variantoptionsforncreate) and described in detail beneath it. There is no principal option.

Table: Variant options for `⎕NCREATE` { #variantoptionsforncreate }

|Variant Option|Valid Values|Default|Effect|
|---|---|---|---|
|[`Unique`](#variant-option-unique)|`0` or `1`|`0`|Whether the created file is given a uniquely generated name.|
|[`IfExists`](#variant-option-ifexists)|`'Error'` or `'Replace'`|`'Error'`|What happens when the named file already exists.|

### Variant Option: `Unique`

The `Unique` variant option (a Boolean) specifies whether a uniquely named file is created.

|---|---|
|`0` <small>(default)</small>|the file named by `X` will be created|
|`1`|a uniquely named file will be created by extending the base name (see [File Name Parts](nparts.md) ) with random characters. If a unique name cannot be created then an error will be signalled. The actual name of the file can be determined from `⎕NNAMES` or `⎕NINFO` .|

### Variant Option: `IfExists`

The `IfExists` variant option (a character vector) specifies what happens when the named file already exists.

|Value|Description|
|---|---|
|`'Error'` <small>(default)</small>|`⎕NCREATE` will generate a `FILE NAME ERROR` if the file already exists|
|`Replace`         |`⎕NCREATE` will replace an existing file with an empty one of the same name.|

<h2 class="example">Examples</h2>
```apl
      ⊢'myfile' ⎕NCREATE 0
¯1
      ⎕NUNTIE ¯1
      ⊢'myfile' ⎕NCREATE 0
FILE NAME ERROR: myfile: Unable to create file ("The file exists.")
      ⊢'myfile'⎕NCREATE 0
               ∧
```
```apl

      ⊢'myfile' (⎕NCREATE⍠'IfExists' 'Replace') 0
```
```apl
¯1    ⍝ Note that it uses same tie number as before

```
```apl

      ⊢'myfile' (⎕NCREATE⍠('Unique' 1)) 0
¯2
      ⎕NNUMS,⎕NNAMES
¯1 myfile      
¯2 myfile52c36z

```

## Notes

- Setting `IfExists` to `'Replace'` has no effect when `Unique` is `1`, because the file cannot already exist.
- The `IfExists` option does not affect the operation of *slippery ties*.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NCREATE NCREATE
</div>
