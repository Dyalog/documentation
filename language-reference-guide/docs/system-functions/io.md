---
search:
  boost: 2
---

# <span>Index Origin</span> `⎕IO`

`⎕IO` determines the index of the first element of a non-empty vector.

`⎕IO` is an [implicit argument](../primitive-functions/notes.md#implicit-arguments) of:

- monadic functions: [`⍳`](../primitive-functions/index-generator.md), [`?`](../primitive-functions/roll.md), [`⍒`](../primitive-functions/grade-down.md), [`⍋`](../primitive-functions/grade-up.md), [`⍸`](../primitive-functions/where.md)
- dyadic functions: [`⍳`](../primitive-functions/index-of.md), [`?`](../primitive-functions/deal.md), [`⍒`](../primitive-functions/dyadic-grade-down.md), [`⍋`](../primitive-functions/dyadic-grade-up.md), [`⍉`](../primitive-functions/dyadic-transpose.md), [`⊃`](../primitive-functions/pick.md), [`⌷`](../primitive-functions/index-function/index.md), [`⍸`](../primitive-functions/interval-index.md)
- operators: [`⌸`](../primitive-operators/key.md), [`@`](../primitive-operators/at.md)
- system functions: [`⎕FX`](fx.md), [`⎕DMX`](dmx.md)
- other syntax: bracket indexing and bracket axis, indexed assignment

`⎕IO` may be assigned the value 0 or 1.  The value in a clear workspace is 1. `⎕IO` has Namespace scope.

<h2 class="example">Examples</h2>
```apl
        ⎕IO←1
        ⍳5
1 2 3 4 5
 
        ⎕IO←0
        ⍳5
0 1 2 3 4
 
        +/[0]2 3⍴⍳6
3 5 7
 
        'ABC',[¯.5]'='
ABC
===
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕IO IO
</div>
