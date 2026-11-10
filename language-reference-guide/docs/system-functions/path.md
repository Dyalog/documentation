---
search:
  boost: 2
---

# <span>Search Path</span> `⎕PATH`

`⎕PATH` lists the namespaces in which the interpreter searches for a function or operator that is not defined in the current namespace. It makes the functions and operators in a utility namespace available from anywhere in the workspace without their full path names, much as the `PATH` environment variable of Microsoft Windows or Unix makes programs available from any directory.

!!! Legacy "Legacy"
    `⎕PATH` is retained for backwards compatibility purposes. Dyalog Ltd recommends referring to a function or operator in another namespace by its full (absolute or relative) namespace path instead.

<h2 class="example">Example</h2>

A utility namespace in `⎕SE` makes `Average` available from any namespace:

```apl
      ⎕PATH←'⎕SE.util'⎕NS''
      ⎕SE.util.Average←{(+/⍵)÷≢⍵}
      'ns'⎕NS''
      ns.(Average 2 4 9)
5
```

## Value

`⎕PATH` is a simple character vector of namespace names separated by spaces. The default is `''`, meaning that no namespaces are searched.

Each name is either a full path name, or a path name relative to the namespace in which the search starts. The name `↑` stands for the ancestors of that namespace, `## ##.## ##.##.##`, up to `#`, or to `⎕SE` if the search starts in `⎕SE`. A name that does not identify an existing namespace is ignored.

## Search

`⎕PATH` is only used when a name cannot be found in the current namespace. The interpreter then searches the namespaces listed in `⎕PATH`, from left to right, and uses the first defined function or operator with that name whose [export type](export-monadic.md#export-types) is `1`, which is the default. [Dyadic `⎕EXPORT`](export-dyadic.md) can set the export type to `0`, to hide a function or operator from the search. Variables and derived functions are never found. If the search finds nothing, `VALUE ERROR` is signalled.

A function or operator that is found through `⎕PATH` runs in the namespace in which it was found, as if it had been referenced by its full path name.

These are the namespaces that some values of `⎕PATH` make the interpreter search, after the current namespace:

|`⎕PATH`|Namespaces searched|
|-------|-------------------|
|`'⎕SE.util'`|`⎕SE.util`|
|`'↑'`|`##`, then `##.##`, and so on, up to `#` (or `⎕SE`)|
|`'util ↑ ⎕SE.util'`|`util` (relative to the current namespace), then `##`, `##.##`, and so on, up to `#` (or `⎕SE`), then `⎕SE.util`|

With `↑` in `⎕PATH`, a function or operator defined in an enclosing namespace can be used from any namespace within it, much as a name defined in an outer block is visible in the inner blocks of a block-structured language with static scope.

## Scope

`⎕PATH` has [session scope](system-functions-by-category.md#system-variables): it applies to the whole workspace, and keeps its value through `)LOAD` and `)CLEAR`. A defined function or operator can localise it.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PATH PATH
</div>
