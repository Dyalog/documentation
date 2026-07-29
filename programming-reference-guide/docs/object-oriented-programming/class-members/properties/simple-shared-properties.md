# Simple Shared Properties

The [ComponentFile Class](component-file-class-example.md){: .noprint }  specifies a Simple Shared Property named `Files` which returns the names of all the Component Files in the current directory.

The previous examples have illustrated the use of Instance Properties. It is also possible to define *Shared* properties.

A Shared property may be used to handle information that is relevant to the Class as a whole, and which is not specific to any a particular Instance.
```apl

    :Property Files
    :Access Public Shared
        ∇ r←get
          r←⎕FLIB''
        ∇
    :EndProperty
```

Note that `⎕FLIB` (invoked by the `Files` `get` function) does not report the names of *tied* files.
```apl

      F1←⎕NEW ComponentFile 'test1'
      ⎕EX'F1'      
      F2←⎕NEW ComponentFile 'test2'
      F2.Files ⍝ NB ⎕FLIB does not report tied files
test1
      ⎕EX'F2'
```

Note that a Shared Property may be accessed from the Class itself. It is not necessary to create an Instance first.
```apl
      ComponentFile.Files
test1
test2
```
