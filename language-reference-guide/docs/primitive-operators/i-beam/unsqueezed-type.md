---
search:
  boost: 2
---


# <span>Unsqueezed Type</span> `R←181⌶Y`{{key}}

`Y` is any array.

The result `R` is an integer scalar that indicates the type in which `Y` is stored, using the values listed for [monadic `⎕DR`](../../system-functions/data-representation-monadic.md).

`181⌶` is identical to monadic `⎕DR`, except that it does not squeeze `Y` into a smaller internal representation. Monadic `⎕DR` squeezes `Y` unless `Y` is data converted by [dyadic `⎕DR`](../../system-functions/data-representation-dyadic.md) to which no function that changes it has been applied. If a workspace compaction occurs during the execution of `181⌶`, then `Y` can still be squeezed before its type is identified.

<h2 class="example">Examples</h2>
```apl
      ⎕DR 1↑1 1000
83
      181⌶ 1↑1 1000
163

      v←645 ⎕DR 64⍴0
      ⎕DR ⍪v
83
      181⌶ ⍪v
645
```

<!-- Hidden search keywords -->
<div style="display: none;">
  181⌶
</div>
