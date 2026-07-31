---
search:
  boost: 2
---

# <span>Set Properties of Current GUI Object</span> `{R}←⎕WS Y`{{key}}

**Windows only.**

This system function resets property values for a GUI object.

The object is the one in the namespace in which the function is being evaluated.  `Y` defines the property or properties to be changed and the new value or values.  If a single property is to be changed, `Y` is a vector whose first element `Y[1]` is a character vector containing the property name.  If `Y` is of length 2, `Y[2]` contains the corresponding property value.  However, if the property value is itself a numeric or nested vector, its elements may be specified in `Y[2 3 4 ...]` instead of as a single nested element in `Y[2]`.  If `Y` specifies more than one property, they may be declared either positionally or with a keyword followed by a value.  Properties are specified positionally by placing their values in `Y` in the order prescribed for an object of that type.  Note that the first property in `Y` must always be specified with a keyword because the `Type` property (which is expected first) may not be changed using `⎕WS`.

If `Y` refers to a non-existent property, or to a property that is not defined for the type of the object, or to a property whose value may not be changed by `⎕WS`, a `DOMAIN ERROR` is reported.

The shy result `R` contains the previous values of the properties specified in `Y`.

GUI objects are named **relative** to the current namespace.  The following examples are equivalent:

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WS WS
</div>
