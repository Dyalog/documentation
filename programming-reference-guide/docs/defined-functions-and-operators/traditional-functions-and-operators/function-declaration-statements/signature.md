# <span>Signature Statement</span> `:Signature`

```apl
:Signature <rslttype←><name><arg1type arg1name>,...
```

This statement identifies the name and signature by which a function is exported as a method to be called from outside Dyalog APL. Several :Signature statements may be specified to allow the method to be called with different arguments and/or to specify a different result type.

|Element   |Description                                         |
|----------|----------------------------------------------------|
|`rslttype`|Specifies the data type for the result of the method|
|`name`    |Specifies the name of the exported method.          |
|`argntype`|Specifies the data type of the nth parameter        |
|`argnname`|Specifies the name of the nth parameter             |

Argument and result data types are identified by the names of .NET Types which are defined in the .NET Assemblies specified by `⎕USING` or by a `:USING` statement.

<h2 class="example">Examples</h2>

In the following examples, it is assumed that the .NET Search Path (defined by `:Using` or `⎕USING` includes `'System'`.

The following statement specifies that the function is exported as a method named `Format` which takes a single parameter of type `System.Object` named `Array`. The data type of the result of the method is an array (vector) of type `System.String`.
```apl
      :Signature String[]←Format Object Array
```

The next statement specifies that the function is exported as a method named `Catenate` whose result is of type `System.Object` and which takes 3 parameters. The first parameter is of type `System.Double` and is named `Dimension`. The second is of type `System.Object` and is named `Arg1`. The third is of type `System.Object` and is named `Arg2`.
```apl
      :Signature Object←Catenate Double Dimension,...
                              ...Object Arg1, Object Arg2
```


The next statement specifies that the function is exported as a method named `IndexGen` whose result is an array of type `System.Int32` and which takes 2 parameters. The first parameter is of type `System.Int32` and is named `N`. The second is of type `System.Int32` and is named `Origin`.
```apl
      :Signature Int32[]←IndexGen Int32 N, Int32 Origin
```

The next block of statements specifies that the function is exported as a method named `Mix`. The method has 4 different signatures; that is, it may be called with 4 different parameter/result combinations.
```apl
      :Signature Int32[,]←Mix Double Dimension, ...
            ...Int32[] Vec1, Int32[] Vec2
      :Signature Int32[,]←Mix Double Dimension,...
            ... Int32[] Vec1, Int32[] Vec2, Int32 Vec3
      :Signature Double[,]←Mix Double Dimension, ...
            ... Double[] Vec1, Double[] Vec2
      :Signature Double[,]←Mix Double Dimension, ...
            ... Double[] Vec1, Double[] Vec2, Double[] Vec3
```


