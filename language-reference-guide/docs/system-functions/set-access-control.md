---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVC SVC
</div>






<h1 class="heading"><span class="name">Set Access Control</span> <span class="command">R←X ⎕SVC Y</span></h1>



This system function sets access control on one or more shared variables.


`Y` is a character scalar, vector, or matrix containing names of shared variables.  Each name may optionally be paired with its surrogate.  If so, the surrogate must be separated from the name by at least one space.


`X` may be a 4-element Boolean vector which specifies the access control to be applied to all of the shared variables named in `Y`.  Alternatively, `X` may be a 4-column Boolean matrix whose rows specify the access control for the corresponding name in `Y`.  `X` may also be a scalar or a 1-element vector.  If so, it treated as if it were a 4-element vector with the same value in each element.



Each shared variable has a current access control vector which is a 4-element Boolean vector.  A 1 in each of the four positions has the following impact :


|-----|-------------------------------------------------------------------------------------------------------------|
|`[1]`|You cannot **set** a new value for the shared variable until after an intervening use or set by your partner.|
|`[2]`|Your partner cannot **set** a new value for the shared variable until after an intervening use or set by you.|
|`[3]`|You cannot **use** the value of the shared variable until after an intervening set by your partner.          |
|`[4]`|Your partner cannot **use** the value of the shared variable until after an intervening set by you.          |


The effect of `⎕SVC` is to reset the access control vectors for each of the shared variables named in `Y` by OR-ing the values most recently specified by your partner with the values in `X`.  This means that you cannot reset elements of the control vector which your partner has set to 1.


Note that the initial value of your partner's access control vector is normally 0 0 0 0.  However, if it is a non-APL client application that has established a hot DDE link, its access control vector is defined to be 1 0 0 1.  This inhibits either partner from setting the value of the shared variable twice, without an intervening use (or set) by the other.  This prevents loss of data which is deemed to be desirable from the nature of the link.  (An application that requests a hot link is assumed to require every value of the shared variable, and not to miss any).  Note that APL's way of inhibiting another application from setting the value twice (without an intervening use) is to delay the acknowledgement of the DDE message containing the second value until the variable has been used by the APL workspace.  An application that waits for an acknowledgement will therefore hang until this happens.  An application that does not wait will carry on obliviously.


The result `R` is a Boolean vector or matrix, corresponding to the structure of `X`, which contains the new access control settings.  If `Y` refers to a name which is not a shared variable, or if the surrogate name is mis-spelt, the corresponding value in `R` is `4⍴0`.

<h2 class="example">Examples</h2>
```apl
      1 0 0 1 ⎕SVC 'X'
1 0 0 1
 
      1 ⎕SVC 'X EXTNAME'
1 1 1 1
 
      (2 4⍴1 0 0 1 0 1 1 0) ⎕SVC ↑'ONE' 'TWO'
1 1 1 1
0 1 1 0
```


