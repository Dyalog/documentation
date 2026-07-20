---
search:
  boost: 2
---

# <span>Allocate Token Range</span> `{R}←{X} ⎕TALLOC Y`{{key}}

`Y` is either a single integer or a 2-element vector. The first (or only) item in `Y` is 0, 1, 2 or ¯1 and indicates the type of operation to perform. If it is 1, then the optional second item is a character vector.

The optional left argument  `X` identifies an existing allocated range of token numbers `n`. `X` must be a scalar greater than or equal to `n`, but must be less than `n+1`.

## Allocation (First element of `Y` is 1)

If the first element of `Y` is 1,  the result `R` is a positive integer that identifies a range of numbers that may be used as token types for `⎕TPUT` and `⎕TGET`. That range is defined as the set of floating-point numbers between `R` and `R+1` (but not the integer end-points). Negated values of these number may also be used.

In this case, the optional `Y[2]` is an arbitrary character vector that serves as a description for the allocated range of tokens.

## De-allocation (`Y` is `¯1`)

If `Y` is `¯1`, `⎕TALLOC` releases a previously allocated range of tokens identified by the left-argument `X`. The result `R` is a shy `⍬`.

To succeed, this range must have previously been allocated, not freed by de-allocation, and must be inactive, that is, its tokens must not currently be  in the token pool or in use by a `⎕TGET`. If not, `⎕TALLOC` will signal a `DOMAIN ERROR`.

A de-allocated range becomes free for subsequent re-allocation by `⎕TALLOC`.

## Querying a description (`Y` is 0)

`Y` is 0, `⎕TALLOC` returns a non-shy result `R` containing the description for a currently allocated range of tokens identified by the left-argument `X`.

If `X` does not represent a currently allocated range, `⎕TALLOC` will signal a `DOMAIN ERROR`.

If `X` is omitted, the result `R` is a vector of 2-element vectors identifying the range and description of all currently allocated ranges.

Descriptions that were not defined are returned as empty character vectors.

## Querying  the Token Pool (`Y` is 2)

`Y` is 2, `⎕TALLOC` returns a non-shy result `R` containing the list of tokens in the token pool that fall in the range specified by the left-argument `X`.

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
 
      1 ⎕TALLOC ¯1 ⍝ Try to de-allocate the range     
DOMAIN ERROR
      1 ⎕TALLOC ¯1 
        ∧
      1 ⎕TALLOC 2  ⍝ Failed due to ¯1.9 token
¯1.9
      ⎕TGET ¯1.9   ⍝ Remove the inexhaustible ¯1.9 token
      1 ⎕TALLOC 2

      1 ⎕TALLOC ¯1 ⍝ De-allocation now works   

```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TALLOC TALLOC
</div>
