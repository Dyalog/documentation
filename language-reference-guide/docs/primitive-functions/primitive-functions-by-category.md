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
|`+Y`&emsp;|[Conjugate](primitive-functions/conjugate)
|`-Y`&emsp;|[Negate](primitive-functions/negate)
|`×Y`&emsp;|[Direction](primitive-functions/direction)
|`÷Y`&emsp;|[Reciprocal](primitive-functions/reciprocal)
|`|Y`&emsp;|[Magnitude](primitive-functions/magnitude)
|`*Y`&emsp;|[Exponential](primitive-functions/exponential)
|`⍟Y`&emsp;|[Natural Logarithm](primitive-functions/natural-logarithm)
|`○Y`&emsp;|[Pi Times](primitive-functions/pi-times)
|`⌈Y`&emsp;|[Ceiling](primitive-functions/ceiling)
|`⌊Y`&emsp;|[Floor](primitive-functions/floor)
|`!Y`&emsp;|[Factorial](primitive-functions/factorial)
|`?Y`&emsp;|[Roll](primitive-functions/roll)
|`~Y`&emsp;|[NOT](primitive-functions/not)

## Dyadic Scalar Functions

Dyadic scalar functions are pervasive, that is, they apply independently to corresponding pairs of simple scalars in their arguments. The result is structured identically to the arguments, subject to _scalar extensions_, but is always numeric.

If a simple scalar corresponds to a non-scalar, the simple scalar is replicated to the shape of the non-scalar.

A singleton (single-element array) is treated as a scalar for scalar extension purposes, but if both arguments are singletons, then the lower-rank argument is extended to the rank of the higher-rank argument.

|Syntax|Meaning
|---:|---
|`X+Y`&emsp;|[Plus](primitive-functions/plus)
|`X-Y`&emsp;|[Minus](primitive-functions/minus)
|`X×Y`&emsp;|[Times](primitive-functions/times)
|`X÷Y`&emsp;|[Divide](primitive-functions/divide)
|`X|Y`&emsp;|[Residue](primitive-functions/residue)
|`X*Y`&emsp;|[Power](primitive-functions/power)
|`X⍟Y`&emsp;|[Logarithm](primitive-functions/logarithm)
|`X○Y`&emsp;|[Circular Functions](primitive-functions/circular-functions)
|`X⌈Y`&emsp;|[Maximum](primitive-functions/maximum)
|`X⌊Y`&emsp;|[Minimum](primitive-functions/minimum)
|`X!Y`&emsp;|[Binomial](primitive-functions/binomial)
|`X∧Y`&emsp;|[Lowest Common Multiple](primitive-functions/lowest-common-multiple-and)
|`X∨Y`&emsp;|[Greatest Common Divisor](primitive-functions/greatest-common-divisor-or)
|`X~Y`&emsp;|[Without](primitive-functions/without)
|`X∧Y`&emsp;|[AND](primitive-functions/lowest-common-multiple-and)
|`X∨Y`&emsp;|[OR](primitive-functions/greatest-common-divisor-or)
|`X⍲Y`&emsp;|[NAND](primitive-functions/nand)
|`X⍱Y`&emsp;|[NOR](primitive-functions/nor)
|`X<Y`&emsp;|[Less Than](primitive-functions/less-than)
|`X≤Y`&emsp;|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)
|`X=Y`&emsp;|[Equal To](primitive-functions/equal-to)
|`X≥Y`&emsp;|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)
|`X>Y`&emsp;|[Greater Than](primitive-functions/greater-than)
|`X≠Y`&emsp;|[Not Equal To](primitive-functions/not-equal-to)

## Mathematical Functions

Mathematical functions perform computations on numeric arguments; all except `+Y`, `⍋Y`, and `⍒Y` will reject non-numeric arguments.  

Several of the monadic forms are equivalent to the dyadic forms with a default left argument.

