# <span>Access Statement</span> `:Access`

```apl
:Access <Private|Public><Instance|Shared>
:Access <WebMethod>
```

The `:Access` statement is used to specify characteristics for functions  that represent Methods in classes (see [Methods](../../../object-oriented-programming/class-members/methods/methods.md)). It is also applicable to Classes and Properties.

|Element|Description|
|---|---|
|`Private|Public`|Specifies whether or not the method is accessible from outside the Class or an Instance of the Class. The default is `Private` .|
|`Instance|Shared`|Specifies whether the method runs in the Class or Instance. The default is `Instance` .|
|`WebMethod`|Specifies that the method is exported as a web method. This applies only to a Class that implements a Web Service.|
|`Overridable`|Applies only to an Instance Method and specifies that the Method may be overridden by a Method in a higher Class. See below.|
|`Override`|Applies only to an Instance Method and specifies that the Method overrides the corresponding Overridable Method defined in the Base Class. See below|

## Overridable/Override

Normally, a Method defined in a higher Class replaces a Method of the same name that is defined in its Base Class, but only for calls made from above or within the higher Class itself (or an Instance of the higher Class). The base method remains available *in the Base Class* and is invoked by a reference to it *from within the Base Class*.

However, a Method declared as being `Overridable` is replaced in-situ (that is, within its own Class) by a Method of the same name in a higher Class if that Method is itself declared with the `Override` keyword. For further information, see [Superseding Base Class Methods](../../../object-oriented-programming/class-members/methods/superceding-base-class-methods.md).

## WebMethod

Note that `:Access WebMethod` is equivalent to:

```other
:Access Public
:Attribute System.Web.Services.WebMethodAttribute
```



