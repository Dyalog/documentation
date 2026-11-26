---
search:
  boost: 2
---

# <span>End Session</span> `⎕OFF{I}`{{key}}

This is a system constant. Evaluating it ends the APL session, and stranding it with an array `I`, as in `⎕OFF 42`, makes `I` the [exit code](#exit-code) that the session returns to the operating system.

<h2 class="example">Example</h2>

In a Unix shell, the exit code of a script is in `$?`:

```other
$ echo '⎕OFF 42' > done.apls
$ dyalogscript done.apls; echo $?
42
```

`⎕OFF` ends the session wherever it is evaluated, including in a defined function or a dfn. Statements after it on the same line do not run.

## Exit Code

`I` is optional, and is what `⎕OFF` is stranded with, such as a number, a name, or an expression in parentheses. Stranding [binds](../../programming-reference-guide/introduction/binding-strength.md) more tightly than a function, meaning that `⎕OFF 2+3` ends the session with the exit code `2`, while `⎕OFF (2+3)` ends it with `5`. If a function immediately follows `⎕OFF`, as in `⎕OFF ≢⎕A`, nothing is stranded with it.

`I` is a whole number from `0` to `255`, as a scalar or as an array with one item. Any other number signals `DOMAIN ERROR`, and more or fewer items signal `LENGTH ERROR`. These errors can be trapped. If `I` is omitted, the exit code is `0`.

!!! Hint "Hints and Recommendations"
    The interpreter uses the [exit codes](../../windows-installation-and-configuration-guide/apl-exit-codes.md) `0` to `13` itself, and Dyalog Ltd recommends values greater than `13` for an application's own exit codes. Under Unix, exit codes greater than `127` usually report the signal that ended a process.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕OFF OFF
</div>
