<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WN WN
</div>






<h1 class="heading"><span class="name">Window Child Names</span> <span class="command">R←{X}⎕WN Y</span></h1>



**Windows only.**


This system function reports the GUI objects whose parent is `Y`.


If `Y` is a name (that is, is a character vector) then the result `R` is a vector of character vectors containing the names of the named direct GUI children of `Y`.


If `Y` is a reference  then the result `R` is a vector of references to  the direct GUI children of `Y`, named or otherwise.


The optional left argument `X` is a character vector which specifies the `Type` of GUI object to be reported; if `X` is not specified, no such filtering is performed.



Names of objects further down the tree are not returned, but can be obtained by recursive use of `⎕WN`.


If `Y` refers to a namespace with no GUI element, a `VALUE ERROR` is reported.


Note that `⎕WN` reports **only** those child objects visible from the current thread.


GUI objects are named **relative** to the current namespace.  The following examples are equivalent:
```apl
      ⎕WN 'F1.B1'
      F1.⎕WN 'B1'
      F1.B1.⎕WN ''    
```

<h2 class="example">Example</h2>
```apl
      f←⎕NEW⊂'Form'
      f.n←⎕NS''                  ⍝ A non-GUI object       
      f.l←f.⎕NEW⊂'Label'         ⍝ A reference to a Label
      'f.b1'⎕WC'Button'          ⍝ A named Button
      f.(b2←⎕NEW ⊂'Button')      ⍝ A reference to a Button
      ⎕WN 'f'
 [Form].b1
      ⎕WN f
 #.[Form].[Label]  #.[Form].b1  #.[Form].[Button]
      'Button' ⎕WN f
 #.[Form].b1  #.[Form].[Button]
```


