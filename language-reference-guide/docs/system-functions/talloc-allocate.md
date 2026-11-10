---
search:
  boost: 2
---

# <span>Allocate Token Range</span> `{R}←⎕TALLOC Y`{{key}}

This function reserves a range of token types for use by [`⎕TPUT`](tput.md) and [`⎕TGET`](tget.md), so that the tokens that one part of an application uses cannot collide with those used by another. For the other operations that `⎕TALLOC` performs, see [Token Allocation](talloc.md).

## Right Argument

`Y` is `1`, or a 2-element vector whose first element is `1` and whose second is a character vector describing the range. The description is arbitrary; it is reported by [`⎕TALLOC 0`](talloc-ranges.md) and is not otherwise used.

## Result

`R` is a positive integer identifying the range allocated. The range is the set of floating-point numbers strictly between `R` and `R+1`, and their negations; the integer end-points are not part of it.

<h2 class="example">Example</h2>

Allocating a range and putting a token from it into the pool:

```apl
      ⎕←trg←⎕TALLOC 1 'cats'
1
      ⎕TPUT trg+0.5
      ⎕TPOOL
1.5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
