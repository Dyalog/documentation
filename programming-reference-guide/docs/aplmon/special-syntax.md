# Special syntax

APL has some special syntax that is treated in a special way by APLMON.

For example, cases of Simple Indexing (where the indexer is a set of semicolon-separated simple arrays) are reported as follows.

The *token* is `simple indexing`, there are no *lfn* or *rfn*, the left argument is the indexed array, and the right argument is as representative of the indices as possible. Dyalog has chosen to make it appear as an array, the rank of which is the number of specified subscripts, and the shape of which is the number of items in these subscripts.

|APL  expression|token            |lfn   |rfn   |ltype   |rtype|lrank|rrank|lbound|rbound|
|---------------|-----------------|------|------|--------|-----|-----|-----|------|------|
|`'abcd'[3 3⍴3]`|`simple indexing`|&nbsp;|&nbsp;|unicode8|int8 |1    |1    |2<4   |5<9   |
|`(2 2⍴4)[1;]`  |`simple indexing`|&nbsp;|&nbsp;|int8    |int8 |2    |1    |2<4   |1<1   |

## Reach and Choose Indexing (where the indexer is a nested array)

The *token* is `reach indexing`, the left argument is the indexed array, and the right argument is the indexer array.

## Axis specification

The token is `axis`, *lfn* is the function whose axis is specified, *rfn* is `non-primitive`, as it is the axis specification constant.

## Assignment

The *token* is `left arrow` and it is considered as a monadic function.

## Modified Assignment

The *token* is `left arrow`, *lfn* is the modifier function, *rfn* is empty, *larg* is the modified value and *rarg* the modifier value.

## Indexed Assignment

The *token* is `indexed assignment`, *lfn* and *rfn* are empty, *larg* is the indexed array, *rarg* is the new value.

## Modified Indexed Assignment

The *token* is `indexed assignment`, *lfn* is the modifier function, *rfn* is empty, *larg* is the indexed array, *rarg* is the new value.

## Selective Assignment

The *token* is `selective assignment`,*lfn* and *rfn* are empty,*larg* is the indexed array, *rarg* is the new value.

## Modified Selective Assignment

The *token* is `selective assignment`, *lfn* is the modifier function, *rfn* is empty, *larg* is the indexed array, *rarg* is the new value.

## Stranding

The *token* is `stranding`, *larg* and *rarg* are the arrays being stranded together.

## Name Lookup

The *token* is `name lookup`. This represents time spent in the parser looking up names in namespaces.

## Defined Function Initialisation

The *token* is `tradfn init`. This represents time spent on entry to a traditional defined function.

## Selective Assignment Pre-scan

The *token* is `selassi pre-scan`. This represents extra time spent in the parser to analyse the syntax of a selective assignment expression.

## Control Structures

The *token* is `control structures`. This represents time spent processing control structures in a traditional defined function.

## Namespace dot syntax

The *token* is `nsref`, lfn and *rfn* are right and left operands respectively, *larg* and *rarg* are as expected.

For example, in the expression: `⎕SE.⎕EX 'var'`

*token* is `nsref`, *lfn* is `⎕EX`, *rfn* is `non-primitive`, *larg* is empty, *rarg* is the character vector.
