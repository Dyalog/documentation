---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FMT FMT
</div>






<h1 class="heading"><span class="name">Format (Monadic)</span> <span class="command">R←⎕FMT Y</span></h1>



`Y` may be any array.  `R` is a simple character matrix which appears the same as the default display of `Y`.  If `Y` contains control characters from `⎕TC`, they will be resolved.


<h2 class="example">Examples</h2>
```apl
      A←⎕FMT '∩' ,⎕TC[1],'∘'
 
      ⍴A
1 1
      A
⍝
 
      A←⎕VR 'FOO'
 
      A
     ∇ R←FOO
[1]    R←10
     ∇
 
      ⍴A
31
      B←⎕FMT A
 
      B
     ∇ R←FOO
[1]    R←10
     ∇
 
      ⍴B
3 12
```


