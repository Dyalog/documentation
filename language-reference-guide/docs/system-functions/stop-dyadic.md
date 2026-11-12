---
search:
  boost: 2
---

# <span>Set Stop Vector</span> `{R}←X ⎕STOP Y`{{key}}

This function sets stop controls on lines of a defined function or operator, replacing any that are already set. [Monadic `⎕STOP`](stop-monadic.md) reports them.

<h2 class="example">Example</h2>

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      ⎕←(0,⍳10) ⎕STOP 'FOO'
0 1
```

## Left Argument

`X` is a simple integer scalar or vector of the line numbers on which stop controls are set. `0` sets a stop control immediately before exit from the function or operator. Other numbers that are not line numbers of the function or operator are ignored, and an empty `X` cancels all its stop controls. `X` does not depend on [`⎕IO`](io.md).

<h3 class="example">Examples</h3>

Setting stop controls cancels the existing ones:

```apl
      ⎕←1 ⎕STOP 'FOO'
1
      ⍴⍬ ⎕STOP 'FOO'
0
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible function or operator. A name that is not the name of a function or operator signals `DOMAIN ERROR`.

## Result

`R` is a simple integer vector of the line numbers on which stop controls are now set, in ascending order, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results). Stop controls apply only to defined functions and operators (tradfns, tradops, dfns, and dops), and cannot be set in a locked function or operator: otherwise, the attempt is ignored, and `R` is empty.

## Stopping

When the function or operator runs, execution is suspended immediately before each line on which a stop control is set, and immediately before exit if a stop control `0` is set. Execution can be resumed by a branch, for example, `→⎕LC`. A stop is event 1001, which can be [trapped](trap.md).

<h3 class="example">Example</h3>

```apl
      0 1 ⎕STOP 'FOO'
      FOO

FOO[1]
      R
VALUE ERROR: Undefined name: R
      R
      ∧
      →1

FOO[0]
      R
10
      →⎕LC
10
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕STOP STOP
</div>
