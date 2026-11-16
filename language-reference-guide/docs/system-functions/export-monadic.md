---
search:
  boost: 2
---

# <span>Query Export Type</span> `R←⎕EXPORT Y`{{key}}

This function reports the export type of functions and operators, which determines whether the [`⎕PATH`](path.md) mechanism finds them. [Dyadic `⎕EXPORT`](export-dyadic.md) sets the export type.

!!! Legacy "Legacy"
    `⎕EXPORT` is retained for backwards compatibility purposes. Dyalog Ltd recommends referring to a function or operator in another namespace by its full (absolute or relative) namespace path instead.

<h2 class="example">Example</h2>

In the namespace `utils`, defined in the [example for dyadic `⎕EXPORT`](export-dyadic.md), the function `Average` calls the function `Sum`, whose export type has been set to `0`:

```apl
      utils.⎕EXPORT 'Average' 'Sum'
1 0
```

## Right Argument

`Y` contains the names of functions and operators. It is a simple character vector containing a single name, a character matrix with one name per row, or a vector of character vectors.

## Result

`R` is an integer vector with one [export type](#export-types) per name in `Y`.

<h3 class="example">Example</h3>

The functions and operators in `utils` that are exported:

```apl
      x←utils.⎕NL ¯3 ¯4
      (utils.⎕EXPORT x)/x
 Average
```

## Export Types

When the `⎕PATH` mechanism locates a referenced function or operator in one of the namespaces that `⎕PATH` lists, it examines the export type of the function or operator:

|Export type|Effect|
|-----------|------|
|`0`|This instance of the function is ignored, and the search resumes at the next namespace in `⎕PATH`. This is typically used for a function in a utility namespace that is not a utility itself, for example, a private sub-function of a utility function|
|`1`|This instance of the function is run in the namespace in which it was found, and the search ends. The effect is the same as if the function had been referenced by its full path name. This is the default|

A defined function or operator has the export type `1` until [dyadic `⎕EXPORT`](export-dyadic.md) sets it to `0`. A name that is not the name of a defined function or operator, for example, a variable or a derived function, has the export type `0`, which cannot be changed. Therefore, `⎕PATH` never finds it.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>
