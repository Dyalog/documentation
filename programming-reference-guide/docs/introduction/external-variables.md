<h1 class="heading"><span class="name">External Variables</span></h1>

An external variable is a variable whose contents (value) reside not in the workspace, but in a file.  An external variable is associated with a file by the system function `⎕XT`.  If at the time of association the file exists, the external variable assumes its value from the contents of the file.  If the file does not exist, the external variable is defined but a `VALUE ERROR` occurs if it is referenced before assignment.  Assignment of an array to the external variable or to an indexed element of the external variable has the effect of updating the file.  The value of the external variable or the value of indexed elements of the external variable is made available in the workspace when the external variable occurs in an expression.  No special restrictions are placed on the usage of external variables.

Normally, the files associated with external variables remain permanent in that they survive the APL session or the erasing of the external variable from the workspace. External variables may be accessed concurrently by several users, or by different nodes on a network, provided that the appropriate file access controls are established.  Multi-user access to an external variable may be controlled with the system function `⎕FHOLD` between co-operating tasks.

Refer to the sections describing the system functions `⎕XT` and `⎕FHOLD` in *Chapter 6* for further details.

<h2 class="example">Examples</h2>
```apl
      'ARRAY' ⎕XT 'V'
 
      V←⍳10
      V[2] + 5
7
 
      ⎕EX'V'
 
      'ARRAY' ⎕XT 'F'
      F
1 2 3 4 5 6 7 8 9 10
```

!!! Info "Information"
    Support for external variables has been deprecated, and is scheduled for removal in a future release. For information on how to identify calls to external variables in your existing codebase, see the [Release Notes](../../release-notes/announcements/deprecated-functionality.md).
