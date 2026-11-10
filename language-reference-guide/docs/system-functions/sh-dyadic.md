---
search:
  boost: 2
---

# <span>Start Unix Auxiliary Processor</span> `{R}←X ⎕SH Y`{{key}}

This function starts an auxiliary processor (AP), which defines one or more external functions in the workspace. [Monadic `⎕SH`](sh-monadic.md) runs a command instead.

`⎕SH` is a synonym of `⎕CMD`; this page describes their behaviour under Unix, and [dyadic `⎕CMD`](cmd-dyadic.md) describes it under Microsoft Windows. The effect on the workspace is the same on both, although the implementation differs.

!!! Hint "Hints and Recommendations"
    Although it is still possible for users to create their own APs, Dyalog Ltd strongly recommends creating shared libraries instead, and calling them through [`⎕NA`](na.md).

!!! Warning "Warning"
    Under macOS and Linux, auxiliary processors cannot be used if the [`ENABLE_CEF`](../../unix-installation-and-configuration-guide/configuration-parameters/environment-variables.md#_table-1) configuration parameter is `1`; they hang if an error occurs. The default value is `1`, except when Dyalog does not run under a desktop, for example, in a PuTTY session.

<h2 class="example">Example</h2>

```apl
      )CLEAR
clear ws
      'xutils' ⎕SH 'xutils'
      )FNS
avx     box     dbr     hex     ltom    ltov    mtol    ss      vtol
```

## Left Argument

`X` is a simple character vector containing the name or path name of a Dyalog APL auxiliary processor. A name is looked up in the directories that the [`WSPATH`](../../unix-installation-and-configuration-guide/configuration-parameters/environment-variables.md#_table-1) configuration parameter lists.

## Right Argument

`Y` is a simple character scalar or vector, or a vector of character vectors. Its items are passed to the auxiliary processor as the arguments `arg0` to `argn` of its command line, as in the Unix [`execl`](https://man7.org/linux/man-pages/man3/exec.3.html) call; `arg0` is conventionally the name of the auxiliary processor:

```apl
      'taskname' ⎕SH 'arg0' 'arg1' ... 'argn'
```

## Result

`R` is the process identifier of the auxiliary processor, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## External Functions

The external functions that the auxiliary processor defines appear in the workspace as locked functions, and are used in the same way as defined functions. When an external function is called, its arguments are piped to the auxiliary processor. If the function returns a result, APL waits while the auxiliary processor computes it; otherwise, APL continues in parallel with the auxiliary processor.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SH SH
</div>
