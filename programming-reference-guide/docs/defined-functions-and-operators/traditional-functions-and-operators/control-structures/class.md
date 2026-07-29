# :Class Statement

`:Class <class name><:base class name> <,interface name...>`
```apl
:Include <namespace>
...
:EndClass
```

A class script begins with a `:Class` statement and ends with a `:EndClass` statement. The elements that comprise the `:Class` statement are as follows:

|Element          |Description                                                                                                     |
|-----------------|----------------------------------------------------------------------------------------------------------------|
|`class name`     |Optionally, specifies the name of the Class, which must conform to the rules governing APL names.               |
|`base class name`|Optionally specifies the name of a Class from which this Class is derived and whose members this Class inherits.|
|`interface name` |The names of one or more Interfaces which this Class supports.                                                  |

A Class may import methods defined in separate plain Namespaces with one or more `:Include` statements. For further details, see [Including Namespaces in Classes](../../../object-oriented-programming/including-namespaces-in-classes/including-namespaces-in-classes.md).

<h2 class="example">Examples</h2>

The following statements define a Class named `Penguin` that derives from (is based upon) a Class named `Animal` and which supports two Interfaces named `BirdBehaviour` and `FishBehaviour`.
```apl
:Class Penguin: Animal,BirdBehaviour,FishBehaviour
...
:EndClass
```

The following statements define a Class named `Penguin` that derives from (is based upon) a Class named `Animal` and includes methods defined in two separate Namespaces named `BirdStuff` and `FishStuff`.
```apl
:Class Penguin: Animal
:Include BirdStuff
:Include FishStuff
...
:EndClass
```
