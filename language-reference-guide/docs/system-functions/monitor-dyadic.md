---
search:
  boost: 2
---

# <span>Set Monitor Controls</span> `{R}←X ⎕MONITOR Y`{{key}}

This function sets monitor controls on lines of a tradfn or tradop, replacing any that are already set. Timing statistics are then collected for those lines each time they are executed, and [monadic `⎕MONITOR`](monitor-monadic.md) reports them.

<h2 class="example">Example</h2>

```apl
      ∇ FOO
[1]    A←?300 300⍴100
[2]    B←⌹A
[3]    C←⌹B
[4]    R1←⌊0.5+A+.×B
[5]    R2←A=C
      ∇
      ⎕←(0,⍳10) ⎕MONITOR 'FOO'
0 1 2 3 4 5
      FOO
```

## Left Argument

`X` is a simple integer scalar or vector of the line numbers on which monitor controls are set. `0` sets a monitor control on the function or operator as a whole. Other numbers that are not line numbers of the function or operator are ignored, and an empty `X` cancels all its monitor controls. `X` does not depend on [`⎕IO`](io.md).

<h3 class="example">Examples</h3>

Setting monitor controls cancels the existing ones, and the statistics collected for them:

```apl
      ⎕←1 ⎕MONITOR 'FOO'
1
      ⍴⍬ ⎕MONITOR 'FOO'
0
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible function or operator. A name that is not the name of a function or operator signals `DOMAIN ERROR`.

## Result

`R` is a simple integer vector of the line numbers on which monitor controls are now set, in ascending order, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results). Monitor controls apply only to tradfns and tradops, and cannot be set in a locked one: otherwise, the attempt is ignored, and `R` is empty.

Monitor controls, and the statistics collected for them, are saved with the workspace.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>
