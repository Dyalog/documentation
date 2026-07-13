# ComponentFile Class

```apl
:Class ComponentFile
    :Field Private Instance tie
    
    ∇ Open filename
      :Implements Constructor
      :Access Public Instance
      :Trap 0
          tie←filename ⎕FTIE 0
      :Else
          tie←filename ⎕FCREATE 0
      :EndTrap
      ⎕DF filename,'(Component File)'
    ∇
    
    ∇ Close
      :Access Public Instance
      ⎕FUNTIE tie
    ∇
    
    ∇ r←Append data
      :Access Public Instance
      r←data ⎕FAPPEND tie
    ∇
    
    ∇ Replace(comp data)
      :Access Public Instance
      data ⎕FREPLACE tie,comp
    ∇
    
    :Property Count
    :Access Public Instance
        ∇ r←get
          r←¯1+2⊃⎕FSIZE tie
        ∇
    :EndProperty ⍝ Count
        
```

```apl
:Property Access
    :Access Public Instance
        ∇ r←get arg
          r←⎕FRDAC tie
        ∇
        ∇ set am;mat;OK
          mat←am.NewValue
          :Trap 0
              OK←(2=⍴⍴mat)^(3=2⊃⍴mat)^^/,mat=⌊mat
          :Else
              OK←0
          :EndTrap
          'bad arg'⎕SIGNAL(~OK)/11
          mat ⎕FSTAC tie
        ∇
    :EndProperty ⍝ Access
    
    :Property Files
    :Access Public Shared
        ∇ r←get
          r←⎕FLIB''
        ∇
    :EndProperty
    
    :Property Numbered Default Component
    :Access Public Instance
        ∇ r←shape args
          r←¯1+2⊃⎕FSIZE tie
        ∇
        ∇ r←get arg
          r←⊂⎕FREAD tie,arg.Indexers
        ∇
        ∇ set arg
          (⊃arg.NewValue)⎕FREPLACE tie,arg.Indexers
        ∇
    :EndProperty
    
    ∇ Delete file;tie
      :Access Public Shared
      tie←file ⎕FTIE 0
      file ⎕FERASE tie
    ∇
:EndClass ⍝ Class ComponentFile
```
