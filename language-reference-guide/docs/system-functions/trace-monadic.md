---
search:
  boost: 2
---

# <span>Query Trace Vector</span> `R←⎕TRACE Y`{{key}}

This function reports the lines of a tradfn or tradop on which trace controls are set. [Dyadic `⎕TRACE`](trace-dyadic.md) sets them.

<h2 class="example">Example</h2>

```apl
      ∇ R←FOO
[1]    R←10
      ∇
      0 1 ⎕TRACE 'FOO'
      ⎕TRACE 'FOO'
0 1
```

## Right Argument

`Y` is a simple character scalar or vector containing the name of a visible function or operator. A name that is not the name of a function or operator signals `DOMAIN ERROR`.

## Result

`R` is a simple integer vector of the line numbers on which trace controls are set, in ascending order. `0` means that a trace control is set to display the result of the function or operator immediately before exit.

Trace controls apply only to tradfns and tradops. For any other function or operator, such as a dfn, a dop, or a derived function, `R` is empty.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TRACE TRACE
</div>
