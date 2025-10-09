<h1 class="heading"><span class="name">Mixed Functions</span></h1>

Mixed rank functions and special symbols are summarised in [](#MixedRankFunctions). For convenience, they are sub-divided into five classes:

Table: Mixed rank functions and special symbols {: #MixedRankFunctions }

|-----------------|--------------------------------------------------------------------------------------------|
|**Structural**   |These functions change the structure of the arguments in some way.                          |
|**Selection**    |These functions select elements from an argument.                                           |
|**Selector**     |These functions identify specific elements by a Boolean map or by an ordered set of indices.|
|**Miscellaneous**|These functions transform arguments in some way, or provide information about the arguments.|
|**Special**      |These symbols have special properties.                                                      |

In general, the structure of the result of a mixed primitive function is different from that of its arguments.

Scalar extension may apply to some, but not all, dyadic mixed functions.

Mixed primitive functions are not pervasive. The function is applied to elements of the arguments, not necessarily independently.

<h2 class="example">Examples</h2>
```apl
      'CAT' 'DOG' 'MOUSE'⍳⊂'DOG'
2 
      3↑ 1 'TWO' 3 'FOUR'
1  TWO  3
```

In the following tables, note that:

- `[]` Implies axis specification is optional
- $  This function is in another class

Table: Structural Primitive Functions {: #Structural }

|Symbol|Monadic                                      |Dyadic                                              |
|------|---------------------------------------------|----------------------------------------------------|
|`⍴`   |$                                            |[Reshape](reshape.md)                               |
|`,`   |[Ravel ](ravel/index.md) `[]`                      |[Catenate/Laminate](catenate-laminate.md) `[]`      |
|`⍪`   |[Table](table.md)                            |[Catenate First / Laminate ](catenate-first.md) `[]`|
|`⌽`   |[Reverse ](reverse.md) `[]`                  |[Rotate ](rotate.md) `[]`                           |
|`⊖`   |[Reverse First ](reverse-first.md) `[]`      |[Rotate First ](rotate-first.md) `[]`               |
|`⍉`   |[Transpose](transpose.md)            |[Dyadic Transpose](dyadic-transpose.md)                    |
|`↑`   |[Mix](mix.md) / [First ](first.md) `[]`|$                                                   |
|`↓`   |[Split ](split.md) `[]`                      |$                                                   |
|`⊂`   |[Enclose ](enclose/index.md) `[]`                  |[Partitioned Enclose ](partitioned-enclose.md) `[]` |
|`⊆`   |[Nest](nest.md)                              |[Partition ](partition.md) `[]`                     |
|`∊`   |[Enlist](enlist.md) (See [Type](type.md) )   |$                                                   |

Table: Selection Primitive Functions {: #Selection }

|Symbol|Monadic                                 |Dyadic                                     |
|------|----------------------------------------|-------------------------------------------|
|`⊃`   |[First ](first.md) / [Mix](mix.md)|[Pick](pick.md)                            |
|`↑`   |$                                       |[Take ](take/index.md) `[]`                      |
|`↓`   |$                                       |[Drop ](drop/index.md) `[]`                      |
|`/`   |&nbsp;                                  |[Replicate ](replicate.md) `[]`            |
|`⌿`   |&nbsp;                                  |[Replicate First ](replicate-first.md) `[]`|
|`\`   |&nbsp;                                  |[Expand ](expand.md) `[]`                  |
|`⍀`   |&nbsp;                                  |[Expand First ](expand-first.md) `[]`      |
|`~`   |$                                       |[Without](without.md)        |
|`∩`   |&nbsp;                                  |[Intersection](intersection.md)            |
|`∪`   |[Unique](unique.md)                     |[Union](union.md)                          |
|`⊣`   |[Same](same.md)                         |[Left](left.md)                            |
|`⊢`   |[Same](same.md)                         |[Right](right.md)                          |
|`⌷`   |[Materialise](materialise.md)           |[Index](index-function/index.md)                          |
|`≠`   |[Unique Mask](unique-mask.md)           |&nbsp;                                     |

Table: Selector Primitive Functions {: #Selector }

|Symbol|Monadic                              |Dyadic                             |
|------|-------------------------------------|-----------------------------------|
|`⍳`   |[Index Generator](index-generator.md)|[Index Of](index-of.md)            |
|`⍸`   |[Where](where.md)                    |[Interval Index](interval-index.md)|
|`∊`   |$                                    |[Membership](membership.md)        |
|`⍋`   |[Grade Up](grade-up.md)      |[Dyadic Grade Up](dyadic-grade-up.md)     |
|`⍒`   |[Grade Down](grade-down.md)  |[Dyadic Grade Down](dyadic-grade-down.md) |
|`?`   |$                                    |[Deal](deal.md)                    |
|`⍷`   |&nbsp;                               |[Find](find.md)                    |

Table: Miscellaneous Primitive Functions {: #Miscellaneous }

|Symbol|Monadic                            |Dyadic                              |
|------|-----------------------------------|------------------------------------|
|`⍴`   |[Shape](shape.md)                  |$                                   |
|`≡`   |[Depth](depth.md)                  |[Match](match.md)                   |
|`≢`   |[Tally](tally.md)                  |[Not Match](not-match.md)           |
|`⍎`   |[Execute](execute.md)              |[Execute](execute.md)               |
|`⍕`   |[Format](format.md)        |[Format](format-by-specification.md)          |
|`⊥`   |&nbsp;                             |[Decode](decode.md)          |
|`⊤`   |&nbsp;                             |[Encode](encode.md)|
|`⌹`   |[Matrix Inverse](matrix-inverse.md)|[Matrix Divide](matrix-divide.md)   |

Table: Special Syntax {: #Special }

|Symbol|Monadic            |Dyadic                                          |
|------|-------------------|------------------------------------------------|
|`→`   |[Abort](abort.md)  |&nbsp;                                          |
|`→`   |[Branch](branch.md)|&nbsp;                                          |
|`←`   |&nbsp;             |[Assignment](assignment/index.md)                     |
|`[I]←`|&nbsp;             |[Assignment(Indexed)](assignment/assignment-indexed.md)    |
|`(I)←`|&nbsp;             |[Assignment(Selective)](assignment/assignment-selective.md)|
|`[]`  |&nbsp;             |[Indexing](indexing.md)                         |
