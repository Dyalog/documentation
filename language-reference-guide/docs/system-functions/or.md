---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕OR OR
</div>






<h1 class="heading"><span class="name">Object Representation</span> <span class="command">R←⎕OR Y</span></h1>



`⎕OR` converts a defined function, defined operator or namespace to a special form, described as its *object representation*, that may be assigned to a variable and/or stored on a component file[^1]. Classes and Instances are however outside the domain of `⎕OR`.


Taking the `⎕OR` of a defined function or operator is an extremely fast operation as it simply changes the type information in the object's header, leaving its internal structure unaltered.  Converting the object representation back to an executable function or operator using `⎕FX` is also very fast.


However, the saved results of `⎕OR` which were produced on a different hardware platform or using an older version of Dyalog APL may require a significant amount of processing when re-constituted using `⎕FX`.  For optimum performance, it is strongly recommended that you save `⎕OR`s using the same version of Dyalog APL and on the same hardware platform that you will use to `⎕FX` them.


`⎕OR` may also be used to convert a namespace (either a plain namespace or a named GUI object created by `⎕WC`) into a form that can be stored in a variable or on a component file.  The namespace may be reconstructed using `⎕NS` or `⎕WC` with its original name or with a new one.  `⎕OR` may therefore be used to *clone* a namespace or GUI object.



`Y` must be a simple character scalar or vector which contains the name of an APL object.


If `Y` is the name of a variable, the result `R` is its value.  In this case, `R←⎕OR Y` is identical to `R←⍎Y`.


Otherwise, `R` is a special form of the name `Y`, re-classified as a variable. The rank of `R` is 0 (`R` is scalar), and the depth of `R` is 1.  These unique characteristics distinguish the result of `⎕OR` from any other object.  The Type of `R` (`∊R`) is itself.  Note that although `R` is scalar, it may not be index assigned to an element of an array unless it is enclosed.


If `Y` is the name of a function or operator, `R` is in the domain of the monadic functions Same (`⊣` and `⊢`), Depth (`≡`), Disclose (`⊃`), Enclose (`⊂`), Rotate (`⌽`), Transpose (`⍉`), Index (`⌷`), Indexing (`[]`), Format (`⍕`), Identity (`+`), Shape (`⍴`), Type (`∊`) and Unique (`∪`), of the dyadic functions Left (`⊣`), Right (`⊢`), Without (`~`), Index Of (`⍳`), Intersection (`∩`), Match (`≡`), Membership (`∊`), Not Match (`≠`) and Union (`∪`), and of the monadic system functions Canonical Representation (`⎕CR`), Cross-Reference (`⎕REFS`), Fix (`⎕FX`), Format (`⎕FMT`), Nested Representation (`⎕NR`) and Vector Representation (`⎕VR`).


Note that a `⎕OR` object can be transmitted through an 'APL-style' TCP socket. This technique may be used to transfer objects including namespaces between APL sessions.


The object representation forms of namespaces produced by `⎕OR` may not be used as arguments to any primitive functions.  The only operations permitted for such objects (or arrays containing such objects) are `⎕EX`, `⎕FAPPEND`, `⎕FREPLACE`, `⎕NS`, and `⎕WC`.

<h2 class="example">Example</h2>
```apl
      F←⎕OR ⎕FX'R←FOO' 'R←10'
 
      ⍴F
 
      ⍴⍴F
0
      ≡F
1
      F≡∊F
1
```


The display of the `⎕OR` form of a function or operator is a listing of the function or operator.  If the `⎕OR` form of a function or operator has been enclosed, then the result will display as the  name preceded by the symbol `∇`.  It is permitted to apply `⎕OR` to a locked function or operator.  In this instance the result will display as for the enclosed form.

<h2 class="example">Examples</h2>
```apl
       F
      ∇ R←FOO
[1]     R←10
      ∇
 
      ⊂F
 ∇FOO
 
      ⎕LOCK'FOO'
 
      ⎕OR'FOO'
∇FOO
```
```apl
      A←⍳5
 
      A[3]←⊂F
 
      A
1 2  ∇FOO  4 5
```


For the `⎕OR` forms of two functions or operators to be considered identical, their unlocked display forms must be the same, they must either both be locked or unlocked, and any monitors, trace and stop vectors must be the same.

<h2 class="example">Example</h2>
```apl
      F←⎕OR ⎕FX 'R←A PLUS B' 'R←A+B'
 
      F≡⎕OR 'PLUS'
1
 
      1 ⎕STOP 'PLUS'
 
      F≡⎕OR 'PLUS'
0
```


## Namespace Examples


The following example sets up a namespace called `UTILS`, copies into it the contents of the `UTIL` workspace, then writes it to a component file:

```apl
      )CLEAR
clear ws
      )NS UTILS
#.UTILS
      )CS UTILS
#.UTILS
      )COPY UTIL
C:\WDYALOG\WS\UTIL saved Fri Mar 17 12:48:06 1995
      )CS
#
      'ORTEST' ⎕FCREATE 1
      (⎕OR'UTILS')⎕FAPPEND 1
```


The namespace can be restored with `⎕NS`, using either the original name or a new one:
```apl
      )CLEAR
clear ws
      'UTILS' ⎕NS ⎕FREAD 1 1
#.UTILS
      )CLEAR
clear ws
      'NEWUTILS' ⎕NS ⎕FREAD 1 1
#.NEWUTILS
```


This example illustrates how `⎕OR` can be used to clone a GUI object; in this case a Group containing some Button objects.  Note that `⎕WC` will accept **only** a `⎕OR` object as its argument (or preceded by the "Type" keyword).  You may not specify any other properties in the same `⎕WC` statement, but you must instead use `⎕WS` to reset them afterwards.
```apl
    'F'⎕WC'Form'
    'F.G1' ⎕WC 'Group' '&One' (10 10)(80 30)
    'F.G1.B2'⎕WC'Button' '&Blue' (40 10)('Style' 'Radio')
    'F.G1.B3'⎕WC'Button' '&Green' (60 10)('Style' 'Radio')
    'F.G1.B1'⎕WC'Button' '&Red' (20 10)('Style' 'Radio')
    'F.G2' ⎕WC ⎕OR 'F.G1'
    'F.G2' ⎕WS ('Caption' 'Two')('Posn' 10 60)
```


Note too that `⎕WC` and `⎕NS` may be used interchangeably to rebuild *pure* namespaces or GUI namespaces from a `⎕OR` object.  You may therefore use `⎕NS` to rebuild a Form or use `⎕WC` to rebuild a pure namespace that has no GUI components.




[^1]: ⎕OR and GUI objects stored in workspaces or in component files are not portable between 32-bit and 64-bit versions of Dyalog nor between different implementations (platforms) and are not backwards compatible