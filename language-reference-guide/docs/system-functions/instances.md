---
search:
  boost: 2
---

# <span>Instances</span> `R←⎕INSTANCES Y`{{key}}

`⎕INSTANCES` returns a list all the current instances of the Class specified by `Y`.

`Y` must be a reference.

If `Y` is a reference to a Class, `R` is a vector of references to all existing Class Instances of  `Y`. Otherwise, `R` is empty.

<h2 class="example">Examples</h2>

This example illustrates a simple inheritance tree or Class hierarchy. There are 3 Classes, namely:
```apl
Animal
    Bird (derived from Animal)
        Parrot (derived from Bird)
```
```apl
:Class Animal
...
:EndClass ⍝ Animal
 
:Class Bird: Animal
...
:EndClass ⍝ Bird
 
:Class Parrot: Bird
...
:EndClass ⍝ Parrot
```

```apl
      Eeyore←⎕NEW Animal
      Robin←⎕NEW Bird
      Polly←⎕NEW Parrot
 
      ⎕INSTANCES Parrot
 #.[Parrot] 
      ⎕INSTANCES Bird
 #.[Bird]  #.[Parrot] 
      ⎕INSTANCES Animal
 #.[Animal]  #.[Bird]  #.[Parrot] 

```
```apl
      Eeyore.⎕DF 'eeyore'
      Robin.⎕DF 'robin'
      Polly.⎕DF 'polly'

      ⎕INSTANCES Parrot
 polly
      ⎕INSTANCES Bird
 robin  polly 
      ⎕INSTANCES Animal
 eeyore  robin  polly 
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕INSTANCES INSTANCES
</div>
