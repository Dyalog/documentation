---
search:
  boost: 2
---

# <span>Map Raw Data File</span> `R←X ⎕MAP Y`{{key}}

This function maps a file of raw data to an array in the workspace, with a given data type and shape. [Monadic `⎕MAP`](map-monadic.md) maps a file that holds an APL array instead.

<h2 class="example">Example</h2>

`data.bin` holds 64-bit floating-point numbers, from 1 to 40, which are mapped as a vector:

```apl
      t←'data.bin' ⎕NCREATE 0 ⋄ (⍳40) ⎕NAPPEND t 645 ⋄ ⎕NUNTIE t
      vec←645 ¯1 ⎕MAP 'data.bin'
      ⍴vec
40
```

!!! windows "Dyalog on Microsoft Windows"
    A file of length zero cannot be mapped.

## Left Argument

`X` is an integer scalar or vector:

|Item |Content|
|-----|-------|
|`⊃X`|The [data type](dr-monadic.md#data-types) of the array|
|`1↓X`|The shape of the array|

The data type is any of the codes that [monadic `⎕DR`](dr-monadic.md) reports, except `326` (pointer) and, in the Unicode Edition, `82`.

One item of the shape (normally the first) can be `¯1`, meaning as many complete records as the file holds. If `X` is a singleton, the array is a scalar, so only the first value in the file is accessible.

<h3 class="example">Examples</h3>

`data.bin`, written in the example above, is mapped as a matrix of 1-byte integers with 20 columns, and as a scalar holding its first byte:

```apl
      ⍴83 ¯1 20 ⎕MAP 'data.bin'
16 20
      83 ⎕MAP 'data.bin'
0
```

## Right Argument

`Y` is a simple character vector containing the name of the file, or a vector of up to 3 items:

|Item |Content|
|-----|-------|
|`⊃Y`|The name of the file|
|`2⊃Y`|The access: `'R'` or `'r'` for read-only access (default), or `'W'` or `'w'` for read-write access|
|`3⊃Y`|The offset of the first byte of the file to map; the default is `0`|

An offset is only permitted with read-only access; with read-write access, it signals `NONCE ERROR`. It must be a multiple of the word size (8 in a 64-bit interpreter, 4 in a 32-bit interpreter).

<h3 class="example">Example</h3>

Bytes 80 to 159 of `data.bin`, written in the example at the top of this page, are mapped as a 5-by-2 matrix:

```apl
      645 5 2 ⎕MAP 'data.bin' 'R' 80
11 12
13 14
15 16
17 18
19 20
```

## Result

`R` is the mapped array. A mapped array does not have to be named; it can be used directly in an expression:

```apl
      +/645 ¯1 ⎕MAP 'data.bin'
820
```

## Updating the File

With read-write access, a change to the array by indexed or pick assignment, for example, `var[a]←b`, is written to the file. With read-only access, the array can still be changed, but the changes are not written to the file.

<h3 class="example">Example</h3>

```apl
      mat←83 ¯1 20 ⎕MAP 'data.bin' 'W'
      mat[2 3;4 5]←2 2⍴⍳4
```

## Compatibility between Editions

In the Unicode Edition, character data that was written to a raw file with data type 82 can be read by mapping the file with data type 83 and using the result `R` to index into [`⎕AVU`](avu.md): `⎕UCS ⎕AVU[⎕IO+256|R]` gives the characters.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MAP MAP
</div>
