<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>






<h1 class="heading"><span class="name">Export Object</span> <span class="command">{R}←{X}⎕EXPORT Y</span></h1>



`⎕EXPORT` is used to set or query the export type of a defined function (or operator) referenced by the `⎕PATH` mechanism.


`Y` is a character matrix or vector-of-vectors representing the names of functions and operators whose export type is to be set or queried.


`X` is an integer scalar or vector (one per name in the namelist) indicating the export type.  `X` can currently be one of the values:

- 0 - not exported.
- 1 - exported (default).


A scalar or 1-element-vector type is replicated to conform with a multi-name list.


The result `R` is a vector that reports the export type of the functions and operators named in `Y`.  When used dyadically to set export type, the result is shy.




When the path mechanism locates a referenced function (or operator) in the list of namespaces in the `⎕PATH` system variable, it examines the function's export type:


|---|---|
|0|This instance of the function is ignored and the search is resumed at the next namespace in the `⎕PATH` list.  Type-0 is typically used for functions residing in a utility namespace which are not themselves utilities, for example the private sub-function of a utility function.|
|1|This instance of the function is executed in the namespace in which it was found and the search terminated.  The effect is exactly as if the function had been referenced by its full path name.|




Warning: The left domain of `⎕EXPORT` may be extended in future to include extra types 2, 3,... (for example, to change the behaviour of the function).  This means that, while `⎕EXPORT` returns a Boolean result in the first version, this may not be the case in the future.  If you need a Boolean result, use `0≠` or an equivalent.
```apl
   (0≠⎕EXPORT ⎕NL 3 4)⌿⎕NL 3 4  ⍝ list of exported
                                ⍝ functions and ops.
```



`⎕EXPORT` does not support derived functions and will not be extended to support them; nor will it be extended to support other types of functions that may be developed in the future. `⎕EXPORT` may therefore be considered an archaic feature.


