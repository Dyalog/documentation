# Simple Instance Properties

A Simple Instance Property is one whose value is accessed (by APL) in its entirety and re-assigned (by APL) in its entirety. The following examples are taken from the [ComponentFile Class](component-file-class-example.md){: .noprint }.

The Simple Property `Count` returns the number of components on a file.
```apl
    :Property Count
    :Access Public Instance
        ∇ r←get
          r←¯1+2⊃⎕FSIZE tie
        ∇
    :EndProperty ⍝ Count
 
      F1←⎕NEW ComponentFile 'test1'
      F1.Append'Hello World'
1
      F1.Count
1
      F1.Append 42 
2
      F1.Count
2
```

Because there is no `set` function defined, the Property is read-only and attempting to change it causes `SYNTAX ERROR`.
```apl
      F1.Count←99
SYNTAX ERROR
      F1.Count←99
     ^
```

The `Access` Property has both `get` and `set` functions which are used, in this simple example, to get and set the component file access matrix.
```apl
    :Property Access
    :Access Public Instance
        ∇ r←get
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
```

Note that the `set` function **must** be monadic. Its argument, supplied by APL, will be an Instance of `PropertyArguments`. This is an internal Class whose `NewValue` field contains the value that was assigned to the Property.

Note too that the set function does not have to accept the new value that has been assigned. The function may validate the value reject or accept it (as in this example), or perform whatever processing is appropriate.
```apl
      F1←⎕NEW ComponentFile 'test1'
      ⍴F1.Access
0 3
        F1.Access←3 3⍴28 2105 16385 0 2073 16385 31 ¯1 0
      F1.Access
28 2105 16385
 0 2073 16385
31   ¯1     0
      
      F1.Access←'junk'
bad arg
      F1.Access←'junk'
     ^
      
      F1.Access←1 2⍴10
bad arg
      F1.Access←1 2⍴10
     ^
```
