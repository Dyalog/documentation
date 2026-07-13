




# <span>INDEX ERROR</span> `3`



This report is given when either:

- The value of an index, whilst being within comparison tolerance of an integer, is outside the range of values defined by the index vector along an axis of the array being indexed.  The permitted range is dependent on the value of `⎕IO`.
- The value specified for an axis, whilst being within comparison tolerance of an integer for a derived function requiring an integer axis value or a non-integer for a derived function requiring a non-integer, is outside the range of values compatible with the rank(s) of the array argument(s) of the derived function.  Axis is dependent on the value of `⎕IO`.

<h2 class="example">Examples</h2>
```apl
      A
1 2 3
4 5 6
 
      A[1;4]
INDEX ERROR
      A[1;4]
      ^
 
      ↑ [2]'ABC' 'DEF'
INDEX ERROR
      ↑ [2]'ABC' 'DEF'
      ^
```



