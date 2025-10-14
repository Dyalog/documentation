
<!-- Hidden search keywords -->
<div style="display: none;">
  5177⌶
</div>






<h1 class="heading"><span class="name">List Loaded File Objects</span> <span class="command">R←5177⌶Y</span></h1>



The editor may be used to edit Dyalog script files (*.dyalog* files) and general text files and to save the contents in the workspace. Additionally `⎕FIX` can be used to fix scripts held in files. This I-Beam returns details about all of the objects in the workspace that are associated with such files.


`Y` must be an empty array.




`R` is a vector of 8-element vectors, one vector per object in the workspace that is associated with a file.


|Element|Contains                                                         |
|-------|-----------------------------------------------------------------|
|1      |Object name or ref (refs are returned for all types of namespace)|
|2      |Parent namespace                                                 |
|3      |Name class (see `⎕NC` )                                          |
|4      |File name                                                        |
|5      |Start line (first line in file, 0 origin, of the object)         |
|6      |Line count (number of lines in file occupied by the object)      |
|7      |File Checksum                                                    |
|8      |File modification time ( `⎕TS` format)                           |



If an object occupies a file in its entirety, both *Start line* and *Line count* will be 0.

<h2 class="example">Examples</h2>
```apl

      )CLEAR
clear ws
      ⊃5177⌶⍬
┌┬──────┬─┬┬─┬─┬────────┬─────────────┐
││[Null]│0││0│0│        │0 0 0 0 0 0 0│
└┴──────┴─┴┴─┴─┴────────┴─────────────┘

      dyalog←2 ⎕NQ '.' 'GetEnvironment' 'DYALOG' 
      aedit←'/SALT/spice/aedit.dyalog'
      ⊢⎕FIX 'file://',dyalog,aedit
#.arrayeditor

      1 1 1 0 1 1 1 1/↑5177⌶⍬ ⍝remove file names for brevity
┌─────────────┬─────────────┬─┬──┬──┬────────┬──────────────────┐
│Run          │#.arrayeditor│3│38│4 │008fe4ed│2018 5 11 8 5 10 0│
├─────────────┼─────────────┼─┼──┼──┼────────┼──────────────────┤
│Help         │#.arrayeditor│3│28│9 │008fe4ed│2018 5 11 8 5 10 0│
├─────────────┼─────────────┼─┼──┼──┼────────┼──────────────────┤
│List         │#.arrayeditor│3│22│5 │008fe4ed│2018 5 11 8 5 10 0│
├─────────────┼─────────────┼─┼──┼──┼────────┼──────────────────┤
│DESC         │#.arrayeditor│3│10│11│008fe4ed│2018 5 11 8 5 10 0│
├─────────────┼─────────────┼─┼──┼──┼────────┼──────────────────┤
│#.arrayeditor│#            │9│0 │0 │008fe4ed│2018 5 11 8 5 10 0│
└─────────────┴─────────────┴─┴──┴──┴────────┴──────────────────┘
	
```


