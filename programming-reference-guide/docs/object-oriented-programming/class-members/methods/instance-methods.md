# Instance Methods

An Instance method runs in the Instance namespace and may only be called via the instance itself. An Instance method has direct access to Fields and Properties, both Private and Public, in the Instance in which it runs.

Class `DomesticParrot` has a `Speak` method defined to be Public and Instance. Where `Speak` refers to `Name`, it obtains the value of `Name` in the current Instance.

Note too that `DomesticParrot.Speak` supersedes the inherited `Parrot.Speak`.
```apl
:Class DomesticParrot: Parrot
    :Field Public Name
    
    ∇ egg nm
      :Access Public
      :Implements Constructor
      Name←nm
    ∇
    
    ∇ R←Speak times
      :Access Public Instance
      R←⊂Name,', ',Name
      R←↑R,times⍴⊂' Who''s a pretty boy, then!'
    ∇
    
:EndClass ⍝ DomesticParrot
 
      pet←⎕NEW DomesticParrot'Polly'
      pet.Speak  3
Polly, Polly             
 Who's a pretty boy, then!
 Who's a pretty boy, then!
 Who's a pretty boy, then!
 
      bil←⎕NEW  DomesticParrot'Billy'
      bil.Speak  1
Billy, Billy             
 Who's a pretty boy, then!
```
