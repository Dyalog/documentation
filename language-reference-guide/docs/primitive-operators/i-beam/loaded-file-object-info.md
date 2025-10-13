
<!-- Hidden search keywords -->
<div style="display: none;">
  5179⌶
</div>






<h1 class="heading"><span class="name">Loaded File Object Info</span> <span class="command">R←5179⌶Y</span></h1>



The editor may be used to edit Dyalog script files (*.dyalog* files) and general text files and to save the contents in the workspace. Additionally `⎕FIX` can be used to fix scripts held in files. This I-Beam returns details about an object in the workspace specified by `Y` that is associated with such a file.


`Y` is a character vector that specifies the name of a workspace object or a ref to an object.


`R` is an 8-element vector containing the following information pertaining to the object and


|Element|Contains                                                   |
|-------|-----------------------------------------------------------|
|1      |Object name or ref ( `Y` )                                 |
|2      |Parent namespace                                           |
|3      |Name class (see `⎕NC` )                                    |
|4      |File name                                                  |
|5      |Start line (first line in file, 0 origin, of the object)   |
|6      |Line count (number of lines in file occupied by the object)|
|7      |File Checksum                                              |
|8      |File modification time ( `⎕TS` format)                     |


If an object occupies a file in its entirety, both *Start line* and *Line count* are 0.


<h2 class="example">Examples</h2>
```apl

      dyalog←2 ⎕NQ '.' 'GetEnvironment' 'DYALOG' 
      aedit←'/SALT/spice/aedit.dyalog'
      ⊢⎕FIX 'file://',dyalog,aedit
#.arrayeditor
      1 1 1 0 1 1 1 1/ 5179⌶'arrayeditor'
┌─────────────┬─┬─┬─┬─┬────────┬───────────────────┐
│#.arrayeditor│#│9│0│0│008fe4ed│2018 5 11 8 56 10 0│
└─────────────┴─┴─┴─┴─┴────────┴───────────────────┘
      1 1 1 0 1 1 1 1/ 5179⌶'arrayeditor.List'
┌────┬─────────────┬─┬──┬─┬────────┬───────────────────┐
│List│#.arrayeditor│3│22│5│008fe4ed│2018 5 11 8 56 10 0│
└────┴─────────────┴─┴──┴─┴────────┴───────────────────┘
      5179⌶'xyz' ⍝ unused name
┌┬────────┬─┬┬─┬─┬────────┬─────────────┐
││ [Null] │0││0│0│        │0 0 0 0 0 0 0│
└┴────────┴─┴┴─┴─┴────────┴─────────────┘
	
```


