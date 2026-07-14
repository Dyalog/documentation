---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TSYNC TSYNC
</div>

# <span>Wait for Threads to Terminate</span> `R←⎕TSYNC Y`{{key}}

`Y` must be a simple array of thread numbers.

If `Y` is a simple scalar, `R` is an array, the result (if any) of the thread.

If `Y` is a simple non-scalar, `R` has the same shape as `Y`, and result is an array of enclosed thread results.

<h2 class="example">Examples</h2>
```apl
      dup←{⍵ ⍵}        ⍝ Duplicate
 
      ⎕←dup&88         ⍝ Show thread number
11
88 88
 
      ⎕TSYNC dup&88    ⍝ Wait for result
88 88
 
      ⎕TSYNC,dup&88
 88 88 
 
      ⎕TSYNC dup&1 2 3
 1 2 3  1 2 3 
 
      ⎕TSYNC dup&¨1 2 3
 1 1  2 2  3 3 
```

### Deadlock

The interpreter detects a potential deadlock if a number of threads wait for each other in a cyclic dependency. In this case, the thread that attempts to cause the deadlock issues error number `1008: DEADLOCK`.
```apl
     ⎕TSYNC ⎕TID      ⍝ Wait for self
DEADLOCK
      ⎕TSYNC ⎕TID
      ^
 
      ⎕EN
1008
```

### Potential Value Error

If any item of `Y` does not correspond to the thread number of an active thread, or if any subject thread terminates without returning a result, then `⎕TSYNC` does not return a result. This means that, if the calling context of the `⎕TSYNC` requires a result, for example: `rslt←⎕TSYNC tnums`, a `VALUE ERROR` will be generated. This situation can occur if threads have completed before `⎕TSYNC` is called.
```apl
      ⎕←÷&4          ⍝ thread (3) runs and terminates.
3
0.25
      ⎕TSYNC 3       ⍝ no result required: no prob
      ⎕←⎕TSYNC 3     ⍝ context requires result
VALUE ERROR
 
      ⎕←⎕TSYNC {}&0  ⍝ non-result-returning fn: no result.
VALUE ERROR
```

Coding would normally avoid such an inconvenient `VALUE ERROR` either by arranging that the thread-spawning and `⎕TSYNC` were on the same line:
```apl
      rslt ← ⎕TSYNC myfn&¨ argvec
```

or
```apl
      tnums←myfn&¨ argvec ⋄ rslt←⎕TSYNC tnums
```

or by error-trapping the `VALUE ERROR`.
