---
search:
  boost: 2
---

# <span>Instances</span> `R←⎕INSTANCES Y`{{key}}

`⎕INSTANCES` returns references to the existing instances of the class `Y`, including instances of the classes derived from it.

<h2 class="example">Example</h2>

`Bird` derives from `Animal`, so an instance of `Bird` is also an instance of `Animal`:

```apl
      :Class Animal
      :EndClass
      :Class Bird: Animal
      :EndClass
      Eeyore←⎕NEW Animal
      Robin←⎕NEW Bird
      ⎕INSTANCES Animal
 #.[Animal]  #.[Bird]
      ⎕INSTANCES Bird
 #.[Bird]
```

## Right Argument

`Y` is a reference to a class. If it is a reference to anything else, for example, an instance or a namespace that is not a class, `R` is empty. Any other value signals `DOMAIN ERROR`.

## Result

`R` is a vector of references to the instances, in the order in which they were created. An instance is included only while something refers to it.

<h3 class="example">Example</h3>

Continuing with the classes from the example above, [`⎕DF`](df.md) gives each instance a display form, which shows which instance is which. When `Robin` is expunged, nothing refers to its instance any more:

```apl
      :Class Parrot: Bird
      :EndClass
      Polly←⎕NEW Parrot
      Eeyore.⎕DF 'eeyore' ⋄ Robin.⎕DF 'robin' ⋄ Polly.⎕DF 'polly'
      ⎕INSTANCES Animal
 eeyore  robin  polly
      ⎕INSTANCES Bird
 robin  polly
      ⎕EX 'Robin'
      ⎕INSTANCES Animal
 eeyore  polly
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕INSTANCES INSTANCES
</div>
