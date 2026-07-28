# Statements

The body of a dfn is a sequence of statements, evaluated in order. Each statement is one of:

- an *expression*, whose value can become the [result](../../introduction/results.md) of the dfn;
- a *guard*: an expression, a colon, and a further expression (`condition: result`), see [Guards](guards.md);
- an *assignment*, which binds a name local to the dfn (see [Global and Local Names](global-local-names.md));
- a *comment*, introduced by `⍝`.

Statements are separated by the diamond (`⋄`) or by newlines. A dfn returns the value of the first statement it evaluates that is neither an assignment nor a guard, and evaluation stops there. When a guard's condition is true, its right-hand expression is evaluated and returned. If evaluation reaches the end of the dfn without producing such a value, the dfn returns [no result](../../introduction/results.md#no-result).

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
