# <span>KeepOnClose</span> <span>Property</span>

[**Applies To**](../propertyapplies/keeponclose.md)

**Description**

This property is either 0 or 1 and determines how the object is treated when its parent Form (or, in the case of a Form, the Form itself) is closed by the user, receives a Close event from `⎕NQ`, or when Close is called as a method.

If `KeepOnClose` is 1 (for the object itself **and** for all its parents) when its parent Form is closed, the object changes from being a GUI object to a pure namespace. For example, the Type of a Button will change from `'Button'` to `'Namespace'`. Effectively, the GUI component of the object is discarded but its Namespace component (and any variables, functions, operators and other namespaces that it contains) remains intact. Monadic `⎕WC` may subsequently be used to re-attach the GUI component to the object. All child GUI objects are treated in the same way.

Note that the default value of `KeepOnClose` depends upon the way in which a GUI object was created with `⎕WC`. If a GUI object is created by dyadic `⎕WC`, KeepOnClose defaults to 0. If a GUI object is attached by monadic `⎕WC`, its KeepOnClose property defaults to 1.

!!! note
    The use of `KeepOnClose` is deprecated; Dyalog may at some point remove this Property or disable its functionality.
