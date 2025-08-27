<h1 class="heading"><span class="name">File Hold</span> <span class="command">{R}←{X} ⎕FHOLD Y</span></h1>

## Access code 2048

This function holds component file(s) and/or external variable(s). It is used  to synchronise access to resources shared between multiple cooperating Dyalog processes. It is not intended to synchronise access between Dyalog threads; for this purpose you should use  `:Hold`.

For a  multi-threaded and multi-process application, a single `⎕FHOLD` is used to synchronise inter-process access, while `:Hold` is used in multiple threads to synchronise access between  threads in the same process. See also [Hold Statement](https://help.dyalog.com/19.0/index.htm#Language/Control%20Structures/hold.htm).

If applied to component files, then `Y` is an integer scalar, vector, or one-row matrix of file tie numbers, or a two-row matrix whose first row contains file tie numbers and whose second row contains passnumbers.

If applied to external variables, then `Y` is a simple scalar character, a character vector, a non-simple scalar character vector, or a vector of character vectors that specifies one or more names of external variable(s) (NOT the file names associated with those variables). Note that when `Y` is simple, each character in `Y` is interpreted as a  variable name. If applied to component files **and** external variables, `Y` is a vector whose elements are either integer scalars representing tie numbers, or character scalars or vectors containing names of external variables.

The effect is as follows:

1. **All** of the user's preceding holds (if any) are released, whether referenced in `Y` or not.
2. Execution is suspended until the designated files are free of holds by any other task.
3. When all the designated files are free, execution proceeds.  Until the hold is released, other tasks using `⎕FHOLD` on any of the designated files will wait.

The optional left argument `X` is a non-negative integer that specifies a time-out in milliseconds. If step 2 (see above) does not complete before the time-out value specified by `X`, `⎕FHOLD` times out and signals a `TIMEOUT` error (1006) after releasing any holds that have succeeded.

A time-out value of 0 indicates that the `⎕FHOLD` should time out at once without waiting if it cannot immediately acquire all holds. If `X` is `¯1`, `⎕FHOLD` behaves as the monadic case, and does not time out.

If `Y` is empty, all of the user's preceding holds (if any) are released, and execution continues.

A hold is released by any of the following:

- Another `⎕FHOLD`
- Untying or retying all the designated files.  If some but not all are untied or retied, they become free for another task but the hold persists for those that remain tied.
- Termination of APL.
- Any untrapped error or interrupt.
- A return to immediate execution mode.

Note that a hold is not released by a request for input through `⎕` or `⍞`.

`⎕FHOLD` is generally useful only when called from a defined function, as holds set in immediate execution (desk calculator) mode are released immediately.

If `Y` is a matrix, the shy result `R` is `Y[1;]`. Otherwise, the  shy result `R` is `Y`.

<h1 class="example">Examples</h1>
```apl
      ⎕FHOLD 1
 
      ⎕FHOLD ⍬
 
      ⎕FHOLD ⊂'XTVAR'
 
      ⎕FHOLD 1 2,[0.5]0 16385
 
      ⎕FHOLD 1 'XTVAR'

      3000 ⎕FHOLD 1
TIMEOUT
      3000 ⎕FHOLD 1
           ∧
```
