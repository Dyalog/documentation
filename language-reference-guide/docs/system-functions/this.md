---
search:
  boost: 2
---

# <span>Current Namespace</span> `R←⎕THIS`{{key}}

`⎕THIS` is a reference to the current namespace, which is the namespace in which it is evaluated.

<h2 class="example">Examples</h2>

```apl
      ⎕THIS
#
      'x'⎕NS ''
      x.⎕THIS
#.x
      x≡x.⎕THIS
1
      x.{⎕THIS}0
#.x
```

## Classes and Instances

In an instance, or in a method that runs in an instance, `⎕THIS` is a reference to that instance, and in a class, it is a reference to that class.

<h3 class="example">Examples</h3>

[`⎕CLASS`](class.md) gives the class of the instance, and [`⎕INSTANCES`](instances.md) then gives every instance of that class:

```apl
      :Class Parrot
          ∇ R←Me
            :Access Public
            R←⎕THIS
          ∇
      :EndClass
      Polly←⎕NEW Parrot
      Polly.⎕THIS
#.[Parrot]
      Polly≡Polly.Me
1
      Polly.(1 1⊃⎕CLASS ⎕THIS)
#.Parrot
      Polly.(≢⎕INSTANCES 1 1⊃⎕CLASS ⎕THIS)
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕THIS THIS
</div>
