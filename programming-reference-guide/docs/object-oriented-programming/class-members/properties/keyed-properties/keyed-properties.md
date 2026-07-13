# Keyed Properties

A Keyed Property is similar to a Numbered Property except that it may **only** be accessed by indexing (so-called square-bracket indexing) and indices are not restricted to integers but may be arbitrary arrays.

To implement a Keyed Property, only a `get` and/or a `set` function are required. APL does not attempt to validate or resolve the specified indices in any way, so does not require the presence of a `shape` function for the Property.

However, APL **does** check that the rank and lengths of the indices correspond to the rank and lengths of the array to the right of the assignment (for an indexed assignment) and the array returned by the get function (for an indexed reference). If the rank or shape of these arrays fails to conform to the rank or shape of the indices, APL will issue a `RANK ERROR` or `LENGTH ERROR`.

Note too that indices **may be elided**. If `KProp` is a Keyed Property of Instance `I1`, the following expressions are all valid.
```apl
      I1.KProp
      I1.KProp[]←10
      I1.KProp[;]←10
      I1.KProp['One' 'Two';]←10
      I1.KProp[;'One' 'Two']←10
```

When APL calls a monadic `get` or a `set` function, it supplies an argument of type PropertyArguments,  which identifies which dimensions and indices were specified. See [PropertyArguments Class](../../../property-section/propertyarguments-class.md).
