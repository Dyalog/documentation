---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SIZE SIZE
</div>






<h1 class="heading"><span class="name">Size of Object</span> <span class="command">R←⎕SIZE Y</span></h1>



`Y` must be a simple character scalar, vector or matrix, or a vector of character vectors containing a list of names. `R` is a simple integer vector of non-negative elements with the same length as the number of names in `Y`.


If the name in `Y` identifies an object with an active referent, the workspace required in bytes by that object is returned in the corresponding element of `R`.  Otherwise, 0 is returned in that element of `R`.


The result returned for an external variable is the space required to store the external array.  The result for a system constant, variable or function is 0.  The result returned for a GUI object gives the amount of workspace needed to store it, but excludes the space required for its children.



Note: Wherever possible, Dyalog APL *shares* the whole or part of a workspace object rather than generates a separate copy; however `⎕SIZE` reports the size as though nothing is shared. `⎕SIZE` also includes the space required for the interpreter's internal information about the object in question.

<h2 class="example">Examples</h2>
```apl
      ⎕VR 'FOO'
     ∇ R←FOO
[1]    R←10
     ∇
 
      A←⍳10
 
      'EXT/ARRAY' ⎕XT'E' ⋄ E←⍳20
 
      ⎕SIZE 'A' 'FOO' 'E' 'UND'
28 76 120 0
```


