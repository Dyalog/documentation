# :Access Statement

```apl
:Access <Private|Public><Instance|Shared><Overridable>
                                         <Override>
:Access <WebMethod>
```

The :Access statement is used to specify characteristics for Classes, Properties and Methods.

|Element|Description|
|---|---|
|`Private|Public`|Specifies whether or not the (nested) Class, Property or Method is accessible from outside the Class or an Instance of the Class. The default is `Private` .|
|`Instance|Shared`|For a Field, specifies if there is a separate value of the Field in each Instance of the Class, or if there is only a single value that is shared between all Instances. For a Property or Method, specifies whether the code associated with the Property or Method runs in the Class or Instance.|
|`WebMethod`|Applies only to a Method and specifies that the method is exported as a web method. This applies only to a Class that implements a Web Service.|
|`Overridable`|Applies only to an Instance Method and specifies that the Method may be overridden by a Method in a higher Class. See below.|
|`Override`|Applies only to an Instance Method and specifies that the Method overrides the corresponding Overridable Method defined in the Base Class. See below.|

## Overridable/Override

Normally, a Method defined in a higher Class replaces a Method of the same name that is defined in its Base Class, but only for calls made from above or within the higher Class itself (or an Instance of the higher Class). The base method remains available *in the Base Class* and is invoked by a reference to it *from within the Base Class*.

However, a Method declared as being `Overridable` is replaced in situ (that is, within its own Class) by a Method of the same name in a higher Class if that Method is itself declared with the `Override` keyword. For further information, see [Superseding Base Class Methods](../../../../object-oriented-programming/class-members/methods/superceding-base-class-methods.md).

## Nested Classes

The `:Access` statement is also used to control the visibility of one Class that is defined within another (a nested Class). A Nested Class may be either `Private` or `Public`. Note that the `:Access` Statement must precede the definition of any Class contents.

A `Public` Nested Class is visible from outside its containing Class and may be used directly in its own right, whereas a `Private` Nested Class is not and may only be used by code inside the containing Class.

However, methods in the containing Class may return instances of Private Nested Classes and in that way expose them to the calling environment.

## WebMethod

Note that `:Access WebMethod` is equivalent to:
```apl
:Access Public
:Attribute System.Web.Services.WebMethodAttribute
```
