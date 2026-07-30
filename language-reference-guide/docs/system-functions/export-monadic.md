---
search:
  boost: 2
---

# <span>Query Export Type</span> `{R}←⎕EXPORT Y`{{key}}

`⎕EXPORT` is used to query the export type of a defined function (or operator) referenced by the `⎕PATH` mechanism.

`Y` is a character matrix or vector-of-vectors representing the names of functions and operators whose export type is to be queried.

The result `R` is a vector that reports the export type of the functions and operators named in `Y`.

When the path mechanism locates a referenced function (or operator) in the list of namespaces in the `⎕PATH` system variable, it examines the function's export type:

|---|---|
|0|This instance of the function is ignored and the search is resumed at the next namespace in the `⎕PATH` list.  Type-0 is typically used for functions residing in a utility namespace which are not themselves utilities, for example the private sub-function of a utility function.|
|1|This instance of the function is executed in the namespace in which it was found and the search terminated.  The effect is exactly as if the function had been referenced by its full path name.|

Warning: `⎕EXPORT` returns a Boolean result at present, but extra types 2, 3,... might be added in future.  If you need a Boolean result, use `0≠` or an equivalent.
```apl
   (0≠⎕EXPORT ⎕NL 3 4)⌿⎕NL 3 4  ⍝ list of exported
                                ⍝ functions and ops.
```

`⎕EXPORT` does not support derived functions and will not be extended to support them; nor will it be extended to support other types of functions that may be developed in the future. `⎕EXPORT` may therefore be considered an archaic feature.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>
