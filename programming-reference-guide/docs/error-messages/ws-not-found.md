

# ws not found

This report is given when a workspace named by the system commands `)LOAD`, `)COPY` or `)PCOPY` does not exist as a file, or when the user does not have read access authorisation for the file.

<h2 class="example">Examples</h2>
```apl
      )LOAD NOWS
ws not found
 
      )COPY NOWS A FOO X
ws not found
```
