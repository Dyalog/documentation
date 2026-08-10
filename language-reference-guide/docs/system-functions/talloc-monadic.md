---
search:
  boost: 2
---

# <span>Allocate New Token Range</span> `{R}←⎕TALLOC Y`{{key}}

`Y` is either a single integer or a 2-element vector. The first (or only) item in `Y` is 0, 1, 2 or ¯1 and indicates the type of operation to perform. If it is 1, then the optional second item is a character vector.

To allocate from an existing token range, use [dyadic `⎕TALLOC`](talloc-dyadic.md).

## Allocation (First element of `Y` is 1)

If the first element of `Y` is 1,  the result `R` is a positive integer that identifies a range of numbers that may be used as token types for `⎕TPUT` and `⎕TGET`. That range is defined as the set of floating-point numbers between `R` and `R+1` (but not the integer end-points). Negated values of these number may also be used.

In this case, the optional `Y[2]` is an arbitrary character vector that serves as a description for the allocated range of tokens.

## Querying a description (`Y` is 0)

The result `R` is a vector of 2-element vectors identifying the range and description of all currently allocated ranges.

<h2 class="example">Examples</h2>
```apl
       ⎕←trg←⎕TALLOC 1 'cats'
1
       ⎕TALLOC 0
┌────────┐
│┌─┬────┐│
││1│cats││
│└─┴────┘│
└────────┘
      ⎕TPUT trg+.1 .2 .3
      ⎕TPUT -trg+.9
      ⎕TPOOL             
1.1 1.2 1.3 ¯1.9
      
      ⎕TGET trg+.1 .2 .3 .9
 
      ⎕TGET ¯1.9   ⍝ Remove the inexhaustible ¯1.9 token
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
