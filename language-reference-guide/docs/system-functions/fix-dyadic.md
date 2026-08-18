---
search:
  boost: 2
---

# <span>Define Objects</span> `{R}←X ⎕FIX Y`{{key}}

`⎕FIX` establishes namespaces, classes, interfaces and functions from the script specified by `Y` in the workspace.

In this section, the term *namespace* covers scripted namespaces, classes, and interfaces.

`Y` can be a simple character vector, or  a vector of character vectors or character scalars. The value of `X` determines what `Y` can contain.

If `Y` is a simple character vector, it must be the name of a file which must exist. The contents of the file must follow the same rules that apply to `Y` when `Y` is a vector of character vectors or scalars. The file name can be relative or absolute; when considering cross-platform portability, using `/` as the directory delimiter is recommended, although `\` is also valid under Windows.

`X` is a numeric scalar, `0`, `1` or `2`. The default, `1`, is equivalent to [monadic `⎕FIX`](fix-monadic.md). The result `R` is shy.

| `X` | `Y` value or content of file `Y` | `R` |
|-----|-----|-----|
| `0` | a single valid *namespace*, which might or might not be named | a reference to the *namespace*. Even if the *namespace* is named, it is not established *per se*, although it will exist for as long as at least one reference to it exists |
| `1` | a single valid *namespace*, which might or might not be named | a reference to the *namespace*. If `Y` contains the definition of a named *namespace*, the *namespace* is established in the workspace |
| `2` | a series of **named** *namespaces* or function definitions, or a combination of functions and namespaces. If the script contains more than one item, tradfn definitions must be delimited by `∇` symbols. Derived and assigned functions can be specified only within namespaces | a vector of character vectors, containing the names of all of the objects that have been established in the workspace; the order of the names in `R` is not defined. Currently `2 ⎕FIX` is not certain to be an atomic operation, although this might change in future versions |

<h2 class="example">Examples</h2>

In the first example, the left-argument of `0` causes the named class `MyClass` to be visible only via the reference to it (`MYREF`). It is there, but hidden.
```apl
      MYREF←0 ⎕FIX ':Class MyClass' ':EndClass'
      )CLASSES
MYREF
      MYREF
#.MyClass
```

In the second example, the left argument of `2` allows a script containing multiple objects to be fixed:

```apl

      src←':Namespace andys' '∇foo' '2' '∇'
      src,←':EndNamespace' 'dfn←{⍺ ⍵}' '∇r←tfn'
      src,←'r←33' '∇' ':Class c1' '∇goo' '1'
      src,←'∇' ':EndClass'
      ≢⎕←2⎕FIX src
 c1  tfn  dfn  andys 
4

```

## Restrictions

`⎕FIX` is unable to fix a namespace from `Y` when `Y` specifies a multi-line dfn which is preceded by a `⋄` (diamond separator).

!!! Legacy "Legacy"
    Before Dyalog v20.0, it was possible to define dfns with unmatched parentheses and brackets. These are now rejected. TradFns will continue to fix as before, but subtle differences in how the code behaves might not be backwards-compatible and could have unexpected results.

## Variant Options

`⎕FIX` can be applied using the _variant_ operator with the options `Quiet`, `FixWithErrors`, `AllowLateBinding`, and `InjectReferences`. These options apply only to namespaces and classes specified by the script. There is no principal option.

## Quiet Option

|---|------------------------------------------------------------------------------|
|`0` (default)|If the script contains errors, these are displayed in the Status Window.      |
|`1`|If the script contains errors, the errors are not shown  in the Status Window.|

## FixWithErrors Option

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`0`|If the script contains errors, `⎕FIX` fails with `DOMAIN ERROR` .                                                                                                      |
|`1` (default)|`⎕FIX` fixes all the namespaces and classes in the script regardless of any errors they might contain.                                                                   |
|`2`|If the script contains errors, `⎕FIX` displays a message box prompting the user to choose whether or not to fix all the offending namespaces and classes in the script.|

## AllowLateBinding Option

|---|---------------------------------------------------------------------------------------------------------------------|
|`0` (default)|`⎕FIX` will only fix a class whose Base class (if specified) is defined in the script or is present in the workspace.|
|`1`|`⎕FIX` will fix a class whose Base class is neither defined in the script nor present in the workspace.            |

## InjectReferences Option

|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|`'All'`    |In order to implement lexical scope, `⎕FIX` will insert internal references into all objects in the script.                                          |
|`'InClasses'` (default)|In order to implement lexical scope, `⎕FIX` will insert internal references ONLY into classes and sub-classes in the script, but not into namespaces.|
|`'None'`   |No internal references are inserted and lexical scope does not apply.                                                                                |

See [Lexical Scope in Scripts](../../../earlier-release-notes/release-notes-v19-0/introduction/lexical-scope-in-scripts).

<h2 class="example">Examples</h2>

The following examples illustrate how different values of the InjectReferences option affect the scope of objects in scripts. The examples are based on the following family tree:

![family tree for fix](../img/family-tree-for-fix.png)

Two scripts are defined to map this tree onto a structure of classes and namespaces. In this scheme, female family members are represented by classes and male family members by namespaces.

So the scripted tree for `Pete` has a parent namespace:
```apl
:Namespace Pete
    :Namespace Andy
        :Class Aisha
        :Access Public
        :Endclass
    :EndNamespace

    :Class Katherine
    :Access Public
        :Namespace Woody
        :EndNamespace
        :Namespace George
        :EndNamespace
    :EndClass
