# Namespaces and Localisation

The rules for name resolution have been generalised for namespaces.

In flat APL, the interpreter searches the state indicator to resolve names referenced by a defined function or operator.  If the name does not appear in the state indicator, then the workspace-global name is assumed.

With namespaces, a defined function or operator is evaluated in its 'home' namespace. When a name is referenced, the interpreter searches only those lines of the state indicator which belong to the home namespace.  If the name does not appear in any of these lines, the home namespace-global value is assumed.

For example, if  `#.FN1`  calls  `XX.FN2`  calls  `#.FN3`  calls  `XX.FN4`, then:

- `FN1`:
    - is evaluated in `#`
    - can see its own dynamic local names
    - can see global names in `#`

- `FN2`:
    - is evaluated in `XX`
    - can see its own dynamic local names
    - can see global names in `XX`

- `FN3`:
    - is evaluated in `#`
    - can see its own dynamic local names
    - can see dynamic local names in `FN1`
    - can see global names in `#`

- `FN4`:
    - is evaluated in `XX`
    - can see its own dynamic local names
    - can see dynamic local names in `FN2`
    - can see global names in `XX`

The following picture illustrates how APL looks down the stack to find names:
```other

    │           │           │
    │    a+b+c  │           │ [8] h references a, b and c
    │    │ │ │  │           │
    │ ∇h;a │ │  │           │ [7] h localises a
    │      │ │  │           │
    │      │ │  │           │ [6] g calls X.h
    │      │ │  │           │
    │      │ │  │    a+b+c  │ [5] g references a, b and c
    │      │ │  │    │ │ │  │
    │      │ │  │ ∇g;a;│ c  │ [4] g localises a and c
    │      │ │  │      │    │
    │      │ │  │      │    │ [3] f calls Y.g
  ↑ │      │ │  │      │    │
  s │    a+b+c  │      │    │ [2] f references a, b and c
  t │    │ │ │  │      │    │
  a │ ∇f;a;b │  │      │    │ [1] f localises a and b
  c │        │  │      │    │
  k │    a b c  │    a b c  │ [0] global names a, b and c 
    └X──────────┴Y──────────┘     in namspaces X and Y
```

The above diagram represents the SI stack, growing upwards from two namespaces `X` and `Y`, which each have three global names `a`, `b` and `c`.

1. Function `f` in `X` localises names `a` and `b`.
2. Function `f` references names `a`, `b` and `c`.
    ```apl
            ∇ f;a;b
        [1]   a+b+c
        [2]   Y.g
    ```
    The interpreter looks down the stack and finds local names `a` and `b` in `f`'s header and `c` in namespace `X`.

1. Function `f` calls function `g` in namespace `Y`.
2. Function `g` in `Y` localises names `a` and `c`.
3. Function `g` references names `a`, `b` and `c`.
    ```apl
            ∇ g;a;c
        [1]   a+b+c
        [2]   X.h
    ```
    The interpreter looks down the stack and finds local names `a` and `c` in `g`'s header and `b` in namespaces `Y`.

1. Function `g` calls function `h` in namespace `X`.
2. Function `h` in `X` localises name `a`.
3. Function `h` references names `a`, `b` and `c`.
    ```apl
            ∇ h;a
        [1]   a+b+c
    ```
    The interpreter looks down the stack and finds local name `a` in `h`'s header; `b` in `f`'s header; and `c` in namespace `X`.

## Qualified Names

A _qualified_ name, one written with a namespace path such as `ns.x`, is resolved in the target namespace according to the above rules. Assigning to a qualified name is therefore not subject to the automatic localisation of a [dfn](../../defined-functions-and-operators/dfns-and-dops/global-local-names.md), and the name is created there if it does not already exist.

Within the target namespace, the name is still resolved through the state indicator. Therefore, if a function in the target namespace is on the stack and has localised the name, a qualified assignment updates that local name rather than creating or modifying a global name.
