---
search:
  boost: 2
---

# <span>Decimal Comparison Tolerance</span> `⎕DCT`

The value of `⎕DCT` determines the precision with which two numbers are judged to be equal when the value of `⎕FR` is 1287. If `⎕FR` is 645, the system uses `⎕CT`.

`⎕DCT` is an [implicit argument](../primitive-functions/notes.md#implicit-arguments) of:

- monadic functions: [`⌈`](../primitive-functions/ceiling.md), [`⌊`](../primitive-functions/floor.md), [`∪`](../primitive-functions/unique.md), [`≠`](../primitive-functions/unique-mask.md)
- dyadic functions: [`~`](../primitive-functions/without.md), [`<`](../primitive-functions/less-than.md), [`≤`](../primitive-functions/less-than-or-equal-to.md), [`=`](../primitive-functions/equal-to.md), [`≥`](../primitive-functions/greater-than-or-equal-to.md), [`>`](../primitive-functions/greater-than.md), [`≠`](../primitive-functions/not-equal-to.md), [`≡`](../primitive-functions/match.md), [`≢`](../primitive-functions/not-match.md), [`⍳`](../primitive-functions/index-of.md), [`∊`](../primitive-functions/membership.md), [`∪`](../primitive-functions/union.md), [`∩`](../primitive-functions/intersection.md), [`⍷`](../primitive-functions/find.md), [`|`](../primitive-functions/magnitude.md), [`∨`](../primitive-functions/greatest-common-divisor-or.md), [`∧`](../primitive-functions/lowest-common-multiple-and.md)
- operators: [`⌸`](../primitive-operators/key.md)
- system functions: [`⎕FMT`](format-dyadic.md)

`⎕DCT` may be assigned any value in the range from `0` to `2*¯32` (about `2.3283064365386962890625E¯10`). A value of `0` ensures exact comparison. The value in a clear workspace is `1E¯28`. `⎕DCT` has Namespace scope.

For further information, see [Comparison Tolerance](ct.md).

<h2 class="example">Examples</h2>
```apl
      ⎕DCT←1E¯10
      1.00000000001 1.0000001 = 1
1 0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DCT DCT
</div>
