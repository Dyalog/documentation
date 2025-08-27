<h1 class="heading"><span class="name">Axis Operator</span></h1>

The axis operator may be applied to all scalar dyadic primitive functions and certain mixed primitive functions.  An integer axis identifies a specific axis along which the function is to be applied to one or both of its arguments.  If the primitive function is to be applied without an axis specification, a default axis is implied, either the first or last.

<h2 class="example">Example</h2>
```apl
      1 0 1/[1] 3 2⍴⍳6
1 2
5 6
```
```apl
      1 2 3+[2]2 3⍴10 20 30
11 22 33
11 22 33
```

Sometimes the axis value is fractional, indicating that a new axis or axes are to be created between the axes identified by the lower and upper integer bounds of the value (either of which might not exist).

<h2 class="example">Example</h2>
```apl
      'NAMES',[0.5]'='
NAMES
=====
```

`⎕IO` is an implicit argument of an axis specification.
