---
search:
  boost: 2
---

# <span>Convert Namespace to GUI Object</span> `{R}←⎕WC Y`{{key}}

**Windows only.**

This system function creates a GUI **object**.  `Y` is either a vector which specifies **properties** that determine the new object's appearance and behaviour, or a ref to or the `⎕OR` of a GUI object that exists or previously existed.

`⎕WC` attaches a GUI component to the current namespace, retaining any functions, variables and other namespaces that it can contain.  Monadic `⎕WC` is discussed in detail at the end of this section.

If `Y` is a nested vector each element specifies a property.  The `Type` property (which specifies the class of the object) **must** be specified.  Most other properties take default values and need not be explicitly stated.  Properties (including `Type`) may be declared either positionally or with a keyword followed by a value. Note that `Type` must always be the first property specified. Properties are specified positionally by placing their values in `Y` in the order prescribed for an object of that type.

If `Y` is a ref or the result of `⎕OR`, the new object is a complete copy of the other, including any child objects, namespaces, functions and variables that it contained at that time.

The shy result `R` is the full name (starting `#.` or   `⎕SE`.) of the namespace.

An object's name is specified by giving its full pathname in the object hierarchy.  At the top of the hierarchy is the `Root` object whose name is "`.`".  Below "`.`" there may be one or more "top-level" objects.  The names of these objects follow the standard rules for other APL objects as described in [Legal Names](../../../programming-reference-guide/introduction/names)

Names for sub-objects follow the same rules except that the character "`.`" is used as a delimiter to indicate parent/child relationships.

The following are examples of legal and illegal names:

|Legal      |Illegal  |
|-----------|---------|
|`FORM1`    |`FORM 1` |
|`form_23`  |`form#1` |
|`Form1.Gp` |`11_Form`|
|`F1.g2.b34`|`Form+1` |

If `Y` refers to a non-existent property, or to a property that is not defined for the type of the object, a `DOMAIN ERROR` is reported.  A `DOMAIN ERROR` is also reported if a value is given that is inconsistent with the corresponding property.  This can occur for example, if `Y` specifies values positionally and in the wrong order.

A "top-level" object created by `⎕WC` whose name is localised in a function/operator header, is deleted on exit from the function/operator.  All objects, including sub-objects, can be deleted using `⎕EX`.

GUI objects are named **relative** to the current namespace.

<h2 class="example">Examples</h2>

Monadic `⎕WC` is used to *attach* a GUI component to an existing object.  The existing object must be a pure namespace or a GUI object.  The operation may be performed by changing space to the object or by running `⎕WC` *inside* the object using the *dot* syntax.  For example, the following statements are equivalent.
```apl
      )CS F
#.F
      ⎕WC 'Form'  ⍝ Attach a Form to this namespace
 
      )CS
#
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WC WC
</div>
