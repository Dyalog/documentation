# APL_MAX_THREADS

The maximum number of system threads used for parallel execution.

Valid values are a positive integer. A value greater than `64` is accepted and is reported by [`1111⌶`](../../language-reference-guide/primitive-operators/i-beam/number-of-threads.md), but Dyalog uses at most 64 threads.

Default is `1`.
