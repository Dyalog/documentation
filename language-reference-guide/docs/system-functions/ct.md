---
search:
  boost: 2
---

# <span>Comparison Tolerance</span> `⎕CT`

The value of `⎕CT` determines the precision with which two numbers are judged to be equal.

`⎕CT` is an [implicit argument](../primitive-functions/notes.md#implicit-arguments) of:

- monadic functions: [`⌈`](../primitive-functions/ceiling.md), [`⌊`](../primitive-functions/floor.md), [`∪`](../primitive-functions/unique.md), [`≠`](../primitive-functions/unique-mask.md)
- dyadic functions: [`~`](../primitive-functions/without.md), [`<`](../primitive-functions/less-than.md), [`≤`](../primitive-functions/less-than-or-equal-to.md), [`=`](../primitive-functions/equal-to.md), [`≥`](../primitive-functions/greater-than-or-equal-to.md), [`>`](../primitive-functions/greater-than.md), [`≠`](../primitive-functions/not-equal-to.md), [`≡`](../primitive-functions/match.md), [`≢`](../primitive-functions/not-match.md), [`⍳`](../primitive-functions/index-of.md), [`∊`](../primitive-functions/membership.md), [`∪`](../primitive-functions/union.md), [`∩`](../primitive-functions/intersection.md), [`⍷`](../primitive-functions/find.md), [`|`](../primitive-functions/magnitude.md), [`∨`](../primitive-functions/greatest-common-divisor-or.md), [`∧`](../primitive-functions/lowest-common-multiple-and.md)
- operators: [`⌸`](../primitive-operators/key.md)
- system functions: [`⎕FMT`](format-dyadic.md)

Two numbers, `X` and `Y`, are judged to be equal if `(|X-Y)≤⎕CT×(|X)⌈|Y`where `≤` is applied without tolerance.

Thus `⎕CT` is not used as an absolute value in comparisons, but rather specifies a relative value that is dependent on the magnitude of the number with the greater magnitude. It then follows that `⎕CT` has no effect when either of the numbers is zero.

`⎕CT` may be assigned any value in the range from `0` to  `2*¯32`  (about `2.3E¯10`). A value of `0` ensures exact comparison.  The value in a clear workspace is `1E¯14`. `⎕CT` has Namespace scope.

If [`⎕FR`](fr.md) is 1287, the system uses `⎕DCT`. See [Decimal Comparison Tolerance ](dct.md).

<h2 class="example">Examples</h2>
```apl
      ⎕CT←1E¯10
      1.00000000001 1.0000001 = 1
1 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CT CT
</div>
