

# name is not a ws

This report is given when the name specified as the parameter of the system commands `)LOAD`, `)COPY` or `)PCOPY` is a reference to an existing file or directory that is not identified as a workspace.

This will also occur if an attempt is made to `)LOAD` a workspace that was `)SAVE`’d using a later version of Dyalog APL.

<h2 class="example">Example</h2>
```apl
      )LOAD EXT\ARRAY
EXT\ARRAY is not a ws
```
