---
search:
  boost: 2
---

# <span>Source</span> `R←⎕SRC Y`{{key}}

`⎕SRC` returns the script that defines the scripted object   `Y`.

`Y` must be a reference to a scripted object. Scripted objects include Classes, Interfaces and scripted Namespaces.

`R` is a vector of character vectors containing the script that was used to define `Y`.

```apl

      )ED ○MyClass
```
```apl

:Class MyClass
∇ r←foo arg
:Access public shared
r←1+arg
∇
:EndClass

      z←⎕SRC MyClass
      ⍴z
6
      ⍴¨z
 14  15  27  13  5  9 
      ⍪z
 :Class MyClass
     ∇ r←foo arg
       :Access public shared
       r←1+arg
     ∇
 :EndClass
```

The only two ways to permanently alter the source of a scripted object are to change the object in the editor, or to refix it using `⎕FIX`.

!!! Hint "Hints and Recommendations"
    A useful technique to ensure that a scripted object is in sync with its source is to `⎕FIX ⎕SRC ref`, where `ref` is an object reference.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SRC SRC
</div>
