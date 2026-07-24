---
search:
  boost: 2
---


# <span>Called Monadically?</span> `R←900⌶Y`{{key}}

Identifies how the current function was called. It reports whether the nearest tradfn on the stack was called without a left argument or not.

`Y` may be any array.

The result `R` is Boolean. 1 means that the nearest tradfn was called monadically; 0 means that it wasn't. If there is no function on the stack, the result is 0.

<h2 class="example">Example</h2>
```apl
     ∇ r←{left}foo right
[1]    r←900⌶⍬
     ∇
      foo 10
1
      0 foo 10
0

```

<!-- Hidden search keywords -->
<div style="display: none;">
  900⌶
</div>
