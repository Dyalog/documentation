---
search:
  boost: 2
---

# <span>Set Export Type</span> `{R}←X ⎕EXPORT Y`{{key}}

This function sets the export type of functions and operators, which determines whether the [`⎕PATH`](path.md) mechanism finds them. [Monadic `⎕EXPORT`](export-monadic.md) reports the export type.

!!! Legacy "Legacy"
    `⎕EXPORT` is retained for backwards compatibility purposes. Dyalog Ltd recommends referring to a function or operator in another namespace by its full (absolute or relative) namespace path instead.

<h2 class="example">Example</h2>

In the namespace `utils`, the function `Average` calls the function `Sum`. Setting the export type of `Sum` to `0` makes `⎕PATH` find `Average` but not `Sum`:

```apl
      :Namespace utils
        ∇ r←Average y
          r←(Sum y)÷≢y
        ∇
        ∇ r←Sum y
          r←+/y
        ∇
      :EndNamespace
      0 utils.⎕EXPORT 'Sum'
      ⎕PATH←'utils'
      Average 1 2 3 4
2.5
      Sum 1 2 3 4
VALUE ERROR: Undefined name: Sum
      Sum 1 2 3 4
      ∧
```

## Left Argument

`X` is an integer scalar or vector of export types, with one item per name in `Y`. A scalar or 1-item vector applies to every name.

When the `⎕PATH` mechanism locates a referenced function or operator in one of the namespaces that `⎕PATH` lists, it examines the export type of the function or operator:

|Export type|Effect|
|-----------|------|
|`0`|This instance of the function is ignored, and the search resumes at the next namespace in `⎕PATH`. This is typically used for a function in a utility namespace that is not a utility itself, for example, a private sub-function of a utility function|
|`1`|This instance of the function is run in the namespace in which it was found, and the search ends. The effect is the same as if the function had been referenced by its full path name. This is the default|

## Right Argument

`Y` contains the names of the functions and operators whose export type is set. It is a simple character vector containing a single name, a character matrix with one name per row, or a vector of character vectors.

A defined function or operator has the export type `1` until `⎕EXPORT` sets it to `0`. A name that is not the name of a defined function or operator, for example, a variable or a derived function, has the export type `0`, which cannot be changed, so `⎕PATH` never finds it.

## Result

`R` is an integer vector of the export types that the names in `Y` have after `⎕EXPORT` sets them, with one item per name, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results). It differs from `X` for a name whose export type cannot be changed.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>
