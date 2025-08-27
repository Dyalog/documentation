<div style="display: none;">
  ,
</div>






<h1 class="heading"><span class="name">Catenate/Laminate</span> <span class="command">R←X,[K]Y</span></h1>



`Y` may be any array.  `X` may be any array.  The axis specification is optional.  If specified, `K` must be a numeric scalar or 1-element vector which may have a fractional value.  If not specified, the last axis is implied.


The form `R←X⍪Y` may be used to imply catenation along the first axis.


Two cases of the function catenate  are permitted:

1. With an integer axis specification, or implied axis specification.
2. With a fractional axis specification, also called **laminate**. 


## Catenation with Integer or Implied Axis Specification


The arrays `X` and `Y` are joined along the required axis to form array `R`.  A scalar is extended to the shape of the other argument except that the required axis is restricted to a unit dimension.  `X` and `Y` must have the same shape (after extension) except along the required axis, or one of the arguments may have rank one less than the other, provided that their shapes conform to the prior rule after augmenting the array of lower rank to have a unit dimension along the required axis. The rank of `R` is the greater of the ranks of the arguments, but not less than 1.

<h2 class="example">Examples</h2>
```apl
      'FUR','LONG'
FURLONG
 
      1,2
1 2
 
      (2 4⍴'THISWEEK')⍪'='
THIS
WEEK
====
 
      S,[1]+⌿S←2 3⍴⍳6
1 2 3
4 5 6
5 7 9
```


If, after extension, exactly one of `X` and `Y` have a length of zero along the joined axis, then the data type of `R` will be that of the argument with a non-zero length. Otherwise, the data type of `R` will be that of `X`.

## Lamination with Fractional Axis Specification


The arrays `X` and `Y` are joined along a new axis created before the `⌈K`th axis.  The new axis has a length of 2.  `K` must exceed `⎕IO` (the index origin) minus 1, and `K` must be less than `⎕IO` plus the greater of the ranks of `X` and `Y`.  A scalar  argument is extended to the shape of the other argument.  Otherwise `X` and `Y` must have the same shape.


The rank of `R` is one plus the greater of the ranks of `X` and `Y`.

<h2 class="example">Examples</h2>
```apl
      'HEADING',[0.5]'-'
HEADING
-------
 
      'NIGHT',[1.5]'*'
N*
I*
G*
H*
T* 
      ⎕IO←0
      'HEADING',[¯0.5]'-'
HEADING
-------
```


