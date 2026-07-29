# Statements

The body of a dfn is a sequence of statements, evaluated in order. Each statement is one of:

- an *expression*, whose value can become the [result](../../introduction/results.md) of the dfn
- a *[guard](guards.md)*: an expression, a colon, and a further expression (`condition: result`)
- an *[error-guard](error-guards.md)*: a vector of error numbers, the digraph `::`, and a further expression (`errnos:: result`)
- an *assignment*, which [binds a name local to the dfn](global-local-names.md)
- a *comment*, introduced by `⍝`

Statements are separated by the diamond (`⋄`) or by newlines. A dfn returns the value of the first statement it evaluates that is not an assignment, a guard, or an error-guard, and evaluation stops there. When a guard's condition is true, its right-hand expression is evaluated and returned. An error-guard returns its right-hand expression only if a matching error occurs while the guard is in scope. If evaluation reaches the end of the dfn without producing a value, the dfn returns [no result](../../introduction/results.md#no-result).

<h2 class="example">Example</h2>
```apl
      sign←{
          ⍵>0: 1        ⍝ guard: returned when ⍵>0
          ⍵<0: ¯1
          0             ⍝ reached only when neither guard holds
      }
      sign ¯4
¯1
```

Control structures and labels are not part of a dfn; conditions are expressed with guards instead (see [Restrictions](restrictions.md)).
