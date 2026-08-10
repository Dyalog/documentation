---
search:
  boost: 2
---

# <span>Put Tokens with Values</span> `{R}←X ⎕TPUT Y`{{key}}

`Y` must be a simple numeric scalar or vector of non-zero token types. Non-integer values in `Y` must fall within a range that has been allocated using `⎕TALLOC`.

To put tokens that carry no value, use [monadic `⎕TPUT`](tput-monadic.md).

`X` is an array of values to be stored in each of the tokens specified by `Y`.

Shy result `R` is a vector of thread numbers (if any) unblocked by the `⎕TPUT`.

<h2 class="example">Examples</h2>
```apl
                        another 2-token into the pool.
 
    88 ⎕TPUT 2        ⍝ put another 2-token into the pool
                        this token has the value 88.
 
    'Hello'⎕TPUT ¯1.9 ⍝ put a ¯1.9-token into the pool
                        with the value 'Hello'.
```

Note that you cannot put a 0-token into the pool; 0-s are removed from `Y`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TPUT TPUT
</div>
