# Function Declaration Statements

Function Declaration statements are used to identify the characteristics of a function in some way.

The following declarative statements are provided.

- [:Access](access.md)

- [:Attribute](attribute.md)

- [:Implements](../control-structures/implements.md)

- [:Signature](../control-structures/signature.md)

With one exception, these statements are not executable statements and may theoretically appear anywhere in the body of the function. However, it is recommended that you place them at the beginning before any executable statements. The exception is:
```apl
:Implements Constructor <[:Base expr]>
```

In addition to being declarative (declaring the function to be a Constructor) this statement also executes the Constructor in the Base Class whether or not it includes :Base expr. Its position in the code is therefore significant.
