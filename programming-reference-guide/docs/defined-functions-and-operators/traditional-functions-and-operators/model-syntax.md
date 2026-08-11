# Model Syntax

The model for the defined operation identifies the name of the operation, its valence, and whether or not an explicit result may be returned.  Valence is the number of explicit arguments or operands, either 0, 1 or 2; whence the operation is termed NILADIC, MONADIC or DYADIC respectively.  Only a defined function may be niladic.  There is no relationship between the valence of a defined operator, and the valence of the derived function which it produces.  Defined functions and derived functions produced by defined operators may be ambivalent, that is,  may be executed monadically with one argument, or dyadically with two.  An ambivalent operation is identified in its model by enclosing the left argument in braces.

The result of a function or derived function is [shy](../../introduction/results.md#shy-results) if the result in its model is enclosed in braces: a shy result is not displayed, although it can still be used or assigned.

The tables below show all possible models for defined functions and operators respectively.

## Defined Functions

|Result    |Niladic|Monadic  |Dyadic     |Ambivalent   |
|----------|-------|---------|-----------|-------------|
|None      |`f`    |`f Y`    |`X f Y`    |`{X} f Y`    |
|Explicit  |`R←f`  |`R←f Y`  |`R←X f Y`  |`R←{X} f Y`  |
|Shy|`{R}←f`|`{R}←f Y`|`{R}←X f Y`|`{R}←{X} f Y`|

Note: the right argument `Y` and/or the result `R` may be represented by a single name, or as a blank-delimited list of names surrounded by parentheses. For further details, see [Namelists](namelists.md).

## Derived Functions produced by Monadic Operator

|----------|-------------|--------------|----------------|
|Result    |Monadic      |Dyadic        |Ambivalent      |
|None      |`(A op)Y`    |`X(A op)Y`    |`{X}(A op)Y`    |
|Explicit  |`R←(A op)Y`  |`R←X(A op)Y`  |`R←{X}(A op)Y`  |
|Shy|`{R}←(A op)Y`|`{R}←X(A op)Y`|`{R}←{X}(A op)Y`|

## Derived Functions produced by Dyadic Operator

|----------|---------------|----------------|------------------|
|Result    |Monadic        |Dyadic          |Ambivalent        |
|None      |`(A op B)Y`    |`X(A op B)Y`    |`{X}(A op B)Y`    |
|Explicit  |`R←(A op B)Y`  |`R←X(A op B)Y`  |`R←{X}(A op B)Y`  |
|Shy|`{R}←(A op B)Y`|`{R}←X(A op B)Y`|`{R}←{X}(A op B)Y`|
