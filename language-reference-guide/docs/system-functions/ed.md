---
search:
  boost: 2
---





# <span>Edit Object</span> `{R}←{X}⎕ED Y`{{key}}



`⎕ED` invokes the Editor.  `Y` is a simple character vector, a simple character matrix, or a vector of character vectors, containing the name(s) of objects to be edited.

The optional left argument `X` is a character scalar or character vector (where `=/≢X Y`) which specifies the type(s) of the corresponding (new) object(s) named in `Y` as:


|---|---------------------------|
|`∇`|function/operator          |
|`→`|simple character vector    |
|`∊`|vector of character vectors|
|`-`|character matrix           |
|`⍟`|Namespace script           |
|`○`|Class script               |
|`∘`|Interface                  |
|`⋄`|array: use array notation  |


If `Y` names an existing object, the type specification for that name in `X` is ignored, unless `X` is `⋄`.

If `X` is `⋄`, `Y` must be undefined or an array.
The Editor opens in array-notation mode; the resulting array can be of any type or structure.

If `⎕ED` is called from the Session, it opens Edit windows for the object(s) named in `Y` and returns a null result.  The cursor is positioned in the first of the Edit windows opened by `⎕ED`, but may be moved to the Session or to any other window which is currently open.  The effect is almost identical to using `)ED`.


If `⎕ED` is called from a defined function or operator, its behaviour is different. On asynchronous terminals, the Edit windows are automatically displayed in "full-screen" mode (ZOOMED). In all implementations, the user is restricted to those windows named in `Y`. The user may not skip to the Session even though the Session may be visible.


`⎕ED` terminates and returns a result ONLY when the user explicitly closes all the windows for the named objects. In this case the result contains the names of any objects which have been newly (re)fixed in the workspace as a result of the `⎕ED`, and has the same structure as `Y`.


Objects named in `Y` that cannot be edited are silently ignored. Objects qualified with a namespace path are (for example, `a.b.c.foo`) are silently ignored if the namespace does not exist.


## Variants of Edit Object


The behaviour of `⎕ED` may be modified using the variant operator `⍠` with the following options:

- `'ReadOnly'` - 0 or 1
- `'EditName'` - `'Default'`, `'Allow'` or `'Disallow'`.



If `ReadOnly` is set to 1, the edit window and all edit windows opened from it will be read-only. Note that setting `ReadOnly` to 0 will have no effect if the edit window is inherently read-only due to the nature of its content.



The `'EditName'` option determines whether or not the user may open another edit window by clicking a name, and its values are interpreted as follows:


|EditName    |`⎕ED` called from session|`⎕ED` called from function|
|------------|-------------------------|--------------------------|
|`'Default'` |Allow                    |Disallow                  |
|`'Allow'`   |Allow                    |Allow                     |
|`'Disallow'`|Disallow                 |Disallow                  |



There is no Principal Option.

<h2 class="example">Examples</h2>
```apl
      A←3 11⍴'Hello World'
```



In the first example, `⎕ED` will display the contents of `A` as an editable character array which the user may change. The user can double-click on *Hello* to open an edit window on an object named `Hello` (which will be a new function if `Hello` is currently undefined). Furthermore, the user can enter any arbitrary name and double-click to edit it. This may be undesirable in an application.
```apl
      ⎕ED A
```




In the second example, the Edit window will display the contents of `A` as a ReadOnly Character array. The user can still open a new edit by double-clicking *Hello* or *World* but nothing else.
```apl
      (⎕ED ⍠ 'ReadOnly' 1) 'A'
```




In the final example, the Edit window will display the contents of `A` as a ReadOnly Character array and the user cannot open a new edit window.
```apl
      (⎕ED ⍠('ReadOnly' 1)('EditName' 'Disallow'))'A'
```



