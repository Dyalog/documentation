---
search:
  boost: 2
---

# <span>Division Method</span> `⎕DIV`

The value of `⎕DIV` determines how division by zero is to be treated.  If `⎕DIV=0`, division by 0 produces a `DOMAIN ERROR` except that the special case of `0÷0` returns 1.

`⎕DIV` is an [implicit argument](../primitive-functions/notes.md#implicit-arguments) of:

- monadic functions: [`÷`](../primitive-functions/reciprocal.md)
- dyadic functions: [`÷`](../primitive-functions/divide.md)

If `⎕DIV=1`, division by 0 returns 0.

`⎕DIV` may be assigned the value 0 or 1.  The value in a clear workspace is 0. `⎕DIV` has Namespace scope.

<h2 class="example">Examples</h2>
```apl
      ⎕DIV←0
 
      1 0 2 ÷ 2 0 1
0.5 1 2
 
      ÷0 1
DOMAIN ERROR
      ÷0 1
      ^
 
      ⎕DIV←1
 
      ÷0 2
0 0.5
 
      1 0 2 ÷ 0 0 4
0 0 0.5
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DIV DIV
</div>
