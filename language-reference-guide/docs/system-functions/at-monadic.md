---
search:
  boost: 2
---

# <span>Object Attributes</span> `R←⎕AT Y`{{key}}

`Y` can be a simple character scalar, vector, or matrix, or a vector of character vectors representing the names of 0 or more defined functions or operators. This function returns information that is appropriate for Dyalog APL; for the form that emulates APL2, see [Object Attributes for APL2](at-dyadic.md).

`Y` specifies one or more names. If `Y` specifies a single name as a character scalar, a character vector, or as a scalar enclosed character vector, the result `R` is a vector. If `Y` specifies one or more names as a character matrix or as a vector of character vectors `R` is a matrix with one row per name in `Y`.

`R` is a 4-element vector or a 4 column matrix with the same number of rows as names in `Y` containing the following attribute information:

`R[1]` or `R[;1]`: Each item specifies _valences_: a 3-element integer vector representing the function header syntax:

|---|---|---|
|1|Function result|0 if the function has no result 1 if the function has an explicit result `¯1` if the function has a shy result|
|2|Function valence|0 if the object is a niladic function or not a function 1 if the object is a monadic function 2 if the object is a dyadic function `¯2` if the object is an ambivalent function|
|3|Operator valence|0 if the object is not an operator 1 if the object is a monadic operator 2 if the object is a dyadic operator|

<h4 class="example">Example</h4>

The following values correspond to the syntax shown alongside:

|--------|--------|
| `0 0 0` | `∇ FOO` |
| `1 0 0` | `∇ Z←FOO` |
| `¯1 0 0` | `∇ {Z}←FOO` |
| `0 ¯2 0` | `∇ {A} FOO B` |
| `¯1 1 2` | `∇ {Z}←(F OP G)B` |

`R[2]` or `R[;2]`: Each item specifies _fix times_: the time the function was last fixed, reported as 7 integer elements in the same form as `⎕TS`. The fix time reported for names in `Y` which are not defined functions or operators is 0.

|---|-------------------------------------------|
|1 |Year |
|2 |Month |
|3 |Day |
|4 |Hour |
|5 |Minute |
|6 |Second |
|7 |Milliseconds (this is always reported as 0)|

`R[3]` or `R[;3]`: Each item specifies _execution properties_: an integer reporting the current [`⎕LOCK`](lock-monadic.md) state of the function:

|---|-------------------------|
|`0`|Not locked |
|`1`|Cannot display function |
|`2`|Cannot suspend function |
|`3`|Cannot display or suspend|

`R[4]` or `R[;4]`: Each item specifies the _author_: a character vector – the user name of the user who last fixed (defined) the function.

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

      ]Display ⎕AT 'myop' 'foo' 'util' 'util2'
┌→────────────────────────────────────────────┐
↓ ┌→──────┐ ┌→─────────────────┐     ┌→───┐   │
│ │¯1 ¯2 1│ │1996 8 2 2 13 56 0│   0 │john│   │
│ └~──────┘ └~─────────────────┘     └────┘   │
│ ┌→────┐   ┌→────────────┐          ┌⊖┐      │
│ │1 0 0│   │0 0 0 0 0 0 0│        3 │ │      │
│ └~────┘   └~────────────┘          └─┘      │
│ ┌→─────┐  ┌→──────────────────┐    ┌→───┐   │
│ │1 ¯2 0│  │1996 3 1 14 12 10 0│  0 │pete│   │
│ └~─────┘  └~──────────────────┘    └────┘   │
│ ┌→─────┐  ┌→───────────────────┐   ┌→─────┐ │
│ │1 ¯2 0│  │1998 8 26 16 16 42 0│ 0 │graeme│ │
│ └~─────┘  └~───────────────────┘   └──────┘ │
└∊────────────────────────────────────────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AT
</div>
