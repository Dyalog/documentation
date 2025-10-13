
<!-- Hidden search keywords -->
<div style="display: none;">
  5176⌶
</div>






<h1 class="heading"><span class="name">List Loaded Files</span> <span class="command">R←5176⌶Y</span></h1>



The editor may be used to edit Dyalog script files (*.dyalog* files) and general text files and to save the contents in the workspace. Additionally `⎕FIX` can be used to fix scripts held in files. This I-Beam returns a list of all of the files which are associated with objects in the workspace, together with information about each file.


`Y` may be any value.


`R` is a vector of vectors, one element per associated file. Each element is a 5 element vector:


|Element|Contains |
|-------|---------|
|1      |File name|
|2      |Encoding |
|3      |Checksum |
|4      |Newline  |
|5      |Flags    |


Encoding, newline and flags are defined the same as for `⎕NGET`. See [File Encodings](../../system-functions/nget.md). Checksum is an 8-character hexadecimal value, see [GetBuildID](../../../../object-reference/methodorevents/getbuildid)  for more information.


<h2 class="example">Examples</h2>
```apl

      )CLEAR
clear ws
      ('' '' (8⍴' ') ⍬ 0)≡⊃5176⌶''
1
      dyalog←2 ⎕NQ '.' 'GetEnvironment' 'DYALOG' 
      aedit←'/SALT/spice/aedit.dyalog'
      ⎕FIX 'file:///',dyalog,aedit
#.arrayeditor

      1↓⊃5176⌶⍬      ⍝ Ignore filename
 UTF-8-BOM  18507aa6  13 10  0

			
```


