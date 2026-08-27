---
search:
  exclude: true
---
# Notes

## Implicit Arguments

_Implicit arguments_ are system functions that affect the result of a primitive function. They are all variables that have a global effect, only limited by the current namespace and function scope (if localised). Implicit argument propagate to newly created namespaces and defined functions at creation/definition time.

!!! Hint "Hints and Recommendations"
    Unexpected values of implicit arguments, especially `⎕IO` and `⎕ML`, are a frequent source of confusion. Dyalog Ltd strongly recommends ensuring that deviations from the default values are limited and local. If a primitive function is not giving the expected result, check the values of its implicit arguments. The status bar of Ride and the Windows IDE shows the current value of `⎕IO` and `⎕ML` and highlights them if they differ from the default values as set by [DEFAULT_IO](../../windows-installation-and-configuration-guide/configuration-parameters/default-io.md) and [DEFAULT_ML](../../windows-installation-and-configuration-guide/configuration-parameters/default-ml.md).

Table: Settings Affecting Behaviour of Primitive Functions { #sysvars }

|System Function  |Name                              |
|------|-----------------------------------------|
|[`⎕CT`](../system-functions/ct.md) |Comparison Tolerance         |
|[`⎕DCT`](../system-functions/dct.md)|Decimal Comp Tolerance      |
|[`⎕DIV`](../system-functions/div.md)|Division Method             |
|[`⎕FR`](../system-functions/fr.md) |Floating-Point Representation|
|[`⎕IO`](../system-functions/io.md) |Index Origin                 |
|[`⎕ML`](../system-functions/ml.md) |Migration Level              |
|[`⎕PP`](../system-functions/pp.md) |Print Precision              |
|[`⎕RL`](../system-functions/rl.md) |Random Link                  |

The dependencies that exist between the system functions shown in [](#sysvars) and the primitive functions are shown in [](#implicitargs).

Table: Implicit arguments { #implicitargs }

|System Function  |Monadic Functions | Dyadic Functions       |
|------|-----------------|-----------------------|
|`⎕CT`, `⎕DCT`| [`⌈`](ceiling.md) [`⌊`](floor.md) [`∪`](unique.md) [`≠`](unique-mask.md) |[`~`](without.md) [`<`](less-than.md) [`≤`](less-than-or-equal-to.md) [`=`](equal-to.md) [`≥`](greater-than-or-equal-to.md) [`>`](greater-than.md) [`≠`](not-equal-to.md) [`≡`](match.md) [`≢`](not-match.md) [`⍳`](index-of.md) [`∊`](membership.md) [`∪`](union.md) [`∩`](intersection.md) [`⍷`](find.md) [`|`](magnitude.md) [`∨`](greatest-common-divisor-or.md) [`∧`](lowest-common-multiple-and.md)|
|`⎕DIV`       | [`÷`](reciprocal.md)        | [`÷`](divide.md)|
|`⎕FR`<sup>1</sup>  | [`÷`](reciprocal.md) [`*`](exponential.md) [`⍟`](natural-logarithm.md) [`!`](factorial.md) [`○`](pi-times.md) [`⌹`](matrix-inverse.md)| [`+`](plus.md) [`-`](minus.md) [`×`](times.md) [`÷`](divide.md) [`*`](power.md) [`⍟`](logarithm.md) [`|`](magnitude.md) [`!`](binomial.md) [`○`](circular-functions.md) [`∨`](greatest-common-divisor-or.md) [`∧`](lowest-common-multiple-and.md) [`⊥`](decode.md) [`⊤`](encode.md) [`⌹`](matrix-divide.md)|
|`⎕FR`<sup>2</sup>  | [`⌈`](ceiling.md) [`⌊`](floor.md) [`∪`](unique.md)| [`~`](without.md) [`<`](less-than.md) [`≤`](less-than-or-equal-to.md) [`=`](equal-to.md) [`≥`](greater-than-or-equal-to.md) [`>`](greater-than.md) [`≠`](not-equal-to.md) [`≡`](match.md) [`≢`](not-match.md) [`⍳`](index-of.md) [`∊`](membership.md) [`∪`](union.md) [`∩`](intersection.md) [`⍷`](find.md)|
|`⎕FR`<sup>3</sup>  | [`⍒`](grade-down.md) [`⍋`](grade-up.md)| [`⌈`](maximum.md) [`⌊`](minimum.md) [`⍒`](dyadic-grade-down.md) [`⍋`](dyadic-grade-up.md) [`⍸`](interval-index.md)|
|`⎕IO`        | [`⍳`](index-generator.md) [`?`](roll.md) [`⍒`](grade-down.md) [`⍋`](grade-up.md) [`⍸`](where.md)| [`⍳`](index-of.md) [`?`](deal.md) [`⍒`](dyadic-grade-down.md) [`⍋`](dyadic-grade-up.md) [`⍉`](dyadic-transpose.md) [`⊃`](pick.md) [`⌷`](index-function/index.md) [`⍸`](interval-index.md)|
|`⎕ML`        | [`∊`](enlist.md) [`↑`](mix.md) [`⊃`](first.md) [`≡`](depth.md)| [`⊂`](partitioned-enclose.md)|
|`⎕PP`        | [`⍕`](format.md)|  |
|`⎕RL`        | [`?`](roll.md)| [`?`](deal.md)|

In [](#implicitargs):

- `⎕FR`<sup>1</sup> indicates functions that compute real numbers and whose precision depends on `⎕FR`
- `⎕FR`<sup>2</sup> indicates functions that perform tolerant comparisons
- `⎕FR`<sup>3</sup> indicates functions that perform intolerant comparisons.

!!! Info "Information"
    Tolerant comparisons depend on `⎕FR` to select which of `⎕CT` and `⎕DCT` is used; `⎕FR` also determines the precision of the comparison computation that can affect results. However, even primitives involving intolerant comparison (including the tolerant ones with all comparison tolerances set to `0`) can depend on `⎕FR` if the argument contains DECFs. This is because DECFs must be converted to doubles for comparison. If two DECFs are different but correspond to the same double, then they will be treated as intolerantly unequal when `⎕FR` is `1287` but equal when it is `645`.

<h2 class="example">Examples</h2>

```apl
      ⍳4
1 2 3 4
      ⎕IO←0
      ⍳4
0 1 2 3

      ≢⍕⎕←÷3
0.3333333333
12
      ⎕PP←4
      ≢⍕⎕←÷3
0.3333
6
```

## Conformability

The arguments of a dyadic function _conform_ if the shape of each argument meets the requirements of the function, possibly after [singleton extension](#scalar-and-singleton-extension).

For a [dyadic scalar function](primitive-functions-by-category.md#dyadic-scalar-functions), the arguments conform if they have the same shape, or if one of them is a [singleton](#scalar-and-singleton-extension) (in particular, a scalar), which is then extended to the shape of the other. Otherwise, the function signals a `RANK ERROR` if the arguments have different ranks, or a `LENGTH ERROR` if they have the same rank but different shapes.

Mixed (non-scalar) primitive functions impose their own conformance requirements, which are described with each function.

<h2 class="example">Examples</h2>
```apl
      2 3 4 + 10 20 30    ⍝ same shape
12 23 34
      10 + 2 3 4          ⍝ scalar (a singleton) extended
12 13 14
      (2 3⍴⍳6) + 10       ⍝ scalar extended to a matrix
11 12 13
14 15 16
      (2 3⍴⍳6) + 1 2 3    ⍝ different rank
RANK ERROR: Mismatched left and right argument ranks
      (2 3⍴⍳6)+1 2 3
              ∧
      1 2 + 1 2 3         ⍝ same rank, different length
LENGTH ERROR: Mismatched left and right argument shapes
      1 2+1 2 3
         ∧
```

## Scalar and Singleton Extension

A _singleton_ is an array with exactly one element, of any rank: a scalar, a one-element vector, a one-by-one matrix, and so on. An array `Y` is a singleton if `1=×/⍴Y`. When a dyadic scalar function is applied to a singleton and a non-singleton, the singleton is extended to conform with the other argument, and the result takes the shape of the non-singleton argument.

<h2 class="example">Examples</h2>
```apl
      (1 1⍴5) + 2 3⍴⍳6    ⍝ a one-by-one matrix extends to the matrix
6  7  8
9 10 11
      (,5) + 2 3⍴⍳6       ⍝ a one-element vector likewise
6  7  8
9 10 11
```

If both arguments are singletons, the result takes the shape of the one with the higher rank.
```apl
      ⍴ (1 1⍴5) + ,2
1 1
```

An array with a one-length axis but more than one element (such as a `1 3` matrix) is not a singleton and does not extend.
```apl
      (1 3⍴1 2 3) + 2 3⍴⍳6
LENGTH ERROR: Mismatched left and right argument shapes
      (1 3⍴1 2 3)+2 3⍴⍳6
                 ∧
```

!!! Hint "Hints and Recommendations"
    Singleton extension can lead to surprising or inconsistent results; it is, therefore, recommended to rely on scalar extension only. In this example, `N←1` returns a matrix while all other values return a vector:
    ```apl
          ⍴(1 1⍴10)+⍳N←3
    3
          ⍴(1 1⍴10)+⍳N←2
    2
          ⍴(1 1⍴10)+⍳N←1
    1 1
          ⍴(1 1⍴10)+⍳N←0
    0
    ```

## Fill Elements and Prototypes

Some primitive functions can include _fill elements_ in their result. The fill element for an array is the enclosed first _prototypical element_ or _prototype_ of the array. The _type_ function ([`∊`](type.md) with `⎕ML←0`) converts an array to consist entirely of prototypical elements; `⎕NULL`s remain unchanged, numbers become zeros, character become spaces, and instances are replaced with new instances of their classes (if they have niladic constructors). With `⎕ML←1` (the default), _type_ can be written as `⊃0⍴⊂` (this exploits the prototype, since, if the array is empty, `⊃Y` gives the disclosed prototype of `Y`).

Primitive functions that can return an array including fill elements are _first_ ([`⊃`](first.md)), _expand_ ([`\`](expand.md) or [`⍀`](expand-first.md)), _replicate_ ([`/`](replicate.md) or [`⌿`](replicate-first.md)), _reshape_ ([`⍴`](reshape.md)), _mix_ ([`↑`](mix.md)), and _take_ ([`↑`](take/index.md)).

<h2 class="example">Examples</h2>

```apl
      Type←⊃0⍴⊂
      Type⍳5
0 0 0 0 0
      ⊂Type⊃⍳5
0
      7↑⍳5
1 2 3 4 5 0 0

      Type⊃(1 2 3)'ABC'
0 0 0
      1 0 1\(1 2 3)'ABC'
┌─────┬─────┬───┐
│1 2 3│0 0 0│ABC│
└─────┴─────┴───┘

      ↑'ABC' 'DE'
ABC
DE 
      ]Repr Type⊃↑'ABC' 'DE'
' '
      ' '=↑'ABC' 'DE'
0 0 0
0 0 1
```

!!! Info "Information"
    The fill element only replaces simple scalars, but does not change lengths. For example, a vector of vectors fills with elements of the same length as the first element, not with empty vectors:
    ```apl
          4↑'Anna' 'Bob'
    ┌────┬───┬────┬────┐
    │Anna│Bob│    │    │
    └────┴───┴────┴────┘
    ```
    There is only one prototype for each array, so a zero-row matrix does not remember the types of its columns:
    ```apl
          1↑0 3⍴(1 2 3) 42 'ABC'
    ┌─────┬─────┬─────┐
    │0 0 0│0 0 0│0 0 0│
    └─────┴─────┴─────┘
    ```

## Axis Specification

Axis specification can be applied to certain mixed primitive functions and to all [dyadic scalar functions](primitive-functions-by-category.md#dyadic-scalar-functions). An integer axis identifies a specific axis along which the function is to be applied to one or both of its arguments. Mixed primitive functions have a default axis, either the first or last.

<h2 class="example">Example</h2>
```apl
      1 0 1 ⌿[2] 2 3⍴⍳6
1 3
4 6

      1 2 3 +[2] 2 3⍴10 20 30
11 22 33
11 22 33
```

Some mixed primitive functions allow a fractional axis value, indicating that a new axis or axes are to be created between the axes identified by the lower and upper integer bounds of the value (either of which might not exist).

<h2 class="example">Example</h2>

```apl
      'NAMES' ,[0.5] '='
NAMES
=====
```

Some mixed primitive functions allow a vector axis value, indicating an operation over a collection of axes.

<h2 class="example">Example</h2>

```apl
      ⍴ ,[2 3] 1 3 4 2⍴⎕A
1 12 2
```

`⎕IO` is an [implicit argument](#implicit-arguments) of axis specification.

!!! Hint "Hints and Recommendations"
    Axis specification only applies to a specific set of primitives and never to defined functions. The [_rank_ operator](../primitive-operators/rank.md) is a more general mechanism. If the function operates along the leading axis, then it can substitute for most axis specifications, particularly in combination with _transpose_ ([`⍉`](transpose.md)). For example:
    ```apl
          1 0 1(⌿⍤1) 2 3⍴⍳6
    1 3
    4 6
          'NAMES' (⍉,⍤0) '='
    NAMES
    =====
    ```
    If we wanted to replace `,` with a defined function that does something similar, then the surrounding code would be identical for the _rank_ operator but axis specification would fail:
    ```apl
          'NAMES' (⍉{⍺,' ',⍵}⍤0) '='
    NAMES
         
    =====
          'NAMES' {⍺,' ',⍵}[0.5] '='
    SYNTAX ERROR
          'NAMES'{⍺,' ',⍵}[0.5]'='
                 ∧
    ```

## Migration Level

The system variable [`⎕ML`](../system-functions/ml.md) (_migration level_) migrates the interpretation of certain primitive functions towards IBM APL2, affecting five primitives:

| Primitive | `⎕ML≤` | Meaning | `⎕ML≥` | Meaning |
|---|--:|---|--:|---|
| Monadic `∊` | 0 | [_type_](type.md) | 1 | [_enlist_](enlist.md)
| Monadic `↑` | 1 | [_mix_](mix.md) | 2 | [_first_](first.md)
| Monadic `⊃` | 1 | [_first_](first.md) | 2 | [_mix_](mix.md)
| Monadic `≡` | 1 | [_depth_](depth.md) with indication of non-uniformity | 2 | deepest [_depth_](depth.md) |
| Dyadic `⊂`  | 2 | [_partitioned enclose_](partitioned-enclose.md) | 3 | [_partition_](partition.md) |

The default is `1`. See [`⎕ML`](../system-functions/ml.md) for the exact effects at each level.
