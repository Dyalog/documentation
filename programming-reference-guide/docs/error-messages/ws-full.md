

# <span>WS FULL</span> `1`

This report is given when there is insufficient workspace in which to perform an operation.  Workspace available is identified by the system constant `⎕WA`.

The maximum workspace size allowed is defined by the environment variable `MAXWS`. See **maxws parameter** for details.

<h2 class="example">Example</h2>
```apl

      ⎕WA⍴1.2
WS FULL
      ⎕WA⍴1.2
      ^
```
