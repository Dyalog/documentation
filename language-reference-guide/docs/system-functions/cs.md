---
search:
  boost: 2
---

# <span>Change Namespace</span> `{R}←{X}⎕CS Y`{{key}}

`⎕CS` changes the namespace in which the current function or operator runs, or the current namespace of the Session, to the namespace `Y`.

<h2 class="example">Example</h2>

`Setup` changes to the namespace `cfg`, so the variables it assigns are in `cfg`:

```apl
      'cfg'⎕NS ''
      ∇ Setup
        ⎕CS 'cfg'
        Width←80
        Height←24
      ∇
      Setup
      cfg.(Width Height)
80 24
```

## Left Argument

`X` is optional, and is the names of objects to *export* to `Y` while the current function runs, as a character scalar, vector or matrix, or a vector of character vectors. In `Y`, an exported name refers to the object that it refers to in the function, and hides any object of the same name in `Y`. The export ends when the function ends.

Exporting needs a traditional function or operator to be running. If none is, for example, at the Session, dyadic `⎕CS` signals `DOMAIN ERROR`.

<h3 class="example">Example</h3>

`Scale` exports its local variable `factor` and the global function `Times` to `cfg`:

```apl
      ∇ R←X Times Y
        R←X×Y
      ∇
      ∇ Scale;factor
        factor←2
        'factor' 'Times'⎕CS 'cfg'
        Width←factor Times Width
      ∇
      Scale
      cfg.Width
160
      cfg.⎕NC 'factor' 'Times'
0 0
```

## Right Argument

`Y` is a reference to a namespace, or its name as a character scalar or vector. The name can be compound, as in `'x.y'`, and can include `⎕SE`, `#`, and `##`. If `Y` is empty, the namespace does not change.

A name that does not identify an existing namespace signals `VALUE ERROR`, and any other value of `Y` signals `DOMAIN ERROR`.

## Result

The [shy](../../programming-reference-guide/introduction/results.md#shy-results) result `R` is the full name of the namespace that was current before `⎕CS`, as a character vector, for example, `'#.cfg'` or `'#'`. With an empty `Y`, `R` is therefore the name of the current namespace.

## Scope

Inside a traditional function or operator, the change lasts until it ends, and the function or operator that called it continues in its own namespace. In the new namespace, global names refer to the objects of `Y`, while the local names of the function still refer to its local objects, and hide any objects of the same names in `Y`. A local reference to a namespace (name class `9`) is not visible.

At the Session, `⎕CS` changes the current namespace of the Session, as [`)CS`](../system-commands/cs.md) does.

`⎕CS` cannot be used in a dfn or dop, and signals `NONCE ERROR` there.

<h3 class="example">Example</h3>

[`⎕THIS`](this.md) reports the current namespace, before and after `⎕CS`. When `Report` ends, the Session is still in `#`:

```apl
      ∇ Report;Width
        Width←'local'
        ⎕THIS
        ⎕CS 'cfg'
        ⎕THIS
        Width
        Height
      ∇
      Report
#
#.cfg
local
24
      ⎕THIS
#
```

<h3 class="example">Example</h3>

`tree` displays a tree of namespaces. It exports its own name each time that it changes namespace, because `tree` is a global name, which would otherwise refer to `tree` in the new namespace:

```apl
      ∇ tabs tree space;subs
        tabs,space
        'tree'⎕CS space
        →(⍴subs←↓⎕NL 9)↓0
        (tabs,'.   ')∘tree¨subs
      ∇
      'x.y'⎕NS ''
      'z'⎕NS ''
      ''tree '#'
#
.   cfg
.   x
.   .   y
.   z
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CS CS
</div>
