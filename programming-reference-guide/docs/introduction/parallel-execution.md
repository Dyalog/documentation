<h1 class="heading"><span class="name">Parallel Execution</span></h1>

If your computer has more than one CPU or is a multi-core processor, then the scalar dyadic functions `÷`, `≥`, `=`, `≤`, `⍟`, `|`, `!`, `○`, `∨` and `∧` will, when applied to arrays with a sufficiently large number of elements,  execute in parallel in separate system threads.

For example,  if you have a computer with 4 cores (either real or virtual) and execute an expression such as (`A÷B`) where `A` and/or `B` contain more than 32,768 elements, then  Dyalog will start 4 separate threads, each performing the division on ¼ of the elements of the array(s) and simultaneously creating the corresponding ¼ of the result array. The threads are only started once, and are reused for subsequent multi-threaded operations.

The maximum number of threads to use can be controlled using `1111⌶`, and the parallel execution threshold is changed using `1112⌶`. These "tuning" I-beams should be considered experimental, and may be changed or replaced  in a future release.  (See [Number of Threads](../../../language-reference-guide/primitive-operators/i-beam/number-of-threads) and [Parallel Execution Threshold](../../../language-reference-guide/primitive-operators/i-beam/parallel-execution-threshold)).

Note that these scalar dyadic functions are not multi-threaded when applied to arrays of Boolean or integer values, they are also not multi-threaded for `+`, `-` or `×` when applied to arrays of 64 bits floating (type 645). Tests show that the overhead of preparing such arrays for multi-threaded operations outweigh the performance benefits.
