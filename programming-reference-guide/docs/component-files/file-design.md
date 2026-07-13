# File Design

Our personnel database could be termed a *record oriented* system. All the information relating to one person is easily obtained, and information relating to a new person is easily added, but if we wish to find the oldest person, we have to read ALL the records in the file.

It is sometimes more useful to have separate components, perhaps stored on separate files, that hold indexes of the data fields that you may wish to search on. For example, suppose we know that we always want to access our personnel database by name. Then it would make sense to hold an index component of names:
```apl
        ⍝ Extract name field from each data record
        'PERSONNEL' ⎕FSTIE 1
        NAMES←⊃∘⎕FREAD¨1,¨⍳¯1+2⊃⎕FSIZE 2
```
```apl
        ⍝ Create index file, and append NAMES
        'INDEX' ⎕FCREATE 2
        NAMES ⎕FAPPEND 2
```

Then if we want to find Pauline's data record:
```apl
        NAMES←⎕FREAD 2,1       ⍝ Read index of names
        CMP←NAMES⍳⊂'Pauline'   ⍝ Search for Pauline
        DATA←⎕FREAD 1,CMP      ⍝ Read relevant record
```

There are many different ways to structure data files; you must design a structure that is the most efficient for your application.
