---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVS SVS
</div>






<h1 class="heading"><span class="name">Shared Variable State</span> <span class="command">R←⎕SVS Y</span></h1>



This system function returns the current state of one or more shared variables.


`Y` is a character scalar, vector or matrix.  If it is a vector it contains a shared variable name and optionally its external name or surrogate separated from it by one of more blanks.  If `Y` is a scalar, it specifies a single 1-character name.  If `Y` is a matrix, each row of `Y` specifies a name and an optional external name as for the vector case.


If `Y` specifies a single name, the result `R` is a 4-element vector indicating its current state.  If `Y` specifies more than one name, `R` is a matrix whose rows indicate the current state of the variable specified by the corresponding row in `Y`.



There are four possible shared variable states:


|---------|-----------------------|
|`0011`|means that you and your partner are both aware of the current value, and neither has since reset it. This is also the initial value of the state when the link is first established.|
|`1010`|means that you have reset the shared variable and your partner has not yet used it. This state can only occur if both partners are APL workspaces.                                  |
|`0101`|means that your partner has reset the shared variable but that you have not yet used it.     |
|`0000`|the name is not that of a shared variable   |

<h2 class="example">Examples</h2>
```apl
      ⎕SVS 'X'
0 1 0 1
 
      ⎕SVS ↑'X SALES' 'Y' 'JUNK'
0 0 1 1
1 0 1 0
0 0 0 0
```


