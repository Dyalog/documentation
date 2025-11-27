---
search:
  boost: 2
---
<div style="display: none;">
  ⍎ execute
</div>






<h1 class="heading"><span class="name">Dyadic Execute</span> <span class="command">R←X⍎Y</span></h1>

!!! Warning "Warning"
	If the right argument to Dyadic Execute could include user input, then this might put data and systems at risk.
	To reduce the risk of this, a system function might be more appropriate than the Dyadic Execute function:

	* To get or set the value of one or more variables named within one or more character vectors, consider using [`⎕VGET`](../system-functions/vget.md) or [`⎕VSET`](../system-functions/vset.md).
	* To make numbers in text form into actual numbers, consider using [`⎕VFI`](../system-functions/vfi.md), [`⎕JSON`](../system-functions/json.md), or [`⎕CSV`](../system-functions/csv.md).
    * To call a function by name, in the namespace with the reference `nsRef`:
      * Niladic: `nsRef.⎕OR fnName nsRef.{⍺⍺})⍬`
      * Monadic: `nsRef.⎕OR fnName nsRef.{⍺⍺ ⍵})Y`
      * Dyadic: `X nsRef.⎕OR fnName nsRef.{⍺ ⍺⍺ ⍵})Y`
      A namespace name can be resolved to a reference with `nsRef←⎕VGET nsName`.

`Y` must be a simple character scalar or vector containing an APL expression to be executed. The expression may contain one or more sub-expressions separated by `⋄` (Diamond) characters.


`X` must be a namespace reference or a simple character scalar or vector representing the name of a namespace in which the expression is to be executed. If `X` is an empty character vector, the expression is executed in the current space.


If the result of the expression is used or is assigned to a name,  `R` is the result (if any) of the last-executed sub-expression and the non-shy results of all preceding expressions (that are not assigned within the expression) are displayed. Otherwise the unassigned non-shy results of all of the sub-expressions are displayed.


If the expression is an empty vector or a vector containing only blanks or one that does not produce a result, then `X⍎Y` has no value and using or assigning it to a name will generate `VALUE ERROR`.


If `Y` contains a branch expression, the branch is effected in the environment from which the _dyadic execute_ was invoked, and `X⍎Y` does not return.


<h2 class="example">Examples</h2>

Using a named namespace:
```apl
      space←'myspace'
      space ⎕NS''
      space⍎'nums←⍳6'
      space⍎'nums'
1 2 3 4 5 6
```
Using a reference:
```apl
      space←⎕NS''
      space⍎'nums←⍳6'
      space⍎'nums'
1 2 3 4 5 6
```

!!! Hint "Hints and Recommendations"
    It is faster and (potentially) safer to use system functions instead of _dyadic execute_ in the above examples as follows:
    
    Using a named namespace:
    ```apl
          space←'myspace'
          space ⎕NS''
          space ⎕VSET⊂'nums'(⍳6)
          space ⎕VGET'nums'
    1 2 3 4 5 6
    ```
    Using a reference:
    ```apl
          space←⎕NS''
          space ⎕VSET⊂'nums'(⍳6)
          space ⎕VGET'nums'
    1 2 3 4 5 6
    ```

