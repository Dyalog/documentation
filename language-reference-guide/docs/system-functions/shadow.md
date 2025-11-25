---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SHADOW SHADOW
</div>






<h1 class="heading"><span class="name">Shadow Name</span> <span class="command">{R}←⎕SHADOW Y</span></h1>



`Y` must be a simple character scalar, vector, or matrix, or a nested vector of character vectors or scalar characters, identifying one or more APL names.  For a simple vector `Y`, names are separated by one or more blanks.  For a matrix `Y`, each row is taken to be a single name.


Each valid name in `Y` is shadowed in the most recently invoked defined function or operator, as though it were included in the list of local names in the function or operator header.  The class of the name becomes 0 (undefined).  The name ceases to be shadowed when execution of the shadowing function or operator is completed.  Shadow has no effect when the state indicator is empty.



The shy result `R` is a Boolean vector of 1s with the same length as the number of names in `Y`.


If a name is ill-formed, or if it is the name of a system constant or system function, `DOMAIN ERROR` is reported.


If the name of a top-level GUI object is shadowed, it is made inactive.

<h2 class="example">Example</h2>
```apl
      ⎕VR'RUN'
     ∇ NAME RUN FN
[1]   ⍝ Runs function named <NAME> defined
[2]   ⍝ from representation form <FN>
[3]    ⎕SHADOW NAME
[4]    ⍎⎕FX FN
     ∇
 
      0 ⎕STOP 'RUN' ⍝ stop prior RUN exiting
 
      'FOO' RUN 'R←FOO' 'R←10'
10
 
RUN[0]
 
      )SINL
#.RUN[0]*       FOO     FN      NAME
 
      →⎕LC
 
      FOO
VALUE ERROR
      FOO
      ^
```


