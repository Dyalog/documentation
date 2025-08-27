<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XT XT
</div>






<h1 class="heading"><span class="name">Set External Variable</span> <span class="command">{R}←X ⎕XT Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be a variable name.  `X` must be a simple character scalar or vector which is taken to be a file reference.  The name given by `Y` is identified as an EXTERNAL VARIABLE associated with an EXTERNAL ARRAY whose value may be stored in file identified by `X`. The shy result `R` has the same value as `X`.


If `Y` is the name of a defined function or operator, a label or a namespace in the active workspace, a `DOMAIN ERROR` is reported.


Attempts to assign namespace references or the `⎕OR` of namespaces to an external array will result in a `DOMAIN ERROR`.


<h2 class="example">Example</h2>
```apl
      'EXT\ARRAY' ⎕XT 'V'
```


If the file reference does not exist, the external variable has no value until a value is assigned:
```apl
      V
VALUE ERROR
      V
      ^
```


A value assigned to an external variable is stored in file space, not within the workspace:
```apl
      ⎕WA
2261186
 
      V←⍳100000
 
      ⎕WA
2261186
```


There are no specific restrictions placed on the use of external variables.  They must conform to the normal requirements when used as arguments of functions or as operands of operators.  The essential difference between a variable and an external variable is that an external variable requires only temporary workspace for an operation to accommodate (usually) a part of its value.

<h2 class="example">Examples</h2>
```apl
      V←⍳5
      +/V
15
 
      V[3]←⊂'ABC'
 
      V
1 2  ABC  4 5
 
      ⍴¨V
     3
```


Assignment allows the structure or the value of an external variable to be changed without fully defining the external array in the workspace.

<h2 class="example">Examples</h2>
```apl
      V,←⊂2 4⍴⍳8
 
      ⍴V
6
 
      V[6]
1 2 3 4
5 6 7 8
 
      V[1 2 4 5 6]×←10
 
      V
10 20  ABC  40 50  10 20 30 40
                   50 60 70 80
```


An external array is (usually) preserved in file space when the name of the external variable is disassociated from the file.  It may be re-associated with any valid variable name.

<h2 class="example">Example</h2>
```apl
      ⎕EX'V'
 
      'EXT\ARRAY'⎕XT'F'
 
      F
10 20  ABC  40 50  10 20 30 40
                   50 60 70 80
```


In UNIX versions, if `X` is an empty vector, the external array is associated with a temporary file which is erased when the array is disassociated.

<h2 class="example">Example</h2>
```apl
      ''⎕XT'TEMP'
 
      TEMP←⍳10
 
      +/TEMP×TEMP
385
 
      ⎕EX'TEMP'
```


An external array may be erased using the native file function: `⎕NERASE`.


In a multi-user environment (UNIX or a Windows LAN) a new file associated with an external array is created with access permission for owner read/write.  An existing file is opened for exclusive use (by the owner) if the permissions remain at this level.  If the access permissions allow any other users to read and write to the file, the file is opened for shared use.  In UNIX versions, access permissions may be modified using the appropriate Operating System command, or in Windows using the supplied function `XVAR` from the UTIL workspace.

!!! Info "Information"
    Support for external variables has been deprecated, and they are scheduled for removal in a future release. For information on how to identify uses of external variables in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).
