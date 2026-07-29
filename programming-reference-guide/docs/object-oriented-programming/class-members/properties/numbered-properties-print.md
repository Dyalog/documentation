---
search:
  exclude: true
---

# Numbered Properties

A Numbered Property behaves like an array (conceptually a vector) which is only ever *partially* accessed and set (one
element at a time) via indices.

To implement a Numbered Property, you **must** specify a PropertyShape function and either or both a PropertyGet and
PropertySet function.

When an expression references or makes an assignment to a Numbered Property, APL first calls its PropertyShape function
which returns the dimensions of the Property. Note that the shape of the result of this function determines the *rank*
of the Property.

If the expression uses indexing, APL checks that the index or indices are within the bounds of these dimensions, and
then calls the PropertyGet or PropertySet function. If the expression specifies a single index, APL calls the
PropertyGet or PropertySet function once. If the expression specifies multiple indices, APL calls the function
successively.

If the expression references or assigns the entire Property (without indexing) APL generates a set of indices for every
element of the Property and calls the PropertyGet or PropertySet function successively for every element in the
Property.

Note that APL generates a `RANK ERROR` if an index contains the wrong number of elements or an `INDEX ERROR` if an index
is out of bounds.

When APL calls a monadic PropertyGet or PropertySet function, it supplies an argument of type PropertyArguments.

## Example {: .example }

The ComponentFile Class (see [Section](./component-file-class-example.md)) specifies a Numbered Property named `Component`
which represents the contents of a specified component on the file.

```apl
    :Property Numbered Component
    :Access Public Instance
        ∇ r←shape
          r←¯1+2⊃⎕FSIZE tie
        ∇
        ∇ r←get arg
          r←⎕FREAD tie arg.Indexers
        ∇
        ∇ set arg
          arg.NewValue ⎕FREPLACE tie,arg.Indexers
        ∇
    :EndProperty
```

```apl

      F1←⎕NEW ComponentFile 'test1'
      
      F1.Append¨(⍳5)×⊂⍳4
1 2 3 4 5
      
      F1.Count
5
      
      F1.Component[4]
 4 8 12 16 
      
      4⊃F1.Component
4 8 12 16
      
      (⊂4 3)⌷F1.Component
 4 8 12 16  3 6 9 12 
```

Referencing a Numbered Property in its entirety causes APL to call the `get` function successively for every element.

```apl
      F1.Component
 1 2 3 4  2 4 6 8  3 6 9 12  4 8 12 16  5 10 15 20
      
      ((⊂4 3)⌷F1.Component)←'Hello' 'World'
      
      F1.Component[3]
 World
```

Attempting to access a Numbered Property with inappropriate indices generates an error:

```apl
      F1.Component[6]
INDEX ERROR
      F1.Component[6]
     ^
      F1.Component[1;2]
RANK ERROR
      F1.Component[1;2]
     ^
```
