# Empty Arrays of Instances: How?

To cater for the need to handle empty arrays of Instances as easily as non-empty arrays, a reference to an empty array of Class Instances is handled in a special way.

Whenever a reference or an assignment is made to the content of an *empty array of Instances*, the following steps are performed:

1. APL creates a *new Instance* of the same Class of which the empty Instance belongs
2. the default (niladic) Constructor is run in the new Instance
3. the appropriate value is obtained or assigned:- if it is a reference is to a Field, the value of the Field is obtained
- if it is a reference is to a Property, the PropertyGet function is run
- if it is a reference is to a Method, the method is executed
- if it is an assignment, the assignment is performed or the PropertySet function is run

4. if it is a reference, the result of step 3 is used to generate an empty result array with a suitable prototype by the application of the function `{0⍴⊂⍵}` to it
5. the Class Destructor (if any) is run in the new Instance
6. the New Instance is deleted

<h2 class="example">Example</h2>
```apl
:Class Bird
    :Field Public Species
    
    ∇ egg spec
      :Access Public Instance
      :Implements Constructor
      ⎕DF Species←spec
    ∇
    ∇ default
      :Access Public Instance
      :Implements Constructor
      ⎕DF Species←'Default Bird'
      #.DISPLAY Species
    ∇
    ∇ R←Speak
      :Access Public
      #.DISPLAY R←'Tweet, Tweet, Tweet'
    ∇
    
:EndClass ⍝ Bird
```

First, we can create an empty array of Instances of Bird using `0⍴`.
```apl
      Empty←0⍴⎕NEW Bird 'Robin'
```

A reference to `Empty.Species` causes APL to create a new Instance and invoke the niladic Constructor `default`. This function sets `Species` to `'Default Bird'`*and* calls `#.DISPLAY` which displays output to the Session.
```apl
      DISPLAY Empty.Species
.→-----------.
|Default Bird|
'------------'
```

APL then retrieves the value of `Species` (`'Default Bird'`), applies the function `{0⍴⊂⍵}` to it and returns this as the result of the expression.
```apl
.⊖---------------.
| .→-----------. |
| |            | |
| '------------' |
'∊---------------'
```

A reference to `Empty.Speak` causes APL to create a new Instance and invoke the niladic Constructor `default`. This function sets `Species` to `'Default Bird'`*and* calls `#.DISPLAY` which displays output to the Session.
```apl
      DISPLAY Empty.Speak
.→-----------.
|Default Bird|
'------------'
```

APL then invokes function `Speak` which displays `'Tweet, Tweet, Tweet'` and returns this as the result of the function.
```apl
.→------------------.
|Tweet, Tweet, Tweet|
'-------------------'
```

APL then applies the function `{0⍴⊂⍵}` to it and returns this as the result of the expression.
```apl
.⊖----------------------.
| .→------------------. |
| |                   | |
| '-------------------' |
'∊----------------------'
```
