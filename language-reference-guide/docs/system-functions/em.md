---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EM EM
</div>

<h1 class="heading"><span class="name">Event Message</span> <span class="command">R←⎕EM Y</span></h1>

`Y` must be a simple non-negative integer scalar or vector of event codes.  If `Y` is a scalar, `R` is a simple character vector containing the associated event message.  If `Y` is a vector, `R` is a vector of character vectors containing the corresponding event messages.

If `Y` refers to an undefined error code "`n`", the event message returned is "`ERROR NUMBER n`".

See [APL Error Messages](../../../programming-reference-guide/error-messages/apl-errors).

<h2 class="example">Example</h2>
```apl
      ⎕EM 11
DOMAIN ERROR
```



