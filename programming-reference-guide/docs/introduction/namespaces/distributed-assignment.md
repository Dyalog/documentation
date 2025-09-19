<h1 class="heading"><span class="name">Distributed Assignment</span></h1>

Assignment pervades nested strands of names to the left of the arrow. The conformability rules are the same as for scalar (pervasive) dyadic primitive functions such as '`+`'. The mechanism can be viewed as a way of naming the parts of a structure.

<h2 class="example">Examples</h2>
```apl
      EMP.(FirstName Age)
  JOHN  43   PAUL  44
 
      EMP.(FirstName Age)←('Jonathan' 21)('Pauline' 22)
 
      EMP.(FirstName Age)
  Johnathan  21   Pauline  22
 
⍝ Distributed assignment is pervasive
      JOHN.Children.(FirstName Age)
  Andy  23   Katherine  19
 
      JOHN.Children.(FirstName Age)←('Andrew' 21)('Kate' 9)
 
      JOHN.Children.(FirstName Age)
  Andrew  21   Kate  9
```

## More Examples
```apl
      ((a b)(c d))←(1 2)(3 4)   ⍝ a←1 ⋄ b←2 ⋄ c←3 ⋄ d←4
 
      ((⎕IO ⎕ML)vec)←0 ⎕AV      ⍝ ⎕IO←0 ⋄ ⎕ML←0 ⋄ vec←⎕AV
 
      (i (j k))+←1 2            ⍝ i+←1 ⋄ j+←2 ⋄ k+←2
 
⍝ Naming of parts:
 
      ((first last) sex (street city state))←n⊃pvec
 
⍝ Distributed assignment in :For loop:
 
      :For (i j)(k l) :In array
 
⍝ Ref array expansion:
 
      (x y).(first last)←('John' 'Doe')('Joe' 'Blow')
      (f1 f2).(b1 b2).Caption←⊂'OK' 'Cancel'

⍝ Structure rearrangement:
      rotate1←{       ⍝ Simple binary tree rotation.
           (a b c)d e←⍵
           a b(c d e)
      }
      rotate3←{       ⍝ Compound binary tree rotation.
           (a b(c d e))f g←⍵
           (a b c)d(e f g)
      }
```
