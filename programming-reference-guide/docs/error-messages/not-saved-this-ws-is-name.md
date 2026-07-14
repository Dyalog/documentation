

# not saved this ws is name

This report is given in the following situations:

- When the system command `)SAVE` is used without a name, and the workspace is not named.  In this case the system reports `not` `saved this ws is CLEAR WS`.
- When the system command `)SAVE` is used with a name, and that name is not the current name of the workspace, but is the name of an existing file.

In neither case is the workspace renamed.

<h2 class="example">Examples</h2>

```apl
      )CLEAR
      )SAVE
not saved this ws is CLEAR WS
 
      )WSID JOHND
      )SAVE
      )WSID ANDYS
      )SAVE JOHND
not saved this ws is ANDYS
```
