---
search:
  boost: 2
---

# <span>Object Attributes for Dyalog</span> `R←⎕AT Y`{{key}}

This function returns information that is appropriate for Dyalog APL; the [dyadic form](at-dyadic.md) closely emulates the APL2 implementation instead.

!!! Legacy "Legacy"
    `⎕AT` reports a fixed set of attributes, and only for defined functions and operators. [`⎕ATX`](atx.md) reports those and many more, selects exactly the ones wanted, and applies to other kinds of name as well.

## Argument

`Y` can be a simple character scalar, vector, or matrix, or a vector of character vectors representing the names of zero or more defined functions or operators.

## Result

If `Y` specifies a single name as a character scalar, a character vector, or as a scalar enclosed character vector, `R` is a vector. If `Y` specifies one or more names as a character matrix or as a vector of character vectors, `R` is a matrix with one row per name in `Y`.

`R` is a 4-element vector or a 4-column matrix with the same number of rows as names in `Y`, holding the four attributes: [valences](#valences), [fix time](#fix-time), [lock state](#lock-state), and [author](#author). For example:

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

### Valences

Each item of `R[1]` or `R[;1]` is a 3-element integer vector representing the function header syntax:

|---|---|---|
|`1 1⊃R` or `1⊃¨R[;1]`|Function result|`0` if the function has no result, `1` if the function has an explicit result, `¯1` if the function has a [shy](../../../programming-reference-guide/introduction/results#shy-results) result|
|`1 2⊃R` or `2⊃¨R[;1]`|Function valence|`0` if the object is a niladic function or not a function, `1` if the object is a monadic function, `2` if the object is a dyadic function, `¯2` if the object is an ambivalent function|
|`1 3⊃R` or `3⊃¨R[;1]`|Operator valence|`0` if the object is not an operator, `1` if the object is a monadic operator, `2` if the object is a dyadic operator|

<h4 class="example">Examples</h4>

|Syntax|`1⊃⎕AT'FOO'`|
|--------|--------|
| `∇ FOO` | `0 0 0` |
| `∇ Z←FOO` | `1 0 0` |
| `∇ {Z}←FOO` | `¯1 0 0` |
| `∇ {A} FOO B` | `0 ¯2 0` |
| `∇ {Z}←(F FOO G)B` | `¯1 1 2` |

### Fix Time

Each item of `R[2]` or `R[;2]` is the time the function was last fixed, reported as 7 integer elements in the same form as `⎕TS`. The fix time reported for names in `Y` which are not defined functions or operators is `0`, and [`⎕LOCK`](lock.md) clears it, as it has for `foo` above.

|---|-------------------------------------------|
|`2 1⊃R` or `1⊃¨R[;2]`|Year|
|`2 2⊃R` or `2⊃¨R[;2]`|Month|
|`2 3⊃R` or `3⊃¨R[;2]`|Day|
|`2 4⊃R` or `4⊃¨R[;2]`|Hour|
|`2 5⊃R` or `5⊃¨R[;2]`|Minute|
|`2 6⊃R` or `6⊃¨R[;2]`|Second|
|`2 7⊃R` or `7⊃¨R[;2]`|Milliseconds (this is always reported as `0`)|

### Lock State

Each item of `R[3]` or `R[;3]` is an integer reporting the current [`⎕LOCK`](lock.md) state of the function:

|---|-------------------------|
|`0`|Not locked |
|`1`|Cannot display function |
|`2`|Cannot suspend function |
|`3`|Cannot display or suspend|

### Author

Each item of `R[4]` or `R[;4]` is a character vector, the [account name](an.md) of the user who last fixed the function. `⎕LOCK` clears it, as it has for `foo` above.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AT
</div>
