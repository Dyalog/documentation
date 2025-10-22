<h1 class="heading"><span class="name">Primitive Functions (by Category)</span></h1>

The primitive functions can be grouped together into categories that exhibit common behaviours or goals. Functions can be in multiple categories.

<style>
th:first-child {text-align:center!important;}
td:first-child code {margin-right: 1em;}
</style>

## Monadic Scalar Functions

Monadic scalar functions are pervasive, that is, they apply independently to each simple scalar in their argument. The result is structured identically to the argument, but is numeric, except for `+Y` which preserves types.

|Syntax|Meaning
|---:|---
|`+Y`|[Conjugate](primitive-functions/conjugate)
|`-Y`|[Negate](primitive-functions/negate)
|`×Y`|[Direction](primitive-functions/direction)
|`÷Y`|[Reciprocal](primitive-functions/reciprocal)
|`|Y`|[Magnitude](primitive-functions/magnitude)
|`*Y`|[Exponential](primitive-functions/exponential)
|`⍟Y`|[Natural Logarithm](primitive-functions/natural-logarithm)
|`○Y`|[Pi Times](primitive-functions/pi-times)
|`⌈Y`|[Ceiling](primitive-functions/ceiling)
|`⌊Y`|[Floor](primitive-functions/floor)
|`!Y`|[Factorial](primitive-functions/factorial)
|`?Y`|[Roll](primitive-functions/roll)
|`~Y`|[NOT](primitive-functions/not)

## Dyadic Scalar Functions

Dyadic scalar functions are pervasive, that is, they apply independently to corresponding pairs of simple scalars in their arguments. The result is structured identically to the arguments, subject to _scalar extensions_, but is always numeric.

If a simple scalar corresponds to a non-scalar, the simple scalar is replicated to the shape of the non-scalar.

A singleton (single-element array) is treated as a scalar for scalar extension purposes, but if both arguments are singletons, then the lower-rank argument is extended to the rank of the higher-rank argument.

|Syntax|Meaning
|---:|---
|`X+Y`|[Plus](primitive-functions/plus)
|`X-Y`|[Minus](primitive-functions/minus)
|`X×Y`|[Times](primitive-functions/times)
|`X÷Y`|[Divide](primitive-functions/divide)
|`X|Y`|[Residue](primitive-functions/residue)
|`X*Y`|[Power](primitive-functions/power)
|`X⍟Y`|[Logarithm](primitive-functions/logarithm)
|`X○Y`|[Circular Functions](primitive-functions/circular-functions)
|`X⌈Y`|[Maximum](primitive-functions/maximum)
|`X⌊Y`|[Minimum](primitive-functions/minimum)
|`X!Y`|[Binomial](primitive-functions/binomial)
|`X∧Y`|[Lowest Common Multiple](primitive-functions/lowest-common-multiple-and)
|`X∨Y`|[Greatest Common Divisor](primitive-functions/greatest-common-divisor-or)
|`X~Y`|[Without](primitive-functions/without)
|`X∧Y`|[AND](primitive-functions/lowest-common-multiple-and)
|`X∨Y`|[OR](primitive-functions/greatest-common-divisor-or)
|`X⍲Y`|[NAND](primitive-functions/nand)
|`X⍱Y`|[NOR](primitive-functions/nor)
|`X<Y`|[Less Than](primitive-functions/less-than)
|`X≤Y`|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)
|`X=Y`|[Equal To](primitive-functions/equal-to)
|`X≥Y`|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)
|`X>Y`|[Greater Than](primitive-functions/greater-than)
|`X≠Y`|[Not Equal To](primitive-functions/not-equal-to)

## Mathematical Functions

Mathematical functions perform computations on numeric arguments; all except `+Y`, `⍋Y`, and `⍒Y` will reject non-numeric arguments.  

Several of the monadic forms are equivalent to the dyadic forms with a default left argument.

|Syntax|Meaning
|---:|---
|`+Y`|[Conjugate](primitive-functions/conjugate)
|`X+Y`|[Plus](primitive-functions/plus)
|`-Y`|[Negate](primitive-functions/negate)
|`X-Y`|[Minus](primitive-functions/minus)
|`×Y`|[Direction](primitive-functions/direction)
|`X×Y`|[Times](primitive-functions/times)
|`÷Y`|[Reciprocal](primitive-functions/reciprocal)
|`X÷Y`|[Divide](primitive-functions/divide)
|`|Y`|[Magnitude](primitive-functions/magnitude)
|`X|Y`|[Residue](primitive-functions/residue)
|`*Y`|[Exponential](primitive-functions/exponential)
|`X*Y`|[Power](primitive-functions/power)
|`⍟Y`|[Natural Logarithm](primitive-functions/natural-logarithm)
|`X⍟Y`|[Logarithm](primitive-functions/logarithm)
|`○Y`|[Pi Times](primitive-functions/pi-times)
|`X○Y`|[Circular Functions](primitive-functions/circular-functions)
|`⌈Y`|[Ceiling](primitive-functions/ceiling)
|`X⌈Y`|[Maximum](primitive-functions/maximum)
|`⌊Y`|[Floor](primitive-functions/floor)
|`X⌊Y`|[Minimum](primitive-functions/minimum)
|`!Y`|[Factorial](primitive-functions/factorial)
|`X!Y`|[Binomial](primitive-functions/binomial)
|`?Y`|[Roll](primitive-functions/roll)
|`X?Y`|[Deal](primitive-functions/deal)
|`X⊤Y`|[Encode](primitive-functions/encode)
|`X⊥Y`|[Decode](primitive-functions/decode)
|`⌹Y`|[Matrix Inverse](primitive-functions/matrix-inverse)
|`X⌹Y`|[Matrix Divide](primitive-functions/matrix-divide)
|`X∧Y`|[Lowest Common Multiple](primitive-functions/lowest-common-multiple-and)
|`X∨Y`|[Greatest Common Divisor](primitive-functions/greatest-common-divisor-or)
|`⍋Y`|[Grade Up](primitive-functions/grade-up)
|`⍒Y`|[Grade Down](primitive-functions/grade-down)
|`X⍕Y`|[Format by Specification](primitive-functions/format-by-specification)

