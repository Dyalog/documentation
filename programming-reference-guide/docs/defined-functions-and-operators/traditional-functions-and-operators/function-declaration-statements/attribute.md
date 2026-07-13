# <span>Attribute Statement</span> `:Attribute`

```apl
:Attribute <Name> [ConstructorArgs]
```

The `:Attribute` statement is used to attach .NET Attributes to a Method (or Class).

Attributes are descriptive tags that provide additional information about programming elements. Attributes are not used by Dyalog APL but other applications can refer to the extra information in attributes to determine how these items can be used. Attributes are saved with the *metadata* of Dyalog APL .NET assemblies.

|Element          |Description                                     |
|-----------------|------------------------------------------------|
|`Name`           |The name of a .NET attribute                    |
|`ConstructorArgs`|Optional arguments for the Attribute constructor|

<h2 class="example">Examples</h2>
```apl
      :Attribute ObsoleteAttribute
      :Attribute ObsoleteAttribute 'Don''t use' 1
```



