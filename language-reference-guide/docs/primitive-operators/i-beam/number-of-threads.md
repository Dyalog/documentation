---
search:
  boost: 2
---


# <span>Number of Threads</span> `R←1111⌶Y`{{key}}

Specifies how many threads are to be used for parallel execution.

If `Y` has the value `⍬`, `R` is the number of virtual processors in the machine.

Otherwise, `Y` is an integer that specifies the number of threads that are to be used henceforth for parallel execution. Prior to this call, the default number of threads is specified by the [`APL_MAX_THREADS`](../../../windows-installation-and-configuration-guide/configuration-parameters/apl-max-threads.md) configuration parameter, which is `1` when that parameter is not set.

`Y` must be a positive integer; `0`, a negative value, or a fractional value signals `DOMAIN ERROR`.

`R` is the previous value.

A value greater than 64 is accepted and is reported back by the next call, but Dyalog uses at most 64 threads, so the effective number of threads is `Y⌊64`:

```apl
      {}1111⌶100
      1111⌶1
100
```

To set the number of threads to be the same as the number of virtual processors, execute the statement:

```apl
      {}1111⌶ 1111⌶⍬
```

See [Parallel Execution](../../../programming-reference-guide/introduction/parallel-execution.md) and [Parallel Execution Threshold](parallel-execution-threshold.md).

<!-- Hidden search keywords -->
<div style="display: none;">
  1111⌶
</div>
