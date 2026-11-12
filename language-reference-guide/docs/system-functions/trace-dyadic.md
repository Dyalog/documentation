---
search:
  boost: 2
---

# <span>Set Trace Vector</span> `{R}←X ⎕TRACE Y`{{key}}

This function sets trace controls on lines of a tradfn or tradop, replacing any that are already set. [Monadic `⎕TRACE`](trace-monadic.md) reports them.

<h2 class="example">Example</h2>

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      ⎕←(0,⍳10) ⎕TRACE 'FOO'
0 1
```

## Left Argument

`X` is a simple integer scalar or vector of the line numbers on which trace controls are set. `0` sets a trace control that displays the result of the function or operator immediately before exit. Other numbers that are not line numbers of the function or operator are ignored, and an empty `X` cancels all its trace controls. `X` does not depend on [`⎕IO`](io.md).

<h3 class="example">Examples</h3>

Setting trace controls cancels the existing ones:

```apl
      ⎕←1 ⎕TRACE 'FOO'
1
      ⍴⍬ ⎕TRACE 'FOO'
0
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible function or operator. A name that is not the name of a function or operator signals `DOMAIN ERROR`.

## Result

`R` is a simple integer vector of the line numbers on which trace controls are now set, in ascending order, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results). Trace controls apply only to tradfns and tradops, and cannot be set in a locked one: otherwise, the attempt is ignored, and `R` is empty.

## Tracing

When the function or operator runs, the result of each complete expression on a line with a trace control is displayed after the line is executed, and so is the result of the function or operator if trace control `0` is set. A line with several expressions separated by `⋄` displays the result of each.

The result is displayed even where it would normally be [shy](../../programming-reference-guide/introduction/results.md#shy-results), for example, the result of an assignment or of a function with a shy result. A branch displays `→` followed by the line number branched to.

Each display shows the name of the function or operator and the line number, followed by the result.

<h3 class="example">Example</h3>

```apl
      ∇ R←DSL SKIP;A;B;C;D
[1]    A←2×3+4
[2]    B←(2 3⍴'ABCDEF')A
[3]    →NEXT×⍳SKIP
[4]    'SKIPPED LINE'
[5]   NEXT:C←'one' ⋄ D←'two'
[6]   END:R←C D
      ∇
      (0,⍳6) ⎕TRACE 'DSL'
      DSL 1
 DSL[1]  14
 DSL[2]   ABC  14
          DEF
 DSL[3]  →5
 DSL[5]  one
 DSL[5]  two
 DSL[6]   one  two
 DSL[0]   one  two
 one  two
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>
