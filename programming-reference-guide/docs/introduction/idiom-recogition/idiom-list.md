# Idiom List

In the following table, arguments to the idiom have types and ranks as follows:

|Type|Description|Rank  |Description            |
|----|-----------|------|-----------------------|
|`C` |Character  |`S`   |Scalar or 1-item vector|
|`B` |Boolean    |`V`   |Vector                 |
|`N` |Numeric    |`M`   |Matrix                 |
|`P` |Nested     |`A`   |Array of any rank      |
|`X` |any type   |&nbsp;|&nbsp;                 |

For example: `NV`: numeric vector, `CM`: character matrix, `PV`: nested vector.

|Idiom|Description|
|---|---|
|`⍴⍴XA`|The rank of `XA` as a 1-element vector|
|`≢⍴XA`|The rank of `XA` as a scalar|
|`BV/⍳NS`|The subset of `NS` corresponding to the 1s in `BV`|
|`BV/⍳⍴XV`|The positions in `XV` corresponding to the 1s in `BV`|
|`NA⊃¨⊂XV`|The subset of `XV` in the index positions defined by `NA` (equivalent to `XV[NA]` )|
|`XA1{}XA2`|`XA1` and `XA2` are ignored (no result produced)|
|`XA1{⍺}XA2`|`XA1` ( `XA2` is ignored)|
|`XA1{⍵}XA2`|`XA2` ( `XA1` is ignored)|
|`XA1{⍺ ⍵}XA2`|`XA1` and `XA2` as a two item vector `(XA1 XA2)`|
|`{0}XA`|0 irrespective of `XA`|
|`{0}¨XA`|0 corresponding to each item of `XA`|
|`,/PV`|The enclose of the items of `PV` (which must be of depth 2) catenated along their last axes|
|`⍪/PV`|The enclose of the items of `PV` (which must be of depth 2) catenated along their first axes|
|`⊃⌽XA`|The item in the top right of `XA` ( `⎕ML<2` )|
|`↑⌽XA`|The item in the top right of `XA` ( `⎕ML≥2` )|
|`⊃⌽,XA`|The item in the bottom right of `XA` ( `⎕ML<2` )|
|`↑⌽,A`|The item in the bottom right of `XA` ( `⎕ML≥2` )|
|`0=⍴XV`|1 if `XV` has a shape of zero, 0 otherwise|
|`0=⍴⍴XA`|1 if `XA` has a rank of zero (scalar), 0 otherwise|
|`0=≡XA`|1 if `XA` has a depth of zero (simple scalar), 0 otherwise|
|`XM1{(↓⍺)⍳↓⍵}XM2`|A simple vector comprising as many items as there are rows in `XM2` , where each item is the number of the first row in `XM1` that matches each row in `XM2` . See note below.|
|`↓⍉↑PV`|A nested vector comprising vectors that each correspond to a position in the original vectors of `PV` – the first vector contains the first item from each vector in `PV` , padded to be the same length as the largest vector, and so on ( `⎕ML<2` )|
|`↓⍉⊃PV`|A nested vector comprising vectors that each correspond to a position in the original vectors of `PV` – the first vector contains the first item from each vector in `PV` , padded to be the same length as the largest vector, and so on ( `⎕ML≥2` )|
|`^\' '=CA`|A Boolean mask indicating the leading blank spaces in each row of `CA`|
|`+/^\' '=CA`|The number of leading blank spaces in each row of `CA`|
|`+/^\BA`|The number of leading 1s in each row of `BA`|
|`{(∨\' '≠⍵)/⍵}CV`|`CV` without any leading blank spaces|
|`{(+/^\' '=⍵)↓⍵}CV`|`CV` without any leading blank spaces|
|`~∘' '¨↓CA`|A nested vector comprising simple character vectors constructed from the rows of `CA` (which must be of depth 1) with all blank spaces removed|
|`{(+/∨\' '≠⌽⍵)↑¨↓⍵}CA`|A nested vector comprising simple character vectors constructed from the rows of `CA` (which must be of depth 1) with trailing blank spaces removed|
|`⊃∘⍴¨XA`|The length of the first axis of each item in `XA` ( `⎕ML<2` )|
|`↑∘⍴¨XA`|The length of the first axis of each item in `XA` ( `⎕ML≥2` )|
|`XA1,←XA2`|`XA1` redefined to be `XA1` with `XA2` catenated along its last axis|
|`XA1⍪←XA2`|`XA1` redefined to be `XA1` with `XA2` catenated along its first axis|
|`{(⊂⍋⍵)⌷⍵}XA`|`XA` sorted into ascending order|
|`{(⊂⍒⍵)⌷⍵}XA`|`XA` sorted into descending order|
|`{⍵[⍋⍵]}XV`|`XV` sorted into ascending order|
|`{⍵[⍒⍵]}XV`|`XV` sorted into descending order|
|`{⍵[⍋⍵;]}XM`|`XM` with the rows sorted into ascending|
|`{⍵[⍒⍵;]}XM`|`XM` with the rows sorted into descending order|
|`1=≡XA`|1 if `XA` has a depth of 1 (simple array), 0 otherwise|
|`1=≡,XA`|1 if `XA` has a depth of 0 or 1 (simple scalar, vector, etc.), 0 otherwise|
|`0∊⍴XA`|1 if `XA` is empty, 0 otherwise|
|`~0∊⍴XA`|1 if `XA` is not empty, 0 otherwise|
|`⊣⌿XA`|The first sub-array along the first axis of `XA`|
|`⊣/XA`|The first sub-array along the last axis of `XA`|
|`⊢⌿XA`|The last sub-array along the first axis of `XA`|
|`⊢/XA`|The last sub-array along the last axis of `XA`|
|`*○NA`|Euler's idiom (accurate when `NA` is a multiple of `0J0.5)`|
|`0=⊃⍴XA`|1 if `XA` has an empty first dimension, 0 otherwise ( `⎕ML<2` )|
|`0≠⊃⍴XA`|1 if `XA` does not have an empty first dimension, 0 otherwise ( `⎕ML<2` )|
|`⎕AV⍳CA`|Classic version only: The character numbers (atomic vector index) corresponding to the characters in `CA`|
|`⌊0.5+NA`|Round to nearest integer|
|`XA↓⍨←NS`|This idiom applies only when `NS` is negative, when it removes the last `-NS` items from `XA` along its leading axis. See note below.|
|`{(⊂⍋⍵)⌷⍵}{(⊂⍒⍵)⌷⍵}`|These idioms provide the fastest way to sort  arrays of any rank|

