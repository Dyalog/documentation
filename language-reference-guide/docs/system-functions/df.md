---
search:
  boost: 2
---

# <span>Display Form</span> `{R}←⎕DF Y`{{key}}

`⎕DF` sets the *Display Form* of a namespace, a GUI object, a Class, or an Instance of a Class.

`Y` must be `⎕NULL` or a simple character array that specifies the display form of a namespace. If defined, this array will be returned by the *format* functions and `⎕FMT` instead of the default for the object in question. This also applies to the string that is displayed when the name is referenced but not assigned (the *default display*). If `Y` is  `⎕NULL`, `⎕DF` resets the Display Form to the default.

The result `R` is the previous value of the Display Form which initially is `⎕NULL`.

<h2 class="example">Example</h2>
```apl

      'F'⎕WC'Form'
      ⍕F
#.F
      ⍴⍕F
3
      ⎕FMT F
#.F
      ⍴⎕FMT F
1 3
      F ⍝ default display uses ⍕
#.F

      F.⎕DF 'Pete''s Form'
      ⍕F
Pete's Form
      ⍴⍕F
11
      ⎕FMT F
Pete's Form
      ⍴⎕FMT F
1 11
```

Notice that `⎕DF` will accept any character array, but `⎕FMT` always returns a matrix.
```apl

      F.⎕DF 2 2 5⍴⎕A
      F
ABCDE
FGHIJ
 
KLMNO
PQRST
      ⍴⍕F
2 2 5

```

```apl

      ⍴⎕←⎕FMT F
ABCDE
FGHIJ
 
KLMNO
PQRST
5 5
```

Note that `⎕DF` defines the Display Form statically, rather than dynamically.
```apl

      'F'⎕WC'Form' 'This is the Caption'
      F
#.F

      F.(⎕DF Caption)⍝ set display form to current caption
      F
This is the Caption

      F.Caption←'New Caption' ⍝ changing caption does not
                              ⍝ change the display form
      F
This is the Caption
```

You may use the Constructor function to assign the Display Form to an Instance of a Class. For example:
```apl

:Class MyClass
    ∇ Make arg
      :Access Public
      :Implements Constructor
      ⎕DF arg
    ∇
:EndClass ⍝ MyClass

      PD←⎕NEW MyClass 'Pete'
      PD
Pete
```

It is possible to set the Display Form for the Root and for `⎕SE`
```apl

      )CLEAR
clear ws
      #
#
      ⎕DF ⎕WSID
      #
CLEAR WS

      ⎕SE
⎕SE
      ⎕SE.⎕DF 'Session'
      ⎕SE
Session
```

Note that `⎕DF` applies directly to the object in question and is not automatically applied in a hierarchical fashion.
```apl

      'X'⎕NS ''
      X
#.X

      'Y'X.⎕NS ''
      X.Y
#.X.Y
      X.⎕DF 'This is X'
      X
This is X

      X.Y
#.X.Y
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DF DF
</div>
