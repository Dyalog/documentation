---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WX WX
</div>






<h1 class="heading"><span class="name">Window Expose</span> <span class="command">⎕WX</span></h1>



`⎕WX` is a system variable with the value 0, 1or 3. `⎕WX` has Namespace scope.


Considered as a sum of bit flags, the first bit in `⎕WX` specifies (a); the second  (b) as follows:

1. whether or not the names of properties, methods and events provided by a Dyalog APL GUI object are exposed 
2. certain aspects of behaviour of .NET and COM objects



If `⎕WX` is 1 (1<sup>st</sup> bit is set), the names of properties, methods and events are exposed as reserved names in GUI namespaces and can be accessed directly by name. This means that the same names may not be used for global variables in GUI namespaces.


If `⎕WX` is 0, these names are hidden and may only be accessed indirectly using `⎕WG` and `⎕WS`.


If `⎕WX` is 3 (2<sup>nd</sup> bit is also set) COM and .NET objects adopt the  behaviour introduced in Version 11, as opposed to the behaviour in previous versions of Dyalog APL.


Any attempt to set `⎕WX` to 2 generates a `DOMAIN ERROR`.


Note that it is the value of `⎕WX` in the object itself, rather than the value of `⎕WX` in the calling environment, that determines its behaviour.


When you create an object, its `⎕WX` (like any other system variable) is initially inherited from its parent.


If the value of `⎕WX` of a GUI object is initially 0, it will not expose its members. If you subsequently change it from 0 to 1, it will expose them. If you change its `⎕WX` back to 0, it will not expose any yet-unexposed members, although already-exposed members will continue to be exposed.


The value of `⎕WX` in a clear workspace is defined by the default_wx parameter (see [ default_wx](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters)) which itself defaults to 3.


`⎕WX` has namespace scope and may be localised in a function header. This allows you to create a utility namespace or utility function in which the exposure of objects is known and determined, regardless of its global value in the workspace.


## Notes

- The visibility of the properties and methods of the Root object are not controlled by `⎕WX` but by the **PropertyExposeRoot** parameter. For further information, see [ PropertyExposeRoot](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).
- `⎕WX` is retained for backwards compatibility and should be considered as deprecated. Dyalog recommends  `⎕WX` be set to 3 and never changed.



