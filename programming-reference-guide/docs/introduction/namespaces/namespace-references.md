# Namespace References

A namespace reference, or ref for short, is a unique data type that is distinct from and in addition to number and character.

Any expression may result in a ref, but the simplest one is the namespace itself:
```apl
      )NS NS1          ⍝ Make a namespace called NS1
      NS1.A←1          ⍝ and populate it with variables A
      NS1.B←2 3⍴⍳6     ⍝ and B
 
      NS1              ⍝ expression results in a ref
#.NS1
```

You may assign a ref; for example:
```apl
      X←NS1
      X     
#.NS1
```

In this case, the display of `X` informs you that `X` refers to the named namespace `#.NS1`.

You may also supply a ref as an argument to a defined function or a dfn:
```apl
     ∇ FOO ARG
[1]    ARG
     ∇
```
```apl
      FOO NS1
#.NS1
```

The name class of a ref is 9.
```apl
      ⎕NC 'X'
9
```

You may use a ref to a namespace anywhere that you would use the namespace itself. For example:
```apl
      X.A
1
      X.B
1 2 3
4 5 6
```

Notice that refs are references to namespaces, so that if you make a copy, it is the reference that is copied, not the namespace itself. This is sometimes referred to as a shallow as opposed to a deep copy. It means that if you change a ref, you actually change the namespace that it refers to.
```apl
      X.A+←1
      X.A
2
      NS1.A
2
```

Similarly, a ref passed to a defined function is call-by-reference, so that modifications to the content or properties of the argument namespace using the passed reference persist after the function exits. For example:
```apl
     ∇ FOO nsref
[1]    nsref.B+←nsref.A
     ∇
 
      FOO NS1
      NS1.B
3 4 5
6 7 8
      FOO X
      NS1.B
5 6  7
8 9 10
```

Notice that the expression to the right of a dot may be arbitrarily complex and will be executed within the namespace or ref to the left of the dot.
```apl
      X.(C←A×B)
      X.C
10 12 14
16 18 20
      NS1.C
10 12 14
16 18 20
```