## Notes

`/⍳` and `/⍳⍴`, as well as providing an execution time advantage, reduce intermediate workspace usage and, consequently, the incidence of memory compactions and the likelihood of a `WS FULL`.

`NA⊃¨⊂XV` is implemented as `XV[NA]`, which is significantly faster. The two are equivalent but the former now has no performance penalty.

`,/` is special-cased only for vectors of vectors or scalars. Otherwise, the expression is evaluated as a series of concatenations. Recognition of this idiom turns **join** from an *n-squared* algorithm into a linear one. In other words, the improvement factor is proportional to the size of the argument vector.

`⊃⌽` and `⊃⌽,` now take constant time. Without idiom recognition, the time taken depends linearly on the number of items in the argument.

`0=≡` takes a small constant time. Without idiom recognition, the time taken would depend on the size and depth of the argument, which in the case of a deeply nested array could be significant.

`↓⍉↑` is special-cased only for a vector of nested vectors, each of whose items is of the same length.

`{(↓⍺)⍳↓⍵}` can accommodate much larger matrices than its constituent primitives. It is particularly effective when bound with a left argument using the compose operator:
```apl
      find←mat∘{(↓⍺)⍳↓⍵}     ⍝ find rows in mat table
```

In this case, the internal hash table for `mat` is retained so that it does not need to be generated each time the monadic derived function `find` is applied to a matrix argument.

`{(∨\' '≠⍵)/⍵}` and `{(+/^\' '=⍵)↓⍵}` are two codings of the same idiom. Both use the same C code for evaluation.

`~∘' '¨↓` typically takes a character matrix argument and returns a vector of character vectors from which all blanks have been removed. An example might be the character matrix of names returned by the system function `⎕NL`. In general, this idiom accommodates character arrays of any rank.

`{(+/∨\' '≠⌽⍵)↑¨↓⍵}` typically takes a character matrix argument and returns a vector of character vectors. Any embedded blanks in each row are preserved but trailing blanks are removed. In general, this idiom accommodates character arrays of any rank.

`⊃∘⍴¨A` (`⎕ML<2`) and `↑∘⍴¨A` (`⎕ML>2`) avoid having to create an intermediate nested array of shape vectors.

For an array of vectors, this idiom quickly returns a *simple array* of the length of each vector.
```apl
      ⊃∘⍴¨ 'Hi' 'Pete' ⍝ Vector Lengths
2 4
```

For an array of matrices, it returns a simple array of the number of rows in each matrix.
```apl
      ⊃∘⍴¨⎕CR¨↓⎕NL 3   ⍝ Lines in functions
5 21...
```

`A,←A` and `A⍪←A` optimise the catenation of an array to another array along the last and first dimension respectively.

Among other examples, this idiom optimises repeated catenation of a scalar or vector to an existing vector.
```apl
      props,←⊂ 'Posn' 0 0
      props,←⊂'Size' 50 50
      vector,←2+4
```

Note that the idiom is not applied if the value of vector `V` is shared with another symbol in the workspace, as illustrated in the following examples:

Example 1: the idiom is used to perform the catenation to `V1`.
```apl
      V1←⍳10
      V1,←11
```

Example 2: the idiom is not used to perform the catenation to `V1`, because its value is at that point shared with `V2`.
```apl
      V1←⍳10
      V2←V1
      V1,←11
```

Example 3: the idiom is not used to perform the catenation to `V` in `Join[1]` because its value is, at that point, shared with the array used to call the function.
```apl
     ∇ V←V Join A
[1]    V,←A
     ∇
      (⍳10) Join 11
1 2 3 4 5 6 7 8 9 10 11
```

`⊢⌿XA`, `⊢/XA`, `⊣⌿XA`, and `⊣/XA` return the first/last rank `(0⌈¯1+⍴⍴A)` sub-array along the first/last axis of `XA`. For example, if `V` is a vector, then:

|-----|--------------------|
|`⊣/V`|First item of vector|
|`⊢/V`|Last item of vector |

Similarly, if `M` is a matrix, then:

|-----|----------------------|
|`⊣⌿M`|First row of matrix   |
|`⊣/M`|First column of matrix|
|`⊢⌿M`|Last row of matrix    |
|`⊢/M`|Last column of matrix |

The idiom generalises uniformly to higher-rank arrays.

**Euler's idiom** `*○NA` produces accurate results for right argument values that are a multiple of `0J0.5`. This is so that Euler's famous identity `0=1+*○0J1` holds, despite pi being represented as a floating point number.

For clarification; `XA↓⍨←NS`. If `NS` is `¯3` then the idiom removes the last `-¯3` (that is, 3) items.

The idiom `XM1{(↓⍺)⍳↓⍵}XM2` is still recognised, but since Version 14.0 is no faster than `XM1⍳XM2`.
