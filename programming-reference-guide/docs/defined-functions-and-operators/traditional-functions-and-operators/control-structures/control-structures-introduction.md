---
search:
  exclude: true
---

<h1 class="heading"><span class="name">Control Structures</span></h1>

Control structures provide a means to control the flow of execution in your APL programs.

Traditionally, lines of APL code are executed one by one from top to bottom and the only way to alter the flow of execution is using the branch arrow.  So how do you handle logical operations of the form "If this, do that; otherwise do the other"?

In APL this is often not a problem because many logical operations are easily performed using the standard array handling facilities that are absent in other languages.  For example, the expression:
```apl
      STATUS←(1+AGE<16)⊃'Adult' 'Minor'
```

sets `STATUS` to `'Adult'` if `AGE` is 16 or more; otherwise sets `STATUS` to `'Minor'`.

Things become trickier if, depending upon some condition, you wish to execute one set of code instead of another, especially when the code fragments cannot conveniently be packaged as functions.  Nevertheless, careful use of array logic, defined operators, the execute primitive function and the branch arrow can produce high quality maintainable and comprehensible APL systems.

Control structures provide an additional mechanism for handling logical operations and decisions.  Apart from providing greater affinity with more traditional languages, Control structures may enhance comprehension and reduce programming errors, especially when the logic is complex.  Control structures are not, however, a replacement for the standard logical array operations that are so much a part of the APL language.
