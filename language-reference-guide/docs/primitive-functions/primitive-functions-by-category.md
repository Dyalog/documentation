<h1 class="heading"><span class="name">Primitive Functions (by Category)</span></h1>

The primitive functions can be grouped together into categories that exhibit common behaviours or goals. Functions can be in multiple categories.

## Scalar Functions

Scalar functions apply to simple scalars and are pervasive.

### Monadic Scalar Functions

Monadic scalar functions apply independently to each simple scalar in their argument.

The result has the same structure as the argument, and is numeric (exception: `+Y` preserves the types of the argument).

|Syntax|Meaning|
|---:|---|
|`+Y`&emsp;|[Conjugate](conjugate.md)|
|`-Y`&emsp;|[Negate](negate.md)|
|`×Y`&emsp;|[Direction](direction.md)|
|`÷Y`&emsp;|[Reciprocal](reciprocal.md)|
|`|Y`&emsp;|[Magnitude](magnitude.md)|
|`*Y`&emsp;|[Exponential](exponential.md)|
|`⍟Y`&emsp;|[Natural Logarithm](natural-logarithm.md)|
|`○Y`&emsp;|[Pi Times](pi-times.md)|
|`⌈Y`&emsp;|[Ceiling](ceiling.md)|
|`⌊Y`&emsp;|[Floor](floor.md)|
|`!Y`&emsp;|[Factorial](factorial.md)|
|`?Y`&emsp;|[Roll](roll.md)|
|`~Y`&emsp;|[NOT](not.md)|

### Dyadic Scalar Functions

Dyadic scalar functions apply independently to corresponding pairs of simple scalars in their arguments. The result has the same structure as the arguments, subject to _scalar extensions_, and is always numeric.

If a simple scalar corresponds to a non-scalar, the simple scalar is replicated to the shape of the non-scalar.

A singleton (single-element array) is treated as a scalar for scalar extension purposes; if both arguments are singletons, then the lower-rank argument is extended to the rank of the higher-rank argument.

|Syntax|Meaning
|---:|---
|`X+Y`&emsp;|[Plus](plus.md)|
|`X-Y`&emsp;|[Minus](minus.md)|
|`X×Y`&emsp;|[Times](times.md)|
|`X÷Y`&emsp;|[Divide](divide.md)|
|`X|Y`&emsp;|[Residue](residue.md)|
|`X*Y`&emsp;|[Power](power.md)|
|`X⍟Y`&emsp;|[Logarithm](logarithm.md)|
|`X○Y`&emsp;|[Circular Functions](circular-functions.md)|
|`X⌈Y`&emsp;|[Maximum](maximum.md)|
|`X⌊Y`&emsp;|[Minimum](minimum.md)|
|`X!Y`&emsp;|[Binomial](binomial.md)|
|`X∧Y`&emsp;|[Lowest Common Multiple](lowest-common-multiple-and.md)|
|`X∨Y`&emsp;|[Greatest Common Divisor](greatest-common-divisor-or.md)|
|`X~Y`&emsp;|[Without](without.md)|
|`X∧Y`&emsp;|[AND](lowest-common-multiple-and.md)|
|`X∨Y`&emsp;|[OR](greatest-common-divisor-or.md)|
|`X⍲Y`&emsp;|[NAND](nand.md)|
|`X⍱Y`&emsp;|[NOR](nor.md)|
|`X<Y`&emsp;|[Less Than](less-than.md)|
|`X≤Y`&emsp;|[Less Than Or Equal To](less-than-or-equal-to.md)|
|`X=Y`&emsp;|[Equal To](equal-to.md)|
|`X≥Y`&emsp;|[Greater Than Or Equal To](greater-than-or-equal-to.md)|
|`X>Y`&emsp;|[Greater Than](greater-than.md)|
|`X≠Y`&emsp;|[Not Equal To](not-equal-to.md)|

## Mathematical Functions

Mathematical functions perform computations on numeric arguments; all except `+Y`, `⍋Y`, and `⍒Y` will reject non-numeric arguments.  

