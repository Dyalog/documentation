---
search:
  boost: 2
---

# <span>Edit Objects</span> `{R}←⎕ED Y`{{key}}

`⎕ED` invokes the Editor. `Y` is a simple character vector, a simple character matrix, or a vector of character vectors, containing the name(s) of objects to be edited.

If a name in `Y` is not already defined, the Editor assumes the new object to be a function or operator; [dyadic `⎕ED`](ed-dyadic.md) can specify other types.

If `⎕ED` is called from the Session, it opens Edit windows for the object(s) named in `Y` and returns a null result. The cursor is positioned in the first of the Edit windows opened by `⎕ED`, but can be moved to the Session or to any other window which is currently open. The effect is almost identical to using `)ED`.

If `⎕ED` is called from a defined function or operator, its behaviour is different. On asynchronous terminals, the Edit windows are automatically displayed in "full-screen" mode (_zoomed_). In all implementations, the user is restricted to those windows named in `Y`. The user cannot skip to the Session even though the Session might be visible.

`⎕ED` terminates and returns a result _only_ when the user explicitly closes all the windows for the named objects. In this case the result contains the names of any objects which have been newly (re)fixed in the workspace as a result of the `⎕ED`, and has the same structure as `Y`.

Objects named in `Y` that cannot be edited are silently ignored. Objects qualified with a namespace path are (for example, `a.b.c.foo`) are silently ignored if the namespace does not exist.

## Variants of Edit Object

The behaviour of `⎕ED` can be modified using the _variant_ operator `⍠` with the following options:

- `'ReadOnly'` - 0 or 1
- `'EditName'` - `'Default'`, `'Allow'`, or `'Disallow'`.

If `ReadOnly` is set to 1, the edit window and all edit windows opened from it will be read-only. Note that setting `ReadOnly` to 0 will have no effect if the edit window is inherently read-only due to the nature of its content.

The `'EditName'` option determines whether or not the user can open another edit window by clicking a name, and its values are interpreted as follows:

|EditName    |`⎕ED` called from session|`⎕ED` called from function|
|------------|-------------------------|--------------------------|
|`'Default'` |Allow                    |Disallow                  |
|`'Allow'`   |Allow                    |Allow                     |
|`'Disallow'`|Disallow                 |Disallow                  |

There is no principal option.

<h2 class="example">Examples</h2>
```apl
      A←3 11⍴'Hello World'
```

In the first example, `⎕ED` will display the contents of `A` as an editable character array which the user can change. The user can double-click on `Hello` to open an edit window on an object named `Hello` (which will be a new function if `Hello` is currently undefined). Furthermore, the user can enter any arbitrary name and double-click to edit it. This might be undesirable in an application.
```apl
      ⎕ED A
```

In the second example, the Edit window will display the contents of `A` as a read-only character array. The user can still open a new edit by double-clicking `Hello` or `World` but nothing else.
```apl
      (⎕ED ⍠ 'ReadOnly' 1) 'A'
```

In the final example, the Edit window will display the contents of `A` as a read-only character array and the user cannot open a new edit window.
```apl
      (⎕ED ⍠('ReadOnly' 1)('EditName' 'Disallow'))'A'
```