## Logic Functions
Logic functions represent logic gates. Their arguments and results are Boolean (comprising only `1`s and `0`s).

|Syntax|Meaning|Logic Gate
|---:|---|---
|`~Y`|[NOT](primitive-functions/not)|NOT 
|`X∧Y`|[AND](primitive-functions/lowest-common-multiple-and)|AND
|`X∨Y`|[OR](primitive-functions/greatest-common-divisor-or)|OR
|`X⍲Y`|[NAND](primitive-functions/nand)|NAND
|`X⍱Y`|[NOR](primitive-functions/nor)|NOR
|`X<Y`|[Less Than](primitive-functions/less-than)|CNIMPLY
|`X≤Y`|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)|IMPLY
|`X=Y`|[Equal To](primitive-functions/equal-to)|XNOR
|`X≥Y`|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)|CIMPLY
|`X>Y`|[Greater Than](primitive-functions/greater-than)|NIMPLY
|`X≠Y`|[Not Equal To](primitive-functions/not-equal-to)|XOR

## Comparison Functions
Comparison functions perform comparisons. They return Boolean results indicating whether the comparisons are true (`1`) or false (`0`).

|Syntax|Meaning
|---:|---
|`X<Y`|[Less Than](primitive-functions/less-than)
|`X≤Y`|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)
|`X=Y`|[Equal To](primitive-functions/equal-to)
|`X≥Y`|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)
|`X>Y`|[Greater Than](primitive-functions/greater-than)
|`X≠Y`|[Not Equal To](primitive-functions/not-equal-to)
|`X≡Y`|[Match](primitive-functions/match)
|`X≢Y`|[Not Match](primitive-functions/not-match)
|`X∊Y`|[Membership](primitive-functions/membership)

## Selection Functions
Selection functions restrict the parts of their arguments that are propagated into their result (exception: `X⊢Y` and `X⊣Y` return one of their arguments).

|Syntax|Meaning
|---:|---
|`X⌷Y`|[Index](primitive-functions/index-function)
|`⊃Y`|[First](primitive-functions/first)
|`X⊃Y`|[Pick](primitive-functions/pick)
|`X/Y`|[Replicate](primitive-functions/replicate)
|`X⌿Y`|[Replicate First](primitive-functions/replicate-first)
|`X\Y`|[Expand](primitive-functions/expand)
|`X⍀Y`|[Expand First](primitive-functions/expand-first)
|`X⍉Y`|[Dyadic Transpose](primitive-functions/dyadic-transpose)
|`X↑Y`|[Take](primitive-functions/take)
|`X↓Y`|[Drop](primitive-functions/drop)
|`X∩Y`|[Intersection](primitive-functions/intersection)
|`∪Y`|[Unique](primitive-functions/unique)
|`X∪Y`|[Union](primitive-functions/union)
|`X⊢Y`|[Right](primitive-functions/right)
|`X⊣Y`|[Left](primitive-functions/left)

## Set Functions
Set functions operate on arrays representing collections. Within the set functions:

- `X∩Y`, `X∪Y`, and `X~Y` are restricted to vectors.
- `X~Y`, `X∩Y`, `∪Y`, and `X∪Y` return new collections.
- `≠Y`, `X≡Y`, `X≢Y`, and `X∊Y` return Boolean results (comprising only `1`s and `0`s).

|Syntax|Meaning
|---:|---
|`X~Y`|[Without](primitive-functions/without)
|`X∩Y`|[Intersection](primitive-functions/intersection)
|`∪Y`|[Unique](primitive-functions/unique)
|`X∪Y`|[Union](primitive-functions/union)
|`≠Y`|[Unique Mask](primitive-functions/unique-mask)
|`X≡Y`|[Match](primitive-functions/match)
|`X≢Y`|[Not Match](primitive-functions/not-match)
|`X∊Y`|[Membership](primitive-functions/membership)

## Search Functions
Search functions determine whether/where values are located.

