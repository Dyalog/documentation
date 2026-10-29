---
search:
  boost: 2
---

# <span>Start Windows Auxiliary Processor</span> `{R}←X ⎕CMD Y`{{key}}

This function starts an auxiliary processor (AP), which defines one or more external functions in the workspace. [Monadic `⎕CMD`](cmd-monadic.md) runs a command or starts a program instead.

`⎕CMD` is a synonym of `⎕SH`; this page describes their behaviour under Microsoft Windows, and [dyadic `⎕SH`](sh-dyadic.md) describes it under Unix. The effect on the workspace is the same on both, although the implementation differs.

!!! Hint "Hints and Recommendations"
    Although it is still possible for users to create their own APs, Dyalog Ltd strongly recommends creating shared libraries or DLLs instead, and calling them through [`⎕NA`](na.md).

<h2 class="example">Example</h2>

```apl
      )CLEAR
clear ws
      'xutils' ⎕CMD ''
      )FNS
avx     box     dbr     getenv  hex     ltom    ltov    mtol    ss      vtol
```

## Left Argument

`X` is a simple character vector containing the name or path name of a Dyalog APL auxiliary processor.

## Right Argument

`Y` is a simple character scalar or vector, or a vector of character vectors. Under Microsoft Windows, its content is ignored.

## Result

`R` is the process identifier of the auxiliary processor, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## External Functions

`⎕CMD` loads the auxiliary processor into memory. If no other auxiliary processors are running, it also allocates an area of memory for communication between APL and auxiliary processors.

The external functions that the auxiliary processor defines appear in the workspace as locked functions, and are used in the same way as defined functions. When an external function is called, its arguments are passed to the auxiliary processor through the communication area, and APL waits while the auxiliary processor computes the result. Under Microsoft Windows, unlike under Unix, external functions cannot run in parallel with APL.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CMD CMD
</div>
