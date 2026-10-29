---
search:
  boost: 2
---

# <span>Call Unix Command Processor</span> `{R}←⎕SH Y`{{key}}

This function runs a command through a Unix shell and returns its output. [Dyadic `⎕SH`](sh-dyadic.md) starts an auxiliary processor instead.

`⎕SH` is a synonym of `⎕CMD`; this page describes their behaviour under Unix, and [monadic `⎕CMD`](cmd-monadic.md) describes it under Microsoft Windows. The [`)SH`](../system-commands/sh.md) system command runs a command in the same way, and [`⎕SHELL`](shell.md) runs an external program with more control over its input, output, and environment.

<h2 class="example">Example</h2>

```apl
      ⎕SH'echo Hello'
Hello
```

!!! Info "Information"
    This function is disabled and instead generates a `DOMAIN ERROR` if the RIDE_SPAWNED parameter is non-zero. This is designed to prevent it being invoked from a Ride session, which does not support this type of user interface. For further details, see the [Ride User Guide](https://dyalog.github.io/ride).

## Right Argument

`Y` is a simple character scalar or vector containing a command, which `⎕SH` runs with the shell `sh`. APL waits for the command to finish.

## Result

`R` is a vector of character vectors, with one item per line that the command writes to its standard output.

If the command writes nothing to its standard output, `R` is `0⍴⊂''`, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

If the result is not used, for example, when `⎕SH` is called in a statement on its own, the output of the command is not collected: the command writes directly to the standard output of APL, which is the session in a terminal, and its [exit status](#exit-status) is not checked. This makes `⎕SH` convenient to use in the session, and is why the output in the first example on this page appears without the leading space of a displayed vector of character vectors. `⎕SHELL` always returns its output.

<h2 class="example">Examples</h2>

```apl
      Z←⎕SH'printf "one\ntwo\n"'
      ⍴Z
2
      ⊃Z
one
      ⎕SH'rm old.log'
```

## Exit Status

If the result is used, and the command ends with a non-zero exit status, `DOMAIN ERROR` is signalled, and the output of the command is lost. A command whose exit status is not significant can end with `exit 0`; for example, `grep` has the exit status `1` when it finds no matching lines:

```apl
      Z←⎕SH'grep xyzzy /etc/passwd'
DOMAIN ERROR: Command interpreter returned failure code 1
      Z←⎕SH'grep xyzzy /etc/passwd'
        ∧
      Z←⎕SH'grep xyzzy /etc/passwd; exit 0'
      ⍴Z
0
```

[`⎕SHELL`](shell.md#return-value) returns the exit status of the command alongside its output, instead of signalling an error.

## Standard Error

`⎕SH` does not collect what the command writes to its standard error. The command can redirect it to its standard output:

```apl
      Z←⎕SH'ls nosuchfile 2>&1; exit 0'
      ⊃Z
ls: cannot access 'nosuchfile': No such file or directory
```

The [`Output`](shell.md#variant-option-output) variant option of `⎕SHELL` collects the standard error separately from the standard output.

## Background Commands

A command that ends with `&` runs in the background. `⎕SH` returns as soon as the shell has started it, but only if the command redirects its standard output and standard error away from `⎕SH`; otherwise, `⎕SH` waits until the command finishes:

```apl
      ⎕SH'./nightly-report.sh >report.log 2>&1 &'
```

APL cannot end a command that runs in the background. The [`Timeout`](shell.md#variant-option-timeout) and [`Signal`](shell.md#variant-option-signal) variant options of `⎕SHELL` can end a program that runs for too long.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SH SH
</div>