Several of the monadic forms are equivalent to the dyadic forms with a default left argument.

|Syntax|Meaning|
|---:|---|
|`+Y`&emsp;|[Conjugate](conjugate.md)|
|`X+Y`&emsp;|[Plus](plus.md)|
|`-Y`&emsp;|[Negate](negate.md)|
|`X-Y`&emsp;|[Minus](minus.md)|
|`×Y`&emsp;|[Direction](direction.md)|
|`X×Y`&emsp;|[Times](times.md)|
|`÷Y`&emsp;|[Reciprocal](reciprocal.md)|
|`X÷Y`&emsp;|[Divide](divide.md)|
|`|Y`&emsp;|[Magnitude](magnitude.md)|
|`X|Y`&emsp;|[Residue](residue.md)|
|`*Y`&emsp;|[Exponential](exponential.md)|
|`X*Y`&emsp;|[Power](power.md)|
|`⍟Y`&emsp;|[Natural Logarithm](natural-logarithm.md)|
|`X⍟Y`&emsp;|[Logarithm](logarithm.md)|
|`○Y`&emsp;|[Pi Times](pi-times.md)|
|`X○Y`&emsp;|[Circular Functions](circular-functions.md)|
|`⌈Y`&emsp;|[Ceiling](ceiling.md)|
|`X⌈Y`&emsp;|[Maximum](maximum.md)|
|`⌊Y`&emsp;|[Floor](floor.md)|
|`X⌊Y`&emsp;|[Minimum](minimum.md)|
|`!Y`&emsp;|[Factorial](factorial.md)|
|`X!Y`&emsp;|[Binomial](binomial.md)|
|`?Y`&emsp;|[Roll](roll.md)|
|`X?Y`&emsp;|[Deal](deal.md)|
|`X⊤Y`&emsp;|[Encode](encode.md)|
|`X⊥Y`&emsp;|[Decode](decode.md)|
|`⌹Y`&emsp;|[Matrix Inverse](matrix-inverse.md)|
|`X⌹Y`&emsp;|[Matrix Divide](matrix-divide.md)|
|`X∧Y`&emsp;|[Lowest Common Multiple](lowest-common-multiple-and.md)|
|`X∨Y`&emsp;|[Greatest Common Divisor](greatest-common-divisor-or.md)|
|`⍋Y`&emsp;|[Grade Up](grade-up.md)|
|`⍒Y`&emsp;|[Grade Down](grade-down.md)|
|`X⍕Y`&emsp;|[Format by Specification](format-by-specification.md)|

## Logic Functions
Logic functions represent logic gates. Their arguments and results are Boolean (comprising only `1`s and `0`s).

|Syntax|Meaning|Logic Gate|
|---:|---|---|
|`~Y`&emsp;|[NOT](not.md)|NOT| 
|`X∧Y`&emsp;|[AND](lowest-common-multiple-and.md)|AND|
|`X∨Y`&emsp;|[OR](greatest-common-divisor-or.md)|OR|
|`X⍲Y`&emsp;|[NAND](nand.md)|NAND|
|`X⍱Y`&emsp;|[NOR](nor.md)|NOR|
|`X<Y`&emsp;|[Less Than](less-than.md)|CNIMPLY|
|`X≤Y`&emsp;|[Less Than Or Equal To](less-than-or-equal-to.md)|IMPLY|
|`X=Y`&emsp;|[Equal To](equal-to.md)|XNOR|
|`X≥Y`&emsp;|[Greater Than Or Equal To](greater-than-or-equal-to.md)|CIMPLY|
|`X>Y`&emsp;|[Greater Than](greater-than.md)|NIMPLY|
|`X≠Y`&emsp;|[Not Equal To](not-equal-to.md)|XOR|

## Comparison Functions
Comparison functions perform comparisons. They return Boolean results indicating whether the comparisons are true (`1`) or false (`0`).

