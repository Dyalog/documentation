---
search:
  boost: 2
---

# <span>Query Allocated Token Ranges</span> `R←{X} ⎕TALLOC 0`{{key}}

This function reports the token ranges currently allocated by [`⎕TALLOC 1`](talloc-allocate.md), and the descriptions given for them. For the other operations that `⎕TALLOC` performs, see [Token Allocation](talloc.md).

## Left Argument

`X` identifies one range to report on. It is a scalar greater than or equal to the number of the range and less than one more than it, so the range's own number will do. If `X` does not identify a currently allocated range, `⎕TALLOC` signals a `DOMAIN ERROR`.

If `X` is omitted, every currently allocated range is reported.

## Result

If `X` is given, `R` is that range's description, or an empty character vector where none was given.

If `X` is omitted, `R` is a vector of 2-element vectors, each pairing a range number with its description.

<h2 class="example">Example</h2>

Two ranges, one without a description and one with:

```apl
      ⎕←a←⎕TALLOC 1
1
      ⎕←b←⎕TALLOC 1 'cats'
2
      ⎕TALLOC 0
┌────┬────────┐
│┌─┬┐│┌─┬────┐│
││1││││2│cats││
│└─┴┘│└─┴────┘│
└────┴────────┘
      a ⎕TALLOC 0

      b ⎕TALLOC 0
cats
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
