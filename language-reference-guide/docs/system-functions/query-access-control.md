---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVC SVC
</div>






<h1 class="heading"><span class="name">Query Access Control</span> <span class="command">R←⎕SVC Y</span></h1>



This system function queries the access control on one or more shared variables.


`Y` is a character scalar, vector, or matrix containing names of shared variables.  Each name may optionally be paired with its surrogate.  If so, the surrogate must be separated from the name by at least one space.


If `Y` specifies a single name, the result `R` is a Boolean vector containing the current effective access control vector.  If `Y` is a matrix of names, `R` is a Boolean matrix whose rows contain the current effective access control vectors for the corresponding row in `Y`.


For further information, see the preceding section on setting the access control vector.

<h2 class="example">Example</h2>
```apl
      ⎕SVC 'X'
0 0 0 0
```



