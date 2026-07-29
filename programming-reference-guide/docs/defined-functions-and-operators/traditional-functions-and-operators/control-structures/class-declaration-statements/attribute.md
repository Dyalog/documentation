# :Attribute Statement

```apl
:Attribute <Name> [ConstructorArgs]
```

The :Attribute statement is used to attach .NET Attributes to a Class or a Method.

Attributes are descriptive tags that provide additional information about programming elements. Attributes are not used by Dyalog APL but other applications can refer to the extra information in attributes to determine how these items can be used. Attributes are saved with the *metadata* of Dyalog APL .NET assemblies.

|Element          |Description                                     |
|-----------------|------------------------------------------------|
|`Name`           |The name of a .NET attribute                    |
|`ConstructorArgs`|Optional arguments for the Attribute constructor|

<h2 class="example">Example</h2>

The following Class has `SerializableAttribute` and `CLSCompliantAttribute` attributes attached to the Class as a whole, and `ObsoleteAttribute` attributes attached to Methods `foo` and `goo` within it.
```apl
:Class c1
:using System
    :attribute SerializableAttribute
    :attribute CLSCompliantAttribute 1
    
    ∇ foo(p1 p2)
      :Access public instance
      :Signature foo Object,Object
      :Attribute ObsoleteAttribute
    ∇
    
    ∇ goo(p1 p2)
      :Access public instance
      :Signature foo Object,Object
      :Attribute ObsoleteAttribute 'Don''t use this' 1
     
    ∇
    
:EndClass ⍝ c1
```

When this Class is exported as a .NET Class, the attributes are saved in its metadata. For example, Visual Studio will warn developers if they make use of a member which has the `ObsoleteAttribute`.
