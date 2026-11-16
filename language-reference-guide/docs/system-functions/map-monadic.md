---
search:
  boost: 2
---

# <span>Map Array File</span> `R←⎕MAP Y`{{key}}

This function maps a file that holds a simple APL array to an array in the workspace. The data type, rank, and shape of the array are recorded in the file. [Dyadic `⎕MAP`](map-dyadic.md) maps a file of raw data instead.

A file of this kind is written by the function `∆MPUT` in the `util` workspace.

<h2 class="example">Example</h2>

```apl
      '∆MPUT' ⎕CY 'util'
      (2 3 4⍴⍳24) ∆MPUT 'var.dat'
      var←⎕MAP 'var.dat' 'W'
      ⍴var
2 3 4
      var[1;1;1]←99
```

## Right Argument

`Y` is a simple character vector containing the name of the file, or a vector of up to 2 items:

|Item |Content|
|-----|-------|
|`⊃Y`|The name of the file|
|`2⊃Y`|The access: `'R'` or `'r'` for read-only access (default), or `'W'` or `'w'` for read-write access|

A file that was not written by `∆MPUT` signals `NONCE ERROR`.

## Result

`R` is the mapped array, with the data type, rank, and shape recorded in the file. A mapped array does not have to be named; it can be used directly in an expression.

## Updating the File

With read-write access, a change to the array by indexed or pick assignment, for example, `var[a]←b`, is written to the file. The new values must be representable in the data type of the array, otherwise `FILE ACCESS ERROR` is signalled. Assigning a new value to the name of the array does not change the file.

With read-only access, the array can still be changed, but the changes are not written to the file.

## Compatibility between Editions

In the Unicode Edition, `⎕MAP` signals `TRANSLATION ERROR` for a file that holds character data of data type 82.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