|Syntax|Meaning|
|---:|---
|`X<Y`&emsp;|[Less Than](less-than.md)|
|`X≤Y`&emsp;|[Less Than Or Equal To](less-than-or-equal-to.md)|
|`X=Y`&emsp;|[Equal To](equal-to.md)|
|`X≥Y`&emsp;|[Greater Than Or Equal To](greater-than-or-equal-to.md)|
|`X>Y`&emsp;|[Greater Than](greater-than.md)|
|`X≠Y`&emsp;|[Not Equal To](not-equal-to.md)|
|`X≡Y`&emsp;|[Match](match.md)|
|`X≢Y`&emsp;|[Not Match](not-match.md)|
|`X∊Y`&emsp;|[Membership](membership.md)|

## Selection Functions
Selection functions restrict the parts of their arguments that are propagated into their result (exception: `X⊢Y` and `X⊣Y` return one of their arguments).

|Syntax|Meaning|
|---:|---|
|`X⌷Y`&emsp;|[Index](index-function/index.md)|
|`⊃Y`&emsp;|[First](first.md)|
|`X⊃Y`&emsp;|[Pick](pick.md)|
|`X/Y`&emsp;|[Replicate](replicate.md)|
|`X⌿Y`&emsp;|[Replicate First](replicate-first.md)|
|`X\Y`&emsp;|[Expand](expand.md)|
|`X⍀Y`&emsp;|[Expand First](expand-first.md)|
|`X⍉Y`&emsp;|[Dyadic Transpose](dyadic-transpose.md)|
|`X↑Y`&emsp;|[Take](take/index.md)|
|`X↓Y`&emsp;|[Drop](drop/index.md)|
|`X∩Y`&emsp;|[Intersection](intersection.md)|
|`∪Y`&emsp;|[Unique](unique.md)|
|`X∪Y`&emsp;|[Union](union.md)|
|`X⊢Y`&emsp;|[Right](right.md)|
|`X⊣Y`&emsp;|[Left](left.md)|

## Set Functions
Set functions operate on arrays representing collections. Within the set functions:

- `X∩Y`, `X∪Y`, and `X~Y` are restricted to vectors.
- `X~Y`, `X∩Y`, `∪Y`, and `X∪Y` return new collections.
- `≠Y`, `X≡Y`, `X≢Y`, and `X∊Y` return Boolean results (comprising only `1`s and `0`s).

|Syntax|Meaning|
|---:|---|
|`X~Y`&emsp;|[Without](without.md)|
|`X∩Y`&emsp;|[Intersection](intersection.md)|
|`∪Y`&emsp;|[Unique](unique.md)|
|`X∪Y`&emsp;|[Union](union.md)|
|`≠Y`&emsp;|[Unique Mask](unique-mask.md)|
|`X≡Y`&emsp;|[Match](match.md)|
|`X≢Y`&emsp;|[Not Match](not-match.md)|
|`X∊Y`&emsp;|[Membership](membership.md)|

## Search Functions
Search functions determine whether/where values are located.

|Syntax|Meaning|
|---:|---|
|`X⍳Y`&emsp;|[Index Of](index-of.md)|
|`⍸Y`&emsp;|[Where](where.md)|
|`X⍸Y`&emsp;|[Interval Index](interval-index.md)|
|`X∊Y`&emsp;|[Membership](membership.md)|
|`X⍷Y`&emsp;|[Find](find.md)|

## Ordering Functions
Ordering functions return indices that can subsequently be used to select from within the original array.

|Syntax|Meaning|
|---:|---|
|`⍳Y`&emsp;|[Index Generator](index-generator.md)|
|`X⍳Y`&emsp;|[Index Of](index-of.md)|
|`X⍸Y`&emsp;|[Interval Index](interval-index.md)|
|`⍋Y`&emsp;|[Grade Up](grade-up.md)|
|`X⍋Y`&emsp;|[Dyadic Grade Up](dyadic-grade-up.md)|
|`⍒Y`&emsp;|[Grade Down](grade-down.md)|
|`X⍒Y`&emsp;|[Dyadic Grade Down](dyadic-grade-down.md)|

## Index Generator Functions
Index generator functions return indices that can then be used directly or to select from within the original array.

