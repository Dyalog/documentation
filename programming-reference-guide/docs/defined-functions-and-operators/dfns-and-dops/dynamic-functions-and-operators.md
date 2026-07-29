# Dfns & Dops

A *dfn* (*dop*)[^1] is an alternative function definition style suitable for defining small to medium sized functions. It bridges the gap between operator expressions: `rank←⍴∘⍴` and full "header style" definitions such as:
```apl
    ∇ rslt←larg func rarg;local...
```

In its simplest form, a dfn is an APL expression enclosed in curly braces `{}`, possibly including the special characters `⍺` and `⍵` to represent the left and right arguments of the function respectively. For example:
```apl
      {(+/⍵)÷⍴⍵} 1 2 3 4    ⍝ Arithmetic Mean (Average)
2.5
      3 {⍵*÷⍺} 64           ⍝ ⍺th root
4
```

dfns can be named in the normal fashion:
```apl
      mean←{(+/⍵)÷⍴⍵}
      mean¨(2 3)(4 5)
 2.5  4.5
```

dfns can be defined and used in any context where an APL function may be found, in particular:

- In immediate execution mode as in the examples above.
- Within a defined function or operator.
- As the operand of an operator such as each (`¨`).
- Within another dfn.
- The last point means that it is easy to define nested local functions.

[^1]: The terms dfn and dop refer to a special type of function (or operator) unique to Dyalog. They were originally named dynamic functions and dynamic operators, later abbreviated to Dfns and Dops or D-Fns and D-Ops, but all these terms have been dropped in favour of the current ones.
