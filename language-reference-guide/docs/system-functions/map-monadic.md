---
search:
  boost: 2
---

# <span>Map Array File</span> `R←⎕MAP Y`{{key}}

`⎕MAP` function associates a mapped file with an APL array in the workspace.

Two types of mapped files are supported; *APL* and *raw*. An *APL* mapped file contains the binary representation of a Dyalog APL array, including its header. A file of this type must be created using the  utility function `∆MPUT` (supplied in the `util` workspace). When you map an APL file, the rank, shape and data type of the array is obtained from the information on the file.

A *raw* mapped file is an arbitrary collection of bytes. When you map a raw file, you must specify the characteristics of the APL array to be associated with this data. In particular, the data type and its shape.

The file is assumed to contain a simple APL array.

The right argument `Y` specifies the name of the file to be mapped and, optionally, the access type and a start byte in the file. `Y` may be a simple character vector, or a 2 or 3-element nested vector containing:

1. file name (character scalar/vector)
2. access code (character scalar/vector) : one of : `'R'` or `'r'` (read-only access), `'W'` or `'w'` (read-write access). If not specified, the file is mapped  read-only.
3. start byte offset (integer scalar/vector). This is only applicable for read-only access and is not supported for read-write access. It must be a multiple of the word size (4 on 32-bit systems, 8 on 64-bit systems). The default is 0.

If you map a file with read-only access you may modify the corresponding array in the workspace, however your changes are not written back to the file.

The file contains a simple APL array, complete with header information (type, rank, shape, etc.). Such mapped files may only be updated by changing the associated array using indexed/pick assignment: `var[a]←b`, the new values must be of the same type as the originals.

Note that a *raw* mapped file may be updated *only* if its *file offset* is 0. Note also that Windows does not support mapped files of zero length.

<h2 class="example">Examples</h2>

Map raw file as a read-only *vector* of doubles:

Map raw file as a 20-column read-write *matrix* of 1-byte integers:

Replace some items in mapped file:
```apl
      mat[2 3;4 5]←2 2⍴⍳4
```

Map bytes 100-160 in raw file as a `5×2` read-only matrix of doubles:

Put simple 4-byte integer array on disk ready for mapping:
```apl
      (⊃83 323 ⎕DR 2 3 4⍴⍳24)∆MPUT'c:\myvar'
```

Then, map a read-write variable:
```apl
      var←⎕MAP'c:\myvar' 'w' 
```

Note that a mapped array need not be *named*. In the following example, a 'raw' file is mapped, summed and released, all in a single expression:

If you fail to specify the shape of the data, the data on file will be mapped as a scalar and only the first value in the file will be accessible:

## Compatibility between Editions

In the Unicode Edition `⎕MAP` will fail with a `TRANSLATION ERROR` (event number 92) if you attempt to map an APL file which contains character data type 82.

In order for the Unicode Edition to correctly interpret data in a raw file that was written using data type 82, the file may be mapped with data type 83 and the characters extracted by indexing into `⎕AVU`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
