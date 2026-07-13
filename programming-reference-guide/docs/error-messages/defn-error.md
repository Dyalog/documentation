




# defn error



This report is given when either:

- The system editor is invoked in order to edit a function that does not exist, or the named function is pendent or locked, or the given name is an object other than a function.
- The system editor is invoked to define a new function whose name is already active.
- The header line of a function is replaced or edited in definition mode with a line whose syntax is incompatible with that of a header line.  The original header line is re-displayed by the system editor with the cursor placed at the end of the line.  Back-spacing to the beginning of the line followed by line-feed restores the original header line.


<h2 class="example">Examples</h2>
```apl
      X←1
      ∇X
defn error
 
      ∇FOO[0⎕]
[0]   R←FOO
[0]   R←FOO:X
defn error
[0]   R←FOO:X
 
      ⎕LOCK'FOO'
      ∇FOO[⎕]
defn error
```


