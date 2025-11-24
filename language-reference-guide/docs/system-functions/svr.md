---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVR SVR
</div>






<h1 class="heading"><span class="name">Shared Variable Retract Offer</span> <span class="command">R←⎕SVR Y</span></h1>



This system function terminates communication via one or more shared variables, or aborts shared variable offers that have not yet been accepted.


`Y` is a character scalar, vector or matrix.  If it is a vector it contains a shared variable name and optionally its external name or surrogate separated from it by one of more blanks.  If `Y` is a scalar, it specifies a single 1-character name.  If `Y` is a matrix, each row of `Y` specifies a name and an optional external name as for the vector case.


The result `R` is vector whose length corresponds to the number of names specified by Y, indicating the level of sharing of each variable after retraction.


See [Shared Variable State](svs.md) for further information on the possible states of a shared variable.



