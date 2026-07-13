# :Property Section

A Property is defined by a `:Property ... :EndProperty` section in a Class Script. The syntax of the :Property Statement, and its optional `:Access` statement is as follows:
```apl
:Property <Simple|Numbered|Keyed> <Default> Name<,Name>...
:Access <Private|Public><Instance|Shared>
...
:EndProperty
 
```

|Element|Description|
|---|---|
|`Name`|Specifies the name of the Property by which it is accessed. Additional Properties, sharing the same PropertyGet and/or PropertySet functions, and the same access behaviour may be specified by a comma-separated list of names.|
|`Simple|Numbered|Keyed`|Specifies the type of Property (see below). The default is `Simple` .|
|`Default`|Specifies that this Property acts as the default property for the Class when indexing is applied directly to an Instance of the Class.|
|`Private|Public`|Specifies whether or not the Property is accessible from outside the Class or an Instance of the Class. The default is `Private` .|
|`Instance|Shared`|Specifies if there is a separate value of the Property in each Instance of the Class, or if there is only a single value that is shared between all Instances.|

A [Simple Property](../class-members/properties/simple-instance-properties.md) is one whose value is accessed (by APL) in its entirety and re-assigned (by APL) in its entirety.

A [Numbered Property](../class-members/properties/numbered-properties/numbered-properties.md) behaves like an array (conceptually a vector) which is only ever *partially* accessed and set (one element at a time) via indices.

A [Keyed Property](../class-members/properties/keyed-properties/keyed-properties.md) is similar to a Numbered Property except that its elements are accessed via arbitrary keys instead of indices.

Numbered and Keyed Properties are designed to allow APL to perform selections and structural operations on the Property.

Within the body of a Property Section there may be:

- one or more `:Access` statements 
- a single [PropertyGet](propertyget-function-syntax.md) function.
- a single [PropertySet](propertyset-function-syntax.md) function
- a single [PropertyShape](propertyshape-function-syntax.md) function

The three functions are identified by case-independent names `Get`, `Set` and `Shape`.

## Errors

When a Class is fixed by the Editor or by `⎕FIX`, APL checks the validity of each Property section and the syntax of [PropertyGet](propertyget-function-syntax.md), [PropertySet](propertyset-function-syntax.md) and [PropertyShape](propertyshape-function-syntax.md) functions within them.

- You may not specify a name which is the same as one of the keywords.
- There must be at least a [PropertyGet](propertyget-function-syntax.md), or a [PropertySet](propertyset-function-syntax.md) or a [PropertyShape](propertyshape-function-syntax.md) function defined.
- You may only define a [PropertyShape](propertyshape-function-syntax.md) function if the Property is Numbered.

If anything is wrong,  the Class is not fixed and an error message is displayed in the Status Window. For example:
```apl
error AC0545: invalid or empty property declaration
error AC0595: this property type should not implement a "shape" function
```
