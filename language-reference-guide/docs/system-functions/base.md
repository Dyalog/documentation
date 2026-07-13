---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕BASE BASE
</div>

# <span>Base Class</span> `R←⎕BASE.Y`{{key}}

`⎕BASE` is used to access the base class implementation of the name specified by `Y`.

`Y` must be the name of a Public member (Method, Field or Property) that is provided by the Base Class of the current Class or Instance.

`⎕BASE` is typically used to call a method in the Base Class which has been *superseded* by a Method in the current Class.

Note that `⎕BASE.Y` is *special syntax* and any direct reference to `⎕BASE` on its own or in any other context, is meaningless and causes `SYNTAX ERROR`.

In the following example, Class `DomesticParrot` derives from Class `Parrot` and supersedes its `Speak` method. `DomesticParrot.Speak` calls the `Speak` method in its Base Class `Parrot`, via `⎕BASE`.
```apl
:Class Parrot: Bird
    ∇ R←Speak
      :Access Public
      R←'Squark!'
    ∇
:EndClass ⍝ Parrot
 
:Class DomesticParrot: Parrot
    ∇ R←Speak
      :Access Public
      R←⎕BASE.Speak,' Who''s a pretty boy, then!'
    ∇
:EndClass ⍝ DomesticParrot

      Maccaw←⎕NEW Parrot
      Maccaw.Speak
Squark!
 
      Polly←⎕NEW DomesticParrot
      Polly.Speak
Squark! Who's a pretty boy, then!
```
