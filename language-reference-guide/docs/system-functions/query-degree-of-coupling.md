---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVO SVO
</div>






<h1 class="heading"><span class="name">Query Degree of Coupling</span> <span class="command">R←⎕SVO Y</span></h1>



This system function returns the current degree of coupling for one or more shared variables.


`Y` is a character scalar, vector or matrix.  If it is a vector it contains a shared variable name and optionally its external name or surrogate separated from it by one of more blanks.


If `Y` is a scalar, it specifies a single 1-character name.  If `Y` is a matrix, each row of `Y` specifies a name and an optional external name as for the vector case.


If `Y` specifies a single name, the result `R` is a 1-element vector whose value 0, 1 or 2 indicates its current degree of coupling.  If `Y` specifies more than one name, `R` is a vector whose elements indicate the current degree of coupling of the variable specified by the corresponding row in `Y`.  A value of 2 indicates that the variable is fully coupled (via a warm or hot DDE link) with a shared variable in another APL workspace, or with a DDE item in another application.  A value of 1 indicates that you have offered the variable but there is no such connection, or that the second application rejected a warm link.  In this case, a transfer of data may have taken place (via a cold link) but the connection is no longer open.  A value of 0 indicates that the name is not a shared variable.

<h2 class="example">Examples</h2>
```apl
      ⎕SVO 'X'
2
      ⎕SVO ↑'X SALES' 'Y' 'JUNK'
2 1 0
```



