# Empty Arrays of Instances: Why?

In APL it is natural to use *arrays* of Instances. For example, consider the following example.
```apl
:Class Cheese
    :Field Public Name←''
    :Field Public Strength←⍬
    ∇ make2(name strength)
      :Access Public
      :Implements Constructor
      Name Strength←name strength
    ∇
    ∇ make1 name
      :Access Public
      :Implements Constructor
      Name Strength←name 1
    ∇
    ∇ make_excuse
      :Access Public
      :Implements Constructor
      ⎕←'The cat ate the last one!'
    ∇
:EndClass
```

We might create an array of Instances of the Cheese Class as follows:
```apl
      cdata←('Camembert' 5)('Caephilly' 2) 'Mild Cheddar'
      cheeses←{⎕NEW Cheese ⍵}¨cdata
```

Suppose we want a range of medium-strength cheese for our cheese board.
```apl
      board←(cheeses.Strength<3)/cheeses
      board.Name
 Caephilly  Mild Cheddar 
```

But look what happens when we try to select really strong cheese:
```apl
      board←(cheeses.Strength>5)/cheeses
      board.Name
The cat ate the last one!
```

Note that this message is not the result of the expression, but was explicitly displayed by the `make_excuse` function. The clue to this behaviour is the shape of `board`; it is empty!
```apl
      ⍴board
0
```

When a reference is made to an empty array of Instances (strictly speaking, a reference that requires a *prototype*), APL creates a new Instance by calling the *niladic* (default) Constructor, uses the new Instance to satisfy the reference, and then discards it. Hence, in this example, the reference:
```apl
      board.Name
```

caused APL to run the *niladic* Constructor `make_excuse`, which displayed:
```apl
The cat ate the last one!
```

Notice that the behaviour of empty arrays of Instances is modelled VERY closely after the behaviour of empty arrays in general. In particular, the Class designer is given the task of deciding what the types of the members of the prototype are.

The full explanation is given in the [next topic](empty-arrays-of-instances-how.md).
