# :Field Statement

```apl
 :Field <Private|Public> <Instance|Shared> <ReadOnly>...
       ... FieldName <← expr>
```

A `:Field` statement is a single statement whose elements are as follows:

|Element|Description|
|---|---|
|`Private|Public`|Specifies whether or not the Field is accessible from outside the Class or an Instance of the Class. The default is `Private` .|
|`Instance|Shared`|Specifies if there is a separate value of the Field in each Instance of the Class, or if there is only a single value that is shared between all Instances.|
|`ReadOnly`|If specified, this keyword prevents the value in the Field from being changed after initialisation.|
|`Type`|If specified, this identifies a .Net type for the Field. This type applies only when the Class is exported as a .NET Assembly.|
|`FieldName`|Specifies the name of the Field (mandatory).|
|`← expr`|Specifies an initial value for the Field.|

<h2 class="example">Examples</h2>

The following statement defines a Field called `Name`. It is (by default), an Instance Field so every Instance of the Class has a separate value. It is a Public Field and so may be accessed (set or retrieved) from outside an Instance.
```apl
:Field Public Name
```

The following statement defines a Field called `Months`.
```apl
:Field Shared ReadOnly Months←12↑(⎕NEW DateTimeFormatInfo.AbbreviatedMonthNames
```

`Months` is a Shared Field so there is just a single value that is the same for every Instance of the Class. It is (by default), a Private Field and may only be referenced by code running in an Instance or in the Class itself. Furthermore, it is ReadOnly and may not be altered after initialisation. Its initial value is calculated by an expression that obtains the short month names that are appropriate for the current locale using the .NET Type DateTimeFormatInfo.

## Notes

Note that Fields are initialised when a Class script is fixed by the editor or by `⎕FIX`. If the evaluation of `expr` causes an error (for example, a `VALUE ERROR`), an appropriate message will be displayed in the Status Window and `⎕FIX` will fail with a `DOMAIN ERROR`. Note that a ReadOnly Field may only be assigned a value by its `:Field` statement.

In the second example above, the expression will only succeed if `⎕USING` is set to the appropriate path, in this case System.Globalization.

You may not define a Field with the name of one of the permissible keywords (such as `public`). In such cases the Class will not fix and an error message will be displayed in the Status Window. For example:
```apl
error AC0541: a field must have a name "    :Field Public public"
```
