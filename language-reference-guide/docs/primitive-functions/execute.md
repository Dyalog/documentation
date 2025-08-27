<div style="display: none;">
  ⍎
</div>






<h1 class="heading"><span class="name">Execute</span> <span class="command">R←{X}⍎Y</span></h1>

!!! Warning
	If the argument to execute could include user input, then this might put data and systems at risk.
	To reduce the risk of this, a system function might be more appropriate than the execute function:

	* To get or set the value of one or more variables named within one or more character vectors, consider using [`⎕VGET`](../system-functions/vget.md) or [`⎕VSET`](../system-functions/vset.md).
	* To make numbers in text form into actual numbers, consider using [`⎕VFI`](../system-functions/vfi.md), [`⎕JSON`](../system-functions/json.md), or [`⎕CSV`](../system-functions/csv.md).

`Y` must be a simple character scalar or vector containing an APL expression to be executed. The expression may contain one or more sub-expressions separated by `⋄` (Diamond) characters.


If the result of the expression is used or is assigned to a name,  `R` is the result (if any) of the last-executed sub-expression and the non-shy results of all preceding expressions (that are not assigned within the expression) are displayed. Otherwise the unassigned non-shy results of all of the sub-expressions are displayed.


If the expression is an empty vector or a vector containing only blanks or one that does not produce a result, then `⍎Y` has no value and using or assigning it to a name will generate `VALUE ERROR`.



If `Y` contains a branch expression, the branch is effected in the environment from which the Execute was invoked, and `⍎Y` does not return.


If specified, `X` must be a namespace reference or a simple character scalar or vector representing the name of a namespace in which the expression is to be executed. If `X` is omitted or is an empty character vector, the expression is executed in the current space.


<h2 class="example">Examples</h2>
```apl

      ⍎'2+2'
4
      ⍎'1+1 ⋄ 2+2'
2
4
      A← ⍎'1+1 ⋄ 2+2'
2
      A
4
      4=⍎'1+1 ⋄ 2+2'
2
1
      ⍎'A←2|¯1↑⎕TS ⋄ →0⍴⍨A ⋄ A'
0
      A
0
      A←⍎''
VALUE ERROR: No result was provided when the context expected one
      A←⍎''
     ∧
      'myspace' ⎕NS''
      myspace⍎'A←⍳6'
      myspace.A
1 2 3 4 5 6
```


