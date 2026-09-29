---
search:
  boost: 2
---

# <span>De-allocate Token Range</span> `{R}←X ⎕TALLOC ¯1`{{key}}

This function releases a range of token types previously reserved by [`⎕TALLOC 1`](talloc-allocate.md), making it free for re-allocation. For the other operations that `⎕TALLOC` performs, see [Token Allocation](talloc.md).

## Left Argument

`X` identifies the range to release. It is a scalar greater than or equal to the number of the range and less than one more than it, so the range's own number will do.

## Result

The [shy](../../programming-reference-guide/introduction/results.md#shy-results) result `R` is `X`.

## Conditions

The range must have been allocated, must not already have been released, and must be inactive: none of its tokens may be in the token pool or awaited by a [`⎕TGET`](tget.md). Otherwise `⎕TALLOC` signals a `DOMAIN ERROR` naming the range. Use [`⎕TALLOC 2`](talloc-pool.md) to see which of its tokens are still pooled.

<h2 class="example">Example</h2>

A range holding a token cannot be released until that token is taken:

```apl
      ⎕←trg←⎕TALLOC 1 'cats'
1
      ⎕TPUT trg+0.5
      trg ⎕TALLOC ¯1
DOMAIN ERROR: Token range 1 is in use
      trg ⎕TALLOC ¯1
          ∧
      trg ⎕TALLOC 2
1.5
      ⎕TGET trg+0.5
      ⎕←trg ⎕TALLOC ¯1
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
