---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AI AI
</div>






<h1 class="heading"><span class="name">Account Information</span> <span class="command">R←⎕AI</span></h1>



This is a simple integer vector, whose four elements are:


|--------|-------------------------------------------------|
|`⎕AI[1]`|user identification. [^1]                        |
|`⎕AI[2]`|compute time for the APL session in milliseconds.|
|`⎕AI[3]`|connect time for the APL session in milliseconds.|
|`⎕AI[4]`|keying time for the APL session in milliseconds. |


Elements beyond 4 are not defined but reserved.

<h2 class="example">Example</h2>
```apl

     ⎕AI
52 7396 2924216 2814831
```





[^1]: Under Windows, this is the aplnid (network ID from configuration dialog box). Under UNIX and Linux this is the effective UID of the account whereas ⎕AN returns the real name.