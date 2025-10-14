
<!-- Hidden search keywords -->
<div style="display: none;">
  180⌶
</div>






<h1 class="heading"><span class="name">Canonical Representation</span> <span class="command">R←180⌶Y</span></h1>



This function is the same as the system function `⎕CR` except that it can be used to obtain the canonical representation of methods in classes. `180⌶` is used by `]PROFILE`.

<h2 class="example">Example</h2>
```apl

      )LOAD ComponentFile
C:\Program Files\Dyalog\Dyalog APL-64 15.0 Unicode\...

      180⌶'ComponentFile.Close'
 Close                          
 :Implements Destructor         
 :If tie∊⎕FNUMS                 
     :If temp ⋄ Name ⎕FERASE tie
     :Else ⋄ ⎕FUNTIE tie        
     :EndIf                     
 :EndIf                         
  
```



