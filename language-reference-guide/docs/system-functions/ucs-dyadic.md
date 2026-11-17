---
search:
  boost: 2
---

# <span>Convert Unicode Representation</span> `R←X ⎕UCS Y`{{key}}

This function encodes characters as integers in UTF-8, UTF-16, or UTF-32, and decodes such integers to characters. [Monadic `⎕UCS`](ucs-monadic.md) converts between characters and their code points.

<h2 class="example">Examples</h2>

```apl
      'UTF-8' ⎕UCS 'ABCÆØÅ'
65 66 67 195 134 195 152 195 133
      'UTF-8' ⎕UCS 195 134, 195 152, 195 133
ÆØÅ
      'UTF-8' ⎕UCS 'γεια σου'
206 179 206 181 206 185 206 177 32 207 131 206 191 207 133
      'UTF-16' ⎕UCS 'γεια σου'
947 949 953 945 32 963 959 965
      'UTF-32' ⎕UCS 'γεια σου'
947 949 953 945 32 963 959 965
```

## Left Argument

`X` is the name of an encoding, `'UTF-8'`, `'UTF-16'`, or `'UTF-32'`, in upper case. It can also be a 2-item vector of the name and the [range](#integer-ranges) of the integers, `0` or `83`. Any other value signals `DOMAIN ERROR`.

|`X`|Integers|
|---|--------|
|`'UTF-8'` or `'UTF-8' 0`|Bytes, from `0` to `255`|
|`'UTF-8' 83`|Bytes, from `¯128` to `127`|
|`'UTF-16'` or `'UTF-16' 0`|16-bit code units, with a [surrogate pair](#surrogate-pairs) for each character above `65535`|
|`'UTF-32'` or `'UTF-32' 0`|Code points, as [monadic `⎕UCS`](ucs-monadic.md) gives them|

## Right Argument

`Y` is a simple character vector to encode, or a simple integer vector to decode. A scalar is treated as a 1-item vector, and an array of higher rank signals `RANK ERROR`. Integers that are not a valid encoding signal `DOMAIN ERROR`, for example, an incomplete UTF-8 sequence, or a byte outside the range that `X` gives.

## Result

`R` is a vector of the integers that encode `Y`, or of the characters that `Y` encodes. An empty `Y` gives an empty `R` of the other type. A byte order mark is decoded like any other character, as `⎕UCS 65279`:

```apl
      ⎕UCS 'UTF-8' ⎕UCS 239 187 191 65
65279 65
```

## Integer Ranges

With `'UTF-8' 83`, the bytes are integers from `¯128` to `127`, as in data type 83 of [`⎕DR`](dr.md), instead of from `0` to `255`:

```apl
      'UTF-8' 83 ⎕UCS 'ABCÆØÅ'
65 66 67 ¯61 ¯122 ¯61 ¯104 ¯61 ¯123
      'UTF-8' 83 ⎕UCS ¯61 ¯122, ¯61 ¯104, ¯61 ¯123
ÆØÅ
```

Data type 83 takes less workspace than data type 163, which the range from `0` to `255` needs. It also suits native files, which read and write bytes of data type 83 with conversion code 83, and [`⎕NA`](na.md) functions that pass signed bytes. For example, a native file can hold UTF-8 text:

```apl
      tn←'letters.txt' ⎕NCREATE 0
      ('UTF-8' 83 ⎕UCS 'ABCÆØÅ') ⎕NAPPEND tn
      'UTF-8' 83 ⎕UCS ⎕NREAD tn 83 ¯1 0
ABCÆØÅ
```

## Surrogate Pairs

UTF-16 represents each character up to `65535`, in the [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane), as one code unit, which is its code point. It represents each character above `65535` as a surrogate pair of two code units:

```apl
      'UTF-16' ⎕UCS 'ABCÆØÅ⍒⍋'
65 66 67 198 216 197 9042 9035
      ⎕←unihan←⎕UCS (2×2*16)+⍳3
𠀁𠀂𠀃
      'UTF-16' ⎕UCS unihan
55360 56321 55360 56322 55360 56323
```

!!! Info "Information"
    In the Classic Edition, characters are limited to those in [`⎕AV`](av.md). Converting to a character that is not in `⎕AV` signals `TRANSLATION ERROR`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕UCS UCS
</div>
