<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WC WC
</div>






<h1 class="heading"><span class="name">Window Create Object</span> <span class="command">{R}←{X}⎕WC Y</span></h1>



**Windows only.**


This system function creates a GUI **object**.  `Y` is either a vector which specifies **properties** that determine the new object's appearance and behaviour, or a ref to or the `⎕OR` of a GUI object that exists or previously existed.  `X` is a character vector which specifies the name of the new object, and its position in the object hierarchy.



If `X` is omitted, `⎕WC` attaches a GUI component to the current namespace, retaining any functions, variables and other namespaces that it may contain.  Monadic `⎕WC` is discussed in detail at the end of this section.


If `Y` is a nested vector each element specifies a property.  The `Type` property (which specifies the class of the object) **must** be specified.  Most other properties take default values and need not be explicitly stated.  Properties (including `Type`) may be declared either positionally or with a keyword followed by a value. Note that `Type` must always be the first property specified. Properties are specified positionally by placing their values in `Y` in the order prescribed for an object of that type.


If `Y` is a ref or the result of `⎕OR`, the new object is a complete copy of the other, including any child objects, namespaces, functions and variables that it contained at that time.


The shy result `R` is the full name (starting `#.` or   `⎕SE`.) of the namespace `X`.


An object's name is specified by giving its full pathname in the object hierarchy.  At the top of the hierarchy is the `Root` object whose name is "`.`".  Below "`.`" there may be one or more "top-level" objects.  The names of these objects follow the standard rules for other APL objects as described in [Legal Names](../../../programming-reference-guide/introduction/names)


Names for sub-objects follow the same rules except that the character "`.`" is used as a delimiter to indicate parent/child relationships.



The following are examples of legal and illegal names:


|Legal      |Illegal  |
|-----------|---------|
|`FORM1`    |`FORM 1` |
|`form_23`  |`form#1` |
|`Form1.Gp` |`11_Form`|
|`F1.g2.b34`|`Form+1` |



If `X` refers to the name of an APL variable, label, function, or operator, a `DOMAIN ERROR` is reported.  If `X` refers to the name of an existing GUI object or namespace, the existing one is replaced by the new one.  The effect is the same as if it were deleted first.


If `Y` refers to a non-existent property, or to a property that is not defined for the type of object `X`, a `DOMAIN ERROR` is reported.  A `DOMAIN ERROR` is also reported if a value is given that is inconsistent with the corresponding property.  This can occur for example, if `Y` specifies values positionally and in the wrong order.


A "top-level" object created by `⎕WC` whose name is localised in a function/operator header, is deleted on exit from the function/operator.  All objects, including sub-objects, can be deleted using `⎕EX`.


GUI objects are named **relative** to the current namespace, so the following examples are equivalent:
```apl
      'F1.B1' ⎕WC 'Button'
```


is equivalent to :
```apl
      )CS F1
#.F1
      'B1' ⎕WC 'Button'
      )CS
#
```


is equivalent to :
```apl
      'B1' F1.⎕WC 'Button'
```

<h2 class="example">Examples</h2>
```apl
⍝ Create a default Form called F1
 
      'F1' ⎕WC 'Form'
 
⍝ Create a Form with specified properties (by position)
⍝   Caption = "My Application"  (Title)
⍝   Posn    = 10 30  (10% down, 30% across)
⍝   Size    = 80 60  (80% high, 60% wide)
 
      'F1' ⎕WC 'Form' 'My Application' (10 30)(80 60)
 

```
```apl
⍝ Create a Form with specified properties (by keyword)
⍝   Caption = "My Application"  (Title)
⍝   Posn    = 10 30  (10% down, 30% across)
⍝   Size    = 80 60  (80% high, 60% wide)
 
      PROPS←⊂'Type' 'Form'
      PROPS,←⊂'Caption' 'My Application'
      PROPS,←⊂'Posn' 10 30
      PROPS,←⊂'Size' 80 60
      'F1' ⎕WC PROPS
 
⍝ Create a default Button (a pushbutton) in the Form F1
 
      'F1.BTN' ⎕WC 'Button'
 
⍝ Create a pushbutton labelled "Ok"
⍝ 10% down and 10% across from the start of the FORM
⍝ with callback function FOO associated with EVENT 30
⍝ (this event occurs when the user presses the button)
 
      'F1.BTN'⎕WC'Button' '&Ok' (10 10)('Event' 30 'FOO')
```



Monadic `⎕WC` is used to *attach* a GUI component to an existing object.  The existing object must be a pure namespace or a GUI object.  The operation may be performed by changing space to the object or by running `⎕WC` *inside* the object using the *dot* syntax.  For example, the following statements are equivalent.
```apl
      )CS F
#.F
      ⎕WC 'Form'  ⍝ Attach a Form to this namespace
 
      )CS
#
      F.⎕WC'Form' ⍝ Attach a Form to namespace F
```



