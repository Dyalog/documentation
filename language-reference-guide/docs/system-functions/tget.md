---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TGET TGET
</div>





<h1 class="heading"><span class="name">Get Tokens</span> <span class="command">{R}←{X} ⎕TGET Y</span></h1>



`Y` must be a simple numeric scalar or vector that specifies one or more tokens, each with a specific non-zero token type, that are to be retrieved from the pool. Non-integer values in `Y` must fall within a range that has been allocated using `⎕TALLOC`.


`X` is an optional time-out value in seconds.


Shy result `R` is a scalar or vector containing the values of the tokens of type `Y` that have been retrieved from the token pool.


Note that types of the tokens in the pool may be positive or negative, and the elements of `Y` may also be positive or negative.


A request (`⎕TGET`) for a *positive* token will be satisfied by the presence of a token in the pool with the same positive or negative type. If the pool token has a positive type, it will be removed from the pool. If the pool token has a negative type, it will remain in the pool. N*egatively* typed tokens will therefore satisfy an infinite number of requests for their positive equivalents. Note that a request for a positive token will remove one if it is present, before resorting to its negative equivalent


A request for a negative token type will only be satisfied by the presence of a negative token type in the pool, and that token will be removed.


If, when a thread calls `⎕TGET`, the token pool satisfies **all** of the tokens specified by `Y`, the function returns immediately with a (shy) result that contains the values associated with the pool tokens. Otherwise, the function will block (wait) until **all** of the requested tokens are present or until a time-out (as specified by `X`) or a weak interrupt occurs.


For example, if the pool contains only tokens of type 2:
```apl
    ⎕TGET 2 4        ⍝ blocks waiting for a 4-token ...
```


The `⎕TGET` operation is atomic in the sense that no tokens are taken from the pool until **all** of the requested types are present. While this last example is waiting for a 4-token, other threads could take any of the remaining 2-tokens.


Note also, that repeated items in the right argument are distinct. The following will block until there are at least 3 `×` 1.9-tokens in the pool:
```apl
    ⎕TGET 3/1.9       ⍝ wait for 3 × 2-tokens ...
```


The pool is administered on a first-in-first-out basis. This is significant only if tokens of the same type are given distinct values. For example:
```apl
    ⎕TGET ⎕TPOOL             ⍝ empty pool.
 
    'ABCDE'⎕TPUT¨2 2 3 2 3  ⍝ pool some tokens.
 
    ⊢⎕TGET 2 3
AC
 
    ⊢⎕TGET 2 3
BE
```


`R` is an empty numeric vector `⍬` (zilde) if a timeout or a weak interrupt occurs.


**Beware** - the following statement will wait forever and can only be terminated by an interrupt.
```apl
    ⎕TGET 0       ⍝ wait forever ...
```


Note too that if a thread waiting to `⎕TGET` tokens is `⎕TKILL`ed, the thread disappears without removing any tokens from the pool. Conversely, if a thread that has removed tokens from the pools is `⎕TKILL`ed, the tokens are not returned to the pool.


