<h1 class="heading"><span class="name">Notes</span></h1>

## Conformability

The arguments of a dyadic function are said to be CONFORMABLE if the shape of each argument meets the requirements of the function, possibly after scalar extension.

## Fill Elements

Some primitive functions may include fill elements in their result.  The fill element for an array is the enclosed type of the disclose of the array (`⊂∊⊃Y` for array `Y` with `⎕ML←0`).  The Type function (`∊` with `⎕ML←0`) replaces a numeric value with zero and a character value with `' '`.

The Disclose function (`⊃`) returns the first item of an array.  If the array is empty, `⊃Y` is the PROTOTYPE of `Y`.  The prototype is the type of the first element of the original array.

Primitive functions which may return an array including fill elements are Expand (`\` or `⍀`), Replicate (`/` or `⌿`), Reshape (`⍴`) and Take (`↑`).

<h2 class="example">Examples</h2>
```apl

      ML←0
      ∊⍳5
0 0 0 0 0
 
      ∊⊃(⍳3)('ABC')
0 0 0
 
      ⊂∊⊃(⍳3)('ABC')
 0 0 0
 
      ⊂∊⊃⊂(⍳3)('ABC')
  0 0 0
 
      A←'ABC' (1 2 3)
      A←0⍴A
      ⊂∊⊃A
 
      ' '=⊂∊⊃A
 1 1 1
```

## Axis Operator

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
