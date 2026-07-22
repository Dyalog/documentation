---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕UCS UCS
</div>

# <span>Unicode Convert</span> `R←{X} ⎕UCS Y`{{key}}

`⎕UCS` converts (Unicode) characters into integers and vice versa.

The optional left argument `X` is either a simple character vector or a one- or two-element nested vector. `X` or its first element is the name of a variable-length Unicode encoding scheme and must be one of:

- `'UTF-8'`
- `'UTF-16'`
- `'UTF-32'`

The second element (if present) is either `0` (the default) to consume and return byte values as positive integers or `83` to use 1-byte integers (type 83). `83` can only be used with `'UTF-8'`.

If `X` does not abide by the above restrictions, a `DOMAIN ERROR` is issued.

If `X` is omitted, `Y` is a simple character or integer array, and the result `R` is a simple integer or character array with the same rank and shape as `Y`.

If `X` is specified, `Y` must be a simple character or integer vector, and the result `R` is a simple integer or character vector.

## Monadic `⎕UCS`

Monadic `⎕UCS` converts any character array to a numeric array of the same shape, or any numeric array to a character array of the same shape. When doing this, characters are converted to Unicode code points and Unicode code points are converted to characters.

With a few exceptions, the first 256 Unicode code points correspond to the ANSI character set.
```apl

      ⎕UCS 'Hello World'
72 101 108 108 111 32 87 111 114 108 100

      ⎕UCS 2 11⍴72 101 108 108 111 32 87 111 114 108 100
Hello World
Hello World
```

The code points for the Greek alphabet are situated in the 900's:
```apl

      ⎕UCS 'καλημέρα'
954 945 955 951 956 941 961 945

```

Unicode also contains the APL character set. For example:
```apl

      ⎕UCS 123 40 43 47 9077 41 247 9076 9077 125
{(+/⍵)÷⍴⍵}

```

## Dyadic `⎕UCS`

Dyadic `⎕UCS` translates between vectors of Unicode characters and one of three standard Unicode encoding schemes – UTF-8, UTF-16, or UTF-32. These represent a character vector as a vector of integers. In the case of UTF-8, the integers can be specified to be unsigned (the default) or signed.
```apl
      'UTF-8' ⎕UCS 'ABC'
65 66 67
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

### UTF-8 Signed Integers

By default, `⎕UCS` uses unsigned integers. For UTF-8 only, if `X` is `'UTF-8' 83`, `⎕UCS` will instead use signed integers which are then represented as single bytes (type 83). For example:

```apl
      'UTF-8' 83 ⎕UCS 'ABCÆØÅ'
65 66 67 ¯61 ¯122 ¯61 ¯104 ¯61 ¯123
      'UTF-8' 83 ⎕UCS ¯61 ¯122, ¯61 ¯104, ¯61 ¯123
ÆØÅ
      'UTF-8' 83 ⎕UCS 'γεια σου'
¯50 ¯77 ¯50 ¯75 ¯50 ¯71 ¯50 ¯79 32 ¯49 ¯125 ¯50 ¯65 ¯49 ¯123
```
This facilitates storing Unicode text in native files as UTF-8. For example:
```apl
      tn←'letters.txt' ⎕NCREATE 0
      ('UTF-8' 83 ⎕UCS 'ABCÆØÅ') ⎕NAPPEND tn
      'UTF-8' 83 ⎕UCS ⎕NREAD tn 83 ¯1 0
ABCÆØÅ
```

### UTF-16 and UCS-2

For most characters in the [first plane of Unicode (0000-FFFF)](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane), UTF-16 and UCS-2 are identical. However, UTF-16 can encode all Unicode characters by using up to two code units for each character.
```apl

      'UTF-16' ⎕UCS 'ABCÆØÅ⍒⍋'
65 66 67 198 216 197 9042 9035
      ⎕←unihan←⎕UCS (2×2*16)+⍳3 ⍝ x20001-x20003

      'UTF-16' ⎕UCS unihan
55360 56321 55360 56322 55360 56323
```

## Translation Error

`⎕UCS` will generate a `DOMAIN ERROR` if the argument cannot be converted. Additionally, in the Classic Edition, a `TRANSLATION ERROR` is generated if the result is not in `⎕AV` or the numeric argument is not in `⎕AVU`.