|Syntax|Meaning|
|---:|---|
|`?Y`&emsp;|[Roll](roll.md)|
|`X?Y`&emsp;|[Deal](deal.md)|
|`⍳Y`&emsp;|[Index Generator](index-generator.md)|
|`X⍳Y`&emsp;|[Index Of](index-of.md)|
|`⍸Y`&emsp;|[Where](where.md)|
|`X⍸Y`&emsp;|[Interval Index](interval-index.md)|
|`⍋Y`&emsp;|[Grade Up](grade-up.md)|
|`X⍋Y`&emsp;|[Dyadic Grade Up](dyadic-grade-up.md)|
|`⍒Y`&emsp;|[Grade Down](grade-down.md)|
|`X⍒Y`&emsp;|[Dyadic Grade Down](dyadic-grade-down.md)|


## Structural Functions
Structural functions modify the structure or shape of their right argument (including omitting values) but they do not otherwise change any scalar values.

|Syntax|Meaning|
|---:|---|
|`X⍴Y`&emsp;|[Reshape](reshape.md)|
|`,Y`&emsp;|[Ravel](ravel/index.md)|
|`X,Y`&emsp;|[Catenate/Laminate](catenate-laminate.md)|
|`⍪Y`&emsp;|[Table](table.md)|
|`X⍪Y`&emsp;|[Catenate First/Laminate](catenate-first.md)|
|`⌽Y`&emsp;|[Reverse](reverse.md)|
|`X⌽Y`&emsp;|[Rotate](rotate.md)|
|`⍉Y`&emsp;|[Transpose](transpose.md)|
|`X⍉Y`&emsp;|[Dyadic Transpose](dyadic-transpose.md)|
|`⊖Y`&emsp;|[Reverse First](reverse-first.md)|
|`X⊖Y`&emsp;|[Rotate First](rotate-first.md)|
|`↑Y`&emsp;|[Mix](mix.md)|
|`X↑Y`&emsp;|[Take](take/index.md)|
|`↓Y`&emsp;|[Split](split.md)|
|`X↓Y`&emsp;|[Drop](drop/index.md)|
|`⊂Y`&emsp;|[Enclose](enclose/index.md)|
|`X⊂Y`&emsp;|[Partitioned Enclose](partitioned-enclose.md)|
|`⊆Y`&emsp;|[Nest](nest.md)|
|`X⊆Y`&emsp;|[Partition](partition.md)|
|`⊃Y`&emsp;|[First](first.md)|
|`X⊃Y`&emsp;|[Pick](pick.md)|
|`∊Y`&emsp;|[Enlist](enlist.md)|

## Data Conversion Functions
Data conversion functions change between different representations of the same data.

|Syntax|Meaning|
|---:|---|
|`⌷Y`&emsp;|[Materialise](materialise.md)|
|`⍎Y`&emsp;|[Execute](execute.md)|
|`X⍎Y`&emsp;|[Dyadic Execute](execute.md)|
|`⍕Y`&emsp;|[Format](format.md)|
|`X⍕Y`&emsp;|[Format by Specification](format-by-specification.md)|

## Identity Functions
Identity functions make it easy to write ambivalent dfns and are useful in tacit programming, as generic operands, and to break up stranding. They do not modify structure, shape, or values (exception: `⌷Y`, when applied to an object, extracts its default value).

|Syntax|Meaning|
|---:|---|
|`⌷Y`&emsp;|[Materialise](materialise.md)|
|`⊢Y`&emsp;|[Same](same.md)|
|`X⊢Y`&emsp;|[Right](right.md)|
|`⊣Y`&emsp;|[Same](same.md)|
|`X⊣Y`&emsp;|[Left](left.md)|

## Array Property Functions
Array property functions provide information about a given array.

|Syntax|Meaning|
|---:|---|
|`⌷Y`&emsp;|[Materialise](materialise.md)|
|`⍴Y`&emsp;|[Shape](shape.md)|
|`≡Y`&emsp;|[Depth](depth.md)|
|`≢Y`&emsp;|[Tally](tally.md)|
