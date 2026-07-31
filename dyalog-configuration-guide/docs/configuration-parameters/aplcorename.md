# AplCoreName

The directory and name of the file in which an *aplcore* is saved. An optional wild-card character (`*`) is replaced by a number when the file is written; if there is more than one `*`, the string is used as is, with no substitution. Dyalog terminates with an exit code of `3` when an aplcore is generated.

Valid values are a file path, optionally containing a single `*`.

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

Related parameters: [MaxAplCores](maxaplcores.md) (including how to prevent aplcore files being generated).

See also [aplcore Parameters](../../../language-reference-guide/primitive-operators/i-beam/aplcore-parameters).
