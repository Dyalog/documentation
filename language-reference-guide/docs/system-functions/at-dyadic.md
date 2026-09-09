---
search:
  boost: 2
---

# <span>Object Attributes for APL2</span> `R←X ⎕AT Y`{{key}}

This function closely emulates the APL2 implementation; the [monadic form](at-monadic.md) returns information more appropriate to Dyalog APL instead.

!!! Legacy "Legacy"
    `⎕AT` reports a fixed set of attributes, and only for defined functions and operators. [`⎕ATX`](atx.md) reports those and many more, selects exactly the ones wanted, and applies to other kinds of name as well.

## Left Argument

`X` can be `1`, `2`, `3`, or `4`, and selects which group of attributes `R` reports: [valences](#valences), [fix time](#fix-time), [execution properties](#execution-properties), or [object size](#object-size).

## Right Argument

`Y` can be a simple character scalar, vector, or matrix, or a vector of character vectors representing the names of zero or more defined functions or operators.

## Result

If `Y` specifies a single name as a character scalar, a character vector, or as a scalar enclosed character vector, `R` is a vector. If `Y` specifies one or more names as a character matrix or as a vector of character vectors, `R` is a matrix with one row per name in `Y`.

`R` contains information that matches the APL2 implementation as closely as possible. The number of elements or columns and their meaning depend upon the value of `X`.

The examples below all use these definitions:

```apl
    ∇ {z}←{l}(fn myop)r
[1] ...

    ∇ z←foo
[1] ...

    ∇ z←{larg}util rarg
[1] ...

      ⎕LOCK'foo'

      util2←util
```

### Valences

If `X` is `1`, `R` contains 3 elements (or columns) whose meaning is as follows:

|---|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
|`R[1]` or `R[;1]`|Explicit result|`1` if the object has an explicit result or is a variable, `0` otherwise|
|`R[2]` or `R[;2]`|Function valence|`0` if the object is a niladic function or not a function, `1` if the object is a monadic function, `2` if the object is a dyadic or ambivalent function|
|`R[3]` or `R[;3]`|Operator valence|`0` if the object is not an operator, `1` if the object is a monadic operator, `2` if the object is a dyadic operator|

<h4 class="example">Examples</h4>

|Syntax|`1⎕AT'FOO'`|
|-----|--------|
| `∇ FOO` | `0 0 0` |
| `∇ Z←FOO` | `1 0 0` |
| `∇ {Z}←FOO` | `1 0 0` |
| `∇ {A} FOO B` | `0 2 0` |
| `∇ {Z}←(F FOO G)B` | `1 1 2` |

```apl
      1 ⎕AT 'myop' 'foo' 'util' 'util2'
1 2 1
1 0 0
1 2 0
1 2 0
```

### Fix Time

If `X` is `2`, `R` reports the time each object named in `Y` was last updated, as 7 integer elements (or columns) in the same form as `⎕TS`. The fix time reported for names in `Y` which are not defined functions or operators is `0`, and [`⎕LOCK`](lock.md) clears it, as it has for `foo` below.

|---|-------------------------------------------|
|`R[1]` or `R[;1]`|Year|
|`R[2]` or `R[;2]`|Month|
|`R[3]` or `R[;3]`|Day|
|`R[4]` or `R[;4]`|Hour|
|`R[5]` or `R[;5]`|Minute|
|`R[6]` or `R[;6]`|Second|
|`R[7]` or `R[;7]`|Milliseconds (this is always reported as `0`)|

```apl
      2 ⎕AT'myop' 'foo' 'util' 'util2'
1996 8  2  2 13 56 0
   0 0  0  0  0  0 0
1996 3  1 14 12 10 0
1998 8 26 16 16 42 0
```

### Execution Properties

If `X` is `3`, `R` contains 4 elements (or columns) whose meaning is as follows:

|---|------------------------|---------------------------------------------------------------------------------------|
|`R[1]` or `R[;1]`|Displayable|`0` if the object is displayable, `1` if the object is not displayable|
|`R[2]` or `R[;2]`|Suspendable|`0` if execution will suspend in the object, `1` if execution will not suspend in the object|
|`R[3]` or `R[;3]`|Weak Interrupt behaviour|`0` if the object responds to interrupt, `1` if the object ignores interrupt|
|`R[4]` or `R[;4]`|&nbsp;|(always `0`)|

### Object Size

If `X` is `4`, `R` contains 2 elements (or columns) that both report the `⎕SIZE` of the object.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AT
</div>
