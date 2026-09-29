---
search:
  boost: 2
---

# <span>Query Pooled Tokens in Range</span> `R←X ⎕TALLOC 2`{{key}}

This function reports which tokens currently in the token pool belong to one allocated range. For the other operations that `⎕TALLOC` performs, see [Token Allocation](talloc.md).

## Left Argument

`X` identifies the range to report on. It is a scalar greater than or equal to the number of the range and less than one more than it, so the range's own number will do.

## Result

`R` is the tokens in the pool that fall within the range, as reported by [`⎕TPOOL`](tpool.md) for the pool as a whole. It is empty when the range holds none, which is the condition [`⎕TALLOC ¯1`](talloc-deallocate.md) requires before it will release the range.

<h2 class="example">Example</h2>

Two ranges, each holding its own tokens:

```apl
      ⎕←a←⎕TALLOC 1 'cats'
1
      ⎕←b←⎕TALLOC 1 'dogs'
2
      ⎕TPUT a+0.1 0.2
      ⎕TPUT b+0.5
      ⎕TPOOL
1.1 1.2 2.5
      a ⎕TALLOC 2
1.1 1.2
      b ⎕TALLOC 2
2.5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
