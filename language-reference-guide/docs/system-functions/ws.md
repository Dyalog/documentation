---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WS WS
</div>






<h1 class="heading"><span class="name">Window Set Property</span> <span class="command">{R}←{X}⎕WS Y</span></h1>



**Windows only.**


This system function resets property values for a GUI object.


`X` is a namespace reference or a character vector containing the name of the object.  `Y` defines the property or properties to be changed and the new value or values.  If a single property is to be changed, `Y` is a vector whose first element `Y[1]` is a character vector containing the property name.  If `Y` is of length 2, `Y[2]` contains the corresponding property value.  However, if the property value is itself a numeric or nested vector, its elements may be specified in `Y[2 3 4 ...]` instead of as a single nested element in `Y[2]`.  If `Y` specifies more than one property, they may be declared either positionally or with a keyword followed by a value.  Properties are specified positionally by placing their values in `Y` in the order prescribed for an object of that type.  Note that the first property in `Y` must always be specified with a keyword because the `Type` property (which is expected first) may not be changed using `⎕WS`.



If `X` refers to a non-existent GUI name, a `VALUE ERROR` is reported.  If `Y` refers to a non-existent property, or to a property that is not defined for the type of object `X`, or to a property whose value may not be changed by `⎕WS`, a `DOMAIN ERROR` is reported.


The shy result `R` contains the previous values of the properties specified in `Y`.


GUI objects are named **relative** to the current namespace.  A null value of `X` (referring to the namespace in which the function is being evaluated) may be omitted.  The following examples are equivalent:
```apl
      'F1.B1' ⎕WS 'Caption' '&Ok'
      'B1' F1.⎕WS 'Caption' '&Ok'
      '' F1.B1.⎕WS 'Caption' '&Ok'
      F1.B1.⎕WS 'Caption' '&Ok'
```

<h2 class="example">Examples</h2>
```apl
      'F1' ⎕WC 'Form'  ⍝ A default Form
 
      'F1' ⎕WS 'Active' 0
 
      'F1' ⎕WS 'Caption' 'My Application'
 
      'F1' ⎕WS 'Posn' 0 0
 
      'F1' ⎕WS ('Active' 1)('Event' 'Configure' 'FOO')
 
      'F1' ⎕WS 'Junk' 10
DOMAIN ERROR
 
      'F1' ⎕WS 'MaxButton' 0
DOMAIN ERROR
```


