---
search:
  boost: 2
---

# <span>Map Array File</span> `R←⎕MAP Y`{{key}}

`⎕MAP` function associates a mapped file with an APL array in the workspace.

To map a file of raw data by giving its type and shape, use [dyadic `⎕MAP`](map-dyadic.md).

An APL mapped file contains the binary representation of a simple Dyalog APL array, including its header. A file of this type must be created using the  utility function `∆MPUT` (supplied in the `util` workspace). When you map an APL file, the rank, shape and data type of the array is obtained from the information on the file.

The right argument `Y` specifies the name of the file to be mapped and, optionally, the access type and a start byte in the file. `Y` can be a simple character vector, or a 2 or 3-element nested vector containing:

1. file name (character scalar/vector)
2. access code (character scalar/vector) : one of : `'R'` or `'r'` (read-only access), `'W'` or `'w'` (read-write access). If not specified, the file is mapped  read-only.
3. start byte offset (integer scalar/vector). This is only applicable for read-only access and is not supported for read-write access. It must be a multiple of the word size (4 on 32-bit systems, 8 on 64-bit systems). The default is 0.

If you map a file with read-only access you can modify the corresponding array in the workspace, however your changes are not written back to the file.

The file contains a simple APL array, complete with header information (type, rank, shape, and so on). Such mapped files can only be updated by changing the associated array using indexed/pick assignment: `var[a]←b`, the new values must be of the same type as the originals.

<h2 class="example">Examples</h2>

First, copy the `∆MPUT` utility from the `util` workspace:
```apl
      '∆MPUT' ⎕CY 'util'
```

Put simple 4-byte integer array on disk ready for mapping:
```apl
      (⊃83 323 ⎕DR 2 3 4⍴⍳24)∆MPUT'c:\myvar'
```

Then, map a read-write variable:
```apl
      var←⎕MAP'c:\myvar' 'w' 
```

Note that a mapped array need not be *named*.

## Compatibility between Editions

In the Unicode Edition `⎕MAP` will fail with a `TRANSLATION ERROR` (event number 92) if you attempt to map an APL file which contains character data type 82.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