|Syntax|Meaning
|---:|---
|`+Y`&emsp;|[Conjugate](primitive-functions/conjugate)
|`X+Y`&emsp;|[Plus](primitive-functions/plus)
|`-Y`&emsp;|[Negate](primitive-functions/negate)
|`X-Y`&emsp;|[Minus](primitive-functions/minus)
|`×Y`&emsp;|[Direction](primitive-functions/direction)
|`X×Y`&emsp;|[Times](primitive-functions/times)
|`÷Y`&emsp;|[Reciprocal](primitive-functions/reciprocal)
|`X÷Y`&emsp;|[Divide](primitive-functions/divide)
|`|Y`&emsp;|[Magnitude](primitive-functions/magnitude)
|`X|Y`&emsp;|[Residue](primitive-functions/residue)
|`*Y`&emsp;|[Exponential](primitive-functions/exponential)
|`X*Y`&emsp;|[Power](primitive-functions/power)
|`⍟Y`&emsp;|[Natural Logarithm](primitive-functions/natural-logarithm)
|`X⍟Y`&emsp;|[Logarithm](primitive-functions/logarithm)
|`○Y`&emsp;|[Pi Times](primitive-functions/pi-times)
|`X○Y`&emsp;|[Circular Functions](primitive-functions/circular-functions)
|`⌈Y`&emsp;|[Ceiling](primitive-functions/ceiling)
|`X⌈Y`&emsp;|[Maximum](primitive-functions/maximum)
|`⌊Y`&emsp;|[Floor](primitive-functions/floor)
|`X⌊Y`&emsp;|[Minimum](primitive-functions/minimum)
|`!Y`&emsp;|[Factorial](primitive-functions/factorial)
|`X!Y`&emsp;|[Binomial](primitive-functions/binomial)
|`?Y`&emsp;|[Roll](primitive-functions/roll)
|`X?Y`&emsp;|[Deal](primitive-functions/deal)
|`X⊤Y`&emsp;|[Encode](primitive-functions/encode)
|`X⊥Y`&emsp;|[Decode](primitive-functions/decode)
|`⌹Y`&emsp;|[Matrix Inverse](primitive-functions/matrix-inverse)
|`X⌹Y`&emsp;|[Matrix Divide](primitive-functions/matrix-divide)
|`X∧Y`&emsp;|[Lowest Common Multiple](primitive-functions/lowest-common-multiple-and)
|`X∨Y`&emsp;|[Greatest Common Divisor](primitive-functions/greatest-common-divisor-or)
|`⍋Y`&emsp;|[Grade Up](primitive-functions/grade-up)
|`⍒Y`&emsp;|[Grade Down](primitive-functions/grade-down)
|`X⍕Y`&emsp;|[Format by Specification](primitive-functions/format-by-specification)

## Logic Functions
Logic functions represent logic gates. Their arguments and results are Boolean (comprising only `1`s and `0`s).

|Syntax|Meaning|Logic Gate
|---:|---|---
|`~Y`&emsp;|[NOT](primitive-functions/not)|NOT 
|`X∧Y`&emsp;|[AND](primitive-functions/lowest-common-multiple-and)|AND
|`X∨Y`&emsp;|[OR](primitive-functions/greatest-common-divisor-or)|OR
|`X⍲Y`&emsp;|[NAND](primitive-functions/nand)|NAND
|`X⍱Y`&emsp;|[NOR](primitive-functions/nor)|NOR
|`X<Y`&emsp;|[Less Than](primitive-functions/less-than)|CNIMPLY
|`X≤Y`&emsp;|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)|IMPLY
|`X=Y`&emsp;|[Equal To](primitive-functions/equal-to)|XNOR
|`X≥Y`&emsp;|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)|CIMPLY
|`X>Y`&emsp;|[Greater Than](primitive-functions/greater-than)|NIMPLY
|`X≠Y`&emsp;|[Not Equal To](primitive-functions/not-equal-to)|XOR

## Comparison Functions
Comparison functions perform comparisons. They return Boolean results indicating whether the comparisons are true (`1`) or false (`0`).

|Syntax|Meaning
|---:|---
|`X<Y`&emsp;|[Less Than](primitive-functions/less-than)
|`X≤Y`&emsp;|[Less Than Or Equal To](primitive-functions/less-than-or-equal-to)
|`X=Y`&emsp;|[Equal To](primitive-functions/equal-to)
|`X≥Y`&emsp;|[Greater Than Or Equal To](primitive-functions/greater-than-or-equal-to)
|`X>Y`&emsp;|[Greater Than](primitive-functions/greater-than)
|`X≠Y`&emsp;|[Not Equal To](primitive-functions/not-equal-to)
|`X≡Y`&emsp;|[Match](primitive-functions/match)
|`X≢Y`&emsp;|[Not Match](primitive-functions/not-match)
|`X∊Y`&emsp;|[Membership](primitive-functions/membership)