|Syntax|Meaning
|---:|---
|`X⍳Y`|[Index Of](primitive-functions/index-of)
|`⍸Y`|[Where](primitive-functions/where)
|`X⍸Y`|[Interval Index](primitive-functions/interval-index)
|`X∊Y`|[Membership](primitive-functions/membership)
|`X⍷Y`|[Find](primitive-functions/find)

## Ordering Functions
Ordering functions return indices that can subsequently be used to select from within the original array.

|Syntax|Meaning
|---:|---
|`⍳Y`|[Index Generator](primitive-functions/index-generator)
|`X⍳Y`|[Index Of](primitive-functions/index-of)
|`X⍸Y`|[Interval Index](primitive-functions/interval-index)
|`⍋Y`|[Grade Up](primitive-functions/grade-up)
|`X⍋Y`|[Dyadic Grade Up](primitive-functions/dyadic-grade-up)
|`⍒Y`|[Grade Down](primitive-functions/grade-down)
|`X⍒Y`|[Dyadic Grade Down](primitive-functions/dyadic-grade-down)

## Index Generator Functions
Index generator functions return indices that can then be used directly or to select from within the original array.

|Syntax|Meaning
|---:|---
|`?Y`|[Roll](primitive-functions/roll)
|`X?Y`|[Deal](primitive-functions/deal)
|`⍳Y`|[Index Generator](primitive-functions/index-generator)
|`X⍳Y`|[Index Of](primitive-functions/index-of)
|`⍸Y`|[Where](primitive-functions/where)
|`X⍸Y`|[Interval Index](primitive-functions/interval-index)
|`⍋Y`|[Grade Up](primitive-functions/grade-up)
|`X⍋Y`|[Dyadic Grade Up](primitive-functions/dyadic-grade-up)
|`⍒Y`|[Grade Down](primitive-functions/grade-down)
|`X⍒Y`|[Dyadic Grade Down](primitive-functions/dyadic-grade-down)


## Structural Functions
Structural functions modify the structure or shape of their right argument (including omitting values) but they do not otherwise change any scalar values.

|Syntax|Meaning
|---:|---
|`X⍴Y`|[Reshape](primitive-functions/reshape)
|`,Y`|[Ravel](primitive-functions/ravel)
|`X,Y`|[Catenate/Laminate](primitive-functions/catenate-laminate)
|`⍪Y`|[Table](primitive-functions/table)
|`X⍪Y`|[Catenate First/Laminate](primitive-functions/catenate-first)
|`⌽Y`|[Reverse](primitive-functions/reverse)
|`X⌽Y`|[Rotate](primitive-functions/rotate)
|`⍉Y`|[Transpose](primitive-functions/transpose)
|`X⍉Y`|[Dyadic Transpose](primitive-functions/dyadic-transpose)
|`⊖Y`|[Reverse First](primitive-functions/reverse-first)
|`X⊖Y`|[Rotate First](primitive-functions/rotate-first)
|`↑Y`|[Mix](primitive-functions/mix)
|`X↑Y`|[Take](primitive-functions/take)
|`↓Y`|[Split](primitive-functions/split)
|`X↓Y`|[Drop](primitive-functions/drop)
|`⊂Y`|[Enclose](primitive-functions/enclose)
|`X⊂Y`|[Partitioned Enclose](primitive-functions/partitioned-enclose)
|`⊆Y`|[Nest](primitive-functions/nest)
|`X⊆Y`|[Partition](primitive-functions/partition)
|`⊃Y`|[First](primitive-functions/first)
|`X⊃Y`|[Pick](primitive-functions/pick)
|`∊Y`|[Enlist](primitive-functions/enlist)

## Data Conversion Functions
Data conversion functions change between different representations of the same data.

|Syntax|Meaning
|---:|---
|`⌷Y`|[Materialise](primitive-functions/materialise)
|`⍎Y`|[Execute](primitive-functions/execute)
|`X⍎Y`|[Dyadic Execute](primitive-functions/execute)
|`⍕Y`|[Format](primitive-functions/format)
|`X⍕Y`|[Format by Specification](primitive-functions/format-by-specification)

## Identity Functions
Identity functions make it easy to write ambivalent dfns and are useful in tacit programming, as generic operands, and to break up stranding. They do not modify structure, shape, or values (exception: `⌷Y`, when applied to an object, extracts its default value).

|Syntax|Meaning
|---:|---
|`⌷Y`|[Materialise](primitive-functions/materialise)
|`⊢Y`|[Same](primitive-functions/same)
|`X⊢Y`|[Right](primitive-functions/right)
|`⊣Y`|[Same](primitive-functions/same)
|`X⊣Y`|[Left](primitive-functions/left)

## Array Property Functions
Array property functions provide information about a given array.

|Syntax|Meaning
|---:|---
|`⌷Y`|[Materialise](primitive-functions/materialise)
|`⍴Y`|[Shape](primitive-functions/shape)
|`≡Y`|[Depth](primitive-functions/depth)
|`≢Y`|[Tally](primitive-functions/tally)