:EndNamespace
```

While the scripted tree for `Jill` has a parent class:
```apl
:Class Jill
:Access Public
    :Namespace Andy
        :Class Aisha
        :Access Public
        :Endclass
    :EndNamespace

    :Class Katherine
    :Access Public
        :Namespace Woody
        :EndNamespace
        :Namespace George
        :EndNamespace
    :EndClass
:EndClass
```

Using the `Pete` namespace, after executing the expression:
```apl
      2(⎕FIX⍠'InjectReferences' 'All')⎕SRC Pete
```

- Code in `Pete` can refer to `Aisha`    , `Andy`     , `George`   , `Katherine`, and `Woody`
- Code in `Andy` can refer to `Aisha`    and `Katherine`
- ... and so forth.

But after executing:
```apl
      2(⎕FIX⍠'InjectReferences' 'InClasses')⎕SRC Pete
```

- Code in `Pete` can refer only to `Andy` and  `Katherine`
- Code in `Andy` can refer only to `Aisha`
- ... and so forth.

The following tables show which objects in namespace `Pete` can *see* (that is, refer to) which other objects representing members of the family, in each case; `All`, `InClasses` and `None`.

|'All'    |Pete  |Andy  |Aisha |Katherine|Woody |George|
|---------|------|------|------|---------|------|------|
|Pete     |&nbsp;|✔     |✔     |✔        |✔     |✔     |
|Andy     |&nbsp;|&nbsp;|✔     |✔        |&nbsp;|&nbsp;|
|Aisha    |✔     |✔     |✔     |&nbsp;   |&nbsp;|&nbsp;|
|Katherine|✔     |✔     |&nbsp;|✔        |✔     |✔     |
|Woody    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|✔     |
|George   |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |✔     |&nbsp;|

|'InClasses'|Pete  |Andy  |Aisha |Katherine|Woody |George|
|-----------|------|------|------|---------|------|------|
|Pete       |&nbsp;|✔     |&nbsp;|✔        |&nbsp;|&nbsp;|
|Andy       |&nbsp;|&nbsp;|✔     |&nbsp;   |&nbsp;|&nbsp;|
|Aisha      |✔     |✔     |✔     |&nbsp;   |&nbsp;|&nbsp;|
|Katherine  |✔     |✔     |&nbsp;|✔        |✔     |✔     |
|Woody      |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|George     |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|

|'None'   |Pete  |Andy  |Aisha |Katherine|Woody |George|
|---------|------|------|------|---------|------|------|
|Pete     |&nbsp;|✔     |&nbsp;|✔        |&nbsp;|&nbsp;|
|Andy     |&nbsp;|&nbsp;|✔     |&nbsp;   |&nbsp;|&nbsp;|
|Aisha    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|Katherine|&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|Woody    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|George   |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|

Whilst the next set of tables show the same for class `Jill`.

|'All'    |Jill  |Andy  |Aisha |Katherine|Woody |George|
|---------|------|------|------|---------|------|------|
|Jill     |✔     |✔     |✔     |✔        |✔     |✔     |
|Andy     |&nbsp;|&nbsp;|✔     |✔        |&nbsp;|&nbsp;|
|Aisha    |✔     |✔     |✔     |&nbsp;   |&nbsp;|&nbsp;|
|Katherine|✔     |✔     |&nbsp;|✔        |✔     |✔     |
|Woody    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|✔     |
|George   |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |✔     |&nbsp;|

|'InClasses'|Jill  |Andy  |Aisha |Katherine|Woody |George|
|-----------|------|------|------|---------|------|------|
|Jill       |✔     |✔     |✔     |✔        |✔     |✔     |
|Andy       |&nbsp;|&nbsp;|✔     |&nbsp;   |&nbsp;|&nbsp;|
|Aisha      |✔     |✔     |✔     |&nbsp;   |&nbsp;|&nbsp;|
|Katherine  |✔     |✔     |&nbsp;|✔        |✔     |✔     |
|Woody      |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|George     |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|

|'None'   |Jill  |Andy  |Aisha |Katherine|Woody |George|
|---------|------|------|------|---------|------|------|
|Jill     |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|Andy     |&nbsp;|&nbsp;|✔     |&nbsp;   |&nbsp;|&nbsp;|
|Aisha    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|Katherine|&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|Woody    |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|
|George   |&nbsp;|&nbsp;|&nbsp;|&nbsp;   |&nbsp;|&nbsp;|

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FIX FIX
</div>