## Selection Functions
Selection functions restrict the parts of their arguments that are propagated into their result (exception: `X⊢Y` and `X⊣Y` return one of their arguments).

|Syntax|Meaning
|---:|---
|`X⌷Y`&emsp;|[Index](primitive-functions/index-function)
|`⊃Y`&emsp;|[First](primitive-functions/first)
|`X⊃Y`&emsp;|[Pick](primitive-functions/pick)
|`X/Y`&emsp;|[Replicate](primitive-functions/replicate)
|`X⌿Y`&emsp;|[Replicate First](primitive-functions/replicate-first)
|`X\Y`&emsp;|[Expand](primitive-functions/expand)
|`X⍀Y`&emsp;|[Expand First](primitive-functions/expand-first)
|`X⍉Y`&emsp;|[Dyadic Transpose](primitive-functions/dyadic-transpose)
|`X↑Y`&emsp;|[Take](primitive-functions/take)
|`X↓Y`&emsp;|[Drop](primitive-functions/drop)
|`X∩Y`&emsp;|[Intersection](primitive-functions/intersection)
|`∪Y`&emsp;|[Unique](primitive-functions/unique)
|`X∪Y`&emsp;|[Union](primitive-functions/union)
|`X⊢Y`&emsp;|[Right](primitive-functions/right)
|`X⊣Y`&emsp;|[Left](primitive-functions/left)

## Set Functions
Set functions operate on arrays representing collections. Within the set functions:

- `X∩Y`, `X∪Y`, and `X~Y` are restricted to vectors.
- `X~Y`, `X∩Y`, `∪Y`, and `X∪Y` return new collections.
- `≠Y`, `X≡Y`, `X≢Y`, and `X∊Y` return Boolean results (comprising only `1`s and `0`s).

|Syntax|Meaning
|---:|---
|`X~Y`&emsp;|[Without](primitive-functions/without)
|`X∩Y`&emsp;|[Intersection](primitive-functions/intersection)
|`∪Y`&emsp;|[Unique](primitive-functions/unique)
|`X∪Y`&emsp;|[Union](primitive-functions/union)
|`≠Y`&emsp;|[Unique Mask](primitive-functions/unique-mask)
|`X≡Y`&emsp;|[Match](primitive-functions/match)
|`X≢Y`&emsp;|[Not Match](primitive-functions/not-match)
|`X∊Y`&emsp;|[Membership](primitive-functions/membership)

## Search Functions
Search functions determine whether/where values are located.

|Syntax|Meaning
|---:|---
|`X⍳Y`&emsp;|[Index Of](primitive-functions/index-of)
|`⍸Y`&emsp;|[Where](primitive-functions/where)
|`X⍸Y`&emsp;|[Interval Index](primitive-functions/interval-index)
|`X∊Y`&emsp;|[Membership](primitive-functions/membership)
|`X⍷Y`&emsp;|[Find](primitive-functions/find)

## Ordering Functions
Ordering functions return indices that can subsequently be used to select from within the original array.

|Syntax|Meaning
|---:|---
|`⍳Y`&emsp;|[Index Generator](primitive-functions/index-generator)
|`X⍳Y`&emsp;|[Index Of](primitive-functions/index-of)
|`X⍸Y`&emsp;|[Interval Index](primitive-functions/interval-index)
|`⍋Y`&emsp;|[Grade Up](primitive-functions/grade-up)
|`X⍋Y`&emsp;|[Dyadic Grade Up](primitive-functions/dyadic-grade-up)
|`⍒Y`&emsp;|[Grade Down](primitive-functions/grade-down)
|`X⍒Y`&emsp;|[Dyadic Grade Down](primitive-functions/dyadic-grade-down)

## Index Generator Functions
Index generator functions return indices that can then be used directly or to select from within the original array.

