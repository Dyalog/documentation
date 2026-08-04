---
search:
  exclude: true
---
# Notes

## Implicit Arguments

_Implicit arguments_ are system functions that affect the behaviour/result of a primitive function.

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
|`⎕ML`        | [`∊`](enlist.md) [`↑`](mix.md) [`⊃`](first.md) [`≡`](depth.md) [`⊂`](enclose.md) [`⊆`](nest.md)|  |
|`⎕PP`        | [`⍕`](format.md)|  |
|`⎕RL`        | [`?`](roll.md)| [`?`](deal.md)|

In [](#implicitargs):

- `⎕FR`<sup>1</sup> indicates functions that compute real numbers and whose precision depends on `⎕FR`
- `⎕FR`<sup>2</sup> indicates functions that perform tolerant comparisons
- `⎕FR`<sup>3</sup> indicates functions that perform tolerant comparisons.

!!! Info "Information"
    Tolerant comparisons depend on `⎕FR` to select which of `⎕CT` and `⎕DCT` is used; `⎕FR` also determines the precision of the comparison computation that can affect results. However, even primitives involving intolerant comparison (including the tolerant ones with all comparison tolerances set to `0`) can depend on `⎕FR` if the argument contains DECFs. This is because DECFs must be converted to doubles for comparison. If two DECFs are different but correspond to the same double, then they will be treated as intolerantly unequal when `⎕FR` is `1287` but equal when it is `645`.

## Conformability

The arguments of a dyadic function are said to _conform_ if the shape of each argument meets the requirements of the function, possibly after scalar extension.

## Fill Elements

Some primitive functions can include _fill elements_ in their result. The fill element for an array is the enclosed type of the disclose of the array (`⊂∊⊃Y` for array `Y` with `⎕ML←0`). The _type_ function (`∊` with `⎕ML←0`) replaces a numeric value with zero and a character value with `' '`.

The _disclose_ function (`⊃`) returns the first item of an array. If the array is empty, `⊃Y` is the _prototype_ of `Y`. The prototype is the type of the first element of the original array.

Primitive functions that can return an array including fill elements are _expand_ ([`\`](expand.md) or [`⍀`](expand-first.md)), _replicate_ ([`/`](replicate.md) or [`⌿`](replicate-first.md)), _reshape_ ([`⍴`](reshape.md)), mix ([`↑`](mix.md), and _take_ ([`↑`](take/index.md)).

<h2 class="example">Examples</h2>
```apl

      ML←0
      ∊⍳5
0 0 0 0 0
 
      ∊⊃(⍳3)('ABC')
0 0 0
 
      ⊂∊⊃(⍳3)('ABC')
 0 0 0
 
      ⊂∊⊃⊂(⍳3)('ABC')
  0 0 0
 
      A←'ABC' (1 2 3)
      A←0⍴A
      ⊂∊⊃A
 
      ' '=⊂∊⊃A
 1 1 1
```

## Axis Operator

The axis operator can be applied to all [dyadic scalar functions](primitive-functions-by-category/#dyadic-scalar-functions) and certain mixed primitive functions. An integer axis identifies a specific axis along which the function is to be applied to one or both of its arguments. If the primitive function is to be applied without an axis specification, a default axis is implied, either the first or last.

<h2 class="example">Example</h2>
```apl
      1 0 1/[1] 3 2⍴⍳6
1 2
5 6
```
```apl
      1 2 3+[2]2 3⍴10 20 30
11 22 33
11 22 33
```

Sometimes the axis value is fractional, indicating that a new axis or axes are to be created between the axes identified by the lower and upper integer bounds of the value (either of which might not exist).

<h2 class="example">Example</h2>
```apl
      'NAMES',[0.5]'='
NAMES
=====
```

`⎕IO` is an [implicit argument](#implicit-arguments) of axis specification.
