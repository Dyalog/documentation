
<!-- Hidden search keywords -->
<div style="display: none;">
  5178⌶
</div>






<h1 class="heading"><span class="name">Remove Loaded File Object Info</span> <span class="command">R←5178⌶Y</span></h1>



The editor may be used to edit Dyalog script files (*.dyalog* files) and general text files and to save the contents in the workspace. Additionally `⎕FIX` can be used to fix scripts held in files. This I-Beam removes the information held about an object in the workspace specified by `Y` that is associated with such a file.


`Y` is a character vector that specifies the name of a workspace object or a ref to an object.


`R` is Boolean. 1 means that the information was removed; 0 that it wasn't.


Note that the workspace object itself remains in the workspace; just the information about its associated file is removed.

<h2 class="example">Examples</h2>
```apl

      dyalog←2 ⎕NQ '.' 'GetEnvironment' 'DYALOG' 
      aedit←'/SALT/spice/aedit.dyalog'
      ⊢⎕FIX 'file://',dyalog,aedit
#.arrayeditor
      5178⌶'arrayeditor'
1
      5178⌶'xyz' ⍝ unused name
0

```



