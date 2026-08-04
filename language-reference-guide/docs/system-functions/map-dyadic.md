---
search:
  boost: 2
---

# <span>Map Raw Data File</span> `R←X ⎕MAP Y`{{key}}

`⎕MAP` function associates a mapped file with an APL array in the workspace.

A raw mapped file is an arbitrary collection of raw data bytes. When you map a raw file, you must specify the characteristics of the APL array to be associated with this data. In particular, the data type and its shape.

The right argument `Y` specifies the name of the file to be mapped and, optionally, the access type and a start byte in the file. `Y` may be a simple character vector, or a 2 or 3-element nested vector containing:

1. file name (character scalar/vector)
2. access code (character scalar/vector) : one of : `'R'` or `'r'` (read-only access), `'W'` or `'w'` (read-write access). If not specified, the file is mapped  read-only.
3. start byte offset (integer scalar/vector). This is only applicable for read-only access and is not supported for read-write access. It must be a multiple of the word size (4 on 32-bit systems, 8 on 64-bit systems). The default is 0.

If you map a file with read-only access you may modify the corresponding array in the workspace, however your changes are not written back to the file.

`X` defines the type and shape to be associated with raw data on file. `X` must be an integer scalar or vector. The first item of `X` specifies the data type and must be one of the following values:

|---------------|-------------------------------------|
|Classic Edition|11, 82, 83, 163, 323 or 645          |
|Unicode Edition|11, 80, 83, 160, 163, 320, 323 or 645|

The values are more fully explained in [Data Representation (Monadic)](data-representation-monadic.md).

Following items determine the shape of the mapped array. A value of `¯1` on any (but normally the first) axis in the shape is replaced by the system to mean: read as many complete records from the file as possible. Only one axis may be specified in this way. Note that if    `X` is a singleton, the data on the file is mapped as a scalar and only the first value on the file is accessible.

Note that a raw mapped file may be updated *only* if its *file offset* is 0. Note also that Windows does not support mapped files of zero length.

<h2 class="example">Examples</h2>

Map raw file as a read-only *vector* of doubles:
```apl
      vec←645 ¯1 ⎕MAP'c:\myfile'
```

Map raw file as a 20-column read-write *matrix* of 1-byte integers:
```apl
      mat←83 ¯1 20 ⎕MAP'c:\myfile' 'W' 
```

Replace some items in mapped file:
```apl
      mat[2 3;4 5]←2 2⍴⍳4
```

Map bytes 100-160 in raw file as a `5×2` read-only matrix of doubles:
```apl
      dat←645 5 2 ⎕MAP'c:\myfile' 'R' 80
```

Note that a mapped array need not be *named*. In the following example, a 'raw' file is mapped, summed and released, all in a single expression:
```apl
      +/163 ¯1 ⎕MAP'c:\shorts.dat'
42
```

If you fail to specify the shape of the data, the data on file will be mapped as a scalar and only the first value in the file will be accessible:
```apl
      83 ⎕MAP 'myfile'   ⍝ map FIRST BYTE of file.
¯86
```

## Compatibility between Editions

In order for the Unicode Edition to correctly interpret data in a raw file that was written using data type 82, the file may be mapped with data type 83 and the characters extracted by indexing into `⎕AVU`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