|Syntax|Meaning
|---:|---
|`?Y`&emsp;|[Roll](primitive-functions/roll)
|`X?Y`&emsp;|[Deal](primitive-functions/deal)
|`⍳Y`&emsp;|[Index Generator](primitive-functions/index-generator)
|`X⍳Y`&emsp;|[Index Of](primitive-functions/index-of)
|`⍸Y`&emsp;|[Where](primitive-functions/where)
|`X⍸Y`&emsp;|[Interval Index](primitive-functions/interval-index)
|`⍋Y`&emsp;|[Grade Up](primitive-functions/grade-up)
|`X⍋Y`&emsp;|[Dyadic Grade Up](primitive-functions/dyadic-grade-up)
|`⍒Y`&emsp;|[Grade Down](primitive-functions/grade-down)
|`X⍒Y`&emsp;|[Dyadic Grade Down](primitive-functions/dyadic-grade-down)


## Structural Functions
Structural functions modify the structure or shape of their right argument (including omitting values) but they do not otherwise change any scalar values.

|Syntax|Meaning
|---:|---
|`X⍴Y`&emsp;|[Reshape](primitive-functions/reshape)
|`,Y`&emsp;|[Ravel](primitive-functions/ravel)
|`X,Y`&emsp;|[Catenate/Laminate](primitive-functions/catenate-laminate)
|`⍪Y`&emsp;|[Table](primitive-functions/table)
|`X⍪Y`&emsp;|[Catenate First/Laminate](primitive-functions/catenate-first)
|`⌽Y`&emsp;|[Reverse](primitive-functions/reverse)
|`X⌽Y`&emsp;|[Rotate](primitive-functions/rotate)
|`⍉Y`&emsp;|[Transpose](primitive-functions/transpose)
|`X⍉Y`&emsp;|[Dyadic Transpose](primitive-functions/dyadic-transpose)
|`⊖Y`&emsp;|[Reverse First](primitive-functions/reverse-first)
|`X⊖Y`&emsp;|[Rotate First](primitive-functions/rotate-first)
|`↑Y`&emsp;|[Mix](primitive-functions/mix)
|`X↑Y`&emsp;|[Take](primitive-functions/take)
|`↓Y`&emsp;|[Split](primitive-functions/split)
|`X↓Y`&emsp;|[Drop](primitive-functions/drop)
|`⊂Y`&emsp;|[Enclose](primitive-functions/enclose)
|`X⊂Y`&emsp;|[Partitioned Enclose](primitive-functions/partitioned-enclose)
|`⊆Y`&emsp;|[Nest](primitive-functions/nest)
|`X⊆Y`&emsp;|[Partition](primitive-functions/partition)
|`⊃Y`&emsp;|[First](primitive-functions/first)
|`X⊃Y`&emsp;|[Pick](primitive-functions/pick)
|`∊Y`&emsp;|[Enlist](primitive-functions/enlist)

## Data Conversion Functions
Data conversion functions change between different representations of the same data.

|Syntax|Meaning
|---:|---
|`⌷Y`&emsp;|[Materialise](primitive-functions/materialise)
|`⍎Y`&emsp;|[Execute](primitive-functions/execute)
|`X⍎Y`&emsp;|[Dyadic Execute](primitive-functions/execute)
|`⍕Y`&emsp;|[Format](primitive-functions/format)
|`X⍕Y`&emsp;|[Format by Specification](primitive-functions/format-by-specification)

## Identity Functions
Identity functions make it easy to write ambivalent dfns and are useful in tacit programming, as generic operands, and to break up stranding. They do not modify structure, shape, or values (exception: `⌷Y`, when applied to an object, extracts its default value).

|Syntax|Meaning
|---:|---
|`⌷Y`&emsp;|[Materialise](primitive-functions/materialise)
|`⊢Y`&emsp;|[Same](primitive-functions/same)
|`X⊢Y`&emsp;|[Right](primitive-functions/right)
|`⊣Y`&emsp;|[Same](primitive-functions/same)
|`X⊣Y`&emsp;|[Left](primitive-functions/left)

## Array Property Functions
Array property functions provide information about a given array.

|Syntax|Meaning
|---:|---
|`⌷Y`&emsp;|[Materialise](primitive-functions/materialise)
|`⍴Y`&emsp;|[Shape](primitive-functions/shape)
|`≡Y`&emsp;|[Depth](primitive-functions/depth)
|`≢Y`&emsp;|[Tally](primitive-functions/tally)
