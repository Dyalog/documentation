# MaxAplCores

The maximum number of *aplcore* files retained. It applies, in conjunction with [`AplCoreName`](aplcorename.md), when the string given by `AplCoreName` ends with an asterisk (`*`). When saving an aplcore, Dyalog finds the highest-numbered matching file (or `0` if none), increments it, saves the new aplcore with that number, and deletes lower-numbered files so that at most this many are kept.

Valid values are a positive integer.

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

Related parameters: [AplCoreName](aplcorename.md).

See also [aplcore Parameters](../../../language-reference-guide/primitive-operators/i-beam/aplcore-parameters).
