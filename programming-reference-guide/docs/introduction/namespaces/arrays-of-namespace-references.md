<h1 class="heading"><span class="name">Arrays of Namespace References</span></h1>

You can construct arrays of refs using strand notation, array notation, catenate (`,`), reshape (`⍴`) and other structural primitives, as well as certain system functions.
```apl
      EMP←JOHN PAUL
      ⍴EMP
2
      EMP
 #.[Namespace]  #.[Namespace]
```

Like any other array, an array of refs has name class 2:
```apl
      ⎕NC 'EMP'
2
```

Expressions such as indexing and pick return refs that may in turn be used as follows:
```apl
      EMP[1].FirstName
John
      (2⊃EMP).Age
44
```

The each (`¨`) operator may be used to apply a function to an array of refs:
```apl
      SHOW¨EMP
 John Smith is 50  Paul Brown is 44
```

An *array* of namespace references (refs) to the left of a '`.`' is expanded according to the following rule, where `x` and `y` are refs, and `exp` is an arbitrary expression:
```apl
      (x y).exp → (x.exp)(y.exp)
```

If `exp` evaluates to a function, the items of its argument array(s) are *distributed* to each referenced function. In the dyadic case, there is a 3-way distribution among: left argument, referenced functions and right argument.

Monadic function `f`:
```apl
      (x y).f d e → (x.f d)(y.f e)
```

Dyadic function `g`:
```apl
      a b (x y).g  d e → (a x.g d)(b y.g e)
```

An array of refs to the left of an assignment arrow is expanded thus:
```apl
      (x y).a←c d → (x.a←c)(y.a←d)
```

Note that the array of refs can be of any rank. In the limiting case of a simple scalar array, the array construct: `refs.exp` is identical to the scalar construct: `ref.exp`.

Note that the expression to the right of the '`.`' pervades a nested array of refs to its left:
```apl
      ((u v)(x y)).exp → ((u.exp)(v.exp))((x.exp)(y.exp))
```

Note also that with successive expansions `(u v).(x y z).` ..., the final number of "leaf" terms is the product of the number of refs at each level.

<h2 class="example">Examples</h2>
```apl
      (JOHN PAUL)←()()
      JOHN.Children←()()
      ⍴JOHN.Children
2
      JOHN.Children[1].FirstName←'Andy'
      JOHN.Children[1].Age←23
      
      JOHN.Children[2].FirstName←'Katherine'
      JOHN.Children[2].Age←19               
 
      PAUL.Children←()()
      PAUL.Children[1].(FirstName Age←'Tom' 25)
      PAUL.Children[2].(FirstName Age←'Jamie' 22)

      EMP←JOHN PAUL
      ⍴EMP
2
      (⊃EMP).Children.(FirstName Age)
  Andy  23   Katherine  19
 
      ]display (2⊃EMP).Children.(FirstName Age)
┌→────────────────────────────┐
│ ┌→─────────┐ ┌→───────────┐ │
│ │ ┌→──┐    │ │ ┌→────┐    │ │
│ │ │Tom│ 25 │ │ │Jamie│ 22 │ │
│ │ └───┘    │ │ └─────┘    │ │
│ └∊─────────┘ └∊───────────┘ │
└∊────────────────────────────┘
 
      EMP.Children ⍝ Is an array of refs
  #.[Namespace]  #.[Namespace]    #.[Namespace]  ...
 
      EMP.Children.(FirstName Age)
   Andy  23   Katherine  19     Tom  25   Jamie  22
```
