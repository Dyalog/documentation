
<!-- Hidden search keywords -->
<div style="display: none;">
  127⌶
</div>






<h1 class="heading"><span class="name">Overwrite Free Pockets</span> <span class="command">R←127⌶Y</span></h1>



Overwrites all free pockets in the workspace.


Some applications (cryptography for example) make use of secure data during execution. The nature of the APL workspace is such that remnants of this secure data may persist in the workspace (and thus the process memory) even after the relevant APL variables have been expunged. This function overwrites all unused data pockets in the workspace so that any potentially secure data is removed.


`Y` is any empty array, preferably `⍬`(zilde). `R` is always 1.


It is the responsibility of the programmer to ensure that there are no USED pockets in the workspace that reference the data.


<h2 class="example">Example</h2>
```apl
     ∇ foo;a
[1]    a←'my secure data'
[2]    ⎕EX'a'
[3]    ⍝ 'my secure data' is now in an
[4]    ⍝ UNUSED pocket in the workspace
[5]    a←127⌶0 ⍝ all unused pockets are overwritten,
[6]            ⍝ 'my secure data' is no longer present
     ∇

```

## Whereas
```apl
     ∇ foo;a;b
[1]    a←'my secure data'
[2]    b←a
[3]    ⎕EX'a'
[4]    ⍝ 'my secure data' is now in an
[5]    ⍝ UNUSED pocket in the workspace
[6]    a←127⌶0 ⍝ all unused pockets are overwritten,
[7]            ⍝ but 'my secure data' is still present
[8]            ⍝ because it is referenced by b
     ∇

```


