---
search:
  boost: 2
---

# <span>Object Attributes for APL2</span> `R←X ⎕AT Y`{{key}}

`Y` can be a simple character scalar, vector, or matrix, or a vector of character vectors representing the names of 0 or more defined functions or operators. This function closely emulates the APL2 implementation; for the form that returns information more appropriate to Dyalog APL, see [Object Attributes](at-monadic.md).

`Y` specifies one or more names. If `Y` specifies a single name as a character scalar, a character vector, or as a scalar enclosed character vector, the result `R` is a vector. If `Y` specifies one or more names as a character matrix or as a vector of character vectors `R` is a matrix with one row per name in `Y`.

It returns the same rank and shape result containing information that matches the APL2 implementation as closely as possible.

The number of elements or columns in `R` and their meaning depends upon the value of `X` which can be 1, 2, 3, or 4.

If `X` is 1, `R` specifies _valences_ and contains 3 elements (or columns) whose meaning is as follows:

|---|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
|1 |Explicit result |1 if the object has an explicit result or is a variable 0 otherwise |
|2 |Function valence|0 if the object is a niladic function or not a function 1 if the object is a monadic function 2 if the object is an ambivalent function|
|3 |Operator valence|0 if the object is not an operator 1 if the object is a monadic operator 2 if the object is a dyadic operator |

<h4 class="example">Examples</h4>

The following values correspond to the syntax shown alongside:

|-----|--------|
| `0 0 0` | `∇ FOO` |
| `1 0 0` | `∇ Z←FOO` |
| `1 0 0` | `∇ {Z}←FOO` |
| `0 2 0` | `∇ {A} FOO B` |
| `1 1 2` | `∇ {Z}←(F OP G)B` |

If `X` is 2, `R` specifies _fix times_ (the time the object was last updated) for functions and operators named in `Y`. The time is reported as 7 integer elements (or columns) in the same form as `⎕TS`, whose meaning is as follows. The fix time reported for names in `Y` which are not defined functions or operators is 0.

|---|-------------------------------------------|
|1 |Year |
|2 |Month |
|3 |Day |
|4 |Hour |
|5 |Minute |
|6 |Second |
|7 |Milliseconds (this is always reported as 0)|

If `X` is 3, `R` specifies _execution properties_ and contains 4 elements (or columns) whose meaning is as follows:

|---|------------------------|---------------------------------------------------------------------------------------|
|1 |Displayable |0 if the object is displayable 1 if the object is not displayable |
|2 |Suspendable |0 if execution will suspend in the object 1 if execution will not suspend in the object|
|3 |Weak Interrupt behaviour|0 if the object responds to interrupt 1 if the object ignores interrupt |
|4 |&nbsp; |(always 0) |

If `X` is 4, `R` specifies _object size_ and contains 2 elements (or columns) that both report the `⎕SIZE` of the object.

<h2 class="example">Examples</h2>

```apl
    ∇ {z}←{l}(fn myop)r

[1] ...

    ∇ z←foo

[1] ...

    ∇ z←{larg}util rarg

[1] ...

      ⎕LOCK'foo'

      util2←util

      1 ⎕AT 'myop' 'foo' 'util' 'util2'
1 2 1
1 0 0
1 2 0
1 2 0

      2 ⎕AT'myop' 'foo' 'util' 'util2'
1996 8  2  2 13 56 0
   0 0  0  0  0  0 0
1996 3  1 14 12 10 0
1998 8 26 16 16 42 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AT
</div>
