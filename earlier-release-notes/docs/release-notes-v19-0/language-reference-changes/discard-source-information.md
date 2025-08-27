<h1 class="heading"><span class="name">Discard Source Information</span> <span class="command">R←5171⌶Y</span></h1>

This function discards source code and file information for scripted objects, namespaces, classes, functions, and operators that is saved in the workspace. See also [Discard Source Code](discard-source-code.md).

`Y` is a vector or scalar containing zero or more references to `#` or `⎕SE`, and specifies from which namespaces the information is removed.

`R` is an integer. A non-zero value indicates that some information was removed. 0 means nothing was discarded.

- The expression `5171⌶ #` discards source code and file information from the workspace, but not from  `⎕SE`.
- `5171⌶⎕SE` discards source code and file information from `⎕SE` but not from the workspace.
- `5171⌶ # ⎕SE` discards source code and file information from the workspace and from  `⎕SE`.

For further information, see [Source as Typed](../introduction/source-as-typed.md).
